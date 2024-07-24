
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
high_score=0
for scores in student_scores:
    if (scores > high_score):
        high_score = scores

print(f"The highest score in the class is: {high_score}")
    
