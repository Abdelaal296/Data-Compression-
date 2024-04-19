class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)



def huffman_code_tree(node, huf=''):
    if type(node) is str:
        return {node: huf}
    (l, r) = node.children()
    d = {}
    d.update(huffman_code_tree(l,  huf + '0'))
    d.update(huffman_code_tree(r,  huf + '1'))
    return d

s = input("Enter Text : ")
# BCAADDDCCACACAC
freq = {}
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1])

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[0]
    (key2, c2) = nodes[1]
    l = len(nodes)
    nodes = nodes[2:l]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1])

huffmanCode = huffman_code_tree(nodes[0][0])
res = {}
for (char, frequency) in freq:
    res[char] = huffmanCode[char]

print(res)
t = ""
for c in s:
    t+=res[c]

print(t)
# res = sorted(res.items(), key=lambda x: x[1])
#


