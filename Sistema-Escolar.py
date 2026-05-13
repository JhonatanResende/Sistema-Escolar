from datetime import datetime, date
from playsound3 import playsound

media = float(input("Digite a média do aluno: "))

if media >= 7.0:
    print("Aprovado.")
    playsound("song.mp3")
elif (media >= 4.0) and (media < 7.0):
    print("Recuperação.")

    data_prazo = date(2026, 1, 31)
    
    dia = data_prazo.day
    mes = data_prazo.month
    ano = data_prazo.year

    print(f"O prazo para a prova de recuperação é até: {dia}/{mes}/{ano}")

    formato_data = "%d/%m/%Y"

    while True:
        try:
            data_prova_str = input("Digite a data de quando o aluno fez a prova de recuperação (dd/mm/aaaa): ").strip()
            data_prova_date = datetime.strptime(data_prova_str, formato_data).date()
            break
        except ValueError:
            print("Data inválida. Por favor, digite a data no formato dd/mm/aaaa.")
            continue

    if data_prova_date <= data_prazo:
        nota_reco = float(input("Digite a nota da recuperação: "))

        if nota_reco >= 7.0:
            print("Aprovado.")
            playsound("song.mp3")
        else:
            print("Reprovado.")
    else:
        print("Data de prova de recuperação ultrapassou o prazo. Reprovado.")

else:
    print("Reprovado.")
    