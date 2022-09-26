import rsa
import argparse

#rsa_crypt.py [-d] -i ARQ_IN -o ARQ_OUT -k ARQ_PASSWORD

def cifrar(arq_in, arq_out, arq_key):
    #Implemente aqui o código para criptografar
    entrada = open(arq_in).read()    
    with open(arq_key, 'rb') as x:
        publicKey = rsa.PublicKey.load_pkcs1(x.read())
    msg_criptografada = rsa.encrypt(entrada.encode('ascii'), publicKey)
    with open(arq_out, 'wb') as y:
        y.write(msg_criptografada)
    pass

def decifrar(arq_in, arq_out, arq_key):
    #Implemente aqui o código para descriptografar
    with open(arq_in,'rb') as x:
        cipher = x.read()
    with open(arq_key, 'rb') as y:
        privateKey = rsa.PrivateKey.load_pkcs1(y.read())         
    msg_descriptografada = rsa.decrypt(cipher, privateKey).decode('ascii')
    with open(arq_out, 'w') as f:
        f.write(msg_descriptografada)
    pass

decrypt = False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--decrypt',
        help='Descriptografar',
        action = 'store_true'
        )
    parser.add_argument('-i', '--input',
        help='Arquivo de entrada',
        type=str,
        required=True
        )
    parser.add_argument('-o', '--output',
        help='Arquivo de saída',
        type=str,
        )

    parser.add_argument('-k', '--key',
        help='Nome do arquivo com a chave para cifrar ou decifrar',
        type=str,
        required=True
        )

    parser.add_argument('-v', '--verbose',
        help='Apresenta informações sobre a operação',
        action='store_true'
        )

    args = parser.parse_args()

    if args.decrypt:
        decrypt = True
    if args.input:
        ARQ_IN = args.input
        ARQ_OUT = f'{ARQ_IN}.out'

    if args.output:
        ARQ_OUT = args.output

    if args.key:
        ARQ_KEY = args.key

    if args.verbose:
        print(f'Decrypt        : {decrypt}')
        print(f'Arquivo senha  : {ARQ_KEY}')
        print(f'Arquivo entrada: {ARQ_IN}')
        print(f'Arquivo saida  : {ARQ_OUT}')

    if decrypt:
        decifrar(ARQ_IN, ARQ_OUT, ARQ_KEY)
    else:
        cifrar(ARQ_IN, ARQ_OUT, ARQ_KEY) 