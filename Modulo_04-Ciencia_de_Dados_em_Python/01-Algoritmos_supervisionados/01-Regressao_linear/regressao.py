import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas


############# Pré-processamento ###############
# Coleta e Integração - Carregar a planilha dentro do programa
arquivo = pandas.read_csv('dados_dengue.csv')

# Dado de treinamento
anos = arquivo[['ano']]  # Extração dos elementos da coluna 'ano'

# Resultado
casos = arquivo[['casos']]  # Extração dos elementos da coluna 'casos'


############## Mineração #################
# Objeto utilizado para treinar (ajustar) a equação da reta que será gerada pela regressão.
regr = LinearRegression()

# Realiza o treinamento
regr.fit(X=anos, y=casos)

ano_futuro = [[2018]]

# Retorna o numero de casos da variável ano_futuro
casos_2018 = regr.predict(ano_futuro)  # type: ignore

print('Casos previstos para 2018 ->', int(casos_2018))

############ Pós-processamento ################
plt.scatter(anos, casos, color='black')
plt.scatter(ano_futuro, casos_2018, color='red')
plt.plot(anos, regr.predict(anos), color='blue')

plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([2018])
plt.yticks([int(casos_2018)])

plt.show()
