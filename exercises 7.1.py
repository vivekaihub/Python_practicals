print("===== AUTOMATED EMAIL SCANNER =====")

text = input("Enter the email text: ")

at_count = text.count("@")
dot_count = text.count(".")
exclamation_count = text.count("!")

print("\n----- SCAN RESULT -----")
print("@ occurs:", at_count, "time(s)")
print(". occurs:", dot_count, "time(s)")
print("! occurs:", exclamation_count, "time(s)")