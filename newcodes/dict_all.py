# Dictionary Practical Program

# 1. Create a dictionary
student = {
    "name": "Dipto",
    "age": 21,
    "course": "B.Tech",
    "marks": 85
}

print("Original dictionary:")
print(student)

# 2. Access values
print("\nName:", student["name"])
print("Course:", student.get("course"))

# 3. Add a new key-value pair
student["city"] = "Dispur"
print("\nAfter adding city:")
print(student)

# 4. Update an existing value
student["marks"] = 90
print("\nAfter updating marks:")
print(student)

# 5. Remove elements
removed_value = student.pop("age")   # removes age
print("\nRemoved age:", removed_value)
print("After pop:")
print(student)

# 6. Keys, values, items
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 7. Loop through dictionary
print("\nLoop through keys and values:")
for key, value in student.items():
    print(key, ":", value)

# 8. Check if key exists
if "name" in student:
    print("\n'name' key exists")

# 9. Nested dictionary
students = {
    "s1": {"name": "Amit", "marks": 78},
    "s2": {"name": "Riya", "marks": 92},
    "s3": {"name": "Rahul", "marks": 88}
}

print("\nNested dictionary:")
print(students)
print("Student s2 name:", students["s2"]["name"])

# 10. Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print("\nDictionary comprehension:")
print(squares)

# 11. Merge dictionaries
extra = {"gender": "Male", "country": "India"}
student.update(extra)
print("\nAfter merging another dictionary:")
print(student)

# 12. Sort dictionary by keys
sorted_dict = dict(sorted(student.items()))
print("\nSorted dictionary by keys:")
print(sorted_dict)