import math

# Essas váriaveis serão utilizadas para tranformar o valor inicial em horas e minutos ao separa o valor inteiro do decimal
minute = 0
hour = 0

# Aqui você irá digitar o horário que você entrou e quantos minutos pretende fazer de almoço
enter = float(input("Entrada: "))
questLounch = int(input("Quantos minutos você fará de almoço? "))

# Aqui será para saber quanto tempo a mais você precisará acrescentar no seu horário dos devidos compromissos
questEnglish = input("Você terá aula de inglês hoje?[s/n] ")
if questEnglish == "s":
    minuteEnglish = int(input("Quantos minutos você terá de aula de inglês? "))
else:
    minuteEnglish = 0

questPED = input("Você terá PED hoje?[s/n] ")
if questPED == "s":
    minutePED = int(input("Quantos minutos você teŕa de PED? "))
else:
    minutePED = 0
    
questCompromise = input("Você terá algum outro compromisso hoje?[s/n] ")
if questCompromise == "s":
    minuteCompromise = int(input("Quantos minutos levará esse compromisso? "))
else:
    minuteCompromise = 0

# Esta função é utilizada para separa o valor inteiro que é a hora e o decimal que são os minutos. OBS: Possa ser que criando a interface as variáveis horas e minutos já possam vir separadas
minute, hour = math.modf(enter)
minute = minute * 100

# Neste momento convertamos o valor de horas em minutos e somamos com os outros tempos que podemos adicionar + 480 minutos que é o valor convertido de 8 horas em minutos
convertMinute = int(hour) * 60
totalMinute = (int(convertMinute) + int(minute) + questLounch + minuteEnglish + minutePED + minuteCompromise) + 480

# Esta parte serve para converte o total de minutos em horas e o restante de mintos guarda nesta ultima variável
convertHour = totalMinute / 60
minuteFInal = (totalMinute % 60)

print(f"Você precisa largar às {int(convertHour)}:{minuteFInal}")