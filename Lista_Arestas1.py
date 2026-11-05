def criar_grafo():

    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
  
    v = vertice.strip()
    if v in vertices:
        print(f"O vértice '{v}' já existe no grafo.")
        return
    vertices.append(v)
    print(f"Vértice '{v}' inserido com sucesso.")


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
 
    o = origem.strip()
    d = destino.strip()
    
    if o not in vertices:
        inserir_vertice(vertices, o)
    if d not in vertices:
        inserir_vertice(vertices, d)
        
    for a in arestas:
        if a == [o, d] or (nao_direcionado and a == [d, o]):
            print("Essa aresta já existe.")
            return

    arestas.append([o, d])
    if nao_direcionado:
        arestas.append([d, o])
    print(f"Aresta entre {o} e {d} inserida com sucesso.")


def remover_aresta(arestas, origem, destino, nao_direcionado=False):

    o = origem.strip()
    d = destino.strip()
    
    removido = False
    novas_arestas = []
    for a in arestas:
        match_direto = (a[0] == o and a[1] == d)
        match_reverso = (nao_direcionado and a[0] == d and a[1] == o)
        if match_direto or match_reverso:
            removido = True
        else:
            novas_arestas.append(a)
            
    arestas.clear()
    arestas.extend(novas_arestas)
    
    if removido:
        print("Aresta removida com sucesso.")
    else:
        print("Aresta não encontrada.")


def remover_vertice(vertices, arestas, vertice):

    v = vertice.strip()
    if v not in vertices:
        print("Vértice não encontrado.")
        return
    
    vertices.remove(v)
    nova_arestas = [a for a in arestas if a[0] != v and a[1] != v]
    arestas.clear()
    arestas.extend(nova_arestas)
    print(f"Vértice '{v}' e suas conexões foram removidos.")


def existe_aresta(arestas, origem, destino):

    o = origem.strip()
    d = destino.strip()
    for a in arestas:
        if a[0] == o and a[1] == d:
            return True
    return False


def vizinhos(vertices, arestas, vertice):

    v = vertice.strip()
    if v not in vertices:
        return []
    
    lista_vizinhos = []
    for a in arestas:
        if a[0] == v:
            if a[1] not in lista_vizinhos:
                lista_vizinhos.append(a[1])
    return lista_vizinhos


def grau_vertices(vertices, arestas):
 
    graus = {}
    for v in vertices:
        graus[v] = {"entrada": 0, "saida": 0, "total": 0}
        
    for a in arestas:
        orig = a[0]
        dest = a[1]
        if orig in graus:
            graus[orig]["saida"] += 1
        if dest in graus:
            graus[dest]["entrada"] += 1
            
    for v in graus:
        graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]
        
    return graus


def percurso_valido(arestas, caminho):
 
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        u = caminho[i].strip()
        v = caminho[i+1].strip()
        if not existe_aresta(arestas, u, v):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):

    v = vertice.strip()
    if v in vertices:
        lista = vizinhos(vertices, arestas, v)
        print(f"Vizinhos de {v}: {lista}")
    else:
        print("Vértice não encontrado.")


def exibir_grafo(vertices, arestas):
  
    print("\n--- Estrutura do Grafo (Lista de Arestas) ---")
    print(f"Vértices: {vertices}")
    print("Arestas:")
    if not arestas:
        print("  Nenhuma aresta cadastrada.")
    else:
        for a in arestas:
            print(f"  {a[0]} -> {a[1]}")
    print("-" * 45)


def main():
    vertices, arestas = criar_grafo()
    
    while True:
        print("\n--- MENU DO GRAFO (LISTA DE ARESTAS) ---")
        print("1. Inserir Vértice")
        print("2. Inserir Aresta")
        print("3. Exibir Grafo")
        print("4. Listar Vizinhos")
        print("5. Verificar Aresta")
        print("6. Calcular Graus")
        print("7. Verificar Percurso")
        print("8. Remover Aresta")
        print("9. Remover Vértice")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            v = input("Digite o nome do vértice: ")
            inserir_vertice(vertices, v)
        elif opcao == "2":
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            nd = input("O grafo é não direcionado? (s/n): ").lower() == 's'
            inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=nd)
        elif opcao == "3":
            exibir_grafo(vertices, arestas)
        elif opcao == "4":
            v = input("Digite o vértice: ")
            listar_vizinhos(vertices, arestas, v)
        elif opcao == "5":
            origem = input("Origem: ")
            destino = input("Destino: ")
            if existe_aresta(arestas, origem, destino):
                print(f"Sim, existe aresta entre {origem} e {destino}.")
            else:
                print(f"Não existe aresta entre {origem} e {destino}.")
        elif opcao == "6":
            graus = grau_vertices(vertices, arestas)
            print("\n--- Graus dos Vértices ---")
            for v, g in graus.items():
                print(f"Vértice {v} -> Entrada: {g['entrada']}, Saída: {g['saida']}, Total: {g['total']}")
            print("-" * 28)
        elif opcao == "7":
            caminho_str = input("Digite o caminho separado por espaços (ex: A B C): ")
            caminho = caminho_str.split()
            if percurso_valido(arestas, caminho):
                print("O percurso é VÁLIDO!")
            else:
                print("O percurso é INVÁLIDO!")
        elif opcao == "8":
            origem = input("Origem da aresta: ")
            destino = input("Destino da aresta: ")
            nd = input("O grafo é não direcionado? (s/n): ").lower() == 's'
            remover_aresta(arestas, origem, destino, nao_direcionado=nd)
        elif opcao == "9":
            v = input("Digite o vértice a ser removido: ")
            remover_vertice(vertices, arestas, v)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()