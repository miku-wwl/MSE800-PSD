import configparser
import mysql.connector
from mysql.connector import Error
from sql_statement import *


class Database:
    def __init__(self, config_filename):
        self.config_filename = config_filename
        self.connection = None  # Hold the connection object
        self._init_database()

    def _init_database(self):
        config = self.load_config()
        self.connection = mysql.connector.connect(**config, autocommit=True)
        if self.connection.is_connected():
            self._check_database_exist()
            self._check_table_exist()
            return True
        return False

    def create_connection_parser(self):
        config = self.load_config()
        self.connection = mysql.connector.connect(**config, autocommit=True)
        if self.connection.is_connected():
            return self.connection.cursor()
        else:
            raise Exception()

    def _check_database_exist(self):
        config = self.load_config()
        if not config.get("database"):
            config['database'] = DEFAULT_DB_NAME
            self.save_config(config)

        cursor = self.create_connection_parser()
        cursor.execute(f"{CREATE_DB} {config['database']};")

    def _check_table_exist(self):
        cursor = self.create_connection_parser()
        cursor.execute(CREATE_STUDENT_TABLE)

    def load_config(self):
        # Load database configurations
        config = configparser.ConfigParser()
        config.read(self.config_filename)
        return {key: value for key, value in config['mysql'].items()}

    def save_config(self, config):
        # Save database configurations to local
        config_parser = configparser.ConfigParser()
        config_parser['mysql'] = config
        # Write the configuration to the file
        with open(self.config_filename, 'w') as configfile:
            config_parser.write(configfile)

    def add_to_database(self, new_student):
        try:
            cursor = self.create_connection_parser()
            values = (new_student.name, new_student.address, new_student.age)
            cursor.execute(INSERT_STUDENT, values)
            new_student.student_id = cursor.lastrowid
            print(f"Student added with ID: {new_student.student_id}")
        except Error as e:
            print(f"Error: {e}")

    def print_table(self):
        try:
            cursor = self.create_connection_parser()
            sql = "Select * from Students"
            cursor.execute(sql)
            print(cursor.fetchall())
        except Error as e:
            print(f"Error: {e}")


class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age


class Student(Person):
    def __init__(self, name, address, age, student_id=None):
        super().__init__(name, address, age)
        self.student_id = student_id


def main():
    db = Database("configfile.ini")
    new_student = Student("Alice", "456 Maple Street", 20)
    db.add_to_database(new_student)
    db.print_table()


if __name__ == '__main__':
    main()
