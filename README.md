
# Sistema de Cadastro de Medicamentos

 ## Descrição do projeto

 Este projeto é um sistema simples desenvolvido em Python para cadastrar, listar e buscar medicamentos. Os dados são armazenados em uma lista de dicionários e salvos em um arquivo JSON para que não sejam perdidos quando o programa for fechado.

 ## Como executar

 1. Instale o Python.
2. Abra a pasta do projeto no Visual Studio Code.
3. Abra o terminal.
4. Execute o comando:

```
python medicamentos.py
```

 5. Escolha uma das opções apresentadas no menu.

 ## Funcionalidades principais

 - **Cadastrar:** adiciona um novo medicamento.
- **Listar:** mostra todos os medicamentos cadastrados.
- **Buscar:** procura um medicamento pelo nome.
- **Sair:** salva os dados no arquivo e encerra o programa.

 ## Requisitos técnicos aplicados

 - **`if/elif/else`** — utilizado para controlar as opções do menu principal.
- **`while`** — mantém o menu funcionando até o usuário escolher a opção "Sair".
- **Funções** — foram criadas funções como `carregar()`, `salvar()` e `buscar()`, utilizando parâmetros e retornos.
- **Lista de dicionários** — os medicamentos são armazenados na variável `medicamentos`.
- **Persistência de dados** — utilizada a biblioteca `json` para salvar e carregar os medicamentos no arquivo `medicamentos.json`.
- **Entrada de dados** — utilizada a função `input()` para receber informações do usuário.

 ## Estrutura

```
projeto/
├── medicamentos.py
├── medicamentos.json
└── README.md
```
