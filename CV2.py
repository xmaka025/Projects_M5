import csv

input_path = "C:/Users/anton/Downloads/Рабочий стол/prices.txt"
output_path = "C:/Users/anton/Downloads/Рабочий стол/prices.csv"

with open(input_path, 'r', encoding='utf-8') as txt_file:
    reader = csv.reader(txt_file, delimiter='\t')
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Count', 'Price'])
        for row in reader:
            writer.writerow(row)

print('ok')

total = 0
with open(output_path, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        count = int(row['Count'])
        price = int(row['Price'])
        total += count * price

print(f"Общая сумма: {total} рублей.")
