# Usa uma imagem Python slim como base. Imagens "slim" são menores,
# o que melhora a segurança e reduz o tempo de download/build.
FROM python:3.9-slim-buster

# Define o diretório de trabalho padrão dentro do contêiner.
# Todas as instruções COPY e RUN subsequentes (sem caminho absoluto)
# serão executadas a partir deste diretório.
WORKDIR /app

# Cria um novo grupo e um novo usuário não-root.
# É uma boa prática não rodar aplicações como 'root' dentro de contêineres por segurança.
# 'groupadd -g 1001 appuser': Cria um grupo chamado 'appuser' com GID 1001.
# 'useradd -r -u 1001 -g appuser appuser': Cria um usuário 'appuser' com UID 1001,
# associado ao grupo 'appuser'.
#   - '-r': Cria um usuário de sistema (sem um diretório home padrão, ideal para contêineres).
#   - '-u 1001': Define o User ID (UID) para 1001 (qualquer UID acima de 1000 geralmente é seguro para usuários não-root).
#   - '-g appuser': Associa o usuário ao grupo 'appuser'.
RUN groupadd -g 1001 appuser && useradd -r -u 1001 -g appuser appuser

# Copia o script da sua aplicação Python (app.py) do seu computador local
# para o diretório de trabalho (/app) dentro da imagem Docker.
COPY app.py .

# **Instrução CRÍTICA de segurança:** Define o usuário 'appuser' como o usuário padrão
# para todas as instruções subsequentes no Dockerfile e para a execução
# do comando CMD (que inicia a aplicação).
# Isso garante que a aplicação não rodará como 'root'.
USER appuser

# Define o comando que será executado quando o contêiner for iniciado a partir desta imagem.
# Neste caso, executa o script Python que acabamos de copiar.
CMD ["python", "app.py"]