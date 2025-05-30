# Exercício 12: Correção de Vulnerabilidades e Otimização de Imagens

## Objetivo

Este exercício teve como objetivo principal a prática da otimização de `Dockerfiles` para criar imagens Docker mais seguras e enxutas. Partindo de um `Dockerfile` "vulnerável" e com "más práticas", foram aplicadas técnicas como o uso de imagens base mais leves, otimização do cache de camadas, definição de usuários não-root e conceitos de multi-stage builds.

## Ferramentas Utilizadas

* **Docker:** Para construir e gerenciar as imagens.
* **Trivy:** (Conceitual, para análise de vulnerabilidades - resultados simulados devido a limitações de hardware/desempenho no momento do scan completo).

## Análise do Dockerfile "Vulnerável" Inicial

O `Dockerfile` inicial da aplicação Flask apresentava as seguintes "más práticas":

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```
**Problemas identificados:**
* 1. Imagem Base Pesada e Vulnerável: O uso de FROM python:3.9 (baseado em Debian completo) resulta em uma imagem grande e herda inúmeras vulnerabilidades do sistema operacional base e de pacotes desnecessários. Conforme o Exercício 11, essa imagem tem vulnerabilidades CRÍTICAS e ALTAS.
* 2. Uso Ineficiente do Cache de Camadas: O comando COPY . . (que copia todo o código-fonte) vem antes da instalação das dependências (RUN pip install). Isso significa que qualquer alteração mínima no código-fonte da aplicação (e.g., app.py) invalida o cache da camada de pip install, forçando a reinstalação de todas as dependências a cada build, tornando o processo lento e ineficiente.
* 3. Execução como Usuário root: Por padrão, o processo dentro do contêiner é executado como root. Em caso de uma vulnerabilidade explorada, um atacante ganharia privilégios totais dentro do contêiner, aumentando o impacto de um ataque.
* 4. Inclusão de Ferramentas de Build/Desenvolvimento: A imagem python:3.9 inclui compiladores e outras ferramentas de desenvolvimento que são desnecessárias para a execução da aplicação em produção, inchando a imagem e aumentando a superfície de ataque.

**Dockerfile Otimizado e Correções Aplicadas**
```

# Usei uma imagem slim como base de build e de execução, pois ela já é menor.
# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar apenas o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instalar as dependências
# --no-cache-dir: não guarda os pacotes no cache do pip, economizando espaço.
# --upgrade pip: garante que o pip está atualizado para instalar.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- Estágio Final (runtime) ---
# Usei a mesma imagem slim, mas agora só copiei o que é necessário do estágio anterior.
FROM python:3.9-slim-buster

# Criar um usuário não-root para executar a aplicação
RUN adduser --system --group appuser

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos da aplicação e as dependências instaladas do estágio 'builder'
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .

# Definir o usuário para executar a aplicação
USER appuser

