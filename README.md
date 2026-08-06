# Sistema de Gerenciamento de Biblioteca

## Descrição

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido em Python. O programa permite cadastrar livros, registrar empréstimos e devoluções, realizar buscas, listar e ordenar os livros cadastrados. Os dados são armazenados em um arquivo JSON para que as informações permaneçam salvas mesmo após o encerramento do programa.

---

## Como executar o programa

### Requisitos
- Python 3 instalado no computador.

### Passos

1. Baixe ou clone o projeto.
2. Abra a pasta do projeto no terminal.
3. Execute o arquivo principal com o comando:

```bash
python biblioteca.py
```

> Caso seu sistema utilize `python3`, execute:

```bash
python3 biblioteca.py
```

O arquivo `biblioteca.json` será criado automaticamente na primeira execução para armazenar os dados da biblioteca.

---

## Principais funcionalidades

- Cadastrar novos livros.
- Listar todos os livros cadastrados.
- Buscar livros pelo título ou autor.
- Registrar empréstimos de livros.
- Registrar devoluções de livros.
- Ordenar os livros por título, autor ou ano de publicação.
- Salvar automaticamente os dados em arquivo para uso nas próximas execuções.

---

## Requisitos técnicos aplicados

- **Menu principal com `if/elif/else`:** utilizado no menu de opções do sistema.
- **Estrutura de repetição (`while`):** mantém o programa em execução até o usuário escolher a opção "Sair".
- **Funções com parâmetros e retorno:** utilizadas em funções como `cadastrar_livro()`, `buscar_livro()`, `emprestar_livro()`, `devolver_livro()`, `listar_livros()` e `ordenar_livros()`.
- **Lista de dicionários:** cada livro é armazenado como um dicionário dentro da lista `livros`.
- **Persistência em arquivo:** leitura e escrita dos dados utilizando o arquivo `biblioteca.json` com a biblioteca `json`.
- **Comentários explicativos:** o código contém comentários descrevendo as principais partes da lógica.
- **Nomes de variáveis e funções significativos:** foram utilizados nomes claros para facilitar a leitura e manutenção do código.
