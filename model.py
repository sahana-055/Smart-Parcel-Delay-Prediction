def predict_delay(distance, traffic, weather, delivery_type):
    score = 0

    if distance > 50:
        score += 1
    if traffic == "High":
        score += 1
    if weather in ["Rainy", "Storm"]:
        score += 1
    if delivery_type == "Standard":
        score += 1

    if score >= 2:
        return "Likely Delayed"
    else:
        return "On Time"
