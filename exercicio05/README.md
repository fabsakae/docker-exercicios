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