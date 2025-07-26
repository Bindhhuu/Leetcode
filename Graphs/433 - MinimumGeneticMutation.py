class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        gene = ['A', 'C', 'G', 'T']
        visited = set()
        queue = deque()
        queue.append((startGene, 0))
       
        while queue:
            curr_gene, mutations = queue.popleft()

            if curr_gene == endGene:
                return mutations

            for i in range(len(curr_gene)):
                for j in gene:
                    if j != curr_gene[i]:
                        mutated = curr_gene[:i] + j + curr_gene[i+1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated ,mutations+1))
        return -1