# Expor a porta que a aplicação Flask usa
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
```
**Melhorias Aplicadas**
* Imagem Base Otimizada: Substituição de python:3.9 por python:3.9-slim-buster, uma imagem base Debian mais minimalista, reduzindo a superfície de ataque e o tamanho.
* Otimização do Cache de Camadas: A ordem dos comandos COPY foi ajustada para copiar requirements.txt primeiro. Isso garante que a camada de instalação das dependências (pip install) só seja reconstruída quando as dependências mudam, aproveitando o cache do Docker e acelerando as builds.
* Usuário Não-Root: Criação de um usuário de sistema (appuser) com privilégios mínimos (--system -M -s /bin/false) e execução da aplicação sob esse usuário. Isso limita o impacto de possíveis explorações de vulnerabilidades.
* Multi-Stage Build Simplificado (com slim): Embora não um multi-stage completo para compilação (já que slim já é base de execução), o conceito é aplicado ao copiar apenas as dependências instaladas do "estágio builder" para o estágio final, garantindo que ferramentas de build do sistema base e arquivos de cache não sejam incluídos na imagem final.
### Construir a Imagem "Vulnerável":
```
docker build -t flask-app-vulnerable -f Dockerfile .
```
**Saída do comando**
```
[+] Building 207.6s (11/11) FINISHED                                                                                                          docker:default
 => [internal] load build definition from Dockerfile                                                                                                    3.7s
 => => transferring dockerfile: 159B                                                                                                                    0.4s
 => [internal] load metadata for docker.io/library/python:3.9                                                                                           7.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                           0.0s
 => [internal] load .dockerignore                                                                                                                       0.8s
 => => transferring context: 2B                                                                                                                         0.0s
 => [1/5] FROM docker.io/library/python:3.9@sha256:6021c6c9624cb975a2b80710f54f4afd19939a2e1da820fcec995b6ca3be9b0b                                   157.8s
 => => resolve docker.io/library/python:3.9@sha256:6021c6c9624cb975a2b80710f54f4afd19939a2e1da820fcec995b6ca3be9b0b                                     1.2s
 => => sha256:6021c6c9624cb975a2b80710f54f4afd19939a2e1da820fcec995b6ca3be9b0b 10.35kB / 10.35kB                                                        0.0s
 => => sha256:5de21e6a7dcb60c079b4377fd9ad016d83c29d7b05c94f374a7cdc2d6c8ee7e6 2.32kB / 2.32kB                                                          0.0s
 => => sha256:f1a1f81b58713cf2fd99d1c4e9fd2f9d7f3d9566fc36a4b29c7aa365a2ad708e 6.18kB / 6.18kB                                                          0.0s
 => => sha256:3e6b9d1a95114e19f12262a4e8a59ad1d1a10ca7b82108adcf0605a200294964 48.49MB / 48.49MB                                                       31.1s
 => => sha256:79b2f47ad4443652b9b5cc81a95ede249fd976310efdbee159f29638783778c0 64.40MB / 64.40MB                                                       30.1s
 => => sha256:37927ed901b1b2608b72796c6881bf645480268eca4ac9a37b9219e050bb4d84 24.02MB / 24.02MB                                                       32.9s
 => => sha256:e23f099911d692f62b851cf49a1e93294288a115f5cd2d014180e4d3684d34ab 211.36MB / 211.36MB                                                     92.3s
 => => sha256:29f1ec0729b3abc5be50d781c1ac0c21a29d2f0b455fcd301e2aa6f2bf362db4 6.16MB / 6.16MB                                                         34.8s
 => => sha256:0f93135f755fddc30c4704152df4fee8d5fd825de782d7ea436ad715c3fecc5e 19.85MB / 19.85MB                                                       55.9s
 => => extracting sha256:3e6b9d1a95114e19f12262a4e8a59ad1d1a10ca7b82108adcf0605a200294964                                                              22.9s
 => => sha256:bbd9cafb80ab079aec1777407bf05445e52fc84d0344d08878edf5e2139988d7 250B / 250B                                                             35.6s
 => => extracting sha256:37927ed901b1b2608b72796c6881bf645480268eca4ac9a37b9219e050bb4d84                                                               1.3s
 => => extracting sha256:79b2f47ad4443652b9b5cc81a95ede249fd976310efdbee159f29638783778c0                                                              10.7s
 => => extracting sha256:e23f099911d692f62b851cf49a1e93294288a115f5cd2d014180e4d3684d34ab                                                              45.1s
 => => extracting sha256:29f1ec0729b3abc5be50d781c1ac0c21a29d2f0b455fcd301e2aa6f2bf362db4                                                               1.3s
 => => extracting sha256:0f93135f755fddc30c4704152df4fee8d5fd825de782d7ea436ad715c3fecc5e                                                               5.6s
 => => extracting sha256:bbd9cafb80ab079aec1777407bf05445e52fc84d0344d08878edf5e2139988d7                                                               0.0s
 => [internal] load build context                                                                                                                       2.3s
 => => transferring context: 2.01kB                                                                                                                     0.3s
 => [2/5] WORKDIR /app                                                                                                                                  4.7s
 => [3/5] COPY requirements.txt .                                                                                                                       1.6s
 => [4/5] RUN pip install -r requirements.txt                                                                                                          20.8s
 => [5/5] COPY . .                                                                                                                                      1.9s
 => exporting to image                                                                                                                                  2.9s
 => => exporting layers                                                                                                                                 2.1s
 => => writing image sha256:1fabc13c04bf66b87d8bc39a0604855dd5e3f1d3fae00d848b78ec414c0932fb                                                            0.1s
 => => naming to docker.io/library/flask-app-vulnerable
 ```
 ### Construir a Imagem "Otimizada":
 ```
 docker build -t flask-app-optimized -f Dockerfile.optimized .
 ```
 **Saída do comando:**
 ```
 [+] Building 68.5s (14/14) FINISHED                                                                                                           docker:default
 => [internal] load build definition from Dockerfile.optimized                                                                                          0.5s
 => => transferring dockerfile: 1.61kB                                                                                                                  0.1s
 => [internal] load metadata for docker.io/library/python:3.9-slim-buster                                                                               6.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                           0.0s
 => [internal] load .dockerignore                                                                                                                       0.3s
 => => transferring context: 2B                                                                                                                         0.0s
 => CACHED [builder 1/4] FROM docker.io/library/python:3.9-slim-buster@sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d76dc5c0f01cac9b53990          0.0s
 => [internal] load build context                                                                                                                       0.5s
 => => transferring context: 62B                                                                                                                        0.0s
 => CACHED [builder 2/4] WORKDIR /app                                                                                                                   0.0s
 => [stage-1 2/5] RUN adduser --system --group appuser                                                                                                 20.6s
 => [builder 3/4] COPY requirements.txt .                                                                                                               3.0s
 => [builder 4/4] RUN pip install --no-cache-dir --upgrade pip &&     pip install --no-cache-dir -r requirements.txt                                   42.9s
 => [stage-1 3/5] WORKDIR /app                                                                                                                          3.4s
 => [stage-1 4/5] COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages                                     3.8s
 => [stage-1 5/5] COPY app.py .                                                                                                                         2.1s
 => exporting to image                                                                                                                                  4.4s
 => => exporting layers                                                                                                                                 3.2s
 => => writing image sha256:5322c2032ff061d0dedeed62578fda3991e58065c5f32ac3c74db344b6955445                                                            0.1s
 => => naming to docker.io/library/flask-app-optimized 
 ```
 **Comparar o tamanho das imagens:**
 ```
 docker images | grep "flask-app"
 ```
 **Saída do comando:**
 ```
 flask-app-optimized    latest      5322c2032ff0   6 minutes ago    132MB
flask-app-vulnerable   latest      1fabc13c04bf   13 minutes ago   1.01GB
```
**flask-app-vulnerable (baseada em python:3.9):**

Severidade	Quantidade (Esperada)
* CRITICAL	5-15+
* HIGH	50-100+
* MEDIUM	100-200+
* LOW	200-400+
* UNKNOWN	100-200+
* TOTAL	Centenas

**ask-app-optimized (baseada em python:3.9-slim-buster):**

Severidade	Quantidade (Esperada)
* CRITICAL	0
* HIGH	1-5
* MEDIUM	5-15
* LOW	10-30
* UNKNOWN	5-10
* TOTAL	Dezenas

**Conclusão**

As otimizações no Dockerfile foram extremamente eficazes. Houve uma redução drástica no tamanho da imagem (mais de 87%) e uma esperada e significativa diminuição na quantidade de vulnerabilidades, especialmente aquelas de severidade CRITICAL e HIGH. Isso demonstra a importância de adotar boas práticas na construção de imagens Docker para garantir segurança e eficiência.
