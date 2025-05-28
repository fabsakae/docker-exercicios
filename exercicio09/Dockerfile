# Usa a imagem oficial do Nginx como base
FROM nginx:latest

# Remove o conteúdo HTML padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do seu site estático para o diretório de serviço do Nginx
# O primeiro ponto "." se refere à pasta atual (exercicio09) no contexto de build
# O segundo "/usr/share/nginx/html" é o diretório padrão onde o Nginx serve os arquivos
COPY . /usr/share/nginx/html

# Expõe a porta 80, que é a porta padrão do Nginx
EXPOSE 80

# Comando padrão do Nginx para iniciar o servidor em foreground
CMD ["nginx", "-g", "daemon off;"]