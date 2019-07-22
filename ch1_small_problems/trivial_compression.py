class CompressedGene:
    def __init__(self, gene: str):
        self.bit_string: int = self._compress(gene)

    def _compress(self, gene: str) -> int:
        bit_string: int = 1
        for nucleotide in gene.upper():
            bit_string <<= 2
            if nucleotide == "A":
                bit_string |= 0b00
            elif nucleotide == "C":
                bit_string |= 0b01
            elif nucleotide == "G":
                bit_string |= 0b10
            elif nucleotide == "T":
                bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide:{nucleotide}")
        return bit_string

    def _decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits:{bits}")
        return gene[::-1]

    def __str__(self) -> str:
        return self._decompress()



if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print(f"original is {getsizeof(original)} bytes")
    compressed = CompressedGene(original)
    print(f"compressed is {getsizeof(compressed.bit_string)} bytes")
    print(compressed.bit_string)
    print(compressed)
    print(f"original and decompressed are the same: {original == str(compressed)}")
