import torch 
from torch.utils.data import Dataset
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from transformers import AdamW
import pandas as pd
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader

model_name = "distilbert-base-uncased"

# reading in the data and splitting into features and labels
df = pd.read_csv("train.csv")
train_texts = df["comment_text"].values
train_labels = df[df.columns[2:]].values

train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=.2)

tokenizer = DistilBertTokenizerFast.from_pretrained(model_name, max_length=1024)

# creating a custom dataset for training
class ToxicDataset(Dataset):
  def __init__(self, texts, labels):
    self.texts = texts
    self.labels = labels
  
  def __getitem__(self, index):
    encodings = tokenizer(self.texts[index], truncation=True, padding='max_length')
    item = {key: torch.tensor(val) for key, val in encodings.items()}
    item['labels'] = torch.tensor(self.labels[index], dtype=torch.float32)
    del encodings #
    return item

  def __len__(self):
    return len(self.labels)
  
  device = torch.device('cuda')

# download model and prepare it for training
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=6, problem_type="multi_label_classification")
model.to(device)
model.train()

# defining the dataset and dataloader
train_dataset = ToxicDataset(train_texts, train_labels)
train_dataloader = DataLoader(train_dataset, batch_size=16)

optim = AdamW(model.parameters(), lr=5e-5)
num_train_epochs = 1

for epoch in range(num_train_epochs):
  for batch in train_dataloader:
    optim.zero_grad()
    input_ids = batch['input_ids'].to(device)
    attention_mask = batch['attention_mask'].to(device)
    labels = batch['labels'].to(device)

    outputs = model(input_ids, attention_mask=attention_mask, labels=labels)

    loss = outputs[0]
    loss.backward()
    optim.step()

model.eval()
