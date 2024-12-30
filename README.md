# Document Search and Retrieval Application

This repository contains a simple document search and retrieval system implemented using a pre-trained BERT model. The application leverages cosine similarity to rank documents based on their relevance to a user-provided query. The user interface is built using Streamlit, making it accessible via a web browser.

## Features
- **Document Search:** Finds the most relevant documents from a dataset based on a query.
- **BERT Embeddings:** Uses the `sentence-transformers` library to generate document embeddings.
- **Cosine Similarity:** Ranks documents using cosine similarity scores.
- **Streamlit UI:** Provides an intuitive web interface for search.
- **Pandas-Based Database:** Manages documents using a CSV file.
- **Dockerized Deployment:** Easily deployable using Docker.

## File Structure
- `Dockerfile`: Configuration for building the Docker image.
- `requirements.txt`: Python dependencies.
- `infer.py`: Core logic for loading documents, generating embeddings, and searching.
- `app.py`: Streamlit application script.
- `database.py`: Script to initialize a sample document database.
- `documents.csv`: Automatically generated CSV file containing the document dataset.

## Prerequisites
- Docker installed on your system.
- Python 3.9 or above (if running locally).

## Setup and Usage

### Step 1: Initialize the Database
Run the `database.py` script to create a sample document database in CSV format:
```bash
python database.py
```

### Step 2: Build the Docker Image
Build the Docker image for the application:
```bash
docker build -t document-search .
```

### Step 3: Run the Docker Container
Start the container:
```bash
docker run -p 8501:8501 document-search
```

### Step 4: Access the Application
Open your web browser and navigate to:
```
http://localhost:8501
```

### Step 5: Search for Documents
1. Enter a search query in the input box.
2. Click the "Search" button.
3. View the top matching documents along with their titles, content, and relevance scores.

## Running Locally (Optional)
If you prefer not to use Docker, follow these steps:

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Access the application at `http://localhost:8501`.

## Customization
- **Add New Documents:** Modify the `initialize_database` function in `database.py` to include new documents.
- **Model Selection:** Change the BERT model used in `infer.py` by replacing `'paraphrase-MiniLM-L6-v2'` with another model from the `sentence-transformers` library.

## Dependencies
- Python 3.9
- `streamlit`
- `transformers`
- `sentence-transformers`
- `scikit-learn`
- `pandas`

## License
This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

## Acknowledgments
- [Hugging Face](https://huggingface.co/) for the `transformers` library.
- [Streamlit](https://streamlit.io/) for the web application framework.
- [Sentence-Transformers](https://www.sbert.net/) for pre-trained models and utilities.

