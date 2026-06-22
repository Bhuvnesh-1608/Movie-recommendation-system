import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allows your future HTML frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 1. LOAD THE MACHINE LEARNING DATA ---
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# --- 2. THE RECOMMENDATION ENDPOINT ---
@app.get("/recommend")
def recommend_movie(movie: str):
    try:
        # Find the index of the requested movie
        # CHANGE THIS LINE INSIDE main.py:
        movie_index = movies_df[movies_df['title'].str.lower() == movie.lower()].index[0]
        distances = similarity[movie_index]
        
        # Sort and grab the top 5 most similar movies
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        for i in movies_list:
            recommended_movies.append(movies_df.iloc[i[0]].title)
            
        return {"status": "success", "data": recommended_movies}
    
    except IndexError:
        return {"status": "error", "message": "Movie not found. Please check your spelling."}


# --- 3. THE FILTER ENDPOINT ---
# --- 3. UPDATED CASE-INSENSITIVE FILTER ENDPOINT ---
@app.get("/filter")
def filter_movies(genre: str = None, actor: str = None, director: str = None):
    filtered_df = movies_df.copy()
    
    # Apply filters dynamically by converting everything to lowercase
    if genre:
        filtered_df = filtered_df[filtered_df['genres'].apply(
            lambda x: any(genre.lower() in item.lower() for item in x)
        )]
    if actor:
        filtered_df = filtered_df[filtered_df['cast'].apply(
            lambda x: any(actor.lower() in item.lower() for item in x)
        )]
    if director:
        filtered_df = filtered_df[filtered_df['crew'].apply(
            lambda x: any(director.lower() in item.lower() for item in x)
        )]
        
    results = filtered_df['title'].head(10).tolist()
    return {"status": "success", "data": results}