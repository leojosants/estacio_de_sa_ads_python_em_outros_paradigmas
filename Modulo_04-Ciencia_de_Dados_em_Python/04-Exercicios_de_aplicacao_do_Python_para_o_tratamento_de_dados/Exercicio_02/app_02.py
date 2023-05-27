from sklearn.datasets import load_digits

digitos = load_digits()

print(f"\nShape dos dados de imagens: {digitos.data.shape}")  # type: ignore

# Apresentar o total de dados rotulados com inteiros de 0 a 9
print(f"Shapedos rotulados: {digitos.target.shape}")  # type: ignore
