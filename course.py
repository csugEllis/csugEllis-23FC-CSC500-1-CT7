# Creating dictionaries for room numbers, instructors, and meeting times
rooms = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# User input for course number
course_number = input("Enter the course number: ").upper()  # Convert to uppercase to match the keys

# Displaying the room number, instructor, and meeting time for the entered course number
if course_number in rooms and course_number in instructors and course_number in meeting_times:
    print(f"Room Number: {rooms[course_number]}")
    print(f"Instructor: {instructors[course_number]}")
    print(f"Meeting Time: {meeting_times[course_number]}")
else:
    print("The entered course number is not valid.")
