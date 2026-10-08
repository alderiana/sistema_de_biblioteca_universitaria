
import psycopg2

class Autor:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",   
                database="biblioteca_universitaria",
                user="postgres",
                password="1234"
            )
        except psycopg2.Error as e:
            print(f"\nErro ao conectar ao banco: {e}")

    def cadastrar_autor(self, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)", (nome, nacionalidade)) 
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao cadastrar autor: {e}")

    def listar_autor(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM autor")
            autores = cursor.fetchall()
            cursor.close()
            return autores
        except psycopg2.Error as e:
            print(f"\nErro ao listar autores: {e}")
            return []

    def atualizar_autor(self, nome, nacionalidade, id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE autor SET nome = %s, nacionalidade = %s WHERE id = %s", 
                (nome, nacionalidade, id))
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao atualizar autor: {e}")


    def excluir_autor(self, id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "DELETE FROM autor WHERE id = %s", 
                (id,))
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao deletar autor: {e}")

