import pyautogui
import time

encontrada = 'Aceitar.png' 
Xerath = 'Xerath.png'
Pickamento = 'Pickar.png'
Banimento = 'Banir.png'
ProcurinhaBan = 'ProcuraBan.png'

ban = pyautogui.prompt(text="",title="Insira o nomde do campeão")


print("Programa iniciado")
time.sleep(10)

while True:

    try:
        aceitar = pyautogui.locateCenterOnScreen(encontrada, confidence=0.7)

        if aceitar:

            pyautogui.click(aceitar)
            print("Aceitei a pardida")
            break
        else:
            print("")

            
    except pyautogui.ImageNotFoundException as e:
        print(f"Erro ao procurar a imagem: {e}")

        time.sleep(5)

time.sleep(5)

"""
while True:

    try:
        Selecionar = pyautogui.locateCenterOnScreen(Xerath, confidence=0.9)

        if Selecionar:

            pyautogui.click(Selecionar)
            print("Xerath selecionado")
            break
        else:
            print("")

            
    except pyautogui.ImageNotFoundException as e:
        print(f"Não foi possivel selecionar o boneqin {e}")

        time.sleep(3)

time.sleep(5)

"""

while True:

    try:
        ProcuraBan = pyautogui.locateCenterOnScreen(ProcurinhaBan, confidence=0.8)

        if ProcuraBan:

            pyautogui.click(ProcuraBan)
            pyautogui.write(ban)
            time.sleep(0.5)
            pyautogui.doubleClick(x=641, y=282)
            print(f"{ban} foi selecionado para o ban.")
            break
        else:
            print("")

            
    except pyautogui.ImageNotFoundException as e:
        print(f"Não foi possivel banir esse champ {e}")

        time.sleep(3)

time.sleep(1.5)

while True:

    try:
        Banzinho = pyautogui.locateCenterOnScreen(Banimento, confidence=0.9)

        if Banzinho:

            pyautogui.click(Banzinho)
            print(f"{ban} foi banido com sucesso")
            break
        else:
            print("")

            
    except pyautogui.ImageNotFoundException as e:
        print("Não foi posivel finalizar o banimento")

        time.sleep(3)

time.sleep(15)



while True:

    try:
        Geladeirar = pyautogui.locateCenterOnScreen(Xerath, confidence=0.9)

        if Geladeirar:

            pyautogui.click(Geladeirar)
            print("Clickei no xerath")
            break
        else:
            print("")

            
    except pyautogui.ImageNotFoundException as e:
        print(f"Não achei o xerath, tentando novamente {e}")

        time.sleep(3)

time.sleep(5)

while True:

    try:
        Pickar = pyautogui.locateCenterOnScreen(Pickamento, confidence=0.7)

        if Pickar:

            pyautogui.click(Pickar)
            print("Geladeira pickada")
            break
        else:
            print("")

            
    except pyautogui.ImageNotFoundException as e:
        print(f"Não consegui pickar Xerath, tentando novamente: {e}")

        time.sleep(4)




print("fim da execução")


