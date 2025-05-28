# Exercícios Docker - Fabíola Sakae

Este repositório contém a resolução dos exercícios propostos na disciplina de Docker, desenvolvidos por Fabíola Sakae.

## Índice dos Exercícios

---
### Exercício 1: Olá, Docker! com Imagem Alpine

**Objetivo:** Criar um Dockerfile que utilize a imagem alpine como base e imprima a mensagem "Olá, Docker!" ao ser executada. Construir a imagem com o nome `meu-echo` e executar um container a partir dela.

**Localização:** `exercicio01/Dockerfile`

**Dockerfile:**
```dockerfile
FROM alpine:latest
CMD ["echo", "Olá, Docker!"]
```
**Comandos Executados:**
1.  **Construir a imagem:**
    ```bash
    docker build -t meu-echo ./exercicio01
    ```
    **Saída do Comando:**
    ```
    [+] Building 18.8s (6/6) FINISHED                                        docker:default
    => [internal] load build definition from Dockerfile                                 2.6s
     => => transferring dockerfile: 190B                                                  0.5s
    => [internal] load metadata for docker.io/library/alpine:latest                      8.8s
     => [auth] library/alpine:pull token for registry-1.docker.io                         0.0s
     => [internal] load .dockerignore                                                     0.8s
    => => transferring context: 2B                                                       0.0s
    => [1/1] FROM docker.io/library/alpine:latest@sha256:a8560b36e8b8210634f77d9f7f9efd7ffa463e380b75e2e74aff4511df3ef88c   1.5s
     => => resolve docker.io/library/alpine:latest@sha256:a8560b36e8b8210634f77d9f7f9efd7ffa463e380b75e2e74aff4511df3ef88c     0.6s
    => => sha256:a8560b36e8b8210634f77d9f7f9efd7ffa463e380b75e2e74aff4511df3ef88c 9.22kB / 9.22kB                                0.0s
    => => sha256:1c4eef651f65e2f7daee7ee785882ac164b02b78fb74503052a26dc061c90474 1.02kB / 1.02kB                                0.0s
    => => sha256:aded1e1a5b3705116fa0a92ba074a5e0b0031647d9c315983ccba2ee5428ec8b 581B / 581B                                  0.0s
     => exporting to image                                                                1.1s
     => => exporting layers                                                               0.0s
     => => writing image sha256:1490c4f3270032c7883c0681e4bbd400a1facead0b38049d4b20a64c5e6409ce     0.2s
    => => naming to docker.io/library/meu-echo
    ```
2.  **Executar o container:**
    ```bash
    docker run meu-echo
    ```
    **Saída do Comando:**
    ```
    Olá, Docker!
    ```
---
---
### Exercício 2: Container Nginx com Página HTML Customizada

**Objetivo:** Criar um container com Nginx que sirva uma página HTML customizada (index.html). Montar um volume local com esse arquivo para que ele apareça na raiz do site (/usr/share/nginx/html) e acessar a página via http://localhost.

**Localização:** `exercicio02/index.html`

