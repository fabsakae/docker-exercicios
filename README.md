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
