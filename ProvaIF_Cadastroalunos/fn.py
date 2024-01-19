alunos = []

def adAlunos(matricula,nome):
    for aluno in alunos:
        if not matricula or matricula in aluno or not nome or nome in aluno:
            print('\nErro ao cadastrar o aluno\n')
            return 
    
    aluno = {
        'Matrícula': matricula,
        'Nome': nome
    }
    alunos.append(aluno)
    print('\nO aluno foi cadastrado com sucesso.\n')
    
def reAlunos(alunos):
    matricula = input('\nDigite o nº de matrícula do aluno para remove-lo:\n')
    for aluno in alunos:
        if matricula == aluno['Matrícula']:
            alunos.remove(aluno)
            return f'\nO aluno {aluno} foi removido com sucesso\n'
    
    return '\nA matrícula não existe\n'
        
def attAlunos(alunos):
    matricula = input('\nDigite o nº de matrícula do aluno para atualizar seu nome:\n')
    for aluno in alunos:
        if matricula == aluno['Matrícula']:
            novo_nome = input('\nDigite o novo nome do aluno:\n')
            aluno.update({'Nome': novo_nome})
            return f'\nO aluno com matrícula {matricula} teve seu nome alterado para {novo_nome}\n'

    return '\nA matrícula não existe\n'  
    
        
def mostrarAlunos(alunos):
    if len(alunos) > 0:
        return f'\nEstá é a lista de alunos:\n \n{alunos}\n'
    else:
        return '\nAdicione alunos a lista.\n'

        