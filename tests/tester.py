
from seqparser import (
        FastaParser,
        FastqParser)

"""
fastq_parser = FastqParser("./data/test.fa")

seqs = []

for header, seq, qual in fastq_parser:
    seqs.append([header, seq, qual])

assert seqs[0][0] == None
"""

fasta_parser = FastaParser("./tests/bad.fa")
seqs = []
for header, seq in fasta_parser:
        seqs.append([header, seq])
print(seqs[0][0])
assert seqs[0][0] == None