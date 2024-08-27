#ECOMMERCE DATA ANALYSIS PROJECT (Python+MySQL)

!pip install mysql-connector-python

!apt-get -y install mysql-server

!service mysql start

!mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root';FLUSH PRIVILEGES;"

import mysql.connector

# Create a connection to the MySQL server
conn = mysql.connector.connect(user='root', password='root', host='localhost')

# Create a cursor to interact with the MySQL server
cursor = conn.cursor()

# Create a new database named 'ecommerce'
cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce")

# Switch to the 'library' database
cursor.execute("USE ecommerce")

# Create the 'customer' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `customer` (
`customer_id` varchar(10) NOT NULL,
`name` varchar(100) NOT NULL,
`city` varchar(65) NOT NULL,
`email` varchar(45) NOT NULL,
`phone_no` varchar(15) NOT NULL,
`address` varchar(100) NOT NULL,
`pin_code` int NOT NULL,
PRIMARY KEY (`customer_id`)
)
''')
# Create the 'product' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS  `product` (
`product_id` varchar(10) NOT NULL,
`product_name` varchar(100) NOT NULL,
`category` varchar(65) NOT NULL,
`sub_category` varchar(45) NOT NULL,
`original_price` double NOT NULL,
`selling_price` double NOT NULL,
`stock` int NOT NULL,
PRIMARY KEY (`product_id`)
)
''')

