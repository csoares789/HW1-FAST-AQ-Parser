# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)
from seqparser import (
        FastaParser)

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    fasta = FastaParser("./data/test.fa")
    seqs = {}
    for header, seq in fasta:
        seqs[header] = seq
    DNA = seqs["seq0"]
    RNA = transcribe(DNA)
    assert RNA == "ACUAACUUAGAAAACUCCCAGUGCCGGGCCUUCGGUCUUAAAGCCCCAGGAGACACCUAUAAUUAGCUCGGGUGUGCCACACUCAAGUCGCCGGGGGCGU"

    pass


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    fasta = FastaParser("./data/test.fa")
    seqs = {}
    for header, seq in fasta:
        seqs[header] = seq
    DNA = seqs["seq0"]
    rev_RNA = reverse_transcribe(DNA)
    assert rev_RNA == "UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA"
    pass