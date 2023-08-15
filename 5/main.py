# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#h = sum(student_heights)
#a = round(h / len(student_heights), 2)
#print(f"the average height is {a}")
t = 0
for h in student_heights:
  t += h
print(t)
a = round(t / h, 2)
#average = round(total_height / range)
print(a)