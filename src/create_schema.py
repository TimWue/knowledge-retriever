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
    "vectorizer": "text2vec-transformers"  # this could be any vectorizer

}

client.schema.create_class(class_obj)  # returns null on success
