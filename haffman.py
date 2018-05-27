def huffman(p):
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1']))
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'
    return c

def lowest_prob_pair(p):
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.
    sorted_p = sorted(p.items(), key=lambda (i,pi): pi)
    return sorted_p[0][0], sorted_p[1][0]

graph = { 'a': 1.0, 'b': 1.0, 'c': 2.0, 'd':3.0, 'e':5.0, 'f':8.0,'g':13.0,'h':21.0 }
print huffman(graph) # => {'a': '0', 'c': '10', 'b': '11'}
