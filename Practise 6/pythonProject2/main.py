import requests
from bs4 import BeautifulSoup
import sqlite3

# Визначаємо URL категорії розпилювачів
url = "https://rozetka.com.ua/ua/sprayers/c156378"

# Отримуємо HTML сторінку
response = requests.get(url)
webpage = response.text

# Парсимо HTML за допомогою BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Визначаємо поля для збору даних: назва продукту, ціна, посилання
products = []
for item in soup.find_all("div", class_="goods-tile__inner"):
    title = item.find("span", class_="goods-tile__title").text.strip()
    price = item.find("span", class_="goods-tile__price-value").text.strip()
    link = item.find("a", class_="goods-tile__heading")["href"]
    products.append((title, price, link))

# Створюємо базу даних і таблицю для зберігання даних
conn = sqlite3.connect('rozetka_products.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS sprayers
          ([id] INTEGER PRIMARY KEY, [title] TEXT, [price] TEXT, [link] TEXT)
          ''')

# Вносимо дані в таблицю
for product in products:
    c.execute('''
              INSERT INTO sprayers (title, price, link)
              VALUES (?, ?, ?)
              ''', (product[0], product[1], product[2]))

# Зберігаємо зміни і закриваємо з'єднання
conn.commit()
conn.close()

print("Дані успішно збережені в базі даних.")
