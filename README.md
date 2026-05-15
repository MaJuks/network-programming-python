# Redes de Computadores — Atividades Práticas

Coleção de exercícios práticos desenvolvidos na disciplina de Redes de Computadores, abordando comunicação via sockets TCP, criptografia e streaming de vídeo em Python.

---

## Tecnologias Utilizadas

- Python 3
- Biblioteca `socket` (TCP/IP)
- Biblioteca `threading` (threads)
- Biblioteca `cv2` — OpenCV (streaming de webcam)
- Biblioteca `rsa` (criptografia assimétrica RSA)
- Biblioteca `PyCryptodome` — `Crypto` (criptografia simétrica DES/AES e hash MD5/SHA256)
- Biblioteca `pickle` (serialização de dados)
- Biblioteca `streamlit`, `geopandas`, `geobr`, `matplotlib` (demo de mapa)

---

## Estrutura do Projeto

```
Redes/
├── chat-server.py               # Servidor de chat TCP interativo
├── chat-client.py               # Cliente de chat TCP interativo
├── sockets-server.py            # Servidor básico (retorna texto em maiúsculas)
├── sockets-client.py            # Cliente básico
├── sockets-server-threads.py    # Servidor com suporte a múltiplos clientes (threads)
├── prank-cd-tray-server.py      # Servidor de brincadeira (ejeta bandeja do CD)
├── prank-cd-tray-client.py      # Cliente da brincadeira
├── webcam-local.py              # Visualizador de webcam local
├── webcam-server.py             # Servidor de streaming de webcam
├── webcam-client.py             # Cliente de streaming de webcam
├── mapa-municipios.py           # Demo: mapa interativo de municípios brasileiros
├── assimetrica/
│   ├── rsa-keys.py              # Geração de chaves RSA (pública e privada)
│   ├── rsa-crypt.py             # Cifragem e decifragem RSA
│   └── rsa-sign.py              # Assinatura e verificação digital RSA
├── cripto/
│   ├── simetrica.py             # Criptografia simétrica (DES/3DES/AES) — em andamento
│   └── des-crypt.py             # Implementação DES com PyCryptodome
└── hash-and-tester/
    ├── hash-generator.py        # Geração de hash MD5 de arquivo
    ├── tester.sh                # Script de teste comparando hash Python vs md5sum
    └── dados.txt                # Arquivo de dados para teste
```

---

## Atividades

### 1. Sockets Básicos — Echo em Maiúsculas
**Arquivos:** `sockets-server.py` + `sockets-client.py`

Primeiro exercício com sockets TCP. O servidor recebe uma mensagem do cliente e a devolve convertida para letras maiúsculas.

```bash
# Terminal 1 — iniciar servidor (porta 8084)
python3 sockets-server.py

# Terminal 2 — enviar mensagem
python3 sockets-client.py
```

---

### 2. Chat TCP Interativo
**Arquivos:** `chat-server.py` + `chat-client.py`

Chat bidirecional entre servidor e cliente via TCP. O cliente digita `logout` para encerrar a conexão.

```bash
# Terminal 1 — iniciar servidor
python3 chat-server.py

# Terminal 2 — conectar como cliente
python3 chat-client.py
```

> O IP do servidor em `chat-client.py` está fixo. Altere a variável `dest` para o IP correto antes de executar.

---

### 3. Servidor com Múltiplos Clientes (Threads)
**Arquivo:** `sockets-server-threads.py`

Servidor TCP multithreaded: cada nova conexão é tratada em uma thread separada, permitindo múltiplos clientes simultâneos.

```bash
python3 sockets-server-threads.py
```

Use `sockets-client.py` para conectar clientes.

---

### 4. Brincadeira — Ejetar Bandeja do CD
**Arquivos:** `prank-cd-tray-server.py` + `prank-cd-tray-client.py`

Quando o cliente se conecta ao servidor, o servidor executa o comando `eject` para abrir e fechar a bandeja do CD da máquina. Atividade de humor desenvolvida em aula.

```bash
# Na máquina "vítima" — iniciar servidor
python3 prank-cd-tray-server.py

# Na máquina do "atacante" — conectar e acionar
python3 prank-cd-tray-client.py
```

