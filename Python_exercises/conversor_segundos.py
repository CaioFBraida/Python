totalSegundos = int(input("Número de segundos que deseja converter"))

dias = totalSegundos // 86400
restoSegundos = totalSegundos % 86400
horas = restoSegundos // 3600
restoSegundos_meio = restoSegundos % 3600
minutos = restoSegundos_meio // 60
restoSegundos_final = restoSegundos_meio % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", restoSegundos_final, "segundos.")