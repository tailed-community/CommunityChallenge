import numpy as np

def cosine_similarity(ratings: np.ndarray) -> np.ndarray:
    """
    Input: user×item rating matrix (zeros = unrated)
    Output: item×item cosine-similarity matrix
    """
    # implement me