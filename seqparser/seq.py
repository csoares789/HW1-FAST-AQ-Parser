# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    transcript = ""
    for base in seq:
        transcript += TRANSCRIPTION_MAPPING[base]
    return transcript

def reverse_transcribe(seq: str) -> str:
    transcript = transcribe(seq)
    rev_transcript = transcript[::-1]
    return rev_transcript