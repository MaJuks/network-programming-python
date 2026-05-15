#executa
# saida do codigo python
for arq in 'dados.txt' 'dados2.txt'
do
        python3 hash.py -l md5 -f $arq > saida.txt
        # saida do terminal
        md5sum $arq | awk '{print $1}' > saida2.txt

        #compara
        if diff saida.txt saida2.txt
        then
            echo "ok $arq"
        else
            echo "erro $arq"
        fi

    # remove arquvivo temp
    rm saida.txt saida2.txt
done