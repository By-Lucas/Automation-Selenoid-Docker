# Automação Selenium + Selenoid + Docker

### Rodando automação sem nacessidade de abrir navegador com selenium

- INICIAR E REINICIAR
~~~start
sudo ./restart.sh
~~~

- OU

**Atualizar docker + executar**

~~~start
docker-compose up --build
~~~

#

- RESULTADO
  
~~~result
 ✔ Network 1selenoiddocker_default          Created                                                                                                                                0.0s 
 ✔ Container 1selenoiddocker-selenoid-1     Started                                                                                                                                0.3s 
 ✔ Container 1selenoiddocker-bot-1          Started                                                                                                                                0.7s 
 ✔ Container 1selenoiddocker-selenoid-ui-1  Started 
~~~

- APÓS A CONCLUSÃO, IRÁ APARECE UM DOCUMENTO `success.txt` COMO RESULTADO DA CONCLUZÃO DA EXECUÇÃO DO PROJETO

#

- VERIFICAR E ANALISAR DASH SELENOID
  
~~~seneloid
  http://localhost:8080/#/
~~~

~~~seneloid
  http://localhost:4444/wd/hub/status
~~~
