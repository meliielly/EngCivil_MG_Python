print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n')
print('= Produzido por: Melissa Gabriely e Lariane =')
print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n\n')
print(' ~ ☕ BEM-VIND@ VAMOS PREPARAR SEU CAFÉ, SELECIONE UMA OPÇAO! ☕')

op = 0
sair = 3

op = int(input('\n[1] Café passado\n[2] Café Instantâneo\n[3] Sair\n>'))

while op != sair:
    
    

    if op == 1:
        aux = int(input('\nPossui cafeteira elétrica? [1] sim ou [2] não\n>'))
        
        if aux == 1:
            print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=')
            print("\nVamos lá! siga os passos baixo:\n\n[1] Colocar o filtro\n[2] Adicionar o pó do café")
            print("[3] Adicionar água\n[4] Ligar a cafeteira\n[5] Aguardar ficar pronto\n[6] Beber o café!\n")
            
            aux2 = int(input('\n\n☕ Está satisfeit@? [1] sim [2] não\n>'))
            
            if aux2 == 1:
                break
            else:
                op = int(input('\n[1] Café passado\n[2] Café Instantâneo\n[3] Sair\n\n>'))  
    
        else:
            print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n')
            print('\nQue pena... Então vamos preprar um café instantâneo!')
            print("\nVamos lá! siga os passos baixo:\n")
            print('[1] Coloque água para ferver em uma chaleira\n[2] Coloque o café dentro de uma caneca')
            print('[3] adicione água quente na caneca\n[4] Aguardar ficar pronto\n[5] Beber o café')
            
            aux2 = int(input('\n\n☕ Está satisfeit@? [1] sim [2] não\n>'))
            
            if aux2 == 1:
                
                break
            else:
                op = int(input('\n[1] Café passado\n[2] Café Instantâneo\n[3] Sair\n\n>'))
    elif op == 2:
        print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=\n')
        print("Vamos lá! siga os passos baixo:\n")
        print('[1] Coloque água para ferver em uma chaleira\n[2] Coloque o café dentro de uma caneca')
        print('[3] adicione água quente na caneca\n[4] Aguardar ficar pronto\n[5] Beber o café')
            
        aux2 = int(input('\n\n☕ Está satisfeit@? [1] sim [2] não\n>'))
            
        if aux2 == 1:
                
            break
        else:
            op = int(input('\n[1] Café passado\n[2] Café Instantâneo\n[3] Sair\n\n>'))
    else:
        break
