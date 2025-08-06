import heapq
from collections import Counter
import math

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(chars, freq):
  
    # Create a priority queue of nodes
    priority_queue = [Node(char, f) for char, f in zip(chars, freq)]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = Node(frequency=left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(node, code="", huffman_codes={}):
    if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes

    

# Given example
# loading the characters from characters file
with open("characters.txt", "r") as file:
    text = file.read()

# OPTIONAL: to remove newlines
text = text.replace('\n', '')

frequency_counter = Counter(text)
chars = list(frequency_counter.keys())
freq = list(frequency_counter.values())

# Build the Huffman tree
root = build_huffman_tree(chars, freq)

# Generate Huffman codes
huffman_codes = generate_huffman_codes(root)

# Print Huffman codes
print(f"{'Character':<10} {'Frequency':<10} {'Code':<10} {'# Bits':<7}")
print("-" * 40)

for char in sorted(huffman_codes.keys()):
    freq = frequency_counter[char]
    code = huffman_codes[char]
    bits = len(code)
    print(f"{char:<10} {freq:<10} {code:<10} {bits:<7}")
    #display_char = repr(char) if char == '\n' else char  # show '\n' clearly
    #print(f"{display_char:<10} {freq:<10} {code:<10} {bits:<7}")

# statistics
total_chars = sum(frequency_counter.values())
total_bits_huffman = sum(frequency_counter[ch] * len(huffman_codes[ch]) for ch in huffman_codes)

# using 8 bits per character (standard ASCII) for fixed-length encoding
fixed_length_bits = 8
total_bits_fixed = total_chars * fixed_length_bits

average_bits = total_bits_huffman / total_chars
compression_gain = (1 - total_bits_huffman / total_bits_fixed) * 100

print("\nStatistics: ")
print("-" * 12)
print(f"Total characters: {total_chars}")
print(f"Average bits per character: {average_bits:.3f}")
print(f"Total bits (Huffman Code): {total_bits_huffman}")
print(f"Total bits (Fixed-length 8-bits): {total_bits_fixed}")
print(f"Compression Gain: {compression_gain:.2f}%")