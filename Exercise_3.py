from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
def read_sales_data(file_path): # Ф-я принимает путь к файлу и возвращает список продаж
    with open(file_path, "r", encoding='utf-8') as file:
        sales_list = []
        for line in file:
            temp_list = line.strip().split(", ")
            map = {"product_name": temp_list[0], "quantity": int(temp_list[1]), "price": int(temp_list[2]),
                   "date": datetime.strptime(temp_list[3], '%Y-%m-%d').date().isoformat()}
            sales_list.append(map)
        return sales_list
def total_sales_per_product(sales_data): # Ф-я принимает список продаж и возвращает словарь,
                                         # где ключ - название продукта,
                                         # а значение общая сумма продаж этого продукта
    total_sales_per_product_m = {}
    for sale in sales_data:
        total_sales_per_product_m[sale["product_name"]] = sale["quantity"] * sale["price"] + total_sales_per_product_m.get(sale["product_name"], 0)
    return total_sales_per_product_m
def sales_over_time(sales_data): # Ф-я принимает список продаж и возвращает словарь,
                                 # где ключ - дата,
                                 # а значение общая сумма продаж за эту дату
    sales_over_time_m = {}
    for sale in sales_data:
        sales_over_time_m[sale["date"]] = sale["quantity"] * sale["price"] + sales_over_time_m.get(
            sale["date"], 0)
    return sales_over_time_m

print("Введите путь к файлу:")
file_path = input()
sales_data = read_sales_data(file_path)
total_sales_per_product_m = total_sales_per_product(sales_data) # Сумма продаж по продуктам
sales_over_time_m = sales_over_time(sales_data) # Сумма продаж по датам
max_revenue_product = max(total_sales_per_product_m, key=total_sales_per_product_m.get)
print("Продукт с наибольшей выручкой:", max_revenue_product)
max_sales_over_time = max(sales_over_time_m, key=sales_over_time_m.get)
print("День с наибольшей суммой продаж:", max_sales_over_time)

#Вывод графика сумм продаж по продуктам
x = np.array([x for x in range(len(total_sales_per_product_m.keys()))])
plt.xticks(x, total_sales_per_product_m.keys())
plt.plot(x, total_sales_per_product_m.values(), linestyle='None', marker='o')
plt.grid(True)
plt.show()
#Вывод графика сумм продаж по датам
x = np.array([x for x in range(len(sales_over_time_m.keys()))])
plt.xticks(x, sales_over_time_m.keys())
plt.plot(x, sales_over_time_m.values(), marker='o')
plt.grid(True)
plt.show()
