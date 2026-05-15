import argparse
from Crypto.Hash import SHA256
import hashlib




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
# parser.add_argument('-a', '--alg', \
#     type=str, help='Algoritmo Hash', \
#     choices=['md5','sha256'])
# parser.add_argument('-f', '--file', \
#     type=str, help='Algoritmo Hash', \
#     choices=['dados.txt','dados2.txt'])


# if args.alg == 'md5':
#     # print(f'Algoritmo escolhido: {args.alg}')
#     data = open(args.file).read()
#     hash = hashlib.md5(data.encode()) 
#     print(hash.hexdigest())

# if args.alg == 'sha256':
#     # print(f'Algoritmo escolhido: {args.alg}')
#     data = open(args.file).read()
#     hash = SHA256.new(data.encode())
#     print(hash.hexdigest())