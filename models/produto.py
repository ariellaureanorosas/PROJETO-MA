class Produto:
    def __init__(self, id_produto, nome, preco, tamanho, cor, quantidade):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho
        self.cor = cor
        self.quantidade = quantidade

    def __repr__(self):
        return f"Produto(id={self.id_produto}, nome='{self.nome}', preco={self.preco}, tamanho={self.tamanho}, cor='{self.cor}', qtd={self.quantidade})"

    def to_dict(self):
        return {
            "id_produto": self.id_produto,
            "nome": self.nome,
            "preco": self.preco,
            "tamanho": self.tamanho,
            "cor": self.cor,
            "quantidade": self.quantidade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_produto=data["id_produto"],
            nome=data["nome"],
            preco=data["preco"],
            tamanho=data["tamanho"],
            cor=data["cor"],
            quantidade=data["quantidade"]
        )
