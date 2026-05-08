PRAGMA foreign_keys = ON;

-- List all products
SELECT * FROM products ORDER BY product_id;

-- Find a product by SKU
SELECT * FROM products WHERE sku = 'SKU-1001';

-- Find low stock products
SELECT * FROM products WHERE quantity < 10 ORDER BY quantity ASC;
