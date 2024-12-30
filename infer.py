from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Initialize the BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

class DocumentSearch:
    def __init__(self, database_path="documents.csv"):
        self.database_path = database_path
        self.documents = self._load_documents()
        self.embeddings = self._generate_embeddings()

    def _load_documents(self):
        """Load documents from the CSV file."""
        return pd.read_csv(self.database_path)

    def _generate_embeddings(self):
        """Generate embeddings for all documents."""
        return model.encode(self.documents['content'].tolist(), convert_to_tensor=True)

    def search(self, query, top_k=5):
        """Search for the most relevant documents."""
        query_embedding = model.encode([query], convert_to_tensor=True)
        scores = cosine_similarity(query_embedding, self.embeddings)[0]
        self.documents['score'] = scores
        return self.documents.nlargest(top_k, 'score')