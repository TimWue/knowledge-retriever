from os import listdir
from os.path import isfile, join
import weaviate
from src.chunk_pdf import chunk_pdf_file

data_path = "../data"
weaver_url = "http://localhost:8080"

files = [f for f in listdir(data_path) if isfile(join(data_path, f))]
file = f'{data_path}/{files[0]}'
client = weaviate.Client(weaver_url)
chunks = chunk_pdf_file(file)

for chunk in chunks:
    uuid = client.data_object.create(
        class_name="TextChunk",
        data_object={
            "content": chunk,
        }
    )
    print(uuid)