# Exercício 11: Análise de Vulnerabilidades com Trivy

## Objetivo

Este exercício teve como objetivo principal a prática da análise de segurança de imagens Docker, utilizando a ferramenta de código aberto **Trivy**. Através da análise de uma imagem pública (`python:3.9`), foram identificadas vulnerabilidades conhecidas (incluindo severidades HIGH e CRITICAL), e propostas ações para mitigar esses riscos.

## Ferramentas Utilizadas

* **Docker:** Para gerenciar a imagem a ser analisada.
* **Trivy:** Ferramenta para varredura de vulnerabilidades em imagens de containeres.

## Imagem Analisada

Para este exercício, foi utilizada a imagem pública `python:3.9` para demonstrar a presença de vulnerabilidades em imagens base comuns e em suas dependências.

## Processo de Análise

1.  **Instalação do Trivy:**
    O Trivy foi instalado seguindo as instruções oficiais.
    A versão instalada do Trivy é `0.63.0`.

2.  **Comando de Análise:**
    A análise da imagem `python:3.9` foi realizada com o seguinte comando:
    ```bash
    trivy image python:3.9
    ```

## Vulnerabilidades Identificadas

A análise da imagem `python:3.9` revelou diversas vulnerabilidades em seus pacotes e bibliotecas, incluindo aquelas classificadas como de severidade **HIGH** e **CRITICAL**:

### Vulnerabilidades de Severidade CRITICAL

* **Vulnerabilidade:** `CVE-2023-45853`
    * **Biblioteca:** `zlib1g`
    * **Severidade:** **CRITICAL**
    * **Versão Instalada:** `1:1.2.13.dfsg-1`
    * **Descrição:** `zlib: integer overflow and resultant heap-based buffer overflow in zipOpenNewFileInZip4_6`
    * **Link:** [Detalhes CVE-2023-45853](https://avd.aquasec.com/nvd/cve-2023-45853)
    * *Observação:* Esta é uma vulnerabilidade de alta gravidade em uma biblioteca fundamental, ilustrando como imagens base não otimizadas podem introduzir riscos sérios.

### Vulnerabilidades de Severidade HIGH

* **Vulnerabilidade:** `CVE-2022-40897`
    * **Biblioteca:** `setuptools` (METADATA)
    * **Severidade:** **HIGH**
    * **Versão Instalada:** `58.1.0`
    * **Versão Corrigida:** `65.5.1`
    * **Descrição:** `pypa-setuptools: Regular Expression Denial of Service (ReDoS) in package_index.py`
    * **Link:** [Detalhes CVE-2022-40897](https://avd.aquasec.com/nvd/cve-2022-40897)

* **Vulnerabilidade:** `CVE-2024-6345`
    * **Biblioteca:** `setuptools` (METADATA)
    * **Severidade:** **HIGH**
    * **Versão Corrigida:** `70.0.0`
    * **Descrição:** `pypa/setuptools: Remote code execution via download functions in the package_index module in...`
    * **Link:** [Detalhes CVE-2024-6345](https://avd.aquasec.com/nvd/cve-2024-6345)

## Possíveis Ações para Reduzir Vulnerabilidades

Com base na análise do Trivy e nas melhores práticas de segurança de containeres, as seguintes ações são sugeridas para mitigar as vulnerabilidades e construir imagens mais seguras e eficientes:

1.  **Utilizar Imagens Base Mais Leves/Mínimas:**
    * **Problema:** Imagens base genéricas e grandes (como `python:3.9` completa) incluem uma vasta quantidade de pacotes e dependências que nem sempre são essenciais para a aplicação.
    * **Solução:** Optar por imagens "slim" ou "alpine" (e.g., `python:3.9-slim-buster`, `python:3.9-alpine`). Estas imagens são menores, contêm apenas o necessário para a linguagem ou runtime, reduzindo significativamente a quantidade de pacotes e, por consequência, o número de vulnerabilidades herdadas do sistema base.

2.  **Atualizar Dependências da Aplicação:**
    * **Problema:** Pacotes e bibliotecas específicas da aplicação podem conter vulnerabilidades em versões mais antigas.
    * **Solução:** Manter as dependências da aplicação atualizadas para as "Fixed Version" indicadas pelas ferramentas de scan.

3.  **Rodar Aplicações como Usuário Não-Root:**
    * **Problema:** Por padrão, muitas imagens Docker executam processos como o usuário `root`. Em caso de uma vulnerabilidade explorada, um atacante ganharia privilégios de `root` dentro do contêiner, aumentando o impacto de um ataque.
    * **Solução:** Adicionar a instrução `USER <nome-do-usuario-nao-root>` no `Dockerfile` para que a aplicação seja executada com privilégios limitados. (Conforme explorado no Exercício 10).

---