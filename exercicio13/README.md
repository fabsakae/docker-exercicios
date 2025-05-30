# Exercício 13: Gerenciamento de Dados com Volumes

## Objetivo

O objetivo deste exercício foi demonstrar e praticar o gerenciamento de dados persistentes em contêineres Docker utilizando **volumes**. Especificamente, foi criado um container Nginx que serve uma página HTML de um diretório no sistema de arquivos do host, mapeado diretamente para o container.

## Passos Realizados

1.  **Criação da Pasta do Exercício e do Arquivo HTML:**
    Uma nova pasta `exercicio13` foi criada dentro de `docker-exercicios`. Dentro desta pasta, foi criado um arquivo `index.html` com o seguinte conteúdo:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meu Nginx com Volume</title>
    </head>
    <body>
        <h1>Olá do Nginx com Volume!</h1>
        <p>Esta página está sendo servida de um volume Docker.</p>
    </body>
    </html>
    ```

2.  **Execução do Contêiner Nginx com Mapeamento de Volume:**
    O contêiner Nginx foi iniciado mapeando o diretório local (`/home/sakae/docker-exercicios/exercicio13`) onde o `index.html` reside para o diretório de conteúdo padrão do Nginx dentro do contêiner (`/usr/share/nginx/html`). A porta 8080 do host foi mapeada para a porta 80 do contêiner.

    Comando utilizado:
    ```bash
    docker run -d -p 8080:80 --name my-nginx-volume -v /home/sakae/docker-exercicios/exercicio13:/usr/share/nginx/html nginx:latest
    ```
**Saída do comando:**
```
ba54660adac7bdc3548414752ded1739c5955e1ada66e269996ae9093656b1b1
```
## Resultados e Verificação

Após a execução do contêiner, a página HTML foi acessível no navegador através de `http://localhost:8080`.

A principal verificação do funcionamento do volume foi realizada ao:
* Alterar o conteúdo do arquivo `index.html` diretamente no sistema de arquivos do host.
* Recarregar a página no navegador sem reiniciar o contêiner.
* As alterações foram refletidas instantaneamente na página web, confirmando que o Nginx estava lendo o arquivo diretamente do volume persistente.

Isso demonstra que os volumes são uma ferramenta poderosa para:
* **Persistência de Dados:** Os dados não são perdidos quando o contêiner é removido.
* **Compartilhamento de Dados:** Dados podem ser facilmente compartilhados entre o host e o contêiner, ou entre múltiplos contêineres.
* **Desenvolvimento:** Facilita o ciclo de desenvolvimento, permitindo edições de código no host que são instantaneamente visíveis no contêiner.

## Limpeza

Após a conclusão do exercício, o contêiner `my-nginx-volume` foi parado e removido:
```bash
docker stop my-nginx-volume
```
```
docker rm my-nginx-volume
```
