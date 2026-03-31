# Basic dictionary operations

student = {
    "name": "Dipto",
    "age": 21,
    "marks": 85
}

# Access
print(student["name"])

# Update
student["age"] = 22

# Add new key
student["city"] = "Guwahati"

# Loop
for key, value in student.items():
    print(key, ":", value)

# Remove
student.pop("city")

print(student)