# --- Fase de Construção (Builder Stage) ---
# Usa uma imagem Go completa para compilar o código
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Copia o código-fonte da aplicação Go para o contêiner
COPY main.go .

# Compila a aplicação Go
# CGO_ENABLED=0 desabilita a vinculação de bibliotecas C para criar um binário estático
# -o gs-ping define o nome do executável final
RUN CGO_ENABLED=0 go build -o gs-ping main.go

# --- Fase Final (Final Stage) ---
# Usa uma imagem Alpine mínima
FROM alpine:latest

# Define o diretório de trabalho no contêiner final
WORKDIR /app

# Copia o executável compilado da fase 'builder' para o contêiner final
COPY --from=builder /app/gs-ping .

# Expõe a porta que a aplicação Go vai usar (8080)
EXPOSE 8080

# Comando para executar a aplicação quando o contêiner inicia
CMD ["./gs-ping"]