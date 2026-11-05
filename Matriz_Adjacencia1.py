def criar_grafo():
  
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
 
    v = vertice.strip()
    if v in vertices:
        print(f"O vértice '{v}' já existe no grafo.")
        return
    
    vertices.append(v)
    for linha in matriz:
        linha.append(0)
    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)
    print(f"Vértice '{v}' inserido com sucesso.")


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
 
    o = origem.strip()
    d = destino.strip()
    
    if o not in vertices:
        inserir_vertice(matriz, vertices, o)
    if d not in vertices:
        inserir_vertice(matriz, vertices, d)
        
    i = vertices.index(o)
    j = vertices.index(d)
    
    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1
    print(f"Aresta entre {o} e {d} inserida com sucesso.")


def remover_vertice(matriz, vertices, vertice):
   
    v = vertice.strip()
    if v not in vertices:
        print("Vértice não encontrado.")
        return
    
    i = vertices.index(v)
    vertices.pop(i)
    matriz.pop(i)
    for linha in matriz:
        linha.pop(i)
    print(f"Vértice '{v}' e suas conexões foram removidos.")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
  
    o = origem.strip()
    d = destino.strip()
    if o in vertices and d in vertices:
        i = vertices.index(o)
        j = vertices.index(d)
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0
        print("Aresta removida com sucesso.")
    else:
        print("Aresta não encontrada.")


def existe_aresta(matriz, vertices, origem, destino):
  
    o = origem.strip()
    d = destino.strip()
    if o in vertices and d in vertices:
        i = vertices.index(o)
        j = vertices.index(d)
        return matriz[i][j] == 1
    return False


def vizinhos(matriz, vertices, vertice):

    v = vertice.strip()
    if v not in vertices:
        return []
    i = vertices.index(v)
    lista_vizinhos = []
    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            lista_vizinhos.append(vertices[j])
    return lista_vizinhos


def grau_vertices(matriz, vertices):
  
    graus = {}
    n = len(vertices)
    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(matriz[j][i] for j in range(n))
        total = entrada + saida
        graus[v] = {"entrada": entrada, "saida": saida, "total": total}
    return graus


def percurso_valido(matriz, vertices, caminho):
  
    if len(caminho) < 2:
        return True
    for k in range(len(caminho) - 1):
        u = caminho[k].strip()
        v = caminho[k+1].strip()
        if not existe_aresta(matriz, vertices, u, v):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
  
    v = vertice.strip()
    if v in vertices:
        lista = vizinhos(matriz, vertices, v)
        print(f"Vizinhos de {v}: {lista}")
    else:
        print("Vértice não encontrado.")


def exibir_grafo(matriz, vertices):
 
    if not vertices:
        print("O grafo está vazio.")
    else:
        print("\n--- Estrutura do Grafo (Matriz de Adjacência) ---")
        cabecalho = "        " + "  ".join(f"{v:>6}" for v in vertices)
        print(cabecalho)
        for i, v in enumerate(vertices):
            linha_str = "  ".join(f"{val:>6}" for val in matriz[i])
            print(f"{v:>6} -> [{linha_str}]")
        print("-" * 55)


def main():
    matriz, vertices = criar_grafo()
    
    while True:
        print("\n--- MENU DO GRAFO (MATRIZ DE ADJACÊNCIA) ---")
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
            inserir_vertice(matriz, vertices, v)
        elif opcao == "2":
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            nd = input("O grafo é não direcionado? (s/n): ").lower() == 's'
            inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=nd)
        elif opcao == "3":
            exibir_grafo(matriz, vertices)
        elif opcao == "4":
            v = input("Digite o vértice: ")
            listar_vizinhos(matriz, vertices, v)
        elif opcao == "5":
            origem = input("Origem: ")
            destino = input("Destino: ")
            if existe_aresta(matriz, vertices, origem, destino):
                print(f"Sim, existe aresta de {origem} para {destino}.")
            else:
                print(f"Não existe aresta direta de {origem} para {destino}.")
        elif opcao == "6":
            graus = grau_vertices(matriz, vertices)
            print("\n--- Graus dos Vértices ---")
            for v, g in graus.items():
                print(f"Vértice {v} -> Entrada: {g['entrada']}, Saída: {g['saida']}, Total: {g['total']}")
            print("-" * 28)
        elif opcao == "7":
            caminho_str = input("Digite o caminho separado por espaços (ex: A B C): ")
            caminho = caminho_str.split()
            if percurso_valido(matriz, vertices, caminho):
                print("O percurso é VÁLIDO!")
            else:
                print("O percurso é INVÁLIDO!")
        elif opcao == "8":
            origem = input("Origem da aresta: ")
            destino = input("Destino da aresta: ")
            nd = input("O grafo é não direcionado? (s/n): ").lower() == 's'
            remover_aresta(matriz, vertices, origem, destino, nao_direcionado=nd)
        elif opcao == "9":
            v = input("Digite o vértice a ser removido: ")
            remover_vertice(matriz, vertices, v)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()