# Create the 'order_details' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS  `order_details` (
`order_id` int NOT NULL AUTO_INCREMENT,
`customer_id` varchar(10) NOT NULL,
`product_id` varchar(10) NOT NULL,
`quantity` double NOT NULL,
`total_price` double NOT NULL,
`payment_mode` varchar(60) NOT NULL,
`order_date` datetime DEFAULT NULL,
`order_status` varchar(20) NOT NULL,
PRIMARY KEY (`order_id`),
KEY `customer_id` (`customer_id`),
KEY `product_id` (`product_id`),
CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`customer_id`)
REFERENCES `customer` (`customer_id`),
CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`product_id`)
REFERENCES `product` (`product_id`)
)
''')
cursor.close()
conn.close()

###############################################################################

import mysql.connector

# Connect to the MySQL server and the 'ecommerce' database
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
cursor = conn.cursor()
customer_data = [
    ('C001', 'John Doe', 'New York', 'john.doe@example.com', '123-456-7890', '123 Elm Street', 10001),
    ('C002', 'Jane Smith', 'Los Angeles', 'jane.smith@example.com', '234-567-8901', '456 Oak Avenue', 90001),
    ('C003', 'Emily Johnson', 'Chicago', 'emily.johnson@example.com', '345-678-9012', '789 Pine Road', 60601),
    ('C004', 'Michael Brown', 'Houston', 'michael.brown@example.com', '456-789-0123', '101 Maple Lane', 77001),
    ('C005', 'Olivia Davis', 'Phoenix', 'olivia.davis@example.com', '567-890-1234', '202 Cedar Blvd', 85001),
    ('C006', 'James Wilson', 'Philadelphia', 'james.wilson@example.com', '678-901-2345', '303 Birch Street', 19101),
    ('C007', 'Ava Martinez', 'San Antonio', 'ava.martinez@example.com', '789-012-3456', '404 Spruce Circle', 78201),
    ('C008', 'William Garcia', 'San Diego', 'william.garcia@example.com', '890-123-4567', '505 Walnut Way', 92101),
    ('C009', 'Sophia Rodriguez', 'Dallas', 'sophia.rodriguez@example.com', '901-234-5678', '606 Fir Drive', 75201),
    ('C010', 'Benjamin Lee', 'San Jose', 'benjamin.lee@example.com', '012-345-6789', '707 Redwood Terrace', 95101),
    ('C011', 'Isabella Lopez', 'Austin', 'isabella.lopez@example.com', '123-654-7890', '808 Sycamore Lane', 73301),
    ('C012', 'Mason Walker', 'San Francisco', 'mason.walker@example.com', '234-765-8901', '909 Redwood Way', 94101),
    ('C013', 'Mia Hall', 'Columbus', 'mia.hall@example.com', '345-876-9012', '1010 Pine Hill', 43201),
    ('C014', 'Ethan Young', 'Indianapolis', 'ethan.young@example.com', '456-987-0123', '1111 Maple Road', 46201),
    ('C015', 'Charlotte Allen', 'Charlotte', 'charlotte.allen@example.com', '567-098-1234', '1212 Oak Circle', 28201),
]

# Insert data using the cursor
cursor.executemany('''
INSERT INTO customer (customer_id, name, city, email, phone_no, address, pin_code) VALUES (%s, %s, %s, %s, %s, %s, %s)
''', customer_data)
# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


###############################################################################

import mysql.connector

# Connect to the MySQL server and the 'ecommerce' database
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
cursor = conn.cursor()
product_data = [
    ('P001', 'Smartphone X', 'Electronics', 'Mobile Phones', 699.99, 649.99, 120),
    ('P002', 'Laptop Pro 15', 'Electronics', 'Laptops', 1199.99, 1149.99, 80),
    ('P003', 'Bluetooth Headphones', 'Electronics', 'Audio', 149.99, 129.99, 150),
    ('P004', '4K Ultra HD TV', 'Electronics', 'Televisions', 799.99, 749.99, 60),
    ('P005', 'Gaming Console', 'Electronics', 'Gaming', 299.99, 279.99, 100),
    ('P006', 'Washing Machine', 'Home Appliances', 'Laundry', 499.99, 479.99, 50),
    ('P007', 'Refrigerator X', 'Home Appliances', 'Kitchen', 999.99, 949.99, 40),
    ('P008', 'Microwave Oven', 'Home Appliances', 'Cooking', 199.99, 179.99, 90),
    ('P009', 'Air Conditioner', 'Home Appliances', 'Cooling', 399.99, 379.99, 30),
    ('P010', 'Electric Kettle', 'Home Appliances', 'Kitchen', 49.99, 39.99, 200),
    ('P011', 'Men\'s Running Shoes', 'Footwear', 'Sports', 89.99, 79.99, 150),
    ('P012', 'Women\'s Leather Boots', 'Footwear', 'Casual', 129.99, 119.99, 75),
    ('P013', 'Classic Watch', 'Accessories', 'Watches', 199.99, 179.99, 100),
    ('P014', 'Stylish Sunglasses', 'Accessories', 'Eyewear', 79.99, 69.99, 120),
    ('P015', 'Leather Wallet', 'Accessories', 'Wallets', 49.99, 44.99, 140)
]

# Insert data using the cursor
cursor.executemany('''
INSERT INTO product (product_id, product_name, category, sub_category, original_price, selling_price, stock) VALUES (%s, %s, %s, %s, %s, %s, %s)
''', product_data)
# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

###############################################################################

import mysql.connector

# Connect to the MySQL server and the 'ecommerce' database
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
cursor = conn.cursor()
order_data = [
    (1,'C001', 'P001', 2, 1299.98, 'Credit Card', '2024-08-01 10:15:00', 'Shipped'),
    (2,'C002', 'P002', 1, 1149.99, 'PayPal', '2024-08-01 11:20:00', 'Delivered'),
    (3,'C003', 'P003', 3, 389.97, 'Debit Card', '2024-08-01 12:25:00', 'Processing'),
    (4,'C004', 'P004', 1, 749.99, 'Credit Card', '2024-08-01 13:30:00', 'Cancelled'),
    (5,'C005', 'P005', 2, 559.98, 'Credit Card', '2024-08-01 14:35:00', 'Shipped'),
    (6,'C006', 'P006', 1, 479.99, 'Bank Transfer', '2024-08-02 09:40:00', 'Delivered'),
    (7,'C007', 'P007', 1, 949.99, 'Debit Card', '2024-08-02 10:45:00', 'Processing'),
    (8,'C008', 'P008', 2, 359.98, 'PayPal', '2024-08-02 11:50:00', 'Shipped'),
    (9,'C009', 'P009', 1, 379.99, 'Credit Card', '2024-08-02 12:55:00', 'Delivered'),
    (10,'C010', 'P010', 5, 199.95, 'Credit Card', '2024-08-02 14:00:00', 'Shipped'),
    (11,'C011', 'P011', 1, 79.99, 'Debit Card', '2024-08-03 09:10:00', 'Processing'),
    (12,'C012', 'P012', 2, 239.98, 'PayPal', '2024-08-03 10:15:00', 'Cancelled'),
    (13,'C013', 'P013', 1, 179.99, 'Credit Card', '2024-08-03 11:20:00', 'Shipped'),
    (14,'C014', 'P014', 3, 209.97, 'Bank Transfer', '2024-08-03 12:25:00', 'Delivered'),
    (15,'C015', 'P015', 2, 89.98, 'Debit Card', '2024-08-03 13:30:00', 'Processing'),
]
# Insert data using the cursor
cursor.executemany('''
INSERT INTO order_details (order_id, customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',order_data)
# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


###############################################################################

import mysql.connector

# Connect to the MySQL server and the 'ecommerce' database
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
cursor = conn.cursor()

# Execute the SELECT query
cursor.execute("SELECT * FROM customer")

# Fetch all the results
records = cursor.fetchall()

# Print the records
for record in records:
    print(record)

# Close the cursor and connection
cursor.close()
conn.close()

###############################################################################

import mysql.connector

# Connect to the MySQL server and the 'ecommerce' database
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
cursor = conn.cursor()

# Execute the SELECT query
cursor.execute("SELECT * FROM product")

# Fetch all the results
records = cursor.fetchall()

# Print the records
for record in records:
    print(record)

# Close the cursor and connection
cursor.close()
conn.close()

###############################################################################

import mysql.connector

# Connect to the MySQL server and the 'ecommerce' database
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
cursor = conn.cursor()

# Execute the SELECT query
cursor.execute("SELECT * FROM order_details")

# Fetch all the results
records = cursor.fetchall()

# Print the records
for record in records:
    print(record)

# Close the cursor and connection
cursor.close()
conn.close()

import mysql.connector
import pandas as pd
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')


#####################################################################
#Identify the total number of customers city wise.
query = '''
SELECT city, COUNT(*) as total_customers
FROM customer
GROUP BY city
'''
customer_city_counts = pd.read_sql(query, conn)
print(customer_city_counts)

#####################################################################


import mysql.connector
import pandas as pd
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
#Identify the most frequent customers based on their order history.
query = '''
SELECT c.name, COUNT(o.order_id) as order_count
FROM customer c
JOIN order_details o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY order_count DESC
'''
most_frequent_customers = pd.read_sql(query, conn)
print(most_frequent_customers)


#####################################################################
#Determine the total number of products available by category.

query = '''
SELECT category, COUNT(*) as total_products
FROM product
GROUP BY category
'''
product_category_counts = pd.read_sql(query, conn)
print(product_category_counts)


#####################################################################
#Analyze the distribution of products across sub-categories.
query = '''
SELECT sub_category, COUNT(*) as total_products
FROM product
GROUP BY sub_category
'''
product_subcategory_counts = pd.read_sql(query, conn)
print(product_subcategory_counts)


#####################################################################
#Identify products with low stock levels.
query = '''
SELECT product_name, stock
FROM product
WHERE stock < 10
'''
low_stock_products = pd.read_sql(query, conn)
print(low_stock_products)


#####################################################################
#Calculate the average, maximum, and minimum prices for products.
query = '''
SELECT
    AVG(original_price) as avg_original_price,
    MAX(original_price) as max_original_price,
    MIN(original_price) as min_original_price,
    AVG(selling_price) as avg_selling_price,
    MAX(selling_price) as max_selling_price,
    MIN(selling_price) as min_selling_price
FROM product
'''
price_stats = pd.read_sql(query, conn)
print(price_stats)


#####################################################################
#Calculate the top 10 orders product wise.
query = '''
SELECT p.product_name, SUM(o.quantity) as total_quantity
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_quantity DESC
LIMIT 10
'''
top_10_orders = pd.read_sql(query, conn)
print(top_10_orders)


#####################################################################
#Analyze the order status distribution (e.g., pending, delivered).
query = '''
SELECT order_status, COUNT(*) as count
FROM order_details
GROUP BY order_status
'''
order_status_distribution = pd.read_sql(query, conn)
print(order_status_distribution)


#####################################################################
#Identify the most popular products based on order quantity.
query = '''
SELECT p.product_name, SUM(o.quantity) as total_quantity
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_quantity DESC
'''
most_popular_products = pd.read_sql(query, conn)
print(most_popular_products)


#####################################################################
#Calculate total revenue generated from orders product wise.
query = '''
SELECT p.product_name, SUM(o.total_price) as total_revenue
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.product_id
'''
revenue_product_wise = pd.read_sql(query, conn)
print(revenue_product_wise)


#####################################################################
#Calculate the total revenue generated from all orders.
query = '''
SELECT SUM(total_price) as total_revenue
FROM order_details
'''
total_revenue = pd.read_sql(query, conn)
print(total_revenue)


#####################################################################
#Calculate total revenue product category wise percentage.
query = '''
SELECT p.category, SUM(o.total_price) as total_revenue
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.category
'''
category_revenue = pd.read_sql(query, conn)
total_revenue_value = category_revenue['total_revenue'].sum()
category_revenue['percentage'] = (category_revenue['total_revenue'] / total_revenue_value) * 100
print(category_revenue)


#####################################################################
#Analyze the performance of different product categories in terms of sales.
query = '''
SELECT p.category, SUM(o.total_price) as total_revenue
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.category
'''
category_performance = pd.read_sql(query, conn)
print(category_performance)


#####################################################################
#Identify the most profitable products based on the difference between original and selling prices.
query = '''
SELECT p.product_name,
       (p.selling_price - p.original_price) as profit_margin
FROM product p
ORDER BY profit_margin DESC
'''
profitable_products = pd.read_sql(query, conn)
print(profitable_products)


#####################################################################
#Identify product names with the highest and lowest order quantities.
query = '''
SELECT p.product_name, SUM(o.quantity) as total_quantity
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_quantity DESC
LIMIT 1
'''
highest_ordered_product = pd.read_sql(query, conn)

query = '''
SELECT p.product_name, SUM(o.quantity) as total_quantity
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_quantity ASC
LIMIT 1
'''
lowest_ordered_product = pd.read_sql(query, conn)
print(highest_ordered_product)
print(lowest_ordered_product)


#####################################################################
#Identify customers with the highest and lowest order quantities by customer name.
query = '''
SELECT c.name, SUM(o.quantity) as total_quantity
FROM order_details o
JOIN customer c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_quantity DESC
LIMIT 1
'''
highest_ordering_customer = pd.read_sql(query, conn)

query = '''
SELECT c.name, SUM(o.quantity) as total_quantity
FROM order_details o
JOIN customer c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_quantity ASC
LIMIT 1
'''
lowest_ordering_customer = pd.read_sql(query, conn)
print(highest_ordering_customer)
print(lowest_ordering_customer)


#####################################################################
#Determine the most preferred payment modes.
query = '''
SELECT payment_mode, COUNT(*) as count
FROM order_details
GROUP BY payment_mode
'''
payment_mode_preference = pd.read_sql(query, conn)
print(payment_mode_preference)


#####################################################################
#Month wise total sales.
query = '''
SELECT DATE_FORMAT(order_date, '%Y-%m') as month, SUM(total_price) as total_sales
FROM order_details
GROUP BY month
'''
monthwise_sales = pd.read_sql(query, conn)
print(monthwise_sales)


#####################################################################
#Month and year wise total sales.
query = '''
SELECT DATE_FORMAT(order_date, '%Y-%m') as month_year, SUM(total_price) as total_sales
FROM order_details
GROUP BY month_year
'''
month_year_sales = pd.read_sql(query, conn)
print(month_year_sales)


#####################################################################
#Identify peak order date.
query = '''
SELECT order_date, COUNT(*) as order_count
FROM order_details
GROUP BY order_date
ORDER BY order_count DESC
LIMIT 1
'''
peak_order_date = pd.read_sql(query, conn)
print(peak_order_date)


#####################################################################
#Explore the distribution of customers across different cities.
query = '''
SELECT city, COUNT(*) as total_customers
FROM customer
GROUP BY city
'''
city_distribution = pd.read_sql(query, conn)
print(city_distribution)


#####################################################################
#Analyze whether certain products or categories are more popular in a specific city.
query = '''
SELECT c.city, p.category, SUM(o.total_price) as total_revenue
FROM order_details o
JOIN customer c ON o.customer_id = c.customer_id
JOIN product p ON o.product_id = p.product_id
GROUP BY c.city, p.category
'''
city_category_sales = pd.read_sql(query, conn)
print(city_category_sales)


#####################################################################
#Identify the top 10 best-selling products.
query = '''
SELECT p.product_name, SUM(o.quantity) as total_quantity
FROM order_details o
JOIN product p ON o.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_quantity DESC
LIMIT 10
'''
top_selling_products = pd.read_sql(query, conn)
print(top_selling_products)


#####################################################################
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='ecommerce')
cursor = conn.cursor()


