

def main():

    with open('input.txt', 'r', 'utf-8')as file:
        open_file = file.readlines()
    return open_file


print(main())