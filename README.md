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
2.  **Executar o contêiner:**
    ```bash
    docker run meu-echo
    ```
    **Saída do Comando:**
    ```
    Olá, Docker!
    ```
---
---
### Exercício 2: Contêiner Nginx com Página HTML Customizada

**Objetivo:** Criar um contêiner com Nginx que sirva uma página HTML customizada (index.html). Montar um volume local com esse arquivo para que ele apareça na raiz do site (/usr/share/nginx/html) e acessar a página via http://localhost.

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
1. **Executar o contêiner Nginx com bind mount e mapeamento de porta:**
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
### Exercício 3: Contêiner Ubuntu com Terminal Interativo (Bash) e Instalação de Curl

**Objetivo:** Iniciar um contêiner da imagem `ubuntu` com um terminal interativo (bash), navegar pelo sistema de arquivos e instalar o pacote `curl` utilizando `apt`.

**Comandos Executados:**

1.  **Iniciar o contêiner Ubuntu com terminal interativo:**
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

2.  **Atualizar a lista de pacotes (dentro do contêiner):**
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

3.  **Instalar o pacote `curl` (dentro do contêiner):**
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

4.  **Verificar a instalação do `curl` (dentro do contêiner):**
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

5.  **Sair do contêiner:**
    ```bash
    exit
    ```
    

---
