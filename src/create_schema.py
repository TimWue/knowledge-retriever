import weaviate

client = weaviate.Client("http://localhost:8080")

class_obj = {
    "class": "TextChunk",
    "properties": [
        {
            "name": "content",
            "dataType": ["text"],
        }
    ],
    "vectorizer": "text2vec-transformers"

}

client.schema.create_class(class_obj)
