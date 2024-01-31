seconds_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_secs = int(seconds_str)

days = total_secs // 86400
secs_left = total_secs % 86400
hours = secs_left // 3600
secs_left_h = total_secs % 3600
minutes = secs_left_h // 60
secs_left_final = secs_left % 60

print(days, "dias,", hours, "horas,", minutes, "minutos e", secs_left_final, "segundos.")
