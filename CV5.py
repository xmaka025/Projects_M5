import os
import shutil

os.makedirs("Управление_файлами", exist_ok=True)
with open("Управление_файлами/file1.txt", "w", encoding="utf-8") as f1:
    f1.write("Кто смотрит вскользь через ограду.")

with open("Управление_файлами/file1.txt", "r", encoding="utf-8") as f1:
    file_cont = f1.read()
print(file_cont)

with open("Управление_файлами/file2.txt", "w", encoding="utf-8") as f2:
    f2.write("На тень деревьев, злак долин.")

with open("Управление_файлами/file2.txt", "r", encoding="utf-8") as f2:
    file_cont2 = f2.read()
print(file_cont2)

if os.path.exists("Управление_файлами/file1.txt"):
    os.remove("Управление_файлами/file1.txt")
os.makedirs("Управление_файлами/Поддиректория", exist_ok=True)

path = "Управление_файлами/Поддиректория/file2.txt"
if os.path.exists(path):
    os.remove(path)

shutil.move("Управление_файлами/file2.txt", path)
print("Фаил перемещен")
shutil.rmtree("Управление_файлами")
print("Папка удалена")