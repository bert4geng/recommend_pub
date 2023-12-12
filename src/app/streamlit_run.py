import pandas as pd
import streamlit as st
import pickle

from src.models.train_model import CollaborativeFiltering

st.set_page_config(layout="wide")
# Streamlit app
st.title("Personalization movies recommendation")

# Specify the file path where you want to save the model
model_filename = './models/cf_model_001.pkl'
matrix_filename = './models/matrix.csv'
MOVIE_DATA_PATH = "./data/external/movie/"
MOVIES = MOVIE_DATA_PATH + "movies.csv"
number_of_recommendations = 100

# Use pickle to load the model from the file
with open(model_filename, 'rb') as model_file:
    collab_filter = pickle.load(model_file)


movies_df = pd.read_csv(MOVIES, header=0)
matrix = pd.read_csv(matrix_filename, index_col=0)

user_id = st.selectbox("Select a User ID", matrix.index)


recommend_movies_ids = collab_filter.recommend_items(user_id, number_of_recommendations)
# check if the movied already watched
watched_movies_mask = matrix.loc[user_id].notna()
watched_movies_ids = matrix.loc[user_id].index[watched_movies_mask]

# Find IDs in A that are not in B
ids_in_recommend_not_in_watched = recommend_movies_ids[~recommend_movies_ids.isin(watched_movies_ids)]

recommend_movies_top20_after_filter_watched = ids_in_recommend_not_in_watched

filtered_movies_df = movies_df[movies_df['movieId'].isin(recommend_movies_top20_after_filter_watched)]

recommend_movies_to_user = filtered_movies_df.set_index('movieId').loc[recommend_movies_top20_after_filter_watched]


st.subheader("Personalized Recommended Movies fore renting:")
st.write(recommend_movies_to_user)


#### watch movies to buy
movies_df_new = movies_df.set_index("movieId")

rate_high_movies = matrix.loc[user_id, watched_movies_ids] > 4


rate_high_movies = rate_high_movies.index[rate_high_movies]

rate_high_movies = [int(_id) for _id in rate_high_movies.tolist()]
watched_movies_for_the_user = movies_df_new.loc[rate_high_movies]


st.subheader("Watched moves that you enjoyed in the past. recommend to buy it")
st.write(watched_movies_for_the_user)

# Run the app
if __name__ == "__main__":
    st.write("")