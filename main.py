import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services import produto_service
from utils.helpers import ler_texto, ler_float, ler_int, formatar_moeda

LIMITE_ESTOQUE_BAIXO = 5


def exibir_cabecalho():
    print("\n" + "=" * 50)
    print("          SISTEMA DE GESTAO - LOJA DE ROUPAS")
    print("=" * 50)


def exibir_menu():
    print("\nMENU PRINCIPAL:")
    print("  1. Cadastrar produto")
    print("  2. Listar todos os produtos")
    print("  3. Buscar produto por nome")
    print("  4. Filtrar por tamanho")
    print("  5. Filtrar por cor")
    print("  6. Atualizar produto")
    print("  7. Deletar produto")
    print("  8. Verificar estoque baixo")
    print("  0. Sair")


def exibir_produto(p):
    print(f"  ID: {p.id_produto} | {p.nome} | {formatar_moeda(p.preco)} | Tam: {p.tamanho} | Cor: {p.cor} | Qtd: {p.quantidade}")


def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    nome = ler_texto("  Nome: ")
    preco = ler_float("  Preco: ")
    tamanho = ler_texto("  Tamanho (P/M/G/GG): ")
    cor = ler_texto("  Cor: ")
    quantidade = ler_int("  Quantidade em estoque: ")

    produto = produto_service.cadastrar(nome, preco, tamanho, cor, quantidade)
    print(f"\n  Produto '{produto.nome}' cadastrado com sucesso! (ID: {produto.id_produto})")


def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")
    produtos = produto_service.obter_todos()
    if not produtos:
        print("  Nenhum produto cadastrado.")
        return
    for p in produtos:
        exibir_produto(p)
    print(f"\n  Total: {len(produtos)} produto(s)")


def buscar_produto():
    print("\n--- BUSCAR POR NOME ---")
    termo = ler_texto("  Digite o nome: ")
    resultados = produto_service.buscar_por_nome(termo)
    if not resultados:
        print("  Nenhum produto encontrado.")
        return
    for p in resultados:
        exibir_produto(p)
    print(f"\n  Encontrado(s): {len(resultados)} produto(s)")


def filtrar_por_tamanho():
    print("\n--- FILTRAR POR TAMANHO ---")
    tamanho = ler_texto("  Tamanho (P/M/G/GG): ")
    resultados = produto_service.filtrar_por_tamanho(tamanho)
    if not resultados:
        print("  Nenhum produto encontrado.")
        return
    for p in resultados:
        exibir_produto(p)
    print(f"\n  Encontrado(s): {len(resultados)} produto(s)")


def filtrar_por_cor():
    print("\n--- FILTRAR POR COR ---")
    cor = ler_texto("  Cor: ")
    resultados = produto_service.filtrar_por_cor(cor)
    if not resultados:
        print("  Nenhum produto encontrado.")
        return
    for p in resultados:
        exibir_produto(p)
    print(f"\n  Encontrado(s): {len(resultados)} produto(s)")


def atualizar_produto():
    print("\n--- ATUALIZAR PRODUTO ---")
    id_produto = ler_int("  ID do produto: ")
    produto = produto_service.obter_por_id(id_produto)
    if not produto:
        print("  Produto nao encontrado.")
        return

    print(f"  Editando: {produto.nome} (deixe vazio para manter)")
    nome = ler_texto(f"  Nome [{produto.nome}]: ", obrigatorio=False)
    preco_str = input(f"  Preco [{produto.preco}]: ").strip().replace(",", ".")
    tamanho = ler_texto(f"  Tamanho [{produto.tamanho}]: ", obrigatorio=False)
    cor = ler_texto(f"  Cor [{produto.cor}]: ", obrigatorio=False)
    qtd_str = input(f"  Quantidade [{produto.quantidade}]: ").strip()

    preco = float(preco_str) if preco_str else None
    quantidade = int(qtd_str) if qtd_str else None

    nome = nome if nome else None
    tamanho = tamanho if tamanho else None
    cor = cor if cor else None

    produto_service.atualizar(id_produto, nome, preco, tamanho, cor, quantidade)
    print("  Produto atualizado com sucesso!")


def deletar_produto():
    print("\n--- DELETAR PRODUTO ---")
    id_produto = ler_int("  ID do produto: ")
    produto = produto_service.obter_por_id(id_produto)
    if not produto:
        print("  Produto nao encontrado.")
        return

    confirmacao = ler_texto(f"  Confirma exclusao de '{produto.nome}'? (s/n): ")
    if confirmacao.lower() == "s":
        produto_service.deletar(id_produto)
        print("  Produto deletado com sucesso!")
    else:
        print("  Exclusao cancelada.")


def verificar_estoque_baixo():
    print("\n--- ESTOQUE BAIXO ---")
    produtos = produto_service.verificar_estoque_baixo(LIMITE_ESTOQUE_BAIXO)
    if not produtos:
        print(f"  Nenhum produto com estoque abaixo de {LIMITE_ESTOQUE_BAIXO}.")
        return
    for p in produtos:
        print(f"  [ALERTA] {p.nome} - Qtd: {p.quantidade}")


def main():
    while True:
        exibir_cabecalho()
        exibir_menu()
        opcao = input("\n  Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            filtrar_por_tamanho()
        elif opcao == "5":
            filtrar_por_cor()
        elif opcao == "6":
            atualizar_produto()
        elif opcao == "7":
            deletar_produto()
        elif opcao == "8":
            verificar_estoque_baixo()
        elif opcao == "0":
            print("\n  Saindo do sistema...\n")
            break
        else:
            print("\n  Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
