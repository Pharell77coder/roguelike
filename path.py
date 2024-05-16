class Node:
    def __init__(self, col, row):
        self.parent = None
        self.col = col
        self.row = row
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        self.solid = False
        self.open = False
        self.checked = False


class PathFinder:
    def __init__(self, entity):
        self.entity = entity
        self.node = []
        self.openList = []
        self.pathList = []
        self.startNode = None
        self.goalNode = None
        self.currentNode = None
        self.goalReached = False
        self.step = 0
        self.instantiate_nodes()

    def instantiate_nodes(self):
        self.node = [[Node(col, row) for row in range(self.entity.maxWorldRow)] for col in
                     range(self.entity.maxWorldCol)]

    def reset_nodes(self):
        for col in range(self.entity.maxWorldCol):
            for row in range(self.entity.maxWorldRow):
                self.node[col][row].open = False
                self.node[col][row].checked = False
                self.node[col][row].solid = False

        self.openList.clear()
        self.pathList.clear()
        self.goalReached = False
        self.step = 0

    def set_nodes(self, start_col, start_row, goal_col, goal_row):
        self.reset_nodes()
        self.startNode = self.node[start_col][start_row]
        self.currentNode = self.startNode
        self.goalNode = self.node[goal_col][goal_row]
        self.openList.append(self.currentNode)

        for col in range(self.entity.maxWorldCol):
            for row in range(self.entity.maxWorldRow):
                tile_num = self.entity.tileM.mapTileNum[self.entity.currentMap][col][row]
                if self.entity.tileM.tile[tile_num].collision:
                    self.node[col][row].solid = True

                for i in range(len(self.entity.iTile[1])):
                    if self.entity.iTile[self.entity.currentMap][i] and self.entity.iTile[self.entity.currentMap][i].destructible:
                        it_col = self.entity.iTile[self.entity.currentMap][i].worldX // self.entity.tileSize
                        it_row = self.entity.iTile[self.entity.currentMap][i].worldY // self.entity.tileSize
                        self.node[it_col][it_row].solid = True

                self.get_cost(self.node[col][row])

    def get_cost(self, node):
        x_distance = abs(node.col - self.startNode.col)
        y_distance = abs(node.row - self.startNode.row)
        node.g_cost = x_distance + y_distance

        x_distance = abs(node.col - self.goalNode.col)
        y_distance = abs(node.row - self.goalNode.row)
        node.h_cost = x_distance + y_distance

        node.f_cost = node.g_cost + node.h_cost

    def search(self):
        while not self.goalReached and self.step < 500:
            col = self.currentNode.col
            row = self.currentNode.row

            self.currentNode.checked = True
            self.openList.remove(self.currentNode)

            if row - 1 >= 0:
                self.open_node(self.node[col][row - 1])

            if col - 1 >= 0:
                self.open_node(self.node[col - 1][row])

            if row + 1 < self.entity.maxWorldRow:
                self.open_node(self.node[col][row + 1])

            if col + 1 < self.entity.maxWorldCol:
                self.open_node(self.node[col + 1][row])

            best_node_index = 0
            best_node_f_cost = 999

            for i in range(len(self.openList)):
                if self.openList[i].f_cost < best_node_f_cost:
                    best_node_index = i
                    best_node_f_cost = self.openList[i].f_cost
                elif self.openList[i].f_cost == best_node_f_cost:
                    if self.openList[i].g_cost < self.openList[best_node_index].g_cost:
                        best_node_index = i

            if len(self.openList) == 0:
                break

            self.currentNode = self.openList[best_node_index]

            if self.currentNode == self.goalNode:
                self.goalReached = True
                self.track_the_path()

            self.step += 1

        return self.goalReached

    def open_node(self, node):
        if not node.open and not node.checked and not node.solid:
            node.open = True
            node.parent = self.currentNode
            self.openList.append(node)

    def track_the_path(self):
        current = self.goalNode
        while current != self.startNode:
            self.pathList.insert(0, current)
            current = current.parent
