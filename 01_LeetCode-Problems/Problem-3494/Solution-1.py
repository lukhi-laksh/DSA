"""
Find the Minimum Amount of Time to Brew Potions

"""
class Solution(object):
    def minTime(self, skill, mana):
        
        so_far = 0
        prev_s = 0

        if len(skill) == 1:
            if len(mana) == 1:
                return mana[0]*skill[0]
            else:
                return skill[0]*sum(mana)
        elif len(mana) == 1:
            return mana[0]*sum(skill)

        for i in range(1,len(mana)):
            cur_s = 0
            so_far = 0
            for j in range(len(skill)):
                cur_time = cur_s + so_far*mana[i]
                so_far += skill[j]
                prev_time = prev_s + so_far*mana[i-1]

                if prev_time > cur_time:
                    cur_s += prev_time - cur_time
            
            prev_s = cur_s
        
        return prev_s  + mana[-1]*so_far


