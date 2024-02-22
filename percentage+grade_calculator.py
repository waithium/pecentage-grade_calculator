'''
    percentage calculator + grade and pass or fail status displayer
    basic algo :-
    1. Inputs marks.
    2. Calculates percentage.
    3. Print percentage.
    4. Calculates grades and pass/fail. Print.
    5. Prints grades and shows pass/fail.
    6. Exit
'''

#function for calculating percentage
def calPercentage(obtMarks,totalMarks):
    percentage = ( obtMarks / totalMarks ) * 100
    return percentage

#taking input
obtMarks = float(input("Enter the toal obtained number of marks: "))
totalMarks = float(input("Enter the total number of numbers: "))

percentage = str(calPercentage(obtMarks, totalMarks))

print("Your percentage is : " + percentage + "%")

percentage = float(percentage)

if percentage < 40:
    print("You have failed the exam!! \nBetter luck next time (keep working hard don't worry lil bro/sis)")

elif percentage >= 40 and percentage < 50 :
    print("Your grade is P \n Congratulations you passed!!")

elif percentage >= 50 and percentage < 60 :
    print("Your grade is D \n Congratulations you passed!!")

elif percentage >= 60 and percentage < 70 :
    print("Your grade is C \n Congratulations you passed!!")

elif percentage >= 70 and percentage < 80 :
    print("Your grade is B \n Congratulations you passed!!")

elif percentage >= 80 and percentage < 90 :
    print("Your grade is A \n Congratulations you passed!!")

elif percentage >= 90 and percentage < 100 :
    print("Your grade is O \n Congratulations you passed!!")
