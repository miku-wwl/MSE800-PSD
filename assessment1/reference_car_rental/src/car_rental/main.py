"""运行入口。"""

try:
    from .controller import run_demo
except ImportError:  # 直接运行 main.py 时使用
    from controller import run_demo


if __name__ == "__main__":
    run_demo()
