
from seqparser import (
        FastaParser,
        FastqParser)
from seqparser import transcribe, reverse_transcribe

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
"""
fasta_parser = FastaParser("./tests/blank.fa")
seqs = []
with pytest.raises(ValueError):
      for header, seq in fasta_parser:
            seqs.append([header, seq])
"""

fasta = FastaParser("./data/test.fa")
seqs = {}
for header, seq in fasta:
        seqs[header] = seq
DNA = seqs["seq0"]
RNA = reverse_transcribe(DNA)

assert RNA == "UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA"
