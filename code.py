from random import randint
from time import sleep

# Palavras a serem escolhidas como palavra principal
palavras_disponiveis = ['MOUSE', 'TECLADO', 'MOUSE PAD', 'CACHORRO', 'JAVASCRIPT', 'HTML', 'PYTHON', 'PASSARINHO',
                        'GATO', 'PAPAGAIO', 'MESA', 'HAMBURGUER', 'COCA COLA', 'JETSKI', 'ESCOLA', 'ENSINO MEDIO']

# Palavra principal
palavra_chave = palavras_disponiveis[randint(0, len(palavras_disponiveis) - 1)]

# Base (Onde o usuário tentará adivinhar cada letra da palavra chave)
base = []
[base.append('_') if palavra_chave[bas] != ' ' else base.append('-') for bas in range(len(palavra_chave))]

# Número de tentativas
tentativas = 7
tentativas_letras = []

acertos = 0
acertos_letras = []

# Enfeite de texto
text_ = 70
lt_text = '='

# Alpha
alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()


def verifica_leta_in_palavra_chave(value):

    if letra in palavra_chave:
        print('\033[32mA letra foi encontrada na palavra!\033[m')

        return True
    else:
        print('\033[31mA letra não foi encontrada na palavra.\033[m')

        return False


def print_palavra_chave(palavra):

    for print_base in palavra:
        print(print_base, end=' ')
    print()


def if_true(value):

    val = 0
    for y in range(0, len(palavra_chave)):

        if palavra_chave[y] == value.upper():
            base[y] = value
            val += 1
    return val


# Verifica se a letra digitada esta em ALPHA('abcdefghi..')
def verifica_letra(value):

    if value not in alpha:
        return False
    return True


# Mostra quais letras o usuário digitou errado
def print_letras_erradas(ls):
    for w in ls:
        print(f'\033[31m{w.upper()}\033[m', end=' ')
    print(), print(lt_text * text_)


# Jogo principal
while True:
    print(lt_text * text_)
    print('Palavra:', end=' ')
    print_palavra_chave(base)
    print(f'\033[31mChances restantes: {tentativas}\033[m')

    if len(tentativas_letras) == 0:
        print(lt_text * text_)
    else:
        print_letras_erradas(tentativas_letras)

    if tentativas == 0:
        break

    elif acertos == len(palavra_chave) - palavra_chave.count(' '):
        break

    while True:
        try:
            letra = str(input('\033[01mDigite uma letra:\033[m '))[0].upper()
        except IndexError:
            print('\033[31mVocê precisa digitar alguma coisa!\033[m')
        else:

            print(lt_text * text_)
            break

    if verifica_letra(letra) is False:

        print('\033[31mApenas letras são permitidas!(Sem acentos)\033[m')
        sleep(0.1)

    else:
        if letra in acertos_letras or letra in tentativas_letras:
            print('\033[31mA letra já foi digitada!Tente outra letra!\033[m')
            sleep(0.1)

        elif letra not in acertos_letras or letra not in tentativas_letras:
            if verifica_leta_in_palavra_chave(letra):
                acertos += if_true(letra)
                acertos_letras.append(letra)
                sleep(0.1)
            else:
                tentativas -= 1
                tentativas_letras.append(letra)
                sleep(0.1)


# PERDEU O JOGO (Errou 6 vezes)
if tentativas == 6:
    print('\033[31mFim de jogo, você perdeu!Tente na proxima.\033[m')
    print('Palavra:', end=' '), print_palavra_chave(palavra_chave)
    print(f'Número de acertos: {acertos}')
    print(lt_text * text_)

# GANHOU O JOGO (Acertou a tdas as letras que tinham na palavra)
else:
    print('\033[32mParabéns, você ganhou!!\033[m')
    print(f'Número de erros: {tentativas}')
    print(lt_text * text_)
