# Take user input and write to output.txt
user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(user_input + "\n")
    
# Append additional data
additional_input = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(additional_input + "\n")

# Read and display the final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())