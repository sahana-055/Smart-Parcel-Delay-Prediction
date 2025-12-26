def predict_priority(amount, delay, customer_type, history):
    score = 0

    if amount > 50000:
        score += 1
    if delay == "60+ days":
        score += 1
    if history == "Poor":
        score += 1
    if customer_type == "Business":
        score += 1

    if score >= 2:
        return "High Priority Case"
    else:
        return "Low Priority Case"
