# 1.Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). 


def read_and_print(file_path):

    try:
        with open(file_path, 'r', encoding = 'utf8') as file:
            content = file.read()
            print("Datnes saturs:")
            print(content)
    except FileNotFoundError:
        print(f"Fails '{file_path}' nav atrasts")
    except Exception as error:
        print(f"Notikusi kļūda: {error}")

file_path = 'fails.txt'
read_and_print(file_path)