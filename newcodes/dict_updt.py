# create and add one value:

students = {'Dipto': 85, 'Kavya': 90, 'Jeeps': 78, 'Abhigyan': 88, 'Arjun': 92}
students['Nayan'] = 80


for i,j in students.items():
    print(i,"=>",j)

print()

# COPY PART ADDED HERE
students_copy = students.copy()

print("Copied Dictionary:")

students_copy.update({'Nayan': 45, 'Dipto': 99})

print()

for i,j in students_copy.items():
    print(i,"=>",j)