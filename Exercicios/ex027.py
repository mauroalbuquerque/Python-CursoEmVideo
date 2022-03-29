nome = instr(put('Digite o seu nome completo: ')).strip()

nome = nome.split()

last = len(nome) - 1

print(nome[0], nome[last])