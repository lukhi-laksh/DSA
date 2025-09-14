import re

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        # Exact matches stored in a set
        direct = set(wordlist)
        
        # Maps lowercase word -> first word with that lowercase form
        capmap = {}
        
        # Maps devoweled word -> first word with that devoweled form
        vowmap = {}
        
        def devowel(word):
            # Replace all vowels with '/' for normalized comparison
            return re.sub('[aeiou]', '/', word)
        
        # Preprocess wordlist
        for word in wordlist:
            lower = word.lower()
            if lower not in capmap:
                capmap[lower] = word
            vword = devowel(lower)
            if vword not in vowmap:
                vowmap[vword] = word
        
        def match(query):
            # 1. Exact match
            if query in direct:
                return query
            
            # 2. Case-insensitive match
            lower = query.lower()
            if lower in capmap:
                return capmap[lower]
            
            # 3. Vowel-error match
            vword = devowel(lower)
            if vword in vowmap:
                return vowmap[vword]
            
            # 4. No match
            return ""
        
        # Answer queries in order
        return [match(q) for q in queries]