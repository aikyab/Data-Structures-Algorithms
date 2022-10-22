import collections

class SocialNetwork:
    def __init__(self,users):
        self.map = collections.defaultdict(list)
        self.users = users

    def create_edge(self):
        for edge in self.users:
            user1,user2 = edge
            self.map[user1].append(user2)
            self.map[user2].append(user1)

    def dfs(self,value,visited):
        count = 0
        if value not in self.map:
            return 0
        for node in self.map[value]:
            if node in visited:
                continue
            else:
                count+=1
                visited.add(node)
                count += self.dfs(node,visited)
        return count

    def find_largest_network(self):
        visited = set()
        max_val = 0
        self.create_edge()
        for key in self.map.keys():
            if key not in visited:
                visited.add(key)
                total_count = self.dfs(key,visited) + 1
                max_val = max(max_val,total_count)
        return max_val

users = [(1,2),(1,5),(1,11),(2,3),(2,4),(6,7),(7,8),(8,6),(9,10)]
adj = SocialNetwork(users)

print(adj.find_largest_network())

