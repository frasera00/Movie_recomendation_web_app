# Movie_recomendation_web_app

The MovieApp file is a Streamlit-based web application for movie recommendations, leveraging Weaviate's vector database. Here are the key functionalities and AI concepts used:

1. Search Tab:
  - Users can search for movies using vector, keyword, or hybrid search.
  - Filter options include rating and year range.
  - Uses Weaviate's near_text, bm25, and hybrid search methods for retrieving movie data.

2. Movie Details Tab:
  - Displays detailed information about a specific movie based on its ID.
  - Uses UUID generation and Weaviate's query capabilities to fetch and display movie details, including title, director, rating, year, synopsis, and reviews.

3. Recommendation Tab:
   - Provides AI-powered movie recommendations based on user input.
   - Uses Weaviate's hybrid search and a grouped task to generate recommendations.

The AI concepts used include:

 - Vector Search: Uses embeddings to find semantically similar movies.
 - Keyword Search: Traditional keyword-based search.
 - Hybrid Search: Combines vector and keyword search for improved accuracy.
 - UUID Generation: Ensures unique identifiers for movies.
 - Retrieval-Augmented Generation (RAG): Enhances recommendations by integrating retrieval-based data with generative models.




