# Exercício 13: Publicando Imagens no Docker Hub

## Objetivo

O principal objetivo deste exercício foi aprender o processo completo de como publicar uma imagem Docker personalizada no Docker Hub. Isso inclui a criação de um Dockerfile para uma aplicação simples, autenticação no Docker Hub, taggeamento da imagem com o nome de usuário do Docker Hub e, finalmente, o envio (push) da imagem para o repositório online.

## Ferramentas Utilizadas

* **Docker:** Para construir a imagem e gerenciar o login/push.
* **Python:** Linguagem da aplicação de exemplo (`app.py`).
* **Docker Hub:** Plataforma de registro de imagens Docker para armazenamento e compartilhamento.

## Estrutura do Projeto

A pasta `exercicio13` contém os seguintes arquivos:

**Conteúdo do app.py:**
```
python
import datetime
import time

print("Iniciando o script Python para o Exercício 13 (Docker Hub)...")

while True:
    print(f"Data e Hora Atual: {datetime.datetime.now()}")
    time.sleep(5)
    
```
**Contúdo do dockerfile:**
```
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```
**Criar uma conta pelo Docker Hub**
**Fazer Login pelo terminal:**
```
docker login
```
### Reconstuindo a imagem e renomeá-la
**Comando para construir e taggear a imagem:**
```Bash
docker build -t fabsakae/meu-echo:v1 .
```
**Saída do comando:**
```
[+] Building 9.5s (5/5) FINISHED                                                                                                              docker:default
 => [internal] load build definition from Dockerfile                                                                                                    1.8s
 => => transferring dockerfile: 190B                                                                                                                    0.5s
 => [internal] load metadata for docker.io/library/alpine:latest                                                                                        0.3s
 => [internal] load .dockerignore                                                                                                                       0.7s
 => => transferring context: 2B                                                                                                                         0.1s
 => CACHED [1/1] FROM docker.io/library/alpine:latest                                                                                                   0.0s
 => exporting to image                                                                                                                                  1.1s
 => => exporting layers                                                                                                                                 0.1s
 => => writing image sha256:1490c4f3270032c7883c0681e4bbd400a1facead0b38049d4b20a64c5e6409ce                                                            0.3s
 => => naming to docker.io/fabsakae/meu-echo:v1 
```
**Fazer o push da imagem para o Docker Hub:**
``` 
docker push fabsakae/meu-echo:v1`
```
**Saída do comando:**
```
The push refers to repository [docker.io/fabsakae/meu-echo]
08000c18d16d: Mounted from dpage/pgadmin4 
v1: digest: sha256:f106b2cb111d1617dbfb7afb878f5ebe4cdffff8fa9e9c21b6f753d8fc52ada0 size: 527
```
## Verificação no Docker Hub
A imagem fabsakae/meu-echo:v1 agora está disponível publicamente no Docker Hub.

Para visualizar o repositório online, acesse: https://hub.docker.com/repositories/fabsakae