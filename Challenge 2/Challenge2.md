# Challenge 2: Item-Based Collaborative-Filtering Recommender

In this exercise, you will build an item-based collaborative-filtering recommender using the MovieLens 100K dataset. All starter files and data splits are provided in this folder—look for the `u1.base`, `u1.test`, and the module stubs (`similarity.py`, `recommender.py`, `evaluation.py`).

## Objective

Create a Python program that:

1. Loads the training split (`u1.base`) into a user×item rating matrix.
2. Computes an item×item cosine-similarity matrix.
3. Predicts ratings for each `(user, item)` pair in the test split (`u1.test`) using a weighted average of a user’s known ratings on the k most similar items.
4. Evaluates the overall RMSE between your predicted ratings and the true ratings in `u1.test`.
5. Prints the test RMSE and displays top-10 recommendations for at least two different users.

## Files Provided

- **u1.base**: Training data (tab-delimited: user_id, item_id, rating, timestamp)
- **u1.test**: Test data (same format as `u1.base`)
- **similarity.py**: Stub for `cosine_similarity(ratings: np.ndarray) -> np.ndarray`
- **recommender.py**: Stub for `recommend(user_id, ratings, sim_matrix, k, n_recs) -> list[int]`
- **evaluation.py**: Stub for `rmse(true_ratings, pred_ratings) -> float`

You can find these files and data splits in the same folder as this challenge file.

## Your Task

1. **Implement**  
   - In `similarity.py`, complete the `cosine_similarity` function so it returns a correctly normalized item×item similarity matrix.
   - In `recommender.py`, complete the `recommend` function to predict top-N item IDs for a given user based on k nearest neighbors.
   - In `evaluation.py`, complete the `rmse` function to compute the root-mean-square error between true and predicted ratings.

2. **Driver Script**  
   Create a new file `run_recommender.py` that:
   - Loads `u1.base` into a NumPy user×item array (zeros indicate unrated).
   - Calls your `cosine_similarity` to build the similarity matrix.
   - Loads `u1.test`, iterates through each test record, and uses your `recommend` logic or a helper that predicts a single rating for that user-item pair.
   - Computes and prints the test RMSE.
   - Displays the top-10 recommended items for at least two sample users.

## Advice & Tips

- Use NumPy for efficient matrix operations: dot products, norms, slicing, and `argsort`.
- When an item vector has zero norm (no ratings), clamp it to a small value to avoid division by zero.
- In `recommend`, if the denominator in your weighted average is zero (no overlap), you can fall back to a default prediction (e.g. zero or the user’s mean rating).
- Keep each module focused on one job: similarity, recommendation logic, or evaluation.
- Test your functions on a small synthetic matrix first to verify correctness before running on the full MovieLens data.
- Really try it yourself before asking ChatGPT !! You'll learn much  more that way even if you feel stuck. 

## Push further 
- Try and run it for other dataset or a production setup that mimicks real life company.
- This is only a recommender system for a movie system. Try and simulate a real-time recommender system like Tiktok.

Good luck! Once your code is running, check that your RMSE is reasonably low (around 1.0 or less) and that your sample recommendations make intuitive sense.  
