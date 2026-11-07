# Conversor de tempo
segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print("{} segundos equivalem a {} hora(s), {} minuto(s) e {} segundo(s).".format(
    segundos, horas, minutos, segundos_restantes
))