**Conteúdo do `index.html`:**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Nginx Customizado</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            padding-top: 50px;
        }
        h1 {
            color: #0056b3;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>Olá do Nginx Customizado de Fabiola!</h1>
    <p>Esta página foi servida por um container Docker.</p>
    <p>Exercício 2 de Docker concluído com sucesso!</p>
</body>
</html>       
```
**Comando executados:**
1. **Executar o container Nginx com bind mount e mapeamento de porta:**
```bash
docker run --name meu-nginx-customizado -p 80:80 -v $(pwd)/exercicio02:/usr/share/nginx/html:ro -d nginx:latest
```
**Saída do comando:**
```
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
61320b01ae5e: Pull complete 
670a101d432b: Pull complete 
405bd2df85b6: Pull complete 
cc80efff8457: Pull complete 
2b9310b2ee4b: Pull complete 
6c4aa022e8e1: Pull complete 
abddc69cb49d: Pull complete 
Digest: sha256:fb39280b7b9eba5727c884a3c7810002e69e8f961cc373b89c92f14961d903a0
Status: Downloaded newer image for nginx:latest
a8b8e00b5345b4b1e2d2ebd4c973724a9f3122c57b41c8279b19383b6871298d
```
**Página no navegador:**
## http://localhost
---
### Exercício 3: Container Ubuntu com Terminal Interativo (Bash) e Instalação de Curl

**Objetivo:** Iniciar um container da imagem `ubuntu` com um terminal interativo (bash), navegar pelo sistema de arquivos e instalar o pacote `curl` utilizando `apt`.

**Comandos Executados:**

1.  **Iniciar o container Ubuntu com terminal interativo:**
    ```bash
    docker run -it ubuntu:latest bash
    ```
    **Saída do Comando:**
    ```
    Unable to find image 'ubuntu:latest' locally
    latest: Pulling from library/ubuntu
    0622fac788ed: Pull complete 
    Digest: sha256:6015f66923d7afbc53558d7ccffd325d43b4e249f41a6e93eef074c9505d2233
    Status: Downloaded newer image for ubuntu:latest
    ```

2.  **Atualizar a lista de pacotes (dentro do container):**
    ```bash
    apt update
    ```
    **Saída de comando:**
    ```
    *Get:1 http://archive.ubuntu.com/ubuntu noble InRelease [256 kB]                                          
    Get:2 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]                                
    Get:3 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [1088 kB]                 
    Get:4 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
    Get:5 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [1434 kB]
    Get:6 http://archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
    Get:7 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [1081 kB]
    Get:8 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Packages [22.1 kB]                                                          
    Get:9 http://archive.ubuntu.com/ubuntu noble/restricted amd64 Packages [117 kB]                                                                     
    Get:10 http://archive.ubuntu.com/ubuntu noble/universe amd64 Packages [19.3 MB]                                                                     
    Get:11 http://archive.ubuntu.com/ubuntu noble/main amd64 Packages [1808 kB]                                                                         
    Get:12 http://archive.ubuntu.com/ubuntu noble/multiverse amd64 Packages [331 kB]                                                                    
    Get:13 http://archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1385 kB]                                                             
    Get:14 http://archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Packages [26.7 kB]                                                           
    Get:15 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1399 kB]                                                                 
    Get:16 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Packages [1478 kB]                                                           
    Get:17 http://archive.ubuntu.com/ubuntu noble-backports/universe amd64 Packages [31.8 kB]                                                           
    Get:18 http://archive.ubuntu.com/ubuntu noble-backports/main amd64 Packages [48.0 kB]                                                               
    Fetched 30.2 MB in 48s (628 kB/s)                                                                                                                   
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    All packages are up to date.*
    ```

3.  **Instalar o pacote `curl` (dentro do container):**
    ```bash
    apt install -y curl
    ```
    ```
    *Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    The following additional packages will be installed:
    ca-certificates krb5-locales libbrotli1 libcurl4t64 libgssapi-krb5-2 libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 libldap-common libldap2
    libnghttp2-14 libpsl5t64 librtmp1 libsasl2-2 libsasl2-modules libsasl2-modules-db libssh-4 openssl publicsuffix
    Suggested packages:
    krb5-doc krb5-user libsasl2-modules-gssapi-mit | libsasl2-modules-gssapi-heimdal libsasl2-modules-ldap libsasl2-modules-otp libsasl2-modules-sql
    The following NEW packages will be installed:
    ca-certificates curl krb5-locales libbrotli1 libcurl4t64 libgssapi-krb5-2 libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 libldap-common
    libldap2 libnghttp2-14 libpsl5t64 librtmp1 libsasl2-2 libsasl2-modules libsasl2-modules-db libssh-4 openssl publicsuffix
    0 upgraded, 21 newly installed, 0 to remove and 0 not upgraded.
    Need to get 3566 kB of archives.
    After this operation, 9211 kB of additional disk space will be used.
    Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 openssl amd64 3.0.13-0ubuntu3.5 [1002 kB]
    Get:2 http://archive.ubuntu.com/ubuntu noble/main amd64 ca-certificates all 20240203 [159 kB]
    Get:3 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 krb5-locales all 1.20.1-6ubuntu2.5 [14.5 kB]
    Get:4 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libkrb5support0 amd64 1.20.1-6ubuntu2.5 [34.1 kB]
    Get:5 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libk5crypto3 amd64 1.20.1-6ubuntu2.5 [82.0 kB]
    Get:6 http://archive.ubuntu.com/ubuntu noble/main amd64 libkeyutils1 amd64 1.6.3-3build1 [9490 B]
    Get:7 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libkrb5-3 amd64 1.20.1-6ubuntu2.5 [347 kB]
    Get:8 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libgssapi-krb5-2 amd64 1.20.1-6ubuntu2.5 [143 kB]
    Get:9 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libnghttp2-14 amd64 1.59.0-1ubuntu0.2 [74.3 kB]
    Get:10 http://archive.ubuntu.com/ubuntu noble/main amd64 libpsl5t64 amd64 0.21.2-1.1build1 [57.1 kB]
    Get:11 http://archive.ubuntu.com/ubuntu noble/main amd64 publicsuffix all 20231001.0357-0.1 [129 kB]
    Get:12 http://archive.ubuntu.com/ubuntu noble/main amd64 libbrotli1 amd64 1.1.0-2build2 [331 kB]
    Get:13 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libsasl2-modules-db amd64 2.1.28+dfsg1-5ubuntu3.1 [20.4 kB]
    Get:14 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libsasl2-2 amd64 2.1.28+dfsg1-5ubuntu3.1 [53.2 kB]
    Get:15 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libldap2 amd64 2.6.7+dfsg-1~exp1ubuntu8.2 [196 kB]
    Get:16 http://archive.ubuntu.com/ubuntu noble/main amd64 librtmp1 amd64 2.4+20151223.gitfa8646d.1-2build7 [56.3 kB]
    Get:17 http://archive.ubuntu.com/ubuntu noble/main amd64 libssh-4 amd64 0.10.6-2build2 [188 kB]
    Get:18 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libcurl4t64 amd64 8.5.0-2ubuntu10.6 [341 kB]
    Get:19 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 curl amd64 8.5.0-2ubuntu10.6 [226 kB]
    Get:20 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libldap-common all 2.6.7+dfsg-1~exp1ubuntu8.2 [31.7 kB]
    Get:21 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libsasl2-modules amd64 2.1.28+dfsg1-5ubuntu3.1 [69.9 kB]
    Fetched 3566 kB in 6s (597 kB/s)           
    debconf: delaying package configuration, since apt-utils is not installed
    Selecting previously unselected package openssl.
    (Reading database ... 4381 files and directories currently installed.)
    Preparing to unpack .../00-openssl_3.0.13-0ubuntu3.5_amd64.deb ...
    Unpacking openssl (3.0.13-0ubuntu3.5) ...
    Selecting previously unselected package ca-certificates.
    Preparing to unpack .../01-ca-certificates_20240203_all.deb ...
    Unpacking ca-certificates (20240203) ...
    Selecting previously unselected package krb5-locales.
    Preparing to unpack .../02-krb5-locales_1.20.1-6ubuntu2.5_all.deb ...
    Unpacking krb5-locales (1.20.1-6ubuntu2.5) ...
    Selecting previously unselected package libkrb5support0:amd64.
    Preparing to unpack .../03-libkrb5support0_1.20.1-6ubuntu2.5_amd64.deb ...
    Unpacking libkrb5support0:amd64 (1.20.1-6ubuntu2.5) ...
    Selecting previously unselected package libk5crypto3:amd64.
    Preparing to unpack .../04-libk5crypto3_1.20.1-6ubuntu2.5_amd64.deb ...
    Unpacking libk5crypto3:amd64 (1.20.1-6ubuntu2.5) ...
    Selecting previously unselected package libkeyutils1:amd64.
    Preparing to unpack .../05-libkeyutils1_1.6.3-3build1_amd64.deb ...
    Unpacking libkeyutils1:amd64 (1.6.3-3build1) ...
    Selecting previously unselected package libkrb5-3:amd64.
    Preparing to unpack .../06-libkrb5-3_1.20.1-6ubuntu2.5_amd64.deb ...
    Unpacking libkrb5-3:amd64 (1.20.1-6ubuntu2.5) ...
    Selecting previously unselected package libgssapi-krb5-2:amd64.
    Preparing to unpack .../07-libgssapi-krb5-2_1.20.1-6ubuntu2.5_amd64.deb ...
    Unpacking libgssapi-krb5-2:amd64 (1.20.1-6ubuntu2.5) ...
    Selecting previously unselected package libnghttp2-14:amd64.
    Preparing to unpack .../08-libnghttp2-14_1.59.0-1ubuntu0.2_amd64.deb ...
    Unpacking libnghttp2-14:amd64 (1.59.0-1ubuntu0.2) ...
    Selecting previously unselected package libpsl5t64:amd64.
    Preparing to unpack .../09-libpsl5t64_0.21.2-1.1build1_amd64.deb ...
    Unpacking libpsl5t64:amd64 (0.21.2-1.1build1) ...
    Selecting previously unselected package publicsuffix.
    Preparing to unpack .../10-publicsuffix_20231001.0357-0.1_all.deb ...
    Unpacking publicsuffix (20231001.0357-0.1) ...
    Selecting previously unselected package libbrotli1:amd64.
    Preparing to unpack .../11-libbrotli1_1.1.0-2build2_amd64.deb ...
    Unpacking libbrotli1:amd64 (1.1.0-2build2) ...
    Selecting previously unselected package libsasl2-modules-db:amd64.
    Preparing to unpack .../12-libsasl2-modules-db_2.1.28+dfsg1-5ubuntu3.1_amd64.deb ...
    Unpacking libsasl2-modules-db:amd64 (2.1.28+dfsg1-5ubuntu3.1) ...
    Selecting previously unselected package libsasl2-2:amd64.
    Preparing to unpack .../13-libsasl2-2_2.1.28+dfsg1-5ubuntu3.1_amd64.deb ...
    Unpacking libsasl2-2:amd64 (2.1.28+dfsg1-5ubuntu3.1) ...
    Selecting previously unselected package libldap2:amd64.
    Preparing to unpack .../14-libldap2_2.6.7+dfsg-1~exp1ubuntu8.2_amd64.deb ...
    Unpacking libldap2:amd64 (2.6.7+dfsg-1~exp1ubuntu8.2) ...
    Selecting previously unselected package librtmp1:amd64.
    Preparing to unpack .../15-librtmp1_2.4+20151223.gitfa8646d.1-2build7_amd64.deb ...
    Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2build7) ...
    Selecting previously unselected package libssh-4:amd64.
    Preparing to unpack .../16-libssh-4_0.10.6-2build2_amd64.deb ...
    Unpacking libssh-4:amd64 (0.10.6-2build2) ...
    Selecting previously unselected package libcurl4t64:amd64.
    Preparing to unpack .../17-libcurl4t64_8.5.0-2ubuntu10.6_amd64.deb ...
    Unpacking libcurl4t64:amd64 (8.5.0-2ubuntu10.6) ...
    Selecting previously unselected package curl.
    Preparing to unpack .../18-curl_8.5.0-2ubuntu10.6_amd64.deb ...
    Unpacking curl (8.5.0-2ubuntu10.6) ...
    Selecting previously unselected package libldap-common.
    Preparing to unpack .../19-libldap-common_2.6.7+dfsg-1~exp1ubuntu8.2_all.deb ...
    Unpacking libldap-common (2.6.7+dfsg-1~exp1ubuntu8.2) ...
    Selecting previously unselected package libsasl2-modules:amd64.
    Preparing to unpack .../20-libsasl2-modules_2.1.28+dfsg1-5ubuntu3.1_amd64.deb ...
    Unpacking libsasl2-modules:amd64 (2.1.28+dfsg1-5ubuntu3.1) ...
    Setting up libkeyutils1:amd64 (1.6.3-3build1) ...
    Setting up libbrotli1:amd64 (1.1.0-2build2) ...
    Setting up libsasl2-modules:amd64 (2.1.28+dfsg1-5ubuntu3.1) ...
    Setting up libpsl5t64:amd64 (0.21.2-1.1build1) ...
    Setting up libnghttp2-14:amd64 (1.59.0-1ubuntu0.2) ...
    Setting up krb5-locales (1.20.1-6ubuntu2.5) ...
    Setting up libldap-common (2.6.7+dfsg-1~exp1ubuntu8.2) ...
    Setting up libkrb5support0:amd64 (1.20.1-6ubuntu2.5) ...
    Setting up libsasl2-modules-db:amd64 (2.1.28+dfsg1-5ubuntu3.1) ...
    Setting up librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2build7) ...
    Setting up libk5crypto3:amd64 (1.20.1-6ubuntu2.5) ...
    Setting up libsasl2-2:amd64 (2.1.28+dfsg1-5ubuntu3.1) ...
    Setting up libkrb5-3:amd64 (1.20.1-6ubuntu2.5) ...
    Setting up openssl (3.0.13-0ubuntu3.5) ...
    Setting up publicsuffix (20231001.0357-0.1) ...
    Setting up libldap2:amd64 (2.6.7+dfsg-1~exp1ubuntu8.2) ...
    Setting up ca-certificates (20240203) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 79.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC entries checked: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.38.2 /usr/local/share/perl/5.38.2 /usr/lib/x86_64-linux-gnu/perl5/5.38 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.38 /usr/share/perl/5.38 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 8.)
    debconf: falling back to frontend: Teletype
    Updating certificates in /etc/ssl/certs...
    146 added, 0 removed; done.
    Setting up libgssapi-krb5-2:amd64 (1.20.1-6ubuntu2.5) ...
    Setting up libssh-4:amd64 (0.10.6-2build2) ...
    Setting up libcurl4t64:amd64 (8.5.0-2ubuntu10.6) ...
    Setting up curl (8.5.0-2ubuntu10.6) ...
    Processing triggers for libc-bin (2.39-0ubuntu8.4) ...
    Processing triggers for ca-certificates (20240203) ...
    Updating certificates in /etc/ssl/certs...
    0 added, 0 removed; done.
    Running hooks in /etc/ca-certificates/update.d...
    done.
    ```

4.  **Verificar a instalação do `curl` (dentro do container):**
    ```bash
    curl --version
    ```
    **Saída do Comando:**
    ```
    curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.7
    Release-Date: 2023-12-06, security patched: 8.5.0-2ubuntu10.6
    Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
    Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
    ```

5.  **Sair do container:**
    ```bash
    exit
    ```
    

---
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
   
---
### Exercício 5: Container Alpine com Variável de Ambiente

**Objetivo:** Criar um container com a imagem `alpine`, passar uma variável de ambiente chamada `MEU_NOME` com um nome escolhido, e imprimir o valor da variável com o comando `echo`.

**Comandos Executados:**

1.  **Iniciar o container Alpine com variável de ambiente e imprimir o nome:**
    ```bash
    docker run --rm -it -e MEU_NOME="Fabiola Sakae" alpine:latest sh -c 'echo "Olá, $MEU_NOME!"'
    ```
    
    **Saída do Comando:**
    ```
    Unable to find image 'alpine:latest' locally
    latest: Pulling from library/alpine
    f18232174bc9: Already exists 
    Digest: sha256:a8560b36e8b8210634f77d9f7f9efd7ffa463e380b75e2e74aff4511df3ef88c
    Status: Downloaded newer image for alpine:latest
    Olá, Fabiola Sakae!
    ```
---
### Exercício 6: Multi-Stage Build para Otimizar uma Aplicação Go

**Objetivo:** Utilizar um multi-stage build para otimizar uma aplicação Go, reduzindo o tamanho da imagem final. Utilizar para praticar o projeto GS PING desenvolvido em Golang.

**Arquivos Criados:**

* `exercicio06/main.go`:
    ```go
    package main

    import (
    	"fmt"
    	"net/http"
    )

    func main() {
    	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    		fmt.Fprintf(w, "Olá do GS PING em Docker (Exercício 6)!")
    	})

    	fmt.Println("Servidor GS PING rodando na porta 8080...")
    	http.ListenAndServe(":8080", nil)
    }
    ```
* `exercicio06/Dockerfile`:
    ```dockerfile
    # --- Fase de Construção (Builder Stage) ---
    FROM golang:1.22-alpine AS builder

    WORKDIR /app

    COPY main.go .

    RUN CGO_ENABLED=0 go build -o gs-ping main.go

    # --- Fase Final (Final Stage) ---
    FROM alpine:latest

    WORKDIR /app

    COPY --from=builder /app/gs-ping .

    EXPOSE 8080

    CMD ["./gs-ping"]
    ```

**Comandos Executados:**

1.  **Navegar até a pasta do exercício:**
    ```bash
    cd exercicio06
    ```

2.  **Construir a imagem Docker com multi-stage build:**
    ```bash
    docker build -t gs-ping-otimizado .
    ```
    **Saída do Comando:**
    ```
    [+] Building 189.9s (14/14) FINISHED                                                                                                  docker:default
    => [internal] load build definition from Dockerfile                                                                                            3.5s
    => => transferring dockerfile: 893B                                                                                                            0.7s
    => [internal] load metadata for docker.io/library/golang:1.22-alpine                                                                           8.4s
    => [internal] load metadata for docker.io/library/alpine:latest                                                                                0.6s
    => [auth] library/golang:pull token for registry-1.docker.io                                                                                   0.0s
    => [internal] load .dockerignore                                                                                                               1.0s
    => => transferring context: 2B                                                                                                                 0.0s
    => [builder 1/4] FROM docker.io/library/golang:1.22-alpine@sha256:1699c10032ca2582ec89a24a1312d986a3f094aed3d5c1147b19880afe40e052            95.2s
    => => resolve docker.io/library/golang:1.22-alpine@sha256:1699c10032ca2582ec89a24a1312d986a3f094aed3d5c1147b19880afe40e052                     1.3s
    => => sha256:1699c10032ca2582ec89a24a1312d986a3f094aed3d5c1147b19880afe40e052 10.30kB / 10.30kB                                                0.0s
    => => sha256:6d405dfc5fdf3a45df1529cf060b920041f52ce523487e0f36f02765af294a51 1.92kB / 1.92kB                                                  0.0s
    => => sha256:4129f51f28c9ae5de799b958ba2aaa8f92f26cc7bf47c107891673fe4b516c03 2.08kB / 2.08kB                                                  0.0s
    => => sha256:1f3e46996e2966e4faa5846e56e76e3748b7315e2ded61476c24403d592134f0 3.64MB / 3.64MB                                                  5.2s
    => => sha256:4d75fd4b73869ed224045c010cdec78756eefb6752a5a8e4804294009eac11e9 294.90kB / 294.90kB                                              4.1s
    => => sha256:afa154b433c7f72db064d19e1bcfa84ee196ad29120328f6bdb2c5fbd7b8eeac 69.36MB / 69.36MB                                               42.0s
    => => sha256:5f837c998576dcb54bc285997f33fcc2166dff6aa48fe3a374da92474efd5fe8 126B / 126B                                                      5.4s
    => => extracting sha256:1f3e46996e2966e4faa5846e56e76e3748b7315e2ded61476c24403d592134f0                                                       4.0s
    => => sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B                                                        7.8s
    => => extracting sha256:4d75fd4b73869ed224045c010cdec78756eefb6752a5a8e4804294009eac11e9                                                       1.3s
    => => extracting sha256:afa154b433c7f72db064d19e1bcfa84ee196ad29120328f6bdb2c5fbd7b8eeac                                                      38.0s
    => => extracting sha256:5f837c998576dcb54bc285997f33fcc2166dff6aa48fe3a374da92474efd5fe8                                                       0.0s
    => => extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1                                                       0.0s
    => [internal] load build context                                                                                                               3.6s
    => => transferring context: 325B                                                                                                               0.1s
    => CACHED [stage-1 1/3] FROM docker.io/library/alpine:latest                                                                                   0.2s
    => [stage-1 2/3] WORKDIR /app                                                                                                                  4.0s
    => [builder 2/4] WORKDIR /app                                                                                                                  3.2s
    => [builder 3/4] COPY main.go .                                                                                                                2.1s
    => [builder 4/4] RUN CGO_ENABLED=0 go build -o gs-ping main.go                                                                                63.4s
    => [stage-1 3/3] COPY --from=builder /app/gs-ping .                                                                                            2.9s
    => exporting to image                                                                                                                          3.1s
    => => exporting layers                                                                                                                         2.0s
    => => writing image sha256:ef37a64af7a88868281ece48c44c1603e27bc1907f8572886f52e9dab0e2c413                                                    0.1s
    => => naming to docker.io/library/gs-ping-otimizado 
    ```

3.  **Verificar o tamanho da imagem otimizada:**
    ```bash
    docker images gs-ping-otimizado
    ```
    **Saída do Comando:**
    ```
    REPOSITORY          TAG         IMAGE ID        CREATED         SIZE
    gs-ping-otimizado   latest      ef37a64af7a8    X minutes ago   14.8MB
    ```

4.  **Executar o contêiner da aplicação Go:**
    ```bash
    docker run --name gs-ping-app -p 8080:8080 -d gs-ping-otimizado
    ```
    **Saída do Comando:**
    ```
    081becffbd7b4f93dfc4a1b1e988b315df9b771b9ac86d301d1a72e8e98eef4c
    ```

5.  **Acessar a aplicação via navegador:**
    * URL: `http://localhost:8080`
    
