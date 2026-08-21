print("===== WORD COUNTER =====")

paragraph = input("Enter a paragraph: ")

count = paragraph.lower().split().count("python")

print("\n----- RESULT -----")
print("The word 'python' appears:", count, "time(s)")