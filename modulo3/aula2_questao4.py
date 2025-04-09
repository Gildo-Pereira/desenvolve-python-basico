classe=input("Digite a classe do personagem (guerreiro, mago ou arqueiro): ")
p_forca=int(input("Digite os pontos de força (de 1 a 20): "))
p_magia=int(input("Digite os pontos de magia (de 1 a 20): "))
res=classe=='guerreiro' and p_forca>=15 and p_magia<=10 or classe=='mago' and p_forca<=10 and p_magia>=15 or classe=='arqueiro' and p_forca<=15 and p_forca>5 and p_magia<=15 and p_magia>5

print(f"Pontos de atributo consistentes com a classe escolhida: {res}")

