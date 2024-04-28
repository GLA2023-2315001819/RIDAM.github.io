#  # P1)  WAP on printing the numbers acc to user input for choice taken for reverse order or forward order and take choice for printing its output in either row wise or column wise by taking starting pt , ending pt and updation/.
#
start=int(input("enter the starting point:"))
end=int(input("enter the ending point:"))
step=int(input("enter the step:"))

rev_choice= input("Do you want to print in reverse order?(yes/no):").lower()
rev_order= True if rev_choice== "yes" else False

row_column_choice= input("Do you want to print in row-wise or column-wise?(row/column)").lower()
row_wise= True if row_column_choice== "row" else False

numbers = range (start,end,step) if not rev_order else range (end,start,-step)

if row_wise:
    for num in numbers:
        print(num, end =" ")
    print()
else:
    for num in numbers:
        print(num)

# OUTPUT:-
# enter the starting point:1
# enter the ending point:5
# enter the step:1
# Do you want to print in reverse order?(yes/no):yes
# Do you want to print in row-wise or column-wise?(row/column)row
# 5432

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # P2 BASIC CALCULATOR
#
print("select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")


n1= float(input("enter the first number:"))
n2= float(input("enter the second number:"))
choice = input("enter the operations (1/2/3/4):")

if choice =="1" :
    n= n1+n2
    print("Addition of both numbers is",n)
elif choice =="2" :
    n= n1-n2
    print("Subtraction of both numbers  is",n)
elif choice =="3" :
    n= n1*n2
    print("Multiplication of both number is",n)
elif choice =="4" :
    if n2==0:
        print("CAN'T DIVIDE BY ZERO")
    else:
        n= n1/n2
        print("Division of both number is",n)

else:
    print("Invalid input")

# OUTPUT:-
# Select operation:
# 1. Add
# 2. Subtract
# 3. Multiplication
# 4. Division
# enter the first number:2
# enter the second number:3
# enter the operations (1/2/3/4):4
# Division of both number is 0.6666666666666666

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#
# P3 GRADING SYSTEM
class Student:
    pass

student1 = Student()
student1.name = input("Name of first student name:")
student1.math_grade = int(input("enter the Math marks"))
student1.science_grade = int(input("enter the science marks"))
student1.history_grade = int(input("enter the history marks"))

student2 = Student()
student2.name = input("enter the second student name :")
student2.math_grade = int(input("enter the math marks"))
student2.science_grade = int(input("enter the science marks"))
student2.history_grade = int(input("enter the history marks"))

student3 = Student()
student3.name = input("enter the third student name:")
student3.math_grade = int(input("enter the Math marks"))
student3.science_grade = int(input("enter the science marks"))
student3.history_grade = int(input("enter the history marks"))

student1_average = (student1.math_grade + student1.science_grade + student1.history_grade) / 3
student2_average = (student2.math_grade + student2.science_grade + student2.history_grade) / 3
student3_average = (student3.math_grade + student3.science_grade + student3.history_grade) / 3

def get_grade_letter(average_grade):
    if average_grade >= 90:
        return "A"
    elif 80 <= average_grade < 90:
        return "B"
    elif 70 <= average_grade < 80:
        return "C"
    elif 60 <= average_grade < 70:
        return "D"
    else:
        return "F"

student1_grade_letter = get_grade_letter(student1_average)
student2_grade_letter = get_grade_letter(student2_average)
student3_grade_letter = get_grade_letter(student3_average)

print("Report Cards:")
print(f"Student: {student1.name}, Average Grade: {student1_average}, Grade: {student1_grade_letter}")
print(f"Student: {student2.name}, Average Grade: {student2_average}, Grade: {student2_grade_letter}")
print(f"Student: {student3.name}, Average Grade: {student3_average}, Grade: {student3_grade_letter}")

