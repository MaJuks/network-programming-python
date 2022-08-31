import argparse
import hashlib

from Crypto.Cipher import DES






parser = argparse.ArgumentParser()

parser.add_argument('-d', action='store_true',help='Descruadfaf')
parser.add_argument('-v', action='store_true',help='mostra info')


parser.add_argument('-a',type=str, choices=['des','3des','aes'],help='Descruadfaf2')

parser.add_argument('-i',type=str,help='entrada',required=True)
parser.add_argument('-o',type=str,help='saida')

parser.add_argument('-k',type=str,help='senha',required=True)
args = parser.parse_args()

encrypt = True

if args.d:
    encrypt = False
    print("ok")
else:
    print("ok2")

algo = 'des'
if args.a:
    algo = args.a
print(algo)

arq_entra = args.i
arq_saida = F'{arq_entra}.crypto'
if args.o:
    arq_saida = args.o


senha= args.k
print('')

if args.v:
    print('ent: ',arq_entra)
    print('said: ',arq_saida)
    print('algori: ',algo)
    print('cripto: ', encrypt)
    print('senha: ',senha)

def criptografar(entrada,saida,algoritmo,senha):
    data = open(entrada.file).read()
    if algoritmo == 'des':
        des = DES.new(senha, DES.MODE_ECB)
        saida = des.encrypt(data)
        return saida
def descriptografar(entrada,saida,algoritmo,senha):
    des = DES.new(senha, DES.MODE_ECB)
    s = des.decrypt(saida)
    return s
    


if encrypt:
    criptografar(arq_entra,arq_saida,algo,senha)
else:
    descriptografar(arq_entra,arq_saida,algo,senha)
