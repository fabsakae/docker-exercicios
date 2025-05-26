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
##http://localhost