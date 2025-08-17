#1
import json
import csv

js_path = "C:/Users/anton/Downloads/Рабочий стол/students.json"
with open(js_path, 'r', encoding='utf-8') as f:
    students = json.load(f)

print(len(students))
old_stud = students[0]
for student in students:
    if student["возраст"] > old_stud["возраст"]:
        old_stud = student
print(old_stud["имя"], old_stud["возраст"], old_stud["город"])

subject = "Python"
count = 0
for student in students:
    if subject in student["предметы"]:
        count += 1
print(count)

#2
total_sum = 0
max_price = 0
max_product = ''
monthly_totals = {}
csv_path = "C:/Users/anton/Downloads/Рабочий стол/sales.csv"
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)

    for row in reader:
        if len(row) < 3:
            continue
        date = row[0]
        product = row[1]
        price = float(row[2])

    total_sum += price

    if price > max_price:
        max_price = price
        max_product = product

    month = date[:7]
    if month not in monthly_totals:
        monthly_totals[month] = 0
    monthly_totals[month] += price
print(f"Общая {total_sum}")
print(f"Самый дорогой: {max_product} — {max_price}")
print("Сумма по месяцах:")
for month in monthly_totals:
    print(f"{month}: {monthly_totals[month]}")

js2_path = "C:/Users/anton/Downloads/Рабочий стол/employees.json"
with open(js2_path, 'r', encoding='utf-8') as f:
    emloyess = json.load(f)
print("Employess:")
for e in emloyess:
    print(e['имя'], "-", e['должность'])


best_id = None
best_perfomance = -1
total = 0
count = 0

csv2_path = "C:/Users/anton/Downloads/Рабочий стол/perfomance.csv"
with open(csv2_path, 'r', encoding='utf-8') as f:
    reader2 = csv.reader(f)
    next(reader2)
    for row in reader2:
        employee_id = int(row[0])
        perfomance = float(row[1])

        total += perfomance
        count += 1

        if perfomance > best_perfomance:
            best_perfomance = perfomance
            best_id = employee_id

avg = total / count if count else 0
print(f"Best employ: {best_id}, mark {best_perfomance}")
print(f"Avg mark: {avg:.2f}")

