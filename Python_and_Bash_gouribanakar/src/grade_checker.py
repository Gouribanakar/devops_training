score = int(input("Enter the score: "))

if score >= 90:
    print("Grade is A")
elif 80 <= score <= 89:
    print("Grade is B")
elif 70 <= score <= 79:
    print("Grade is C")
elif 60 <= score <= 69:
    print("Grade is D")
else:
    print("Grade is F")
    
