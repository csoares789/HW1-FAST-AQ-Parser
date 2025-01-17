import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seqparser import (
        FastaParser,
        FastqParser)

fasta_parser = FastaParser("./HW1-FAST-AQ-Parser/data/test.fa")

# Iterate over the parsed records
for header, sequence in fasta_parser:
    print(f"Header: {header}")
    print(f"Sequence: {sequence}")
