import numpy as np

def recommend(
    user_id: int,
    ratings: np.ndarray,
    sim_matrix: np.ndarray,
    k: int = 5,
    n_recs: int = 10
) -> list[int]:
    
    all_item_ids = range(ratings.shape[1])
    
    rated_items = [i for i in all_item_ids if ratings[user_id, i] > 0]
    unrated_items = [i for i in all_item_ids if ratings[user_id, i] == 0]

    
    predictions: dict[int, float] = {}

    
    for i in unrated_items:
        # Pair each rated item with its similarity to item i
        sims = [(j, sim_matrix[i, j]) for j in rated_items]
        # Sort by similarity descending and take top-k neighbors
        top_neighbors = sorted(sims, key=lambda x: x[1], reverse=True)[:k]

        
        numerator = sum(s * ratings[user_id, j] for j, s in top_neighbors)
        denominator = sum(abs(s) for _, s in top_neighbors)

        pred_rating = numerator / denominator if denominator > 0 else 0.0

        predictions[i] = pred_rating

    
    sorted_preds = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
    
    return [item for item, _ in sorted_preds[:n_recs]]