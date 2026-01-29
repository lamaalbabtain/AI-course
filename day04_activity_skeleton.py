"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

# TODO: Implement the tasks above using nested dict access.


# 1) Get Alice's AI301 grade
print(students["S001"]["courses"]["AI301"]["grade"])

# 2) Calculate Bob's GPA (weighted by credits)
points = credits = 0
for c in students["S002"]["courses"].values():
    points += c["grade"] * c["credits"]
    credits += c["credits"]
print(points / credits)

# 3) Find all students in CS101
cs101 = []
for s in students.values():
    if "CS101" in s["courses"]:
        cs101.append(s["name"])
print(cs101)

# 4) Get average grade across all courses
grades = []
for s in students.values():
    for c in s["courses"].values():
        grades.append(c["grade"])
print(sum(grades) / len(grades))

# 5) Find student with highest GPA
best_name = ""
best_gpa = 0

for s in students.values():
    p = c = 0
    for course in s["courses"].values():
        p += course["grade"] * course["credits"]
        c += course["credits"]
    gpa = p / c
    if gpa > best_gpa:
        best_gpa = gpa
        best_name = s["name"]

print(best_name)
print(best_gpa)