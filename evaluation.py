from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
import numpy as np

resumes = ["Resume text 1", "Resume text 2", "Resume text 3"]
labels = ["Good", "Average", "Poor"]

label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)

resume_embeddings = np.array([get_bert_embeddings(resume).flatten() for resume in resumes])

X_train, X_test, y_train, y_test = train_test_split(resume_embeddings, labels_encoded, test_size=0.2, random_state=42)

mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
mlp.fit(X_train, y_train)

accuracy = mlp.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

new_resume = read_pdf('/mnt/data/Resume-varneeth (3).pdf')
new_resume_embedding = get_bert_embeddings(new_resume).flatten().reshape(1, -1)
prediction = mlp.predict(new_resume_embedding)
predicted_label = label_encoder.inverse_transform(prediction)
print(f"Predicted Resume Rating: {predicted_label[0]}")
