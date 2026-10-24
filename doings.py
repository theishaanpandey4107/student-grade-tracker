student = {}

def show_menu():
     print("------marks tracker--------")
     print("1-add student")
     print("2 - View All Students")
     print("3-search student")
     print("4-exit")

def add_student(name,marks1,marks2,):
     student[name]={"marks1":marks1
                    ,"marks2":marks2,"avg": (marks1+marks2)/2}   
def view_all_student():
     print(student)

while True:
     show_menu()
     choice = int(input("enter choice"))
     if choice == 1:
          name = input("enter name")
          marks1= int(input("enter m1"))
          marks2= int(input("enter mm2"))
          add_student(name,marks1,marks2)
          print(student)
     elif choice==2:
          view_all_student()
     
     elif choice ==3:
          name = input("enter name")
          if name in student:
               print("avg",student[name]["avg"])
               print("Marks 1:", student[name]["marks1"])
               print("Marks 2:", student[name]["marks2"])
          else:
               print("student not exist")
     elif choice == 4 :
          print("exit")
          break
     else:
          print("invalid option")
          
    
     


    


