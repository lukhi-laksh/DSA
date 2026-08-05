from collections import defaultdict

"""
Remove Methods From Project

"""
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        edges = defaultdict(list)
        indegree = [0]*n
        sus = [0]*n
        for u,v in invocations:
            edges[u].append(v)
            indegree[v]+=1
        queue = [k]
        sus[k]=1
        while queue:
            node = queue.pop(0)
            if sus[node]==1:
                for child in edges[node]:
                    indegree[child]-=1

                    if sus[child]==0:
                        queue.append(child)
                        sus[child]=1
        remove=True
        for i in range(n):
            if sus[i]==1 and indegree[i]>0:
                remove=False
                break
        if remove:
            return [i for i in range(n) if sus[i]==0]
        else:
            return list(range(n))

"""

Time Complexity:  O(n² + m)
Space Complexity: O(n + m)

"""