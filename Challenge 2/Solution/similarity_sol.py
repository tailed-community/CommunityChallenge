import numpy as np

def cosine_similarity(matrix: np.ndarray) -> np.ndarray:
    item_vectors = matrix.T  # shape (n_items, n_users)

    # Compute the Euclidian norm for each item vector
    norms = np.linalg.norm(item_vectors, axis=1)  # shape (n_items)
    norms[norms == 0] = 1e-10

    # Compute the full dot‐product matrix between items
    dot_products = item_vectors @ item_vectors.T

    # Normalize by outer product of norms
    sim = dot_products / (norms[:, None] * norms[None, :])

    return sim