#Identify the total number of customers City wise.
query = '''
SELECT city, COUNT(*) as total_customers
FROM customer
GROUP BY city
'''
customer_city_counts = pd.read_sql(query, conn)
plt.figure(figsize=(6, 6))
plt.pie(customer_city_counts['total_customers'], labels=customer_city_counts['city'], autopct='%1.1f%%', colors=plt.cm.Paired(range(len(customer_city_counts['city']))))
plt.title('Distribution of Customers by City')
plt.show()


#####################################################################
#Identify the most frequent customers based on their order history.

query = '''
SELECT c.name, COUNT(o.order_id) as order_count
FROM customer c
JOIN order_details o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY order_count DESC
LIMIT 10
'''
frequent_customers = pd.read_sql(query, conn)
plt.figure(figsize=(7, 5))
plt.bar(frequent_customers['name'], frequent_customers['order_count'], color='skyblue')
plt.xlabel('Customer Name')
plt.ylabel('Number of Orders')
plt.title('Top 10 Most Frequent Customers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


#####################################################################
#Determine the total number of products available by category.

query = '''
SELECT category, COUNT(*) as total_products
FROM product
GROUP BY category
'''
product_by_category = pd.read_sql(query, conn)
plt.figure(figsize=(6, 6))
plt.pie(product_by_category['total_products'], labels=product_by_category['category'], autopct='%1.1f%%', colors=plt.cm.Paired(range(len(product_by_category['category']))))
plt.title('Distribution of Products by Category')
plt.show()


#####################################################################
#Analyze the distribution of products across sub-categories.
query = '''
SELECT sub_category, COUNT(*) as total_products
FROM product
GROUP BY sub_category
'''
product_distribution = pd.read_sql(query, conn)
plt.figure(figsize=(8, 4))
plt.bar(product_distribution['sub_category'], product_distribution['total_products'], color='lightgreen')
plt.xlabel('Sub-Category')
plt.ylabel('Total Number of Products')
plt.title('Distribution of Products Across Sub-Categories')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


#####################################################################
#Identify products with low stock levels.
query = '''
SELECT product_id, product_name, stock
FROM product
WHERE stock < 100
ORDER BY stock ASC
'''
low_stock_products = pd.read_sql(query, conn)
plt.figure(figsize=(8, 4))
plt.bar(low_stock_products['product_name'], low_stock_products['stock'], color='salmon')
plt.xlabel('Product Name')
plt.ylabel('Stock Level')
plt.title('Products with Low Stock Levels')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


#####################################################################
#Calculate the average, maximum, and minimum selling prices for products.
query = '''
SELECT
    AVG(selling_price) AS average_price,
    MAX(selling_price) AS max_price,
    MIN(selling_price) AS min_price
FROM product
'''
price_stats = pd.read_sql(query, conn)
labels = ['Average Price', 'Maximum Price', 'Minimum Price']
values = [price_stats['average_price'][0], price_stats['max_price'][0], price_stats['min_price'][0]]
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=['blue', 'green', 'red'])
plt.xlabel('Price Type')
plt.ylabel('Price')
plt.title('Average, Maximum, and Minimum Selling Prices')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#####################################################################
#Calculate the top 10 orders product wise.
query = '''
SELECT
    p.product_name,
    SUM(od.total_price) AS total_sales
FROM
    order_details od
JOIN
    product p ON od.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    total_sales DESC
LIMIT 10;
'''
top_products = pd.read_sql(query, conn)
product_names = top_products['product_name']
total_sales = top_products['total_sales']
plt.figure(figsize=(8,6))
plt.pie(total_sales, labels=product_names, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(product_names))))
plt.title('Top 10 Products by Total Sales')
plt.axis('equal')
plt.show()


