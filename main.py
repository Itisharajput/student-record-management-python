from student import add_student,
view_student
from storage import load_data, save_data

def main():
  students = load-data()

while True:
  print("\nStudent Record Management System")
  print("1. Add Student")
  print("2. View Students")
  print("3. Exit")

choice == input("Enter choice: ")

if choice == "1":
  add_student(students)
  save_data(students)
elif choice =="2":
  view_students(students)
elif:
  choice == "3":
  print("Exiting program...")
  break
else:
  print("Invalid choice")
  if __name__=="__main__":
  main()
