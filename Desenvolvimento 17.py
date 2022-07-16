def calculadora():
    sair = 0
    while (sair == 0):
        opc = int(input("Digite a operação:\n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n 0. Sair\n"))
        if opc == 0:
            sair =1
            res = "FIM"
        elif (opc > 0) and (opc <= 4):
            num1= float(input("Digite o primeiro número \n"))
            num2 = float(input("Digite o segundo número \n"))
            if opc == 1:
                res = num1+num2
            elif opc == 2:
                res = num1-num2
            elif opc == 3:
                res = num1*num2
            else:
                res = num1/num2
            
            print(res)   
        else:
            res = "Essa opção não existe"
    

calculadora()
