from datasets import load_dataset
import torch

# we load this dataset to get the speaker embeddings
print("we load this dataset to get the speaker embeddings")
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

print(embeddings_dataset)

speaker_embeddings = embeddings_dataset[7306]["xvector"]
speaker_embeddings = torch.tensor(speaker_embeddings).unsqueeze(0)

print(speaker_embeddings)