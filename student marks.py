# Program to calculate total and average marks

# Input marks for three subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate total
total = mark1 + mark2 + mark3

# Calculate average
average = total / 3

# Display results
print("Total marks:", total)
print("Average marks:", round(average, 2))