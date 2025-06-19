# This program creates and modifies a 2D list of subjects and grades to simulate a gradebook system.
# It uses list methods like append, remove, and indexing to update and merge current and previous semester data.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Creating The List Of Subjects & Grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#Creating The 2-D List of Subjects & Grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
print("\n")

#Appending Computer Science & Visual Arts To The Gradebook List
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)
print("\n")

#Modifying Visual Arts & Poetry
gradebook[-1][-1] = 97
gradebook.remove(gradebook[2])
gradebook.append(["poetry", "Pass"])
print(gradebook)
print("\n")

#Creating Full Gradebook List
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
print("\n")









