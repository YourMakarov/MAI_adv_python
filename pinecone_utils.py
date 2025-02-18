import time
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from config import API_KEY, INDEX_NAME

def initialize_pinecone():
    pc = Pinecone(api_key=API_KEY)
    if not pc.has_index(INDEX_NAME):
        pc.create_index(
            name=INDEX_NAME,
            dimension=312,  # Замените на реальное значение embeddings_len
            metric="cosine",
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    while not pc.describe_index(INDEX_NAME).status['ready']:
        time.sleep(1)
    return pc.Index(INDEX_NAME)

def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def upsert_vectors(index, data_vector_bd):
    for batch_data in batch(data_vector_bd, 100):
        index.upsert(
            vectors=batch_data,
            namespace="example-namespace"
        )