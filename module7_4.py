print("В команде Мастера кода участников %(team1_num)s" % {"team1_num": 5} + "!")
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s" % {"team1_num": 5, "team2_num": 6} + "!")
print("Команда Волшебники данных решила задач {score_2}".format(score_2=42) + "!")
print("Волшебники данных решили задачи за {team1_time}".format(team1_time=18015.2) +"с!")

score_1 = 40
score_2 = 42
print(f"Команды решили {score_1} и {score_2} задач.")

team1_time = 1552.512
team2_time = 2153.31451

result = "Победа команды Мастера кода!"
result_1 = "Победа команды Волшебники Данных!"
result_2 = "Ничья"

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f"Результат битвы: {result}")
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f"Результат битвы: {result_1}")
else:
    print(result_2)

tasks_total = 82
time_avg = 45.2
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
