import weaviate

client = weaviate.Client("http://localhost:8080")

uuid = client.data_object.create(
    class_name="TextChunk",
    data_object={
        "content": "This vector DB is OSS & supports automatic property type inference on import",
    }
)

print(uuid)