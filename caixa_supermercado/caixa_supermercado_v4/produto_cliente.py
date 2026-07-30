import produto_service as service


def testar_listar():
    print("\n--- Listar todos ---")
    for p in service.listar_todos():
        print(p)


def testar_consultar_valido():
    print("\n--- Consultar ID 1 (válido) ---")
    try:
        print(service.consultar(1))
    except ValueError as e:
        print(f"Erro: {e}")


def testar_consultar_invalido():
    print("\n--- Consultar ID 0 (inválido) ---")
    try:
        print(service.consultar(0))
    except ValueError as e:
        print(f"Erro esperado: {e}")


def testar_consultar_inexistente():
    print("\n--- Consultar ID 9999 (inexistente) ---")
    try:
        print(service.consultar(9999))
    except ValueError as e:
        print(f"Erro esperado: {e}")


def testar_criar():
    print("\n--- Criar produto ---")
    try:
        id_novo = service.criar("Produto Teste", 10, 9.99)
        print(f"Produto criado com ID {id_novo}")
        return id_novo
    except ValueError as e:
        print(f"Erro: {e}")
        return None


def testar_atualizar(id: int):
    print(f"\n--- Atualizar produto ID {id} ---")
    try:
        service.atualizar(id, "Produto Teste Editado", 20, 19.99)
        print(f"Produto ID {id} atualizado.")
        print(service.consultar(id))
    except ValueError as e:
        print(f"Erro: {e}")


def testar_remover(id: int):
    print(f"\n--- Remover produto ID {id} ---")
    try:
        service.remover(id)
        print(f"Produto ID {id} removido.")
    except ValueError as e:
        print(f"Erro: {e}")


def testar_estoque_insuficiente():
    print("\n--- Descontar estoque além do disponível ---")
    try:
        service.descontar_estoque(1, 9999)
    except ValueError as e:
        print(f"Erro esperado: {e}")


def testar_produtos_sem_estoque():
    print("\n--- Produtos sem estoque ---")
    sem_estoque = service.obter_produtos_sem_estoque()
    if sem_estoque:
        for p in sem_estoque:
            print(p)
    else:
        print("Todos os produtos têm estoque disponível.")


def main():
    testar_listar()
    testar_consultar_valido()
    testar_consultar_invalido()
    testar_consultar_inexistente()

    id_novo = testar_criar()
    if id_novo:
        testar_atualizar(id_novo)
        testar_remover(id_novo)

    testar_estoque_insuficiente()
    testar_produtos_sem_estoque()

    print("\n--- Testes concluídos ---")


if __name__ == "__main__":
    main()
