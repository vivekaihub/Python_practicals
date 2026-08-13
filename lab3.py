print("✨✨✨✨✨✨✨✨College Admission Eligiblity Check✨✨✨✨✨✨✨✨")
age=int(input("Enter age of student:"))
marks=int(input("Enter marks:"))

if(age>=17 and age<=25):
    print("Eligible for admission")

    if(marks>60):
        print("Eligible for b.tech")

        if(marks>85):
            print("Eligible for AIML.")
        elif(marks>75):
            print("Eligible for CSE.")
        else:
            print("Eligible for MECH,ENTC,CIVIL,ELECTRICAL.")

    else:
        print("Not eligible for b.tech")
else:
    print("Not eligible for admission") 
    
    
print("✨✨✨✨✨✨✨✨Thank You✨✨✨✨✨✨✨✨")