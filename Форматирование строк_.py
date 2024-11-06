#Использование %

team1_num = 5
print("В команде Мастера кода участников: %s" %(team1_num))

team1_num = 5
team2_num = 6
print("Итого сегодня в командах участников:%s и %s!"%(team1_num, team2_num))

#Использование format

score_2 = 41
print("Команда волшебников данных решила задач:{}".format(score_2))

team1_time = 18015.2
print(f"Волшебники данных решили задачи за {team1_time} c!")

#Использование f- строки

score_1 = 40
score_2 = 42
print(f"Результаты битвы: {score_1} и {score_2} задач")

challenge_result = "победа"
print(f"Результат битвы: {challenge_result} команды Мастера кода!")

task_total = 82
tame_avg = 350.4
print(f"Сегодня было решено {task_total} задач, в среднем по {tame_avg} секунды на задачу!")