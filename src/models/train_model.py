
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error


class CollaborativeFiltering:
    def __init__(self, dataframe, k = 10):
        self.dataframe = dataframe.copy()
        self.user_similarities = None
        self.k = k

    def fit(self):
        # Calculate cosine similarity between users
        self.user_similarities = cosine_similarity(self.dataframe)
        self.user_similarities = pd.DataFrame(
            self.user_similarities,
            index=self.dataframe.index,
            columns=self.dataframe.index
        )

    def predict(self, user_id):
        # Predict the rating for each item
        if self.user_similarities is None:
            raise ValueError("Fit the model first using the fit() method.")

        # Get similar users
        similar_users = self.user_similarities[user_id].sort_values(ascending=False).index[1: self.k + 1]

        # Get ratings from similar users
        similar_user_ratings = self.dataframe.loc[similar_users]
        # Calculate weighted average rating for unseen items
        weighted_sum = similar_user_ratings.T.dot(self.user_similarities.loc[user_id, similar_users])
        sum_of_weights = self.user_similarities.loc[user_id, similar_users].sum()

        # Recommend unseen items with highest predicted ratings
        predicted_ratings = weighted_sum / (sum_of_weights + 1e-9)
        
        return predicted_ratings
    
    def recommend_items(self, user_id, num_recommendations):
        predicted_ratings = self.predict(user_id)

        recommendations = predicted_ratings.sort_values(ascending=False).index[:num_recommendations]
        
        return recommendations
    
    def batch_predict(self, eval_dataframe):
        # Predict the rating for each item
        if self.user_similarities is None:
            raise ValueError("Fit the model first using the fit() method.")

        _eval_dataframe = eval_dataframe.copy()
        _predictions = pd.DataFrame(index=_eval_dataframe.index, columns=_eval_dataframe.columns)

        for user in _eval_dataframe.index:
            _predictions.loc[user] = self.predict(user)

        return _predictions

    def evaluate(self, eval_dataframe, missing_rating):
        if self.user_similarities is None:
            raise ValueError("Make sure training first.")

        # Flatten actual and predicted ratings for evaluation
        actual_ratings = eval_dataframe.fillna(0).values.flatten()
        
        _predicted_ratings = self.batch_predict(eval_dataframe)
        predicted_ratings = _predicted_ratings.values.flatten()

        # Calculate Mean Squared Error (MSE) and Root Mean Squared Error (RMSE)
        mse = mean_squared_error(actual_ratings, predicted_ratings)
        rmse = np.sqrt(mse)

        return {'MSE': mse, 'RMSE': rmse}