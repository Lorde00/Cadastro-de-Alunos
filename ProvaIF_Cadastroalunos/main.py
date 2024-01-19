from fn import adAlunos, reAlunos, attAlunos, mostrarAlunos, alunos

print('\nBem vindo ao Portal do Diretor!\n')

while True:
    op = int(input('\nEscolha uma opção que deseja: \n[1]Adicionar Alunos \n[2]Mostrar alunos \n[3]Atualizar aluno \n[4]Remover aluno \n[5]Sair\n\n'))
    match op:

        case 1:
            matricula = input('\nDigite a matrícula do aluno:\n')
            nome = input('\nDigite o nome do aluno:\n')
            adAlunos(matricula, nome)

        case 2:
            print(mostrarAlunos(alunos))

        case 3:
            if len(alunos) > 0:
                print(attAlunos(alunos))
            else:
                print('\nAdicione alunos a lista para utilizar essa função.\n')
        
        case 4:
            if len(alunos) > 0:
                print(reAlunos(alunos))
            else:
                print('\nAdicione alunos a lista para utilizar essa função.\n')

        case 5:
            print('\nObrigado por utilizar o programa do Diretor!\n')