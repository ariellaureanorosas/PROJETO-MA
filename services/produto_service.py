from models.produto import Produto
from database.db import carregar_dados, salvar_dados


def obter_todos():
    dados = carregar_dados()
    return [Produto.from_dict(p) for p in dados]


def obter_por_id(id_produto):
    produtos = obter_todos()
    for p in produtos:
        if p.id_produto == id_produto:
            return p
    return None


def gerar_proximo_id():
    produtos = obter_todos()
    if not produtos:
        return 1
    return max(p.id_produto for p in produtos) + 1


def cadastrar(nome, preco, tamanho, cor, quantidade):
    produtos = obter_todos()
    novo_id = gerar_proximo_id()
    novo_produto = Produto(novo_id, nome, preco, tamanho, cor, quantidade)
    produtos.append(novo_produto)
    salvar_dados([p.to_dict() for p in produtos])
    return novo_produto


def atualizar(id_produto, nome=None, preco=None, tamanho=None, cor=None, quantidade=None):
    produtos = obter_todos()
    for p in produtos:
        if p.id_produto == id_produto:
            if nome is not None:
                p.nome = nome
            if preco is not None:
                p.preco = preco
            if tamanho is not None:
                p.tamanho = tamanho
            if cor is not None:
                p.cor = cor
            if quantidade is not None:
                p.quantidade = quantidade
            salvar_dados([p.to_dict() for p in produtos])
            return p
    return None


def deletar(id_produto):
    produtos = obter_todos()
    novos_produtos = [p for p in produtos if p.id_produto != id_produto]
    if len(novos_produtos) == len(produtos):
        return False
    salvar_dados([p.to_dict() for p in novos_produtos])
    return True


def buscar_por_nome(termo):
    produtos = obter_todos()
    termo = termo.lower()
    return [p for p in produtos if termo in p.nome.lower()]


def filtrar_por_tamanho(tamanho):
    produtos = obter_todos()
    return [p for p in produtos if p.tamanho.lower() == tamanho.lower()]


def filtrar_por_cor(cor):
    produtos = obter_todos()
    return [p for p in produtos if p.cor.lower() == cor.lower()]


def verificar_estoque_baixo(limite=5):
    produtos = obter_todos()
    return [p for p in produtos if p.quantidade <= limite]