# OUTPUT:
# Name of first student name:RIDAM
# enter the Math marks52
# enter the science marks12
# enter the history marks45
# enter the second student name :KAUSHAL
# enter the math marks21
# enter the science marks23
# enter the history marks45
# enter the third student name:KSHITIJ
# enter the Math marks2
# enter the science marks23
# enter the history marks15
# Report Cards:
# Student: RIDAM, Average Grade: 36.333333333333336, Grade: F
# Student: KAUSHAL, Average Grade: 29.666666666666668, Grade: F
# Student: KSHITIJ, Average Grade: 13.333333333333334, Grade: F

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# P4 GUESSING THE NUMBER
import random

print("Welcome to the Guessing Game")

s = random.randint(1, 100)

while True:
    g = int(input("Guess the number (between 1 and 100): "))

    if (g == s):
        print("Congratulations! You guessed the correct number!")
        break
    elif (g < s):
        print("its too low, Try guessing higher.")
    else:
        print("its too high, Try guessing lower.")

# OUTPUT:
# Welcome to the Guessing Game
# Guess the number (between 1 and 100): 10
# its too low, Try guessing higher.
# Guess the number (between 1 and 100): 20
# Congratulations! You guessed the correct number!

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# P5 ROCK PAPER SCISSORS
import random

