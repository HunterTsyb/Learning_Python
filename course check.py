python_course = {"Анна", "Сергей", "Мария", "Олег", "Ирина"}
ml_course = {"Павел", "Мария", "Олег", "Елена", "Дмитрий"}
data_course = {"Ирина", "Мария", "Сергей", "Дмитрий"}

print(f"Ребят активных во всех трех курсах: {len(python_course&ml_course&data_course)} Ребят активных только в одном курсе: {len(python_course^ml_course^data_course)}")
print(f"Ребята которые прошли все три курса: {python_course&ml_course&data_course}")
print(f"Ребят активные только в одном курсе: {python_course^ml_course^data_course}")
print(f"Ребята которые проходящие курсы: {python_course|ml_course|data_course} ")
print(f"Ребята которые проходят два курса: {(python_course&ml_course|python_course & data_course|ml_course & data_course)-(python_course&ml_course&data_course)}")

student_name = input("Введите имя студента: ")
print(f'ученик "{student_name}" состоит в курсах: ', end="")
if student_name in python_course:
  print(" python_course", end="")
if student_name in ml_course:
  print(" ml_course", end="")
if student_name in data_course:
  print(" data_course", end="")
if student_name not in data_course and student_name not in ml_course and student_name not in python_course:
  print(" Ни в каких", end="")

python_course.add("Киррил")

all_students=list(python_course)+list(ml_course)+list(data_course)
print(f"\nКолличество уникальных имен: {len(set(all_students))}")