class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        adj = [[] for _ in xrange(n)]
        for i in xrange(1, n):
            adj[parent[i]].append(i)

        new_parent = list(parent)
        char_ancestor = [-1] * 26

        def dfs1(u):
            c = ord(s[u]) - ord('a')
            prev = char_ancestor[c]
            if prev != -1:
                new_parent[u] = prev
            char_ancestor[c] = u

            for v in adj[u]:
                dfs1(v)

            char_ancestor[c] = prev

        dfs1(0)

        new_adj = [[] for _ in xrange(n)]
        for i in xrange(1, n):
            new_adj[new_parent[i]].append(i)

        subtree_size = [0] * n

        def dfs2(u):
            sz = 1
            for v in new_adj[u]:
                sz += dfs2(v)
            subtree_size[u] = sz
            return sz

        dfs2(0)
        return subtree_size