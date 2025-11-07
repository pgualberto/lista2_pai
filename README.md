# Lista 2

## Informações do Projeto

**Disciplina:** Processamento e Análise de Imagens
**Professor:** Profa. Carolina Stephanie Jerônimo de Almeida
**Universidade:** Pontifícia Universidade Católica de Minas Gerais (PUC Minas)
**Autor:** Paulo Ricardo Ferreira Gualberto
**Data:** Novembro de 2025

-----

## Como Executar

Existem duas formas de executar este projeto: via Google Colab (recomendado) ou localmente.

### Opção 1: Google Colab (Recomendado)

1.  Acesse o Google Colab.
2.  Abra ou faça o upload do arquivo `googleColab/lista_2_pai.py`.
3.  No painel de arquivos do Colab, faça o upload das três imagens:
      * `pessoa.jpg`
      * `pucminas.jpg`
      * `vaticano.jpg`
4.  Execute as células do notebook. Os resultados serão exibidos.

### Opção 2: Execução Local

**Pré-requisitos:**
É necessário ter o Python e as bibliotecas do projeto instaladas.

```bash
pip install opencv-python numpy matplotlib
```

**Questão 1 (Otsu vs. Canny):**

1.  Navegue até o diretório `questao_1/`.
2.  Execute o script: `python questao1.py`
3.  O script salvará `comparative_visual_report.png` e exibirá a comparação.

**Questão 2 (Fecho Convexo):**

1.  Navegue até o diretório `questao_2/`.
2.  Execute o script: `python questao2.py`
3.  O script salvará `processed_hull_image.png` e `comparison_image.png`, e exibirá a comparação.
