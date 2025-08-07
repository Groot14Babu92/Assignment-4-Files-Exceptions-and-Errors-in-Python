try:
    with open("myTxt.txt", "r") as file1:
        for line in file1:
            print(line.strip())

    with open("myTxt1.txt", "r") as file1:
        for line in file1:
            print(line.strip())

except FileNotFoundError:
    print("File not found. Please ensure 'myTxt1.txt' exists in the current directory.")