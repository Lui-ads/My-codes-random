import os
def hax(ctrlp):
    lista = {
        'A': '41', 'B': '42', 'C': '43', 'D': '44', 'E': '45', 'F': '46', 'G': '47',
        'H': '48', 'I': '49', 'J': '4A', 'K': '4B', 'L': '4C', 'M': '4D', 'N': '4E',
        'O': '4F', 'P': '50', 'Q': '51', 'R': '52', 'S': '53', 'T': '54', 'U': '55',
        'V': '56', 'W': '57', 'X': '58', 'Y': '59', 'Z': '5A',
        'a': '61', 'b': '62', 'c': '63', 'd': '64', 'e': '65', 'f': '66', 'g': '67',
        'h': '68', 'i': '69', 'j': '6A', 'k': '6B', 'l': '6C', 'm': '6D', 'n': '6E',
        'o': '6F', 'p': '70', 'q': '71', 'r': '72', 's': '73', 't': '74', 'u': '75',
        'v': '76', 'w': '77', 'x': '78', 'y': '79', 'z': '7A',
        '0': '30', '1': '31', '2': '32', '3': '33', '4': '34', '5': '35', '6': '36',
        '7': '37', '8': '38', '9': '39',
        ' ': '20', '!': '21', '?': '3F', '.': '2E', ',': '2C', ':': '3A', ';': '3B',
        '=': '3D'
    }
    
    final = []
    for letra in ctrlp:
        final.append(lista.get(letra, letra))
    return "".join(final)

def deshax(hex_texto):
    lista_reversa = {
        '41': 'A', '42': 'B', '43': 'C', '44': 'D', '45': 'E', '46': 'F', '47': 'G',
        '48': 'H', '49': 'I', '4A': 'J', '4B': 'K', '4C': 'L', '4D': 'M', '4E': 'N',
        '4F': 'O', '50': 'P', '51': 'Q', '52': 'R', '53': 'S', '54': 'T', '55': 'U',
        '56': 'V', '57': 'W', '58': 'X', '59': 'Y', '5A': 'Z',
        '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g',
        '68': 'h', '69': 'i', '6A': 'j', '6B': 'k', '6C': 'l', '6D': 'm', '6E': 'n',
        '6F': 'o', '70': 'p', '71': 'q', '72': 'r', '73': 's', '74': 't', '75': 'u',
        '76': 'v', '77': 'w', '78': 'x', '79': 'y', '7A': 'z',
        '30': '0', '31': '1', '32': '2', '33': '3', '34': '4', '35': '5', '36': '6',
        '37': '7', '38': '8', '39': '9',
        '20': ' ', '21': '!', '3F': '?', '2E': '.', '2C': ',', '3A': ':', '3B': ';',
        '3D': '='
    }
    
    final = []
    i = 0
    while i < len(hex_texto):
        if i + 2 <= len(hex_texto):
            chunk = hex_texto[i:i+2]
            if chunk in lista_reversa:
                final.append(lista_reversa[chunk])
                i += 2
                continue
        final.append(hex_texto[i])
        i += 1
    
    return "".join(final)

os.system('clear')
while True:
    try:
        acao=input('Quer criptografar (crip) ou descriptogafar (descrip)? ')
        if acao == 'crip':
            fala=input('\nSua frase: ')
            fim=hax(fala)
            print(f'\n{fim}\n')
        elif acao == 'descrip':
            codigo=input('\nSua frase criptografada: ')
            fim=deshax(codigo)
            print(f'\n{fim}\n')
        elif acao == 'fim':
            break
    except:
        break
os.system('clear')