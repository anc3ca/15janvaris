# 1.Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). 


def read_and_print(file_path):
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as error:
        print(f"An error occurred: {error}")

# Replace 'your_file.txt' with the actual path of your text file
file_path = 'your_file.txt'
read_and_print(file_path)