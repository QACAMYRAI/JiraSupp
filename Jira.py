import pickle
import gspread
from selenium import webdriver

# Указываем путь к JSON
gc = gspread.service_account(filename= r'D:\Myproject\JiraSupp\python-318418-abbe0bd95ea9.json')
#Открываем тестовую таблицу
sh = gc.open("TESTSHEETS")

worksheet_list = sh.worksheets()
#Выводим значение ячейки A1
#print(sh.sheet1.get('A1'))

nedded_list = sh.worksheet('Operatives & Gear')
values_list = nedded_list.col_values(5)

allelements = []
for elements in values_list:
    if elements[:4] == "http":
            if "\n" in elements:
                for i in (elements.split("\n")):
                    if i not in("", ' ', '', ):
                        allelements.append(i)
            else:
                allelements.append(elements)

print(*allelements, sep="\n")