> Funciona apenas em sistemas Linux com drive de CD físico.

---

### 5. Streaming de Webcam via Socket
**Arquivos:** `webcam-local.py`, `webcam-server.py`, `webcam-client.py`

Transmissão de frames de webcam entre máquinas usando sockets TCP e serialização com `pickle`.

- `webcam-local.py` — exibe a webcam local (sem rede)
- `webcam-server.py` — captura um frame e envia ao cliente conectado
- `webcam-client.py` — recebe o frame e exibe na tela

```bash
# Visualizar webcam local
python3 webcam-local.py

# Servidor (máquina com câmera)
python3 webcam-server.py

# Cliente (máquina que recebe o frame)
python3 webcam-client.py
```

> Dependências: `pip install opencv-python`

---

### 6. Criptografia Simétrica (DES/3DES/AES)
**Pasta:** `cripto/`

Implementação de criptografia simétrica com os algoritmos DES, 3DES e AES via linha de comando. Projeto em desenvolvimento durante a disciplina.

```bash
python3 cripto/des-crypt.py -i entrada.txt -o saida.crypto -k senha -a des
```

> Dependências: `pip install pycryptodome`

---

### 7. Criptografia Assimétrica (RSA)
**Pasta:** `assimetrica/`

Implementação completa de criptografia RSA: geração de chaves, cifragem/decifragem e assinatura digital.

```bash
# 1. Gerar chaves
python3 assimetrica/rsa-keys.py -u maria -s 1024 -v

# 2. Cifrar arquivo
python3 assimetrica/rsa-crypt.py -i entrada.txt -o saida.enc -k maria_public_key.pem

# 3. Decifrar arquivo
python3 assimetrica/rsa-crypt.py -d -i saida.enc -o decifrado.txt -k maria_private_key.pem

# 4. Assinar arquivo
python3 assimetrica/rsa-sign.py -s -i arquivo.txt -t assinatura.sig -k maria_private_key.pem

# 5. Verificar assinatura
python3 assimetrica/rsa-sign.py -i arquivo.txt -t assinatura.sig -k maria_public_key.pem
```

> Dependências: `pip install rsa`

---

### 8. Hash e Verificação de Integridade
**Pasta:** `hash-and-tester/`

Geração de hash MD5 de um arquivo usando PyCryptodome e script shell que compara o resultado com o comando `md5sum` do sistema para validar a implementação.

```bash
# Gerar hash do arquivo
python3 hash-and-tester/hash-generator.py

# Executar testes comparativos
bash hash-and-tester/tester.sh
```

---

### Extra: Mapa Interativo de Municípios Brasileiros
**Arquivo:** `mapa-municipios.py`

Aplicação Streamlit que exibe um mapa interativo dos estados e municípios do Brasil usando a biblioteca `geobr`. Demonstração apresentada em aula.

```bash
pip install streamlit geopandas geobr matplotlib
streamlit run mapa-municipios.py
```

---

## Instalação das Dependências

```bash
# Sockets e threading (já incluídos no Python)
# Sem instalação necessária para as atividades 1–4

# OpenCV (atividade 5)
pip install opencv-python

# Criptografia (atividades 6–8)
pip install pycryptodome rsa

# Mapa interativo (extra)
pip install streamlit geopandas geobr matplotlib
```

---

## Informações Acadêmicas

| Campo | Informação |
|---|---|
| Disciplina | Redes de Computadores |
| Professor | Darlon Vasata |
| Instituição | IFPR — Instituto Federal do Paraná, Campus Cascavel |
| Curso | Ensino Médio Técnico Integrado em Informática |
| Período | 2º semestre de 2022 |
| Descrição | Atividades práticas de programação em redes: sockets TCP, criptografia simétrica e assimétrica, hashing e streaming de mídia |

---

## Autor

**Maria Julia**
Estudante de Ensino Médio Técnico Integrado em Informática — IFPR Campus Cascavel

---

## Status do Projeto

Concluído — atividades acadêmicas finalizadas no 2º semestre de 2022.

---

**Criado em:** 18 de abril de 2022
