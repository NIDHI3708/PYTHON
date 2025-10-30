Physics = int(input("Marks in Physics out of 100:"))
Chemistry = int(input("Marks in Chemistry out of 100:"))
Mathematics = int(input("Marks in Mathematics out of 100:"))
Total = Physics + Chemistry + Mathematics
Percentage = (Total/300)*100
if (Percentage >= 40):
    print("The student has passed the examination.")
elif(Percentage >= 33):
    print("The student has just passed the examination, need to work hard.")
else:
    print("The student has failed the examination, better luck next time.")

print("Total marks obtained:", Total)
print("Percentage obtained:", Percentage)