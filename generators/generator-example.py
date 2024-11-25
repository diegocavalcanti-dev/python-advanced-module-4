# A simple generator function
def my_gen():
    n = 1
    print('Primeiro print, n é igual a {}'.format(n))
    # Generator function contains yield statements
    yield n

    n += 1
    print('Segundo print, n é igual a {}'.format(n))
    yield n

    n += 1
    print('Terceiro e ultimo print , n é igual a {}'.format(n))
    yield n
    
# Não se usa mais .next, agora é next( ... )

# Então, no final do vídeo, o certo seria: next(test) no lugar de test.next()