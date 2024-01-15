# 2.	Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila. (3 punkti)

import csv

def read_and_print(file_path):
    try:
        with open(file_path, 'r', newline='', encoding = 'utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            print("Dati no otrās kolonnas: ")
            for row in csv_reader:

                if len(row) > 1:
                    print(row[1].strip())  
                else:
                    print("Rindai nav otrās kolonnas")
    except FileNotFoundError:
        print(f"Fails '{file_path}' nav atrasts")
    except Exception as e:
        print(f"Notikusi kļūda {e}")


file_path = 'aaa.csv'
read_and_print(file_path)