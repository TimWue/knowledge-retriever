import json

import weaviate

weaver_url = "http://localhost:8080"
client = weaviate.Client(weaver_url)


response = (
    client.query
    .get("TextChunk", ["content"])
    .with_near_text({
        "concepts": ["Was wird als Antivalenz bezeichnet?"]
    })
    .with_limit(2)
    .with_additional(["distance"])
    .do()
)

print(json.dumps(response, indent=2))