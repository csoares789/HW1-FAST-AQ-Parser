# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    #Test on proper fasta files
    fasta_parser = FastaParser("./data/test.fa")
    seqs = {}
    for header, seq in fasta_parser:
        seqs[header] = seq

    assert seqs["seq0"] == "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    assert seqs["seq99"] == "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA"

    #It appears FastaParse() cannot handle the edge case files without throwing an error, so I wrote tests assuming that was the intended behavior
    #Test on file with no sequences
    fasta_parser = FastaParser("./tests/bad.fa")
    seqs = []
    with pytest.raises(ValueError):
        for header, seq in fasta_parser:
            seqs.append([header, seq])
    
    #Test for blank file
    fasta_parser = FastaParser("./tests/blank.fa")
    seqs = []
    with pytest.raises(ValueError):
        for header, seq in fasta_parser:
            seqs.append([header, seq])


    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fasta_parser = FastaParser("./data/test.fq")
    seqs = []
    for header, seq in fasta_parser:
        seqs.append([header, seq])
    
    assert seqs[0][0] == None

    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq_parser = FastqParser("./data/test.fq")

    seqs = {}
    for header, seq, qual in fastq_parser:
        seqs[header] = [seq, qual]

    assert seqs["seq0"][0] == "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG"
    assert seqs["seq0"][1] == "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32="
    assert seqs["seq99"][0] == "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG"
    assert seqs["seq99"][1] == "2$7)*5:\"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)!%)4%$=0\":02\"0=!0#/>+*1$1$39!.8+9<'1$*1$321&<'&9,)2"

    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_parser = FastqParser("./data/test.fa")

    seqs = []

    for header, seq, qual in fastq_parser:
        seqs.append([header, seq, qual])

    assert seqs[0][0] == None

    pass