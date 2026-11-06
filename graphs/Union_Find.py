class UnionFind:
    def __init__(self, size):
        # parent list - each node's parent is itself
        self.parent = list(range(size))

        # initial size of each component = 1
        self.size = [1] * size

        # initially largest component size = 1
        self.max_component_size = 1

    def find(self, i) -> int:
        """Find the root representative of element i with Path Compression."""
        # Pass 1: Find the absolute root node
        root = i
        while root != self.parent[root]:
            root = self.parent[root]

        # Pass 2: Iterative Path Compression
        # Traverse from the original node up to the root, updating pointers
        curr = i
        while curr != root:
            # 1. store immediate parent of curr
            next = self.parent[curr]

            # 2. point curr to root
            self.parent[curr] = root

            # 3. update curr to next so that it's parent also point to root
            curr = next

        return root

    def union(self, i, j) -> bool:
        """Merge components containing i and j. Tracks largest cluster size."""
        root_i = self.find(i)
        root_j = self.find(j)

        # If they are already in the same component, do nothing
        if root_i == root_j:
            return False

        # Structural Hook: Attach smaller tree under the larger tree
        if self.size[i] < self.size[j]:
            # update parent of root of smaller component to root of bigger component
            self.parent[root_i] = root_j

            # update size of bigger component
            self.size[root_j] += self.size[root_i]

            # dynamically update max_component_size
            self.max_component_size = max(self.max_component_size, self.size[root_j])

        else:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.max_component_size = max(self.max_component_size, self.size[root_i])

        return True

    def get_max_size(self):
        """Returns the size of the largest connected cluster in O(1) time."""
        return self.max_component_size


# Initialize a network simulation of 6 isolated servers (IDs 0 to 5)
network = UnionFind(6)
print(f"Initial Max Cluster Size: {network.get_max_size()}")
# Output: 1 (Everyone is isolated)

# Connection Step 1: Connect Server 0 and Server 1
network.union(0, 1)
print(f"Max Cluster Size after union(0,1): {network.get_max_size()}")
# Output: 2 -> Cluster {0, 1} now contains 2 nodes.

# Connection Step 2: Connect Server 2 and Server 3
network.union(2, 3)
# Connection Step 3: Connect Server 3 and Server 4
network.union(3, 4)
print(f"Max Cluster Size after creating cluster {{2,3,4}}: {network.get_max_size()}")
# Output: 3 -> Cluster {2, 3, 4} has overtaken the network size record.

# Connection Step 4: Bridge the two distinct networks together (Connect 1 to 2)
network.union(1, 2)
print(f"Max Cluster Size after bridging all together: {network.get_max_size()}")
# Output: 5 -> Combined cluster {0, 1, 2, 3, 4} now spans 5 nodes!
