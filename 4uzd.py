# 4.	Izveidot Python programmu, kur  lietotājs ievada par faila nosaukumu un faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.  Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas! (8 punkti)


def read_and_print(file_name, file_format):
    try:
        file_path = f"{file_name}.{file_format}"

        with open(file_path, 'r', 'utf-8') as file:
            content = file.read()
            print(f"Faila {file_name}.{file_format} saturs:")
            print(content)
    except FileNotFoundError:
        print(f"Fails'{file_name}.{file_format}' nav atrasts")
    except Exception as e:
        print(f"Notikusui kļūda: {e}")

def main():

    file_name = input("Ievadi faila nosaukumu: ")
    file_format = input("ievadi faila paplašinājumu: ")


    read_and_print(file_name, file_format)

if __name__ == "__main__":
    main()