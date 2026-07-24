import random
import time
import os

print('BEM-VINDO!')

while True:

    user = input(f'Selecioner uma das opções abaixo!\n[G] Gerar CPF, [V] Validar CPF ou [S] Sair: ').upper()

    if not user:
        os.system('cls')
        print('Por favor, selecione uma das opções.')
        print('Reiniciando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')
        time.sleep(0.5)
        os.system('cls')
        continue

    if user not in ['G','V','S']:
        print('Você selecionou algo que não existe.')
        print('Reiniciando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')
        time.sleep(0.5)
        os.system('cls')
        continue

    if user == 'S':
        os.system('cls')
        print('Encerrando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')
        time.sleep(0.5)
        break

    # Gerador
    
    if user == 'G':
        os.system('cls')
        print('Gerando CPF', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        os.system('cls')
        print('CPF gerado com sucesso!')
        nove_digitos = ''
        for i in range(0, 9):  
            nove_digitos += str(random.randint(0,9))
        contador_regressivo_1 = 10 
        resultado_digito_1 = 0
        for digito_1 in nove_digitos:
            resultado_digito_1 += int(digito_1) * contador_regressivo_1 
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0
        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11
        resultado_digito_2 = 0
        for digito_2 in dez_digitos:
            resultado_digito_2 += int(digito_2) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2) * 10 % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
        cpf_formado = f'{nove_digitos}{digito_1}{digito_2}'
        print(f'{cpf_formado[0:3]}.{cpf_formado[3:6]}.{cpf_formado[6:9]}-{cpf_formado[9:11]}')
        time.sleep(1)
        continue
        
    # Validação

    try:
        os.system('cls')
        cpf = input('Digite os números do seu cpf: ')
        cpf_limpo = cpf.replace('.', '').replace('-', '')
        cpf_int = int(cpf_limpo)
    except ValueError:
        os.system('cls')
        print('Por favor, digite apenas números.')
        print('Reiniciando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')
        time.sleep(0.5)
        os.system('cls')
        continue

    cpf_maximo_digitos = len(cpf_limpo) > 11
    cpf_minimo_digitos = len(cpf_limpo) < 11

    if cpf_maximo_digitos:
        os.system('cls')
        print('O máximo é 11 dígitos. Tente novamente. ')
        print('Reiniciando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')
        time.sleep(1)
        os.system('cls')
        continue
    if cpf_minimo_digitos:
            os.system('cls')
            print('O mínimo é 11 dígitos. Tente novamente. ')
            print('Reiniciando', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='\n')
            time.sleep(1)
            os.system('cls')
            continue
    if cpf:
        conversao_str = str(cpf_int)
        nove_digitos = conversao_str[:9]
        contador_regressivo_1 = 10 
        resultado_digito_1 = 0
        for digito_1 in nove_digitos:
            resultado_digito_1 += int(digito_1) * contador_regressivo_1 
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0
        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11
        resultado_digito_2 = 0
        for digito_2 in dez_digitos:
            resultado_digito_2 += int(digito_2) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2) * 10 % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
        cpf_formado = f'{nove_digitos}{digito_1}{digito_2}'
    cpf_valido = cpf_limpo == cpf_formado
    if cpf_valido:
        os.system('cls')
        print('CPF válido!')
        time.sleep(1)
    else:
        os.system('cls')
        print('CPF inválido. Tente novamente.')
        print('Reiniciando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='\n')
        time.sleep(0.5)
        os.system('cls')
        continue