---
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
# Exercício 8: PostgreSQL e PgAdmin com Docker Compose

## Objetivo

O objetivo deste exercício foi utilizar o Docker Compose para definir e executar uma aplicação multi-container, composta por um servidor de banco de dados PostgreSQL e uma interface de gerenciamento gráfica, o pgAdmin. 

## Conteúdo do `docker-compose.yml`


```yaml
version: '3.8' 

services:
  db:
    image: postgres:13
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin_interface
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    depends_on:
      - db

volumes:
  postgres_data:
```
## Iniciando o serviço com Docker compose
**Comando:**
```bash
docker compose up -d
```
**Saida do Comando:**
```
WARN[0002] /home/sakae/docker-exercicios/exercicio08/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 32/32
 ✔ pgadmin Pulled                                                                                                                             172.7s 
 ✔ db Pulled                                                                                                                                  104.7s 
                                                                                                                                                     
                                                                                                                                                     
[+] Running 4/4
 ✔ Network exercicio08_default         Created                                                                                                  3.7s 
 ✔ Volume "exercicio08_postgres_data"  Created                                                                                                  0.4s 
 ✔ Container postgres_db               Started                                                                                                 27.8s 
 ✔ Container pgadmin_interface         Started 
```
**Status dos Containers: Comando:**
```
Docker ps
```
**Saída do Comando:**
```
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                              NAMES
2942ad8480a8   dpage/pgadmin4   "/entrypoint.sh"         10 minutes ago   Up 9 minutes    443/tcp, 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   pgadmin_interface
a92059f87cf4   postgres:13      "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp        postgres_db
```
## Acessar a Interface do pgAdmin no Navegador:
## http://localhost:8080
Usar as credenciais do docker-compose.yml:
Email: admin@example.com
Senha: admin
Após fazer login, adicionar um novo servidor para se conectar ao PostgreSQL. Configurar o Add New Server com as informações do Docker compose.yml.
O painel principal mostrará o dashboard do servidor PostgreSQL, com métricas e gráficos.


