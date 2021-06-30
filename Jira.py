import pickle
import gspread

# Указываем путь к JSON
gc = gspread.service_account(filename= r'C:\Users\натали\PycharmProjects\pythonProject\JiraSupp\python-318418-abbe0bd95ea9.json')
#Открываем тестовую таблицу
sh = gc.open("TESTSHEETS")

worksheet_list = sh.worksheets()
#Выводим значение ячейки A1
#print(sh.sheet1.get('A1'))

nedded_list = sh.worksheet('Operatives & Gear')
values_list = nedded_list.col_values(5)
print(values_list)