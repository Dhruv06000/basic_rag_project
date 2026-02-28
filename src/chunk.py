from typing import List
import re

from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap_fraction: float = 0.1) -> List[str]:
    """
    Splits the input text into overlapping chunks of words.

    Args:
        text (str): The input text to be chunked.
        chunk_size (int): Number of words per chunk. Default is 500.
        overlap_fraction (float): Fraction of words to overlap with previous chunk. Default is 0.1 (10%).

    Returns:
        List[str]: A list of text chunks.
    """
    text_words = text.split()
    overlap_words = int(chunk_size * overlap_fraction)

    chunks = []

    for i in range(0, len(text_words), chunk_size):
        start = max(0, i - overlap_words)
        end = i + chunk_size
        chunk_words = text_words[start:end]
        chunks.append(" ".join(chunk_words))

    return chunks

