def evaluate(target, guess):
    result = ["gray"] * len(guess)
    target_unmatched = []

    # First pass: identify exact matches (green)
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
        else:
            target_unmatched.append(target[i])

    # Second pass: mark remaining letters yellow if available in target
    for i, ch in enumerate(guess):
        if result[i] != "green" and ch in target_unmatched:
            result[i] = "yellow"
            target_unmatched.remove(ch)

    return result

