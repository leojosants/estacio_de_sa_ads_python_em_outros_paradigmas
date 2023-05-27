import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digitos = load_digits()

plt.figure(figsize=(14, 4))

# type: ignore
# type: ignore
for index, (imagem, rotulo) in enumerate(zip(digitos.data[0:5], digitos.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(imagem, (8, 8)), cmap=plt.cm.gray)  # type: ignore
    plt.title('Treinamento: {}\n'.format(rotulo, fontsize=15))

# print(f"\nShape dos dados de imagens: {digitos.data.shape}")  # type: ignore

# # Apresentar o total de dados rotulados com inteiros de 0 a 9
# print(f"Shapedos rotulados: {digitos.target.shape}")  # type: ignore