while True:
    uc = input("Enter your choice (rock, paper, scissors): ").lower()
    c = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chooses:", c)

    if uc == c:
        print("It's a tie!")
    elif (uc == 'rock' and c == 'scissors') or \
         (uc == 'paper' and c == 'rock') or \
         (uc == 'scissors' and c == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    o = input("Do you want to play again? (yes/no): ").lower()
    if o != 'yes':
        print("Thanks for playing!")
        break

# OUTPUT:
# Enter your choice (rock, paper, scissors): ROCK
# Computer chooses: scissors
# You win!
# Do you want to play again? (yes/no): NO
# Thanks for playing!

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# P6 ROLL THE DICE GAME
import random

print("Welcome to RollTheDice!")
while True:
    input("Press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)
    print("You rolled:", dice_roll)
    play_again = input("Do you want to roll again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
# OUTPUT:-
# Welcome to RollTheDice!
# Press Enter to roll the dice...
# You rolled: 5
# Do you want to roll again? (yes/no): yes
# Press Enter to roll the dice...
# You rolled: 2
# Do you want to roll again? (yes/no): no
# Thanks for playing!

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# P7 INVENTORY SYSYTEM FOR VEGETABLES SHOP

VEG1_name = input("Enter the name of the vegetable: ")
VEG1_price = float(input("Enter the price per kg: "))
VEG1_quantity = int(input("Enter the available quantity in kg: "))

VEG2_name = input("Enter the name of the vegetable: ")
VEG2_price = float(input("Enter the price per kg: "))
VEG2_quantity = int(input("Enter the available quantity in kg: "))

VEG3_name = input("Enter the name of the vegetable: ")
VEG3_price = float(input("Enter the price per kg: "))
VEG3_quantity = int(input("Enter the available quantity in kg: "))

VEG1_total = VEG1_price * VEG1_quantity
VEG2_total = VEG2_price * VEG2_quantity
VEG3_total = VEG3_price * VEG3_quantity

print("Vegetable Inventory:")
print(VEG1_name + ": Rs" + str(VEG1_price) + " per kg - Available Quantity: " + str(VEG1_quantity) + " kg - Total Price: Rs" + str(VEG1_total))
print(VEG2_name + ": Rs" + str(VEG2_price) + " per kg - Available Quantity: " + str(VEG2_quantity) + " kg - Total Price: Rs" + str(VEG2_total))
print(VEG3_name + ": Rs" + str(VEG3_price) + " per kg - Available Quantity: " + str(VEG3_quantity) + " kg - Total Price: Rs" + str(VEG3_total))

total_price = VEG1_total + VEG2_total + VEG3_total
print("Total Price of all vegetables: Rs" + str(total_price))

# OUTPUT:
# Enter the name of the vegetable: carrot
# Enter the price per kg: 45
# Enter the available quantity in kg: 2
# Enter the name of the vegetable: raddish
# Enter the price per kg: 52
# Enter the available quantity in kg: 4
# Enter the name of the vegetable: pea
# Enter the price per kg: 5
# Enter the available quantity in kg: 2
# Vegetable Inventory:
# carrot: Rs45.0 per kg - Available Quantity: 2 kg - Total Price: Rs90.0
# raddish: Rs52.0 per kg - Available Quantity: 4 kg - Total Price: Rs208.0
# pea: Rs5.0 per kg - Available Quantity: 2 kg - Total Price: Rs10.0
# Total Price of all vegetables: Rs308.0

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# P8 REPORT CARD USING FILE HANDLING

file = open("report_card.txt", "w")
file.write("Student Name, Math Grade, Science Grade, History Grade, Average Grade\n")

while True:
    student_name = input("Enter student's name (or type 'quit' to exit): ")
    if student_name.lower() == 'quit':
        break
    math_grade = float(input("Enter math grade for {}: ".format(student_name)))
    science_grade = float(input("Enter science grade for {}: ".format(student_name)))
    history_grade = float(input("Enter history grade for {}: ".format(student_name)))

    average_grade = (math_grade + science_grade + history_grade) / 3

    file.write("{}, {}, {}, {}, {:.2f}\n".format(student_name, math_grade, science_grade, history_grade, average_grade))

file.close()

print("Report card created successfully!")

#OUTPUT:
# Student Name, Math Grade, Science Grade, History Grade, Average Grade
# ridam, 52.0, 45.0, 52.0, 49.67
# kshitij, 42.0, 22.0, 45.0, 36.33
# kaushal, 45.0, 23.0, 45.0, 37.67

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# P9 VOTING SYSTEM

candidates = {}
num_candidates = int(input("How many candidates are there? "))

for i in range(num_candidates):
    candidate_name = input("Enter candidate's name: ")
    candidates[candidate_name] = 0

voters = []
num_voters = int(input("How many voters are there? "))

for i in range(num_voters):
    voter_name = input("Enter voter's name: ")

    if voter_name in voters:
        print("You've already voted!")
    else:
        voters.append(voter_name)
        print("Candidates: ", list(candidates.keys()))
        candidate_vote = input("Enter your vote: ")

        if candidate_vote in candidates:
            candidates[candidate_vote] += 1
            print("Vote recorded!")
        else:
            print("Invalid candidate!")

print("Election Results:")
max_votes = max(candidates.values())
for candidate, votes in candidates.items():
    print("- Candidate {}: {} votes".format(candidate, votes))

winners = [candidate for candidate, votes in candidates.items() if votes == max_votes]

if len(winners) == 1:
    print("The winner is:", winners[0])
else:
    print("It's a tie between:", ", ".join(winners))

# OUTPUT:
# How many candidates are there? 4
# Enter candidate's name: BJP
# Enter candidate's name: CONG
# Enter candidate's name: AAP
# Enter candidate's name: BSPA
# How many voters are there? 5
# Enter voter's name: RIDAM
# Candidates:  ['BJP', 'CONG', 'AAP', 'BSPA']
# Enter your vote: CONG
# Vote recorded!
# Enter voter's name: KSHITIJ
# Candidates:  ['BJP', 'CONG', 'AAP', 'BSPA']
# Enter your vote: BJP
# Vote recorded!
# Enter voter's name: KAUSHAL
# Candidates:  ['BJP', 'CONG', 'AAP', 'BSPA']
# Enter your vote: BJP
# Vote recorded!
# Enter voter's name: AMAN
# Candidates:  ['BJP', 'CONG', 'AAP', 'BSPA']
# Enter your vote: CONG
# Vote recorded!
# Enter voter's name: PARI
# Candidates:  ['BJP', 'CONG', 'AAP', 'BSPA']
# Enter your vote: CONG
# Vote recorded!
# Election Results:
# - Candidate BJP: 2 votes
# - Candidate CONG: 3 votes
# - Candidate AAP: 0 votes
# - Candidate BSPA: 0 votes
# The winner is: CONG




