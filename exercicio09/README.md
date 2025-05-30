# Exercício 9: Site Estático com Nginx em Docker (Usando Creative Tim Now UI Kit)

## Objetivo

O objetivo deste exercício foi criar uma imagem Docker personalizada para hospedar um site HTML/CSS estático usando o servidor web Nginx. O diferencial foi a utilização de um template moderno e completo, o **Now UI Kit** do Creative Tim, para uma experiência de desenvolvimento e implantação mais realista e visualmente atraente.

## Ferramentas Utilizadas

* **Docker:** Utilizado para construir a imagem e gerenciar o ciclo de vida do contêiner.
* **Nginx:** Servidor web leve escolhido para servir os arquivos estáticos do site dentro do contêiner.
* **Creative Tim's Now UI Kit:** Um template HTML/CSS gratuito e responsivo que forneceu a estrutura e o design da página web.
* **WSL (Windows Subsystem for Linux):** Ambiente Linux utilizado para a execução dos comandos Docker.

## Estrutura do Projeto

A estrutura de arquivos do projeto reflete a organização dos arquivos essenciais do template "Now UI Kit", copiados diretamente para a pasta `exercicio09`. Pastas de documentação e exemplos do template original foram omitidas para manter a imagem Docker final o mais enxuta possível.
## Arquivos do Template (Now UI Kit)

O template "Now UI Kit" fornece uma estrutura completa para um site moderno. Os arquivos copiados para este exercício incluem:

* `index.html`: O arquivo HTML principal do site.
* `assets/`: Pasta contendo recursos essenciais como imagens (`img/`), fontes (`fonts/`), estilos (`css/`) e scripts (`js/`) utilizados pelo template.
* `nucleo-icons.html`: Um arquivo HTML relacionado aos ícones utilizados no template.

## Arquivo `Dockerfile`

Este Dockerfile define as instruções para construir a imagem Docker que servirá o site estático com Nginx.

```dockerfile
# Usa a imagem oficial do Nginx como base
FROM nginx:latest

# Remove o conteúdo HTML padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do template para o diretório de serviço do Nginx
COPY . /usr/share/nginx/html

# Expõe a porta 80, que é a porta padrão do Nginx
EXPOSE 80

# Comando padrão do Nginx para iniciar o servidor em foreground
CMD ["nginx", "-g", "daemon off;"]
```
**Construção da Imagem Docker**
```
docker build -t meu-site-nginx .
```
**Saída do comando:**
```
+] Building 20.5s (9/9) FINISHED                                                                                                             docker:default
 => [internal] load build definition from Dockerfile                                                                                                    0.5s
 => => transferring dockerfile: 627B                                                                                                                    0.1s
 => [internal] load metadata for docker.io/library/nginx:latest                                                                                         7.3s
 => [auth] library/nginx:pull token for registry-1.docker.io                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                       0.4s
 => => transferring context: 2B                                                                                                                         0.0s
 => [1/3] FROM docker.io/library/nginx:latest@sha256:fb39280b7b9eba5727c884a3c7810002e69e8f961cc373b89c92f14961d903a0                                   0.8s
 => => resolve docker.io/library/nginx:latest@sha256:fb39280b7b9eba5727c884a3c7810002e69e8f961cc373b89c92f14961d903a0                                   0.8s
 => [internal] load build context                                                                                                                       1.5s
 => => transferring context: 9.53MB                                                                                                                     0.6s
 => CACHED [2/3] RUN rm -rf /usr/share/nginx/html/*                                                                                                     0.0s
 => [3/3] COPY . /usr/share/nginx/html                                                                                                                  4.9s
 => exporting to image                                                                                                                                  2.1s
 => => exporting layers                                                                                                                                 1.2s
 => => writing image sha256:2c22ad14f269a3123af2388a362b48d1c0d2659f6c220caa551e309a3ced293c                                                            0.1s
 => => naming to docker.io/library/meu-site-nginx
 ```
 **Execução do Container:**

 ```
 docker run -d -p 8080:80 --name meu-site-online meu-site-nginx
 ```
 **Saída do comando:**
 ```
 2839a39d2b2a02a4ba01a35c4500ee9e1867bb4a4171a9d814d8f3563fddb1f7
 ```
 **Verifica se o container está rodando:**
 ```
 docker ps
 ```
 **Saída do comando:**
 ```
 CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                     NAMES
2839a39d2b2a   meu-site-nginx   "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   meu-site-online
```

##Acesse o site no navegador: http://localhost:8080.
---