HIGH_RISK = [
    "penalty", "indemnify", "non-compete",
    "terminate without cause", "unlimited liability",
    "exclusive ownership"
]

MEDIUM_RISK = [
    "auto-renew", "lock-in", "arbitration",
    "governing law", "jurisdiction"
]

def assess_risk(clause):
    clause = clause.lower()

    if any(k in clause for k in HIGH_RISK):
        return "High"
    if any(k in clause for k in MEDIUM_RISK):
        return "Medium"
    return "Low"

def overall_risk(scores):
    weight = {"High": 3, "Medium": 2, "Low": 1}
    total = sum(weight[s] for s in scores)

    avg = total / len(scores)

    if avg >= 2.3:
        return "High Risk"
    elif avg >= 1.6:
        return "Medium Risk"
    return "Low Risk"
