
from seqparser import (
        FastaParser,
        FastqParser)

import pytest

"""
fastq_parser = FastqParser("./data/test.fa")

seqs = []

for header, seq, qual in fastq_parser:
    seqs.append([header, seq, qual])

assert seqs[0][0] == None
"""
"""
fasta_parser = FastaParser("./tests/bad.fa")
seqs = []
with pytest.raises(ValueError):
        for header, seq in fasta_parser:
                seqs.append([header, seq])

"""
fasta_parser = FastaParser("./tests/blank.fa")
seqs = []
with pytest.raises(ValueError):
      for header, seq in fasta_parser:
            seqs.append([header, seq])