#####################################################################
#Analyze the order status distribution (e.g., pending, delivered)
query = '''
SELECT
    order_status,
    COUNT(*) AS order_count
FROM
    order_details
GROUP BY
    order_status
ORDER BY
    order_status;
'''
order_status_data = pd.read_sql(query, conn)
statuses = order_status_data['order_status']
counts = order_status_data['order_count']
plt.figure(figsize=(8, 5))
plt.plot(statuses, counts, marker='o', linestyle='-', color='b')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.title('Order Status Distribution')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#####################################################################
#Identify the most popular products based on order quantity.
query = '''
SELECT
    p.product_name,
    SUM(od.quantity) AS total_quantity
FROM
    order_details od
JOIN
    product p ON od.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    total_quantity DESC
LIMIT 10;
'''
product_popularity = pd.read_sql(query, conn)
product_names = product_popularity['product_name']
quantities = product_popularity['total_quantity']
plt.figure(figsize=(9, 6))
plt.barh(product_names, quantities, color='skyblue')
plt.xlabel('Total Quantity Ordered')
plt.ylabel('Product Name')
plt.title('Top 10 Most Popular Products Based on Order Quantity')
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.show()


#####################################################################
#Calculate total revenue generated from orders product wise.
query = '''
SELECT
    p.product_name,
    SUM(od.total_price) AS total_revenue
FROM
    order_details od
JOIN
    product p ON od.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    total_revenue DESC;
'''
df_revenue = pd.read_sql(query, conn)
product_names = df_revenue['product_name']
total_revenues = df_revenue['total_revenue']
plt.figure(figsize=(9, 6))
plt.barh(product_names, total_revenues, color='skyblue')
plt.xlabel('Total Revenue ($)')
plt.ylabel('Product Name')
plt.title('Total Revenue Generated from Orders by Product')
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.show()


#######################################################################
#Calculate total revenue product category wise percentage.
query = '''
SELECT
    p.category,
    SUM(od.total_price) AS total_revenue
FROM
    order_details od
JOIN
    product p ON od.product_id = p.product_id
GROUP BY
    p.category;
'''
df_revenue_by_category = pd.read_sql(query, conn)
df_revenue_by_category['percentage_revenue'] = (df_revenue_by_category['total_revenue'] / df_revenue_by_category['total_revenue'].sum()) * 100
plt.figure(figsize=(10, 7))
plt.fill_between(df_revenue_by_category['category'],
                 df_revenue_by_category['percentage_revenue'],
                 color="skyblue", alpha=0.4)
plt.plot(df_revenue_by_category['category'],
         df_revenue_by_category['percentage_revenue'],
         color="Slateblue", alpha=0.6, linewidth=2)
plt.xlabel('Product Category')
plt.ylabel('Percentage Revenue (%)')
plt.title('Revenue Distribution by Product Category')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


#####################################################################
#Calculate the total revenue generated from all orders.
query = '''
SELECT
    SUM(total_price) AS total_revenue
FROM
    order_details;
'''
df_revenue = pd.read_sql(query, conn)
total_revenue = df_revenue['total_revenue'][0]
categories = ['Total Revenue']
values = [total_revenue]
plt.figure(figsize=(8, 6))
plt.scatter(categories, values, color='blue', s=100, alpha=0.7)
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.title('Total Revenue from All Orders')
plt.grid(True)
plt.tight_layout()
for i, txt in enumerate(values):
    plt.annotate(f'${txt:,.2f}', (categories[i], values[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()


################################################################################################
#Identify the most profitable products based on the difference between original and selling prices.
query = '''
SELECT
    product_id,
    product_name,
    (selling_price - original_price) AS profit
FROM
    product
ORDER BY
    profit DESC;
'''
df_profit = pd.read_sql(query, conn)
products = df_profit['product_name']
profits = df_profit['profit']
plt.figure(figsize=(9, 6))
plt.step(products, profits, where='mid', color='green', linestyle='-', marker='o')
plt.xlabel('Product Name')
plt.ylabel('Profit ($)')
plt.title('Profitability of Products Based on Price Difference')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()


#####################################################################
#Identify product names with the highest and lowest order quantities.
query = '''
SELECT
    p.product_name,
    SUM(od.quantity) AS total_quantity
FROM
    order_details od
JOIN
    product p ON od.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    total_quantity DESC;
'''
df_quantity = pd.read_sql(query, conn)
products = df_quantity['product_name']
quantities = df_quantity['total_quantity']
plt.figure(figsize=(9, 5))
plt.fill_between(products, quantities, color='skyblue', alpha=0.4)
plt.plot(products, quantities, color='Slateblue', alpha=0.6, linewidth=2)
plt.xlabel('Product Name')
plt.ylabel('Total Quantity Ordered')
plt.title('Product Order Quantities')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()


####################################################################################
#Identify customers with the highest and lowest order quantities by customer name.
query = '''
SELECT
    c.name AS customer_name,
    SUM(od.quantity) AS total_quantity
FROM
    order_details od
JOIN
    customer c ON od.customer_id = c.customer_id
GROUP BY
    c.name
ORDER BY
    total_quantity DESC;
'''
df_quantity = pd.read_sql(query, conn)
customers = df_quantity['customer_name']
quantities = df_quantity['total_quantity']
plt.figure(figsize=(9, 5))
plt.bar(customers, quantities, color='skyblue')
plt.xlabel('Customer Name')
plt.ylabel('Total Quantity Ordered')
plt.title('Total Order Quantities by Customer')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#####################################################################
#Determine the most preferred payment modes.
query = '''
SELECT
    payment_mode,
    COUNT(*) AS total_orders
FROM
    order_details
GROUP BY
    payment_mode
ORDER BY
    total_orders DESC;
'''
df_payment_modes = pd.read_sql(query, conn)
payment_modes = df_payment_modes['payment_mode']
total_orders = df_payment_modes['total_orders']
plt.figure(figsize=(8, 5))
plt.fill_between(payment_modes, total_orders, color="skyblue", alpha=0.4)
plt.plot(payment_modes, total_orders, color="Slateblue", alpha=0.6, linewidth=2)
plt.xlabel('Payment Mode')
plt.ylabel('Total Orders')
plt.title('Total Orders by Payment Mode')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


#####################################################################
#Month wise total sales.
query = '''
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(total_price) AS total_sales
FROM
    order_details
GROUP BY
    month
ORDER BY
    month;
'''
df_monthly_sales = pd.read_sql(query, conn)
months = df_monthly_sales['month']
total_sales = df_monthly_sales['total_sales']
plt.figure(figsize=(8, 4))
plt.bar(months, total_sales, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Month-Wise Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#####################################################################
#Identify peak order date.
query = '''
SELECT
    DATE(order_date) AS order_date,
    COUNT(*) AS order_count
FROM
    order_details
GROUP BY
    DATE(order_date)
ORDER BY
    order_count DESC
LIMIT 5;
'''
df_peak_orders = pd.read_sql(query, conn)
dates = df_peak_orders['order_date']
order_counts = df_peak_orders['order_count']
plt.figure(figsize=(8, 4))
plt.bar(dates, order_counts, color='skyblue')
plt.xlabel('Order Date')
plt.ylabel('Number of Orders')
plt.title('Top 10 Peak Order Dates')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#####################################################################
#Explore the distribution of customers across different cities.
query = '''
SELECT
    city,
    COUNT(*) AS customer_count
FROM
    customer
GROUP BY
    city
ORDER BY
    customer_count DESC;
'''
df_customer_distribution = pd.read_sql(query, conn)
cities = df_customer_distribution['city']
customer_counts = df_customer_distribution['customer_count']
plt.figure(figsize=(8, 4))
plt.plot(cities, customer_counts, marker='o', linestyle='-', color='b')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.title('Customer Distribution Across Cities')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()


#####################################################################
#Analyze whether certain products or categories are more popular in a specific city.
query = '''
SELECT
    c.city,
    p.product_name,
    SUM(od.quantity) AS total_quantity
FROM
    order_details od
JOIN
    customer c ON od.customer_id = c.customer_id
JOIN
    product p ON od.product_id = p.product_id
GROUP BY
    c.city, p.product_name
ORDER BY
    c.city, total_quantity DESC;
'''
df_product_popularity = pd.read_sql(query, conn)
cities = df_product_popularity['city'].unique()
products = df_product_popularity['product_name'].unique()
df_pivot = df_product_popularity.pivot_table(index='city', columns='product_name', values='total_quantity', fill_value=0)
plt.figure(figsize=(9, 6))
df_pivot.plot(kind='area', stacked=True, figsize=(12, 8))
plt.xlabel('City')
plt.ylabel('Total Quantity')
plt.title('Product Popularity by City')
plt.legend(title='Products')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()



#####################################################################
#Identify the best-selling products.
query = '''
SELECT
    p.product_name,
    SUM(od.quantity) AS total_quantity_sold
FROM
    order_details od
JOIN
    product p ON od.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    total_quantity_sold DESC;
'''
df_best_selling_products = pd.read_sql(query, conn)
product_names = df_best_selling_products['product_name']
total_quantities = df_best_selling_products['total_quantity_sold']
plt.figure(figsize=(9, 7))
plt.barh(product_names, total_quantities, color='skyblue')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product Name')
plt.title('Best-Selling Products')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


#####################################################################
#Identify top 10 slow-moving products based on low sales.
query = '''
SELECT
    p.product_name,
    IFNULL(SUM(od.quantity), 0) AS total_quantity_sold
FROM
    product p
LEFT JOIN
    order_details od ON p.product_id = od.product_id
GROUP BY
    p.product_name
ORDER BY
    total_quantity_sold ASC
LIMIT 10;
'''
df_slow_moving_products = pd.read_sql(query, conn)
product_names = df_slow_moving_products['product_name']
total_quantities = df_slow_moving_products['total_quantity_sold']
plt.figure(figsize=(9, 6))
plt.barh(product_names, total_quantities, color='lightcoral')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product Name')
plt.title('Top 10 Slow-Moving Products')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

conn.commit()
cursor.close()
conn.close()