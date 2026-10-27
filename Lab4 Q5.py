import re

class DNA:
    def __init__(self, left_strand="A-C-G-G-T-C",right_strand="T-G-C-C-A-G"):
        self.left_strand = left_strand
        self.right_strand = right_strand
        self.left = left_strand.replace("-", "")
        self.right = right_strand.replace("-", "")

    def isValidDNA(self):
        if re.fullmatch(r"[ATCG]+", self.left) and re.fullmatch(r"[ATCG]+", self.right):
            return True
        else:
            return False

    def complementWC(self):
        pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
        self.complement_left = ""
        self.complement_right = ""

        for letter in self.left:
            self.complement_left += pairs[letter]

        for letter in self.right:
            self.complement_right += pairs[letter]

        print(f"The complement of {self.left} is {self.complement_left}")
        print(f"The complement of {self.right} is {self.complement_right}")

    def palindromeWC(self):
        reverse_left = self.complement_left[::-1]
        reverse_right = self.complement_right[::-1]

        print("Left strand is a WC palindrome:", self.left == reverse_left)
        print("Right strand is a WC palindrome:", self.right == reverse_right)

    def containsSequence(self, seq):
        seq = seq.replace("-", "").upper()
        return seq in self.left or seq in self.right

    @staticmethod
    def summarise(dna):
        print("Original left strand:", dna.left_strand)
        print("Original right strand:", dna.right_strand)

        if dna.isValidDNA():
            print("Is valid")
            dna.complementWC()
            dna.palindromeWC()
        else:
            print("Not valid DNA")


strands = input("Enter two DNA strands separated by a space: ").upper().split()

if len(strands) == 2:
    dna = DNA(strands[0], strands[1])
    DNA.summarise(dna)
else:
    print("Please enter exactly two strands, separated by a space.")