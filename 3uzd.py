# 3.	Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu. (3 punkti)


def funk_lasit(file_path):
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            # Read the lines of the file
            lines = file.readlines()

            # Check if the file has at least three rows
            if len(lines) >= 3:
                third_row_content = lines[2].strip()  # Index 2 corresponds to the third row
                print("3. rindas saturs:")
                print(third_row_content)
            else:
                print("Failā nav vismaz 3 rindas")
    except FileNotFoundError:
        print(f"Fails '{file_path}' nav atrasts")
    except Exception as e:
        print(f"Notikusi kļūda {e}")


file_path = 'fails.txt'
funk_lasit(file_path)