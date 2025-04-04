class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = self.validar_nota(nota)

    def validar_nota(self, nota):
        try:
            nota = float(nota)
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                raise ValueError("Nota incorreta!")
        except ValueError as e:
            print(f"Erro ao validar nota para o {self.nome}: {e}")
            return None
        
class Registro_notas:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def salvar_nota(self, aluno):
        if aluno.nota is not None:
            try:
                with open(self.arquivo, "a") as f:
                    f.write(f"Nota do {aluno.nome}: {aluno.nota}\n")
                    print(f"Nota do {aluno.nome} salva com sucesso!")
            except IOError as e:
                print(f"Erro ao salvar a nota: {e}")

        else:
            print(f"Nota incorreta para o {aluno.nome}")

    def listar_notas(self):
        try:
            with open(self.arquivo, "r") as f:
                print("Notas dos alunos:")
                print(f.read())
        except FileNotFoundError:
            print("Arquivo de notas não encontrado.")
        except IOError as e:
            print(f"Erro ao ler o arquivo: {e}")

# Exemplo de uso
arquivo_notas = "notas.txt"
registro = Registro_notas(arquivo_notas)

# Criando alunos
aluno1 = Aluno("João", 8.5)
aluno2 = Aluno("Maria", 12)  # Nota inválida
aluno3 = Aluno("Pedro", 9.0)

# Salvando notas
registro.salvar_nota(aluno1)
registro.salvar_nota(aluno2)
registro.salvar_nota(aluno3)

# Listando as notas salvas
registro.listar_notas()
