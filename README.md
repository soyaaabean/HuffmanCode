
# Huffman Coding Project

This project implements Huffman coding to compress a set of characters based on their frequencies.

## Features

- Reads characters from a file (`characters.txt`)
- Builds a Huffman tree
- Generates Huffman codes for each character
- Displays a table with character, frequency, Huffman code, and bit length
- Calculates compression statistics:
  - Average bits per character
  - Total bits using Huffman coding
  - Total bits using fixed-length (8-bit) encoding
  - Compression gain percentage

## How to Use

1. Save your input text in a file named `characters.txt` in the same folder as the script.
2. Run the script using Python 3:

```
python huffman_coding.py
```

3. The output will display in the terminal.

## Requirements

- Python 3.x

No external libraries are needed — the script only uses built-in modules.

## Notes

- Newline characters (`\n`) are removed before processing.
- Fixed-length encoding assumes 8 bits per character (standard ASCII).

## Example Output

```
Character  Frequency    Code            # Bits
---------------------------------------------
a          24480        00001           5
b          71040        0001            4
...
--- Statistics ---
Total characters: 1053840
Average bits per character: 2.579
Total bits (Huffman): 2718000
Total bits (Fixed-length): 8430720
Compression gain: 67.76%
```

## Author

This project was developed as part of the **Algorithms and Data Structures** course for Spring 2025.

---

## License

This code is provided for educational purposes. You are free to modify and reuse it for non-commercial use.
