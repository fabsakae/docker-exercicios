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