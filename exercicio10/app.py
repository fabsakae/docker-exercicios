import os
import time

print("Iniciando a aplicação Python...")
print(f"Rodando como usuário: {os.getuid()} (Nome: {os.getenv('USER')})")

# Este loop mantém o script rodando indefinidamente,
# o que mantém o container ativo para que possamos inspecioná-lo depois.
while True:
    print(f"Aplicação ainda rodando em {time.ctime()}...")
    time.sleep(5)