"""
Avoid Flood in the City

"""

class Solution:
    def avoidFlood(self, rains):
        dry_lands = []    # Index of dry lands that are not used yet
        last_flood = dict()    # index of previous flood
        res = []      # result list to return
        for i,r in enumerate(rains):
            if r == 0:
                dry_lands.append(i)
                res.append(1)
            else:
                if r in last_flood:
                    dried = False
                    for j,dl in enumerate(dry_lands):
                        if dl > last_flood[r]:
                            res[dl] = r
                            last_flood[r] = i
                            del dry_lands[j]
                            dried = True
                            break
                    if not dried:
                        return []
                else:
                    last_flood[r] = i
                res.append(-1)
        return res
    
sol = Solution()
print(sol.avoidFlood([1,2,3,4]))

"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""