### Exercício 4: Container MySQL com Dados Persistidos via Volume Nomeado

**Objetivo:** Iniciar um container MySQL, definir uma senha de root, persistir os dados usando um volume nomeado e criar um banco de dados de teste.

**Comandos Executados:**

1.  **Criar o volume nomeado para persistência de dados:**
    ```bash
    docker volume create dados-mysql
    ```
    **Saída do Comando:**
    ```
    dados-mysql
    ```

2.  **Iniciar o container MySQL com volume e senha:**
    ```bash
    docker run --name meu-mysql -e MYSQL_ROOT_PASSWORD=teste -p 3306:3306 -v dados-mysql:/var/lib/mysql -d mysql:latest
    ```
    
    **Saída do Comando:**
    ```
    Unable to find image 'mysql:latest' locally
    latest: Pulling from library/mysql
    c2eb5d06bfea: Pull complete 
    ba361f0ba5e7: Pull complete 
    0e83af98b000: Pull complete 
    770e931107be: Pull complete 
    a2be1b721112: Pull complete 
    68c594672ed3: Pull complete 
    cfd201189145: Pull complete 
    e9f009c5b388: Pull complete 
    61a291920391: Pull complete 
    c8604ede059a: Pull complete 
    Digest: sha256:2247f6d47a59e5fa30a27ddc2e183a3e6b05bc045e3d12f8d429532647f61358
    Status: Downloaded newer image for mysql:latest
    4226047f7639db6753e7e37f1995b2451371516df05b5de51f259be317e8a0e3
    ```

3.  **Acessar o terminal do container MySQL:**
    ```bash
    docker exec -it meu-mysql bash
    ```
    **Saída do Comando:**
    ```
    bash-5.1#
    ```

4.  **Conectar-se ao MySQL e criar banco de dados:**
    ```bash
    mysql -u root -p
    ```
   
    **Saída do Comando (`mysql>` prompt):**
    ```sql
    CREATE DATABASE minha_base_de_dados;
    ```
    ```
    Query OK, 1 row affected (1.920 sec)
    ```

    **Verificar bancos de dados:**
    ```sql
    SHOW DATABASES;
    ```
    **Saída do Comando:**
    ```
    +---------------------+
    | Database            |
    +---------------------+
    | information_schema  |
    | minha_base_de_dados |
    | mysql               |
    | performance_schema  |
    | sys                 |
    +---------------------+
    5 rows in set (1.408 sec)
    ```

5.  **Sair do cliente MySQL e do container:**
    ```sql
    exit;
    ```
    ```bash
    exit
    ```