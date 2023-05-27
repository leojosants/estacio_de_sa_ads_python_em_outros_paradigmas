# Treinamento supervisionado - classificação

# from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

lisa = 1
irregular = 0
pera = 1
laranja = 0

pomar = [[120, lisa], [140, lisa], [180, irregular], [200, irregular]]

resultado = [pera, pera, laranja, laranja]

# Gerar uma árvore de decisão
clf = tree.DecisionTreeClassifier()  # type: ignore

# Classificador
clf = clf.fit(pomar, resultado)

peso = 220
# 1 para lisa e 0 para irregular
superficie = 1

resultado_do_usu = clf.predict([[peso, superficie]])

if resultado_do_usu == 1:
    print('Pera')
else:
    print('Laranja')
