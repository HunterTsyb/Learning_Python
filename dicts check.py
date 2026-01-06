students = [
    {"name": "Анна", "score": 85, "age": 19},
    {"name": "Виктор", "score": 74, "age": 18},
    {"name": "Мария", "score": 92, "age": 20},
    {"name": "Елена", "score": 65, "age": 21},
    {"name": "Сергей", "score": 90, "age": 19}
]

#создаем функцию для key, чтобы вытащить скор или эйдж
def sort_by_score(student: dict) -> int:
  return student["score"]
def sort_by_age(student: dict) -> int:
  return student["age"]

#-------------------код-------------

#сортировка по шаблону (что, как выдаем, по какому принципу сортируем)
score_students=sorted(students, reverse=1, key=sort_by_score)
print(score_students)
age_students=sorted(students, key=sort_by_age)
print(age_students)

#лучший студент будет перым в сортированном по оценке списке, и худший будет последним
best_student=score_students[0]
worst_student=score_students[-1]
average_score=(best_student["score"]+worst_student["score"])/2
print(average_score)

#из списка по очереде перебираем студ, если у студ скор будет больше 80, забираем себе
smart_students = [stud for stud in students if stud["score"] >= 80]
print(smart_students)