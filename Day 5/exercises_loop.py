student_heights = [180 ,124,165 ,173, 189, 169, 146]

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total=0
  number_student=0
  for height in student_heights:
    total += height
    number_student =  number_student + 1

  
print(f"total height = {total}")
print(f"number of students = {number_student}")
average_height= round(total / number_student)
print(f"average height = {average_height}")