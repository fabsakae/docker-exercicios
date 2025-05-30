# Exercício 6: Otimização de Imagens com Multi-Stage Builds (Aplicação Go - GS PING)

## Objetivo

O principal objetivo deste exercício foi demonstrar e praticar a otimização de imagens Docker utilizando o conceito de **Multi-Stage Builds**. Essa técnica permite criar imagens finais muito menores e mais seguras, pois separamos as etapas de construção (compilação de código, instalação de dependências) das etapas de empacotamento da aplicação final. Utilizamos uma aplicação Go (GS PING) como exemplo para ilustrar esse processo.

## Ferramentas Utilizadas

* **Docker:** Para construir a imagem e executar o contêiner.
* **Go (Golang):** Linguagem de programação da aplicação de exemplo (GS PING).

## Estrutura do Projeto

### Arquivo `gs-ping.go` .

**Código-fonte da aplicação Go compilada e empacotada:**

```go
package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		hostname, err := os.Hostname()
		if err != nil {
			fmt.Fprintf(w, "Erro ao obter hostname: %v", err)
			return
		}
		fmt.Fprintf(w, "Olá do contêiner Docker! Hostname: %s\n", hostname)
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080" // Porta padrão se não for definida
	}
	fmt.Printf("Servidor GS PING rodando na porta %s...\n", port)
	http.ListenAndServe(":"+port, nil)
}
```
**Arquivo Dockerfile (Multi-Stage Build):**
``` 
FROM golang:1.20-alpine AS builder

WORKDIR /app

# Copia o arquivo fonte Go para o contêiner
COPY gs-ping.go .

# Compila a aplicação Go.
RUN CGO_ENABLED=0 go build -o gs-ping gs-ping.go

# --- Estágio 2: Runner (para a imagem final, muito menor) ---
# Usamos uma imagem Alpine mínima, que não contém nenhuma ferramenta de compilação.
# Isso torna a imagem final extremamente leve.
FROM alpine:latest

WORKDIR /app

# Copia o binário compilado do estágio 'builder' para o estágio 'runner'
COPY --from=builder /app/gs-ping .

# Define o comando que será executado quando o contêiner for iniciado
CMD ["./gs-ping"]

# Expõe a porta que a aplicação Go escutará
EXPOSE 8080
```
**Contruir a imagem:**
```
docker build -t gs-ping-otimizado .
```
**SAída do comando:**
```
+] Building 26.3s (14/14) FINISHED                                                                                                           docker:default
 => [internal] load build definition from Dockerfile                                                                                                    5.4s
 => => transferring dockerfile: 893B                                                                                                                    0.4s
 => [internal] load metadata for docker.io/library/alpine:latest                                                                                        0.5s
 => [internal] load metadata for docker.io/library/golang:1.22-alpine                                                                                   8.8s
 => [auth] library/golang:pull token for registry-1.docker.io                                                                                           0.0s
 => [internal] load .dockerignore                                                                                                                       1.4s
 => => transferring context: 2B                                                                                                                         0.0s
 => [builder 1/4] FROM docker.io/library/golang:1.22-alpine@sha256:1699c10032ca2582ec89a24a1312d986a3f094aed3d5c1147b19880afe40e052                     0.0s
 => [stage-1 1/3] FROM docker.io/library/alpine:latest                                                                                                  0.0s
 => [internal] load build context                                                                                                                       1.7s
 => => transferring context: 325B                                                                                                                       0.1s
 => CACHED [stage-1 2/3] WORKDIR /app                                                                                                                   0.0s
 => CACHED [builder 2/4] WORKDIR /app                                                                                                                   0.0s
 => CACHED [builder 3/4] COPY main.go .                                                                                                                 0.0s
 => CACHED [builder 4/4] RUN CGO_ENABLED=0 go build -o gs-ping main.go                                                                                  0.0s
 => CACHED [stage-1 3/3] COPY --from=builder /app/gs-ping .                                                                                             0.1s
 => exporting to image                                                                                                                                  1.0s
 => => exporting layers                                                                                                                                 0.0s
 => => writing image sha256:ef37a64af7a88868281ece48c44c1603e27bc1907f8572886f52e9dab0e2c413                                                            0.3s
 => => naming to docker.io/library/gs-ping-otimizado
 ```
 **Execução do container:**
 ```
 docker run -d -p 8080:8080 --name meu-gs-ping gs-ping-otimizado
 ```
 **Saída do comando:**
 ```
 c72d7ad93df0b5b50f55e0824bdb043af932398e4873a96c8edc9982e0927e03
 ```
 **Container rodando:**
 ```
 docker ps
 ```
 **Saida do comando:**
 ```
 CONTAINER ID   IMAGE               COMMAND       CREATED              STATUS          PORTS                                         NAMES
c72d7ad93df0   gs-ping-otimizado   "./gs-ping"   About a minute ago   Up 57 seconds   0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   meu-gs-ping
```
**Testando a Aplicação:**
```
curl http://localhost:8080
```
**Saída do comando:**
```
Olá do GS PING em Docker (Exercício 6)!sakae@DESKTOP-N13N2GV:~/docker-exercicios/exercicio06$
```