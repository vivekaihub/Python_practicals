# Accept marks for three subjects

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total = sub1 + sub2 + sub3
average = total / 3

# Print scorecard
print("\n----- SCORECARD -----")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))