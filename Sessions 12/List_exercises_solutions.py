def nested_sum(t):
    total = 0
    for sublist in t:
        total += sum(sublist)
    return total

def cumsum(t):
    result = []
    total = 0
    for num in t:
        total += num
        result.append(total)
    return result

def middle(t):
    return t[1:-1]

def chop(t):
    del t[0]
    del t[-1]

def is_sorted(t):
    return t == sorted(t)

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def has_duplicates(s):
    return len(set(s)) != len(s)

def has_adjacent_duplicates(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t)) 

    t = [1, 2, 3]
    print(cumsum(t))  
    t = [1, 2, 3, 4]
    print(middle(t))  
    chop(t)
    print(t)  

    print(is_sorted([1, 2, 2]))  
    print(is_sorted(['b', 'a']))  

    print(is_anagram('stop', 'pots')) 
    print(is_anagram('different', 'letters'))  
    print(is_anagram([1, 2, 2], [2, 1, 2]))  
    
    print(has_duplicates('cba'))  
    print(has_duplicates('abba'))  
    print(has_adjacent_duplicates('cba')) 
    print(has_adjacent_duplicates('abca')) 
    print(has_adjacent_duplicates('abbc'))  

if __name__ == "__main__":
    main()