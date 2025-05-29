# Exercício 10: Rodar Containeres com Usuário Não-Root

## Objetivo

O principal objetivo deste exercício foi aprender a configurar um `Dockerfile` para que a aplicação dentro do container seja executada por um **usuário não-root**. Esta é uma prática essencial de segurança em Docker, pois reduz a superfície de ataque ao limitar os privilégios da aplicação dentro do ambiente conteinerizado.

## Ferramentas Utilizadas

* **Docker:** Para construir a imagem e executar o contêiner.
* **Python:** Linguagem da aplicação de exemplo.
* **Comandos de usuário Linux (`groupadd`, `useradd`):** Utilizados no `Dockerfile` para criar o usuário não-root.

## Estrutura do Projeto

A estrutura de arquivos do projeto é simples, contendo apenas o script Python:
### `app.py`

```python
import os
import time

print("Iniciando a aplicação Python...")
print(f"Rodando como usuário: {os.getuid()} (Nome: {os.getenv('USER')})")

# Mantém o script rodando para que o contêiner não saia imediatamente,
# permitindo a inspeção de seu status.
while True:
    print(f"Aplicação ainda rodando em {time.ctime()}...")
    time.sleep(5)
    
```
### Estrutura do Dockerfile:
```
# Usa uma imagem Python slim como base, que é mais leve e segura
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Adiciona um novo grupo e usuário não-root.

RUN groupadd -g 1001 appuser && useradd -r -u 1001 -g appuser appuser

# Copia o script Python para o diretório de trabalho
COPY app.py .

# Define o usuário 'appuser' como o usuário padrão
USER appuser

# Executa o script Python que acabamos de copiar.
CMD ["python", "app.py"]

```
**Construir a imagem Docker**
```bash
docker build -t app-nao-root .
```
**Saída do comando:**
```
[+] Building 102.3s (10/10) FINISHED                                                                                                  docker:default
 => [internal] load build definition from Dockerfile                                                                                            3.6s
 => => transferring dockerfile: 1.72kB                                                                                                          0.5s
 => [internal] load metadata for docker.io/library/python:3.9-slim-buster                                                                      10.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                   0.0s
 => [internal] load .dockerignore                                                                                                               1.0s
 => => transferring context: 2B                                                                                                                 0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim-buster@sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d76dc5c0f01cac9b53990                49.2s
 => => resolve docker.io/library/python:3.9-slim-buster@sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d76dc5c0f01cac9b53990                 1.7s
 => => sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d76dc5c0f01cac9b53990 988B / 988B                                                      0.0s
 => => sha256:d5cca64dca485c37ccf06721e36a93bf4331b0404bfd3ef2c7873867965359b7 1.37kB / 1.37kB                                                  0.0s
 => => sha256:c84dbfe3b8deeb39e17d121220107f8354a9083b468a320a77708cd128f11c87 6.82kB / 6.82kB                                                  0.0s
 => => sha256:8b91b88d557765cd8c6802668755a3f6dc4337b6ce15a17e4857139e5fc964f3 27.14MB / 27.14MB                                               27.1s
 => => sha256:8d53da26040835f622504d7762fad14d226ac414efeb5363f5febebc89ff224d 11.04MB / 11.04MB                                               32.0s
 => => sha256:824416e234237961c9c5d4f41dfe5b295a3c35a671ee52889bfb08d8e257ec4c 2.78MB / 2.78MB                                                 16.6s
 => => sha256:84c8c79126f669beec1dcf6f34cd88094471745570c19c29b465dfa7db1fdabd 243B / 243B                                                     17.3s
 => => sha256:2e1c130fa3ec1777a82123374b4c500623959f903c1dd731ee4a83e1f1b38ff2 3.14MB / 3.14MB                                                 28.5s
 => => extracting sha256:8b91b88d557765cd8c6802668755a3f6dc4337b6ce15a17e4857139e5fc964f3                                                       4.0s
 => => extracting sha256:824416e234237961c9c5d4f41dfe5b295a3c35a671ee52889bfb08d8e257ec4c                                                       0.7s
 => => extracting sha256:8d53da26040835f622504d7762fad14d226ac414efeb5363f5febebc89ff224d                                                       1.2s
 => => extracting sha256:84c8c79126f669beec1dcf6f34cd88094471745570c19c29b465dfa7db1fdabd                                                       0.0s
 => => extracting sha256:2e1c130fa3ec1777a82123374b4c500623959f903c1dd731ee4a83e1f1b38ff2                                                       1.2s
 => [internal] load build context                                                                                                               2.2s
 => => transferring context: 396B                                                                                                               0.1s
 => [2/4] WORKDIR /app                                                                                                                          9.9s
 => [3/4] RUN groupadd -g 1001 appuser && useradd -r -u 1001 -g appuser appuser                                                                18.2s
 => [4/4] COPY app.py .                                                                                                                         1.8s
 => exporting to image                                                                                                                          2.3s
 => => exporting layers                                                                                                                         1.6s
 => => writing image sha256:772235bb05424935dd1c9754190c3d68b11441d87100e320655e407bc5054578                                                    0.1s
 => => naming to docker.io/library/app-nao-root 
 ```
 **Rodar o container a partir da imagem construida nele:**
 ```bash
 docker run --name minha-app-segura app-nao-root
 ```
 **Saída do comando:**
 ```
 Iniciando a aplicação Python...
Rodando como usuário: 1001 (Nome: None)
Aplicação ainda rodando em Wed May 28 22:46:20 2025...
Aplicação ainda rodando em Wed May 28 22:46:25 2025...
Aplicação ainda rodando em Wed May 28 22:46:30 2025...
Aplicação ainda rodando em Wed May 28 22:46:35 2025...
Aplicação ainda rodando em Wed May 28 22:46:40 2025...
Aplicação ainda rodando em Wed May 28 22:46:45 2025...
Aplicação ainda rodando em Wed May 28 22:46:50 2025...
Aplicação ainda rodando em Wed May 28 22:46:55 2025...
Aplicação ainda rodando em Wed May 28 22:47:00 2025...
Aplicação ainda rodando em Wed May 28 22:47:05 2025...
Aplicação ainda rodando em Wed May 28 22:47:10 2025...
Aplicação ainda rodando em Wed May 28 22:47:15 2025...
Aplicação ainda rodando em Wed May 28 22:47:20 2025...
Traceback (most recent call last):
  File "/app/app.py", line 11, in <module>
    time.sleep(5)
KeyboardInterrupt
```
**Remover container após execução:**
```bash
docker rm minha-app-segura
```