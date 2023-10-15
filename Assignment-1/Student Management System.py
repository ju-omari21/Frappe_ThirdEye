

class Student:
    option = ""
    student_list = ["Jullunar", "Ayman", "Gojo"]
    user_input = input("Please Enter student name: ").capitalize().strip()
    
    def __init__(self, first_name, last_name, id, gender):
        self.fname = first_name
        self.lname = last_name
        self.id = id
        self.gender = gender
    
    print("Welcome to Student Management System")
    
    def display(self):
        print(self.student_list)
    
    def get_all_info (self):
        return f"Student information is {self.fname} {self.lname}, the id is {self.id} and the gender is {self.gender}"

    def accept(self):
        if self.user_input in self.student_list:
            print("You are accepted") 
        else:
            print("You are not accepted")
            

    def search(self):
        pass
    
    def delete_update(self):
        self.option = input("Delete or Update your name: ").strip().capitalize()
        
    if option == 'Update':
        thenewname = input("Type your new name: ")

        student_list[student_list.index[0,1,2]] = thenewname
        
        print("The name has been updated secussfully!")
        print(student_list)

    elif option == 'Delete':
        student_list.remove()
        print(student_list)

Student_one = Student("Jullunar", "Alomari", "12", "female")
Student_two = Student("Ayman", "Khalil", "132", "male")
Student_three = Student("Gojo", "Saturou", "125", "male")

print(Student.get_all_info(Student_one))
print(Student.get_all_info(Student_two))
print(Student.get_all_info(Student_three))
print(Student.accept(Student_one))
print(Student.accept(Student_two))
print(Student.accept(Student_three))
print(Student.delete_update(Student_one))
print(Student.delete_update(Student_two))
print(Student.display(Student_three))