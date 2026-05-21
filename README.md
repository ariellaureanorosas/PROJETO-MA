# Sistema de Gestão de Estoque — Loja de Roupas

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-acad%C3%AAmico-orange)

Sistema de gerenciamento de estoque para loja de roupas desenvolvido em Python com arquitetura modular, separação de responsabilidades e persistência de dados via JSON. Projeto acadêmico da disciplina de Programação Estruturada.

---

## Sobre o Projeto

Este projeto foi desenvolvido como trabalho avaliativo para a disciplina de **Metodologias Agéis** do curso de **Ciência da Computação**. O objetivo é aplicar os princípios de programação modular, manipulação de arquivos e validação de dados em um sistema funcional de gestão de estoque.

---

## Funcionalidades

### Operações CRUD
- **Cadastrar** novos produtos com nome, preço, tamanho, cor e quantidade
- **Listar** todos os produtos cadastrados
- **Atualizar** dados de produtos existentes
- **Deletar** produtos com confirmação

### Busca e Filtros
- **Buscar por nome** — pesquisa parcial *case-insensitive*
- **Filtrar por tamanho** — P, M, G, GG
- **Filtrar por cor** — qualquer cor cadastrada

### Controle de Estoque
- **Alerta de estoque baixo** — produtos abaixo do limite configurável (padrão: 5 unidades)
- **Visualização de quantidade** em tempo real

### Validações
- Inputs validados (float, int, texto não vazio)
- Formatação automática de moeda (BRL — R$)
- Proteção contra valores negativos

---

## Estrutura do Projeto

```
PROJETO DPT/
├── main.py                    # Ponto de entrada e menu interativo
├── database/
│   └── db.py                  # Persistência e carregamento de dados JSON
├── models/
│   └── produto.py             # Modelo de dados da classe Produto
├── services/
│   └── produto_service.py     # Regras de negócio e operações CRUD
├── utils/
│   └── helpers.py             # Validações e formatações auxiliares
├── data/
│   └── produtos.json          # Banco de dados em formato JSON
└── .gitignore
```

---

## Requisitos

- Python 3.6 ou superior
- Nenhuma dependência externa (apenas biblioteca padrão)

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/ariellaureanorosas/PROJETO-DPT.git
   cd PROJETO-DPT
   ```

2. Execute o sistema:
   ```bash
   python main.py
   ```

---

## Uso

Após iniciar o sistema com `python main.py`, o menu interativo será exibido:

```
==================================================
          SISTEMA DE GESTAO - LOJA DE ROUPAS
==================================================

MENU PRINCIPAL:
  1. Cadastrar produto
  2. Listar todos os produtos
  3. Buscar produto por nome
  4. Filtrar por tamanho
  5. Filtrar por cor
  6. Atualizar produto
  7. Deletar produto
  8. Verificar estoque baixo
  0. Sair

  Escolha uma opcao:
```

### Exemplo de Cadastro

```
--- CADASTRAR PRODUTO ---
  Nome: Camiseta Básica
  Preco: 49.90
  Tamanho (P/M/G/GG): M
  Cor: Preta
  Quantidade em estoque: 20

  Produto 'Camiseta Básica' cadastrado com sucesso! (ID: 1)
```

---

## Arquitetura

### Princípios Aplicados

| Princípio | Descrição |
|-----------|-----------|
| **Separação de Responsabilidades** | Cada módulo possui uma função específica e bem definida |
| **Single Responsibility** | Classes e funções responsáveis por uma única tarefa |
| **DRY (Don't Repeat Yourself)** | Código reutilizável e modular |
| **Persistência** | Dados preservados entre execuções via arquivo JSON |

### Fluxo de Dados

```
main.py → services/produto_service.py → database/db.py → data/produtos.json
     ↕                                      ↕
utils/helpers.py                      models/produto.py
```

---

## Tecnologias

| Tecnologia | Versão | Finalidade |
|------------|--------|------------|
| Python | 3.6+ | Linguagem principal de programação |
| JSON | nativo | Persistência de dados |
| OS/Sys | nativo | Manipulação de caminhos e limpeza de tela |

---

## Licença

Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
