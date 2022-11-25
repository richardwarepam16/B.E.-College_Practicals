class Node:
    def __init__(self, prob, symbol, left = None, right = None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols

codes = dict()
def Calculate_Codes(node, value = ''):
    newValue = value + str(node.code)
    if(node.left):
        Calculate_Codes(node.left, newValue)
    if(node.right):
        Calculate_Codes(node.right, newValue)
    if(not node.left and not node.right):
        codes[node.symbol] = newValue
    return codes

def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        print(coding[c], end = '')
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string

def Total_Gain(data,coding):
    before_compression = len(data) * 8
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])
    print("Space usage before compression (in bits): ", before_compression)
    print("Space Usage after compression (in bits): ", after_compression)

def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)

    nodes = []

    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1

        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    
    huffman_encoding = Calculate_Codes(nodes[0])
    print(huffman_encoding)
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data, huffman_encoding)
    print("Encoded output: ", encoded_output)
    return encoded_output, nodes[0]

def HuffmanDecoding(encodedData, huffmanTree):
    treeHead = huffmanTree
    decodedOutput = []
    for x in encodedData:
        if x == '1':
            huffmanTree = huffmanTree.right
        elif x == '0':
            huffmanTree = huffmanTree.left
        try:
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None:
                pass
        except AttributeError:
            decodedOutput.append(huffmanTree.symbol)
            huffmanTree =treeHead
    string = ''.join([str(item) for item in decodedOutput])
    return string

data = "AAAAAABBBBBBCCCCCCDDDDDE"
print(data)
encoding, tree = Huffman_Encoding(data)
print("Encoded Output", encoding)
print("Decoded Output", HuffmanDecoding(encoding, tree))