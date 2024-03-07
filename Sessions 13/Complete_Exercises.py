def histogram(s):
    d = dict()
    words = s.split()
    for word in words:
        d[word] = d.get(word, 0) + 1
    return d

def print_hist(h):
    for c in sorted(h):
        print(c, h[c])

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

known = {0: 0, 1: 1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def has_duplicates(seq):
    seen = set()
    for x in seq:
        if x in seen:
            return True
        seen.add(x)
    return False

# Example usage
if __name__ == "__main__":
    h = histogram('Happy Birthday to you Happy Birthday to you Happy Birthday dear Someone Happy Birthday to you')
    print_hist(h)
    print(reverse_lookup(h, 3))  
    print(invert_dict(h))
    for i in range(10):
        print(fibonacci(i), end=", ")
    print()
    print(has_duplicates(['a', 'b', 'c', 'a']))  