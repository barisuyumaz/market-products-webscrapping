# 🛒 Market Product Scraper with Selenium & PostgreSQL

This project scrapes product data from the **ŞOK Market** official website using `Selenium`, extracts key product attributes (name, brand, price, origin, stock status, etc.), and stores them in a structured **PostgreSQL database**. The collected data is later analyzed using SQL queries to generate insightful charts and reports.

> ✅ Intended for educational and non-commercial use only.

---

## 🚀 Features

- Scrapes all main and subcategories from sokmarket.com.tr
- Extracts detailed product information:
  - Name, brand, origin, price, stock info, category
- Stores the data into a PostgreSQL table
- Includes sample SQL queries with visual output (brand frequency, category breakdown, foreign product distribution)

---

## 🐍 Tech Stack

- **Python 3.x**
- **Technologies:**
  - `selenium` — browser automation
  - `beautifulsoup4` — HTML parsing
  - `webdriver-manager` — auto-installs ChromeDriver
  - `psycopg2` — PostgreSQL connector for Python

---

## ⚙️ Setup Instructions

### 1. Install Required Python Libraries

```bash
pip install selenium
pip install beautifulsoup4
pip install webdriver-manager
pip install psycopg2
```

### 2. ChromeDriver Setup

You **do NOT need to manually download chromedriver.exe**.

The script uses `webdriver-manager`, which:
- Detects your installed Chrome version
- Automatically downloads the matching ChromeDriver
- Configures Selenium to use it

> ✅ Just make sure Google Chrome is installed on your machine.

To check your Chrome version:
- Open Chrome → 3-dot Menu → Help → About Google Chrome

### 3. Configure PostgreSQL Connection

Edit `python_to_pgadmin.py`:

```python
hostname = "localhost"
database = "your_database"
username = "your_username"
pwd = "your_password"
port_id = 5432  # adjust if needed
```

Also ensure you have the following table created in your PostgreSQL database:

```sql
CREATE TABLE products (
  id INT PRIMARY KEY,
  product_code TEXT,
  product_name TEXT,
  product_price TEXT,
  product_brand TEXT,
  stock_info TEXT,
  origin TEXT,
  product_category TEXT,
  product_type TEXT
);
```

---

## ▶️ How to Run

Just run:

```bash
python marketveriler-selenium.py
```

> ⏱️ The script may take some time depending on the number of products and categories being scraped.

---

## 📊 Example SQL Queries & Visual Results

### 🔍 1. View All Products

```sql
SELECT * FROM products;
```

![All Products](https://user-images.githubusercontent.com/44267861/226697720-2caaacff-dd98-44b8-b663-d90112f18dcc.png)

---

### 🌍 2. Products by Country of Origin (excluding Turkey)

```sql
SELECT origin, COUNT(*) 
FROM products 
WHERE origin != 'TÜRKİYE' 
GROUP BY origin 
ORDER BY origin;
```

![Foreign Origins](https://user-images.githubusercontent.com/44267861/226697996-a0865e17-17bb-47c2-8333-79d4d0d44809.png)

---

### 🏷️ 3. Top 10 Brands by Product Count

```sql
SELECT product_brand, COUNT(*) AS itemcount 
FROM products 
WHERE product_brand != '' 
GROUP BY product_brand 
ORDER BY itemcount DESC 
LIMIT 10;
```

![Top Brands](https://user-images.githubusercontent.com/44267861/226698814-e2b0d28e-0476-46f5-8b99-01c8a2e4502c.png)

---

### 📦 4. Most Common Product Categories

```sql
SELECT product_category, COUNT(*) AS itemcount 
FROM products 
GROUP BY product_category 
ORDER BY itemcount DESC;
```

![Category Count - Bar](https://user-images.githubusercontent.com/44267861/226699546-a189e2aa-aa93-4883-a857-8616f63a8e80.png)

![Category Count - Pie](https://user-images.githubusercontent.com/44267861/226699564-d708e1dc-5531-4624-a27d-f6a8206177e7.png)

---

## 📁 Project Structure

```
📦 market-products-webscrapping/
├── marketveriler-selenium.py       # Main scraping script
├── python_to_pgadmin.py            # PostgreSQL connector
├── README.md                       # Documentation
```

---

## ✅ Example Use Cases

- Monitoring e-commerce product availability and prices
- Analyzing imported vs. domestic product distributions
- Brand frequency and category insights in retail
- Feeding clean structured data into BI dashboards

---

## 👨‍💻 Author

**Barış Uyumaz**  
🔗 [GitHub](https://github.com/barisuyumaz)

---

## 📄 License

This project is provided for educational and research purposes only.
