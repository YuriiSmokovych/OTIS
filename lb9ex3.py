students_age = {}
students_height = {
    'koval': 175,
    'smith': 180,
    'viliams': 181,
    'betelgeuse': 176,
    'vizli': 180,
    'potter': 186,
    'daz': 190,
    'bases': 173,
    'shmidts': 178,
    'smidt': 179,
    }
for key, value in students_height.items():
    if value >= 190: age = 19
    elif value <= 175: age = 16
    elif 175 < value < 184: age = 17
    else: age = 18
    students_age[key] = age
print(students_age)

for key, value in students_age.items():
    print(key, '    \t', value)


