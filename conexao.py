import sqlite3

conexao = sqlite3.connect('ProjetoBD') #apontando para qual arquivo vamso utilizar
cursor = conexao.cursor() #passando para uma nova variável

#CRIANDO TABELAS
'''
cursor.execute('CREATE TABLE estudante (Matricula INT PRIMARY KEY, Nome_Estudante VARCHAR(255), Telefone_Estudante VARCHAR(20),     Curso_Estudante INT, FOREIGN KEY (Curso_Estudante) REFERENCES curso(Codigo_Curso));')

cursor.execute('CREATE TABLE disciplina (Codigo_Disciplina INT PRIMARY KEY, Nome_Disciplina VARCHAR(255), Professor_Disciplina INT, Curso_Disciplina INT, FOREIGN KEY (Professor_Disciplina) REFERENCES professor(SIAPE), FOREIGN KEY (Curso_Disciplina) REFERENCES curso(Codigo_Curso));')

cursor.execute('CREATE TABLE professor (SIAPE INT PRIMARY KEY,     Nome_Professor VARCHAR(255), Email_Professor VARCHAR(255), Departamento_Professor INT, FOREIGN KEY (Departamento_Professor) REFERENCES departamento(Codigo_Departamento));')

cursor.execute('CREATE TABLE curso (Codigo_Curso INT PRIMARY KEY, Nome_Curso VARCHAR(255), Departamento_Curso INT, FOREIGN KEY (Departamento_Curso) REFERENCES departamento(Codigo_Departamento));')

cursor.execute('CREATE TABLE departamento (Codigo_Departamento INT PRIMARY KEY, Nome_Departamento VARCHAR(255), Campus_Departamento INT, FOREIGN KEY (Campus_Departamento) REFERENCES campus(Codigo_Campus));')

cursor.execute('CREATE TABLE campus (Codigo_Campus INT PRIMARY KEY,Endereco_Campus VARCHAR(255));')
'''


#INSERINDO DADOS
'''
cursor.execute('INSERT INTO campus (Codigo_Campus, Endereco_Campus) VALUES (1, "Paulista")')

cursor.execute('INSERT INTO campus (Codigo_Campus, Endereco_Campus) VALUES (2, "Recife")')

cursor.execute('INSERT INTO campus (Codigo_Campus, Endereco_Campus) VALUES (3, "Olinda")')

cursor.execute('INSERT INTO departamento (Codigo_Departamento, Nome_Departamento, Campus_Departamento) VALUES (1, "Departamento de Matematica", 1)')

cursor.execute('INSERT INTO departamento (Codigo_Departamento, Nome_Departamento, Campus_Departamento) VALUES (2, "Departamento de Engenharia", 2)')

cursor.execute('INSERT INTO departamento (Codigo_Departamento, Nome_Departamento, Campus_Departamento) VALUES (3, "Departamento de Informática", 3)')

cursor.execute('INSERT INTO curso (Codigo_Curso, Nome_Curso, Departamento_Curso) VALUES (1, "Bacharelado em Matematica", 1)')

cursor.execute('INSERT INTO curso (Codigo_Curso, Nome_Curso, Departamento_Curso) VALUES (2, "Engenharia Quimica", 2)')

cursor.execute('INSERT INTO curso (Codigo_Curso, Nome_Curso, Departamento_Curso) VALUES (3, "Analise e Desenvolvimento de Sistemas", 3)')

cursor.execute('INSERT INTO professor (SIAPE, Nome_Professor, Email_Professor, Departamento_Professor) VALUES (1, "João Silva", "joao.silva@universidade.edu.br", 1)')

cursor.execute('INSERT INTO professor (SIAPE, Nome_Professor, Email_Professor, Departamento_Professor) VALUES (2, "Maria Souza", "maria.souza@universidade.edu.br", 2)')

cursor.execute('INSERT INTO professor (SIAPE, Nome_Professor, Email_Professor, Departamento_Professor) VALUES (3, "Carlos Pereira", "carlos.pereira@universidade.edu.br", 3)')

cursor.execute('INSERT INTO disciplina (Codigo_Disciplina, Nome_Disciplina, Professor_Disciplina, Curso_Disciplina) VALUES (1, "Calculo Diferencial e Integral I", 1, 1)')

cursor.execute('INSERT INTO disciplina (Codigo_Disciplina, Nome_Disciplina, Professor_Disciplina, Curso_Disciplina) VALUES (2, "Mecanica dos Fluidos", 2, 2)')

cursor.execute('INSERT INTO disciplina (Codigo_Disciplina, Nome_Disciplina, Professor_Disciplina, Curso_Disciplina) VALUES (3, "Banco de Dados", 3, 3)') 

cursor.execute('INSERT INTO estudante (Matricula, Nome_Estudante, Telefone_Estudante, Curso_Estudante) VALUES (1, "Ana Lima", "81999999999", 1)')

cursor.execute('INSERT INTO estudante (Matricula, Nome_Estudante, Telefone_Estudante, Curso_Estudante) VALUES (2, "Pedro Alves", "81988888888", 2)')

cursor.execute('INSERT INTO estudante (Matricula, Nome_Estudante, Telefone_Estudante, Curso_Estudante) VALUES (3, "Julia Costa", "81977777777", 3)')
'''

conexao.commit() #enviar para a conexao
conexao.close #fechar o arquivo python