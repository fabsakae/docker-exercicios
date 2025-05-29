# Exercício 8: PostgreSQL e PgAdmin com Docker Compose

## Objetivo

O objetivo deste exercício foi utilizar o Docker Compose para definir e executar uma aplicação multi-container, composta por um servidor de banco de dados PostgreSQL e uma interface de gerenciamento gráfica, o pgAdmin. 

## Conteúdo do `docker-compose.yml`


```yaml
version: '3.8' 

services:
  db:
    image: postgres:13
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin_interface
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    depends_on:
      - db

volumes:
  postgres_data:
```
## Iniciando o serviço com Docker compose
**Comando:**
```bash
docker compose up -d
```
**Saida do Comando:**
```
WARN[0002] /home/sakae/docker-exercicios/exercicio08/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 32/32
 ✔ pgadmin Pulled                                                                                                                             172.7s 
 ✔ db Pulled                                                                                                                                  104.7s 
                                                                                                                                                     
                                                                                                                                                     
[+] Running 4/4
 ✔ Network exercicio08_default         Created                                                                                                  3.7s 
 ✔ Volume "exercicio08_postgres_data"  Created                                                                                                  0.4s 
 ✔ Container postgres_db               Started                                                                                                 27.8s 
 ✔ Container pgadmin_interface         Started 
```
**Status dos Containers: Comando:**
```
Docker ps
```
**Saída do Comando:**
```
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                              NAMES
2942ad8480a8   dpage/pgadmin4   "/entrypoint.sh"         10 minutes ago   Up 9 minutes    443/tcp, 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   pgadmin_interface
a92059f87cf4   postgres:13      "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp        postgres_db
```
## Acessar a Interface do pgAdmin no Navegador:
## http://localhost:8080
Usar as credenciais do docker-compose.yml:
Email: admin@example.com
Senha: admin
Após fazer login, adicionar um novo servidor para se conectar ao PostgreSQL. Configurar o Add New Server com as informações do Docker compose.yml.
O painel principal mostrará o dashboard do servidor PostgreSQL, com métricas e gráficos.
---
---