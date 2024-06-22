from sklearn.metrics.pairwise import cosine_similarity

def evaluate_skills(job_description_embeddings, resume_embeddings):
    similarity_score = cosine_similarity(job_description_embeddings, resume_embeddings)
    return similarity_score[0][0]

skill_evaluation_score = evaluate_skills(job_description_embeddings, resume_embeddings)
print(f"Skill Evaluation Score: {skill_evaluation_score}")
