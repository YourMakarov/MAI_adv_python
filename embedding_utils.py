import torch
from transformers import AutoTokenizer, AutoModel

tokenizer_embedder = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2")
model_embedder = AutoModel.from_pretrained("cointegrated/rubert-tiny2")

def embed_bert_cls(text):
    t = tokenizer_embedder(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model_embedder(**{k: v.to(model_embedder.device) for k, v in t.items()})
    embeddings = model_output.last_hidden_state[:, 0, :]
    embeddings = torch.nn.functional.normalize(embeddings)
    return embeddings[0].cpu().numpy()

def get_embeddings(text_arr):
    return [embed_bert_cls(text) for text in text_arr]