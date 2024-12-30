import pandas as pd

def initialize_database():
    data = [
        {"title": "Document 1", "content": "This is the content of the first document."},
        {"title": "Document 2", "content": "Here we have another document, slightly different."},
        {"title": "Document 3", "content": "The third document has unique information."},
        {"title": "Document 4", "content": "More text in this fourth document to search through."},
        {"title": "Document 5", "content": "Finally, the last document in our database."}
    ]
    df = pd.DataFrame(data)
    df.to_csv("documents.csv", index=False)

if __name__ == "__main__":
    initialize_database()