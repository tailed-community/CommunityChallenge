import numpy as np
from similarity_sol import cosine_similarity
from recommender_sol import recommend

def load_user_item_matrix(path):
    
    data = np.loadtxt(path, dtype=int, delimiter='\t')
    
    
    n_users = data[:, 0].max()
    n_items = data[:, 1].max()
    
    ratings = np.zeros((n_users + 1, n_items + 1), dtype=np.float32)
    
    for user_id, item_id, rating, _ in data:
        ratings[user_id, item_id] = rating
    
    return ratings


train_matrix = load_user_item_matrix('Challenge 2/Dataset/u1.base')
data = np.loadtxt('Challenge 2/Dataset/u1.test', dtype=int, delimiter='\t')
users, items, ratings, timestamps = data.T


# Cosine similarity
sim_matrix = cosine_similarity(train_matrix)

#Recommender system
n_users, n_items = train_matrix.shape
all_recs = {}
for user_id in range(1, n_users):
    if np.count_nonzero(train_matrix[user_id]) == 0:
        continue
    
    top_items = recommend(
        user_id=user_id,
        ratings=train_matrix,
        sim_matrix=sim_matrix,
        k=5,
        n_recs=10 # Best 10 recommendations
    )
    all_recs[user_id] = top_items
sample = 45
print(f"Top 10 recommendations for user {sample}: {all_recs[sample]}")