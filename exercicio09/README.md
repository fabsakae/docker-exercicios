# Exercício 9: Site Estático com Nginx em Docker

## Objetivo

O objetivo deste exercício foi criar uma imagem Docker personalizada para hospedar um site HTML/CSS estático usando o servidor web Nginx.

## Ferramentas Utilizadas

* **Docker:** Para construir a imagem e executar o contêiner.
* **Nginx:** Servidor web leve utilizado dentro do contêiner para servir os arquivos estáticos.
* **HTML/CSS:** Linguagens base para a construção do conteúdo e estilo do site.

## Estrutura do Projeto

A estrutura de arquivos do projeto é simples, contendo o arquivo HTML principal e uma pasta para os estilos CSS:

exercicio09/
├── index.html
└── css/
└── style.css

**Arquivo `index.html`**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Site Docker</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>Bem-vindo ao Meu Site Docker!</h1>
    </header>
    <main>
        <p>Este é um site HTML/CSS simples, servido por um contêiner Nginx.</p>
        <p>Feito com Docker para o Exercício 9.</p>
    </main>
    <footer>
        <p>&copy; 2025 Fabiola Docker</p>
    </footer>
</body>
</html>
```
**Arquivo style.css**
```
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
    text-align: center;
}

header {
    background-color: #007bff;
    color: white;
    padding: 20px 0;
}

main {
    padding: 20px;
}

footer {
    background-color: #333;
    color: white;
    padding: 10px 0;
    position: fixed;
    bottom: 0;
    width: 100%;
}
```
**Arquivo Dockerfile**
```
# Usa a imagem oficial do Nginx como base
FROM nginx:latest

# Remove o conteúdo HTML padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do seu site estático para o diretório de serviço do Nginx
COPY . /usr/share/nginx/html
    
# Expõe a porta 80, que é a porta padrão do Nginx
EXPOSE 80

# Comando padrão do Nginx para iniciar o servidor em foreground
CMD ["nginx", "-g", "daemon off;"]
```
**Construir a imagem Docker:**
```bash
docker build -t meu-site-nginx .
```
**Saída do comando:**
```
[+] Building 40.1s (8/8) FINISHED                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                            1.4s
 => => transferring dockerfile: 627B                                                                                                            0.1s
 => [internal] load metadata for docker.io/library/nginx:latest                                                                                 0.0s
 => [internal] load .dockerignore                                                                                                               1.6s
 => => transferring context: 2B                                                                                                                 0.0s
 => [1/3] FROM docker.io/library/nginx:latest                                                                                                  19.0s
 => [internal] load build context                                                                                                               8.9s
 => => transferring context: 1.68kB                                                                                                             0.1s
 => [2/3] RUN rm -rf /usr/share/nginx/html/*                                                                                                    7.1s
 => [3/3] COPY . /usr/share/nginx/html                                                                                                          2.8s
 => exporting to image                                                                                                                          3.6s
 => => exporting layers                                                                                                                         2.2s
 => => writing image sha256:6b0102691ac37cc70b7b99b420235a9b593891cd2cd869acac5d4751ae8c8318                                                    0.1s
 => => naming to docker.io/library/meu-site-nginx 
 ```
 **Iniciar o container:**
 ```
 docker run -d -p 8080:80 --name meu-site-online meu-site-nginx
 ```
 **Saída do Comando:**
 ```
 008a0507d463df9404ea111dcf217911528160b7d6832b80dddbc6df995fb698
 ```
 **Verificar o container:**
 ```
 docker ps
 ```
 **saída do comando:**
 ```
 CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS                                     NAMES
008a0507d463   meu-site-nginx   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   meu-site-online
```
##Acesse o site no navegador: http://localhost:8080.
---