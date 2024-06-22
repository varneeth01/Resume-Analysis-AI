from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

resume_text = read_pdf('/mnt/data/Resume-varneeth (3).pdf')
job_description = "Job description text here"
resume_embeddings = get_bert_embeddings(resume_text)
job_description_embeddings = get_bert_embeddings(job_description)
