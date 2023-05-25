from functools import partial


# def main():

usuario = {
    'nome': 'Joao',
    'redes': [{
            'nome': 'facebook',
            'imagem_profile': "",
            'imagem_capa': 'imagem1'
    }, {
        'nome': 'twitter',
        'imagem_profile': 'imagem2',
        'imagem_capa': ""
    }]
}


def get_imagem_profile(usuario):  # Retorna a imagem do perfil
    for rede in usuario['redes']:
        if rede['imagem_profile']:
            return rede['imagem_profile']
    return 'default'


def get_imagem_capa(usuario):  # Retorna a imagem da capa
    for rede in usuario['redes']:
        if rede['imagem_capa']:
            return rede['imagem_capa']
    return 'default'

# Utilizando partial


def get_imagem(qual_imagem, usuario):
    for rede in usuario['redes']:
        if rede[qual_imagem]:
            return rede[qual_imagem]
    return 'ddefault'


get_imagem_profile = partial(get_imagem, 'imagem_profile')
get_imagem_capa = partial(get_imagem, 'imagem_capa')

print('\nSaída partial final')
print(get_imagem_profile(usuario))
print(get_imagem_capa(usuario))


# if __name__ == '__main__':
#     main()
