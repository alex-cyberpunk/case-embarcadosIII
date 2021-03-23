chmod +rwx myscript.sh
#esse comando é para dar permissão de acesso ao pid.txt ao arquivo myscript.sh
while true
#um looping infinito
do
        while IFS= read -r linha || [[ -n "$linha" ]]; do
                                                for pid in $(pidof -x python3 parte_python.py); do
                                               
														if [ $pid == $linha ]; then
                                                                echo "1: It is alive"
                                                        fi
                                                done
												#este looping identifica todos os pids ativos e ve se coincide com o pid lido no arquivo 
			if [ "0" == $linha ]; then
				echo "1:It is dead"
			#uma string 0 foi escolhida como ponto de identificacão que o programa não esta mais rodando
			fi
        done < pid.txt
sleep .1
done
