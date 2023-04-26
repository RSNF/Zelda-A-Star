from queue import PriorityQueue
from classes.Map import Map
from classes.Point import Point

class AStar:

    def __h(current_point:Point, end_point:Point) -> int:
        x1, y1 = current_point
        x2, y2 = end_point
        
        return abs(x1 - x2) + abs(y1 - y2)
    
    def find_path(map:Map, start_point:Point, end_point:Point) -> list:
        came_from = {}
        g_count = 0

        # Lista aberta
        open_list = {start_point}

        # Lista fechada
        closed_list = PriorityQueue()
        closed_list.put((0, g_count, start_point))

        # Faz o calculo do G para cada ponto
        g_score = {point: float("inf") for row in map.points for point in row}
        g_score[start_point] = 0

        # Faz o calculo do F para cada ponto
        f_score = {point: float("inf") for row in map.points for point in row}
        f_score[start_point] = AStar.__h(start_point.getLocation(), end_point.getLocation())

        # Loop de execução do algoritmo enquanto a lista fechada não estiver vazia
        while not closed_list.empty():

            # Pega o ponto com maior prioridade da lista fechada e o remove
            current = closed_list.get()[2]
            open_list.remove(current)

            # Verifica se chegou no objetivo e constroi o caminho ate o mesmo
            if current == end_point:
                # Converte o dicionario came_from em uma lista
                came_from_list = [current]
                while current in came_from:
                    current = came_from[current]
                    came_from_list.append(current)

                # Retorna uma lista com o melhor caminho encontrado (do inicio para o final)
                return list(reversed(came_from_list))

            # Calcula o F, G e H dos vizinhos do ponto atual
            for neighbor in current.neighbors:
                temp_g = g_score[current] + neighbor.cost

                if temp_g < g_score[neighbor]:
                    came_from[neighbor] = current

                    # Define o F e G Scores para cada vizinho
                    g_score[neighbor] = temp_g
                    f_score[neighbor] = temp_g + \
                        AStar.__h(neighbor.getLocation(), end_point.getLocation())

                    # Veifica se o vizinho nao esta na lista aberta
                    if neighbor not in open_list:
                        g_count += temp_g
                        closed_list.put((f_score[neighbor], g_count, neighbor))
                        open_list.add(neighbor)