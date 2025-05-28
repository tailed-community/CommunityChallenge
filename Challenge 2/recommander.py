import numpy as np

def recommend(
    user_id: int,
    ratings: np.ndarray,
    sim_matrix: np.ndarray,
    k: int = 5,
    n_recs: int = 10
) -> list[int]:
    """
    For a given user, produce top-n_recs item IDs,
    using their k most similar rated neighbors.
    """
    # implement me