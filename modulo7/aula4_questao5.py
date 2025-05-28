# Abrir o arquivo para escrita
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escrever o cabeçalho da planilha
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrever os dados de cada livro (sem espaços após as vírgulas e com quebra de linha no final)
    arquivo.write("1984,George Orwell,1949,328\n")
    arquivo.write("Dom Casmurro,Machado de Assis,1899,256\n")
    arquivo.write("O Senhor dos Anéis,J.R.R. Tolkien,1954,1178\n")
    arquivo.write("Cem Anos de Solidão,Gabriel García Márquez,1967,417\n")
    arquivo.write("Orgulho e Preconceito,Jane Austen,1813,279\n")
    arquivo.write("Harry Potter e a Pedra Filosofal,J.K. Rowling,1997,223\n")
    arquivo.write("A Revolução dos Bichos,George Orwell,1945,112\n")
    arquivo.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")
    arquivo.write("Memórias Póstumas de Brás Cubas,Machado de Assis,1881,208\n")
    arquivo.write("O Hobbit,J.R.R. Tolkien,1937,310\n")

print("Arquivo 'meus_livros.csv' criado com sucesso!")
