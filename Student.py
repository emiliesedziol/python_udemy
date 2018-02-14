student_list = []   # empty list

def create_student():
    name = input("Enter student name:")
    student_data = {
        'name': name,
        'marks': []
    }
    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)


def calc_avg_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0
    total = sum(student['marks'])
    return total/number


def print_student_details(student):
    print("{}, average grade {}".format(student['name'],
                                        calc_avg_mark(student)))


def print_students_list(students):
    for i, student in enumerate(students):
        print("Id: {}".format(i))
        print_student_details(student)


def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a student, 'a' to add a mark to a student, or 'e' to exit ")
    while selection !='e':
        if selection == 'p':
            print_students_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter Student Id: "))
            student = student_list[student_id]
            new_mark = int(input("Enter grade: "))
            add_mark(student, new_mark)
            print(student_list)


        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a student, 'a' to add a mark to a student, or 'e' to exit ")


menu()


# s = create_student()
# print(calc_avg_mark(s))
# add_mark(s, 5)
# print(calc_avg_mark(s))



# print(sum([1, 3, 5]))  #  --> 9

#-------------------------------
# def create_student():
#    name = input("Enter student name:")
#    student_data = {
#        'name': name,
#        'marks': []
#    }
#    return student_data

# s = create_student()
#
# def add_mark(student, mark):
#    student['marks'].append(mark)


#add_mark(s, 5)  # --> {'name': 'me', 'marks': [5]}  passing my reference

# print(s)   #---> {'name': 'me', 'marks': []}


#---------------------------
# z = 5

# def add_number(z, 10):
#    x = x + y


# add_number(z,10)  # passing by value

# print(z)  --> returns 5

#---------------------------
# print(create_student())

# my_list = []
#my_list.append(5)


# print(my_list.append(5))
# print(my_list)   --> returns 5
# print(my_list.append(5))  --> returns none, modifies the list inplace

#--------------------
#def create_student():
#    name = input("Enter student name:")
#    student_data = {
#        'name': name,
#        'marks': []
#    }
#    return student_data  --> returns {'name': 'me', 'marks': []}
#
#print(create_student())

#--------------------------
# student = {"name": "Jose",
#
#           "mark": [70, 80, 50, 99],
#           "exams": {
#               "final": 70,
#               "midterm": 65
#           }}

# print(student['name'])  --->> returns Jose
# print(student['exams']['midterm'])  --> returns 65

#-----------------------
# sample_dictionary = {"name": "Jose", "mark":70}  # similar to json

# print(sample_dictionary["name"])  # has to be in quotes because it is alpha

# sample_set = {3, 5, 2, 9, 1}

# sample_dictionary = {3:7, 2:25}   '3' and '2' are keys

# print(sample_set)

 # print(sample_dictionary[3])