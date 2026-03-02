import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('../data/processed_data.csv')

# تجهيز TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["اسم المتقدم"])


def search_name(query):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    sim_series = pd.Series(similarities, index=df.index)
    top_n = len([r for r in sim_series if r > 0])
    top_idx = sim_series.nlargest(top_n).index

    results = df.loc[top_idx].assign(
        similarity=(sim_series.loc[top_idx].values * 100).round(2)
    )

    return results.to_dict(orient="records")  # نرجع قائمة قواميس (JSON-friendly)
