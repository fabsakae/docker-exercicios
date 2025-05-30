# Exercício 7: Comunicação entre MongoDB e Mongo Express com Rede Docker Personalizada

## Objetivo

O objetivo deste exercício é criar uma rede Docker personalizada para permitir a comunicação entre dois containers: um servidor MongoDB e uma interface de gerenciamento MongoDB Express. Garantir que a comunicação funcione corretamente e que os serviços possam ser acessados via navegador.


1.  **Criação da Rede Docker Personalizada:**
    Criar uma rede Docker personalizada chamada `app-mongo-net` para que os containers possam se comunicar usando seus nomes de serviço.
    ```bash
    docker network create app-mongo-net
    ```
    Saída esperada:
    ```
    fec66a9c7e96b48012b1b077a546334eead9a60cb08ff55875febe8a93c099fe
    ```

3.  **Iniciando o Container do MongoDB (versão 4.4):**
    Iniciar o contêiner do MongoDB na rede `app-mongo-net` usando a imagem `mongo:4.4` (devido à exigência de AVX em versões mais recentes). Mapeei a porta 27017 para acesso externo, embora a comunicação interna seja via rede Docker.
    ```bash
    docker run --name mongodb -p 27017:27017 --network app-mongo-net -d mongo:4.4
    ```
    Saída esperada :
    ```
    Unable to find image 'mongo:4.4' locally
    4.4: Pulling from library/mongo
    d4c3c94e5e10: Pull complete 
    bca5893fe8bd: Pull complete 
    35ec036951f8: Pull complete 
    ddb77a597b02: Pull complete 
    7ab9eb5a4d9d: Pull complete 
    a6c1ba219414: Pull complete 
    83b651df5384: Pull complete 
    e233f2d1b360: Pull complete 
    Digest: sha256:52c42cbab240b3c5b1748582cc13ef46d521ddacae002bbbda645cebed270ec0
    Status: Downloaded newer image for mongo:4.4
    ab7b6d34d28cbf30275da4679fc7371d7bb6f0ee4029c84c9e564090443a6825
    ```
    Verifique se o MongoDB está rodando:
    ```bash
    docker ps
    ```
    Saída esperada:
    ```
    ab7b6d34d28c   mongo:4.4   "docker-entrypoint.s…"   About a minute ago   Up 59 seconds   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   mongodb
    ```
    4.  **Iniciando o Container do Mongo Express:**
    Iniciar o contêiner do Mongo Express na mesma rede, configurando-o para se conectar ao `mongodb` usando o nome do container como host.
    ```bash
    docker run --name mongo-express -p 8081:8081 --network app-mongo-net \
      -e ME_CONFIG_MONGODB_SERVER=mongodb -e ME_CONFIG_MONGODB_PORT=27017 -d mongo-express
    ```
    Saída esperada:
    ```
    56c771279bc912bb83a9330d6606802acd35c1faa4eb5bc370fe6c99b7436cee
    ```
    Verificar se ambos os containeres estão rodando:
    ```bash
    docker ps
    ```
    Saída:
    ```
    CONTAINER ID        IMAGE           COMMAND                  CREATED             STATUS          PORTS                                              NAMES
    56c771279bc9        mongo-express   "/sbin/tini -- /dock…"   10 seconds ago       Up 7 seconds    0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp        mongo-express
    ab7b6d34d28c        mongo:4.4       "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes    0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp    mongodb
    ```

5.  **Acessando a Interface do Mongo Express:**
    No navegador, acesse `http://localhost:8081`.
    ---