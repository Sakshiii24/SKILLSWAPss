from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_best_matches(user_skills: str, all_offers):
    user_vec = model.encode(user_skills, convert_to_tensor=True)
    results = []
    for offer in all_offers:
        offer_vec = model.encode(offer.skill_wanted, convert_to_tensor=True)
        similarity = util.cos_sim(user_vec, offer_vec)
        results.append((offer, similarity.item()))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:5]