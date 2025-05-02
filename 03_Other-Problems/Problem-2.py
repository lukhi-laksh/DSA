haxTable = {}

lists = ['a', 'b', 'c', 'e', 'j', 'k', 'p', 's', 'a', 'r', 'r', 'a', 'l', 'a']

for i in lists:
    new_asc = ord(i)
    if new_asc in haxTable:
        haxTable[new_asc] += 1
    else:
        haxTable[new_asc] = 1

print(haxTable)

for ch in lists:
    print(f"Character '{ch}' appears {haxTable[ord(ch)]} times")