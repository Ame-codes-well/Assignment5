student={'Alice':87, 'Bob':90, 'Maria':91, 'Charlie':88, 'Jane':99 }
name=input('Enter student name: ')
if name in student:
    print(f'{name}\'s marks: {student[name]}')
if name not in student:
    print("student not found.")
