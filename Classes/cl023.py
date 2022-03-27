try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problemas com os tipos de dados que vc digitou!')
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontado foi -> {erro.__cause__}')
else:
    print(r)
finally:
    print('\n\033[31mFIM DO PROGRAMA!\033[m')
