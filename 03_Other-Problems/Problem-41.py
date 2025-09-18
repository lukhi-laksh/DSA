import re

class Solution(object):
    def spellchecker(self, wordlist, queries):

        direct = set(wordlist)
        capmap = {}
        vowmap = {}
        
        def devowel(word):
            return re.sub('[aeiou]', '/', word)

        for word in wordlist:
            lower = word.lower()
            if lower not in capmap:
                capmap[lower] = word
            vword = devowel(lower)
            if vword not in vowmap:
                vowmap[vword] = word
        
        def match(query):
            if query in direct:
                return query

            lower = query.lower()
            if lower in capmap:
                return capmap[lower]

            vword = devowel(lower)
            if vword in vowmap:
                return vowmap[vword]

            return ""

        return [match(q) for q in queries]

sol = Solution()
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
print(sol.spellchecker(wordlist, queries))