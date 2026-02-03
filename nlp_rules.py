import re

def extract_clauses(text):
    pattern = r"(?:\n|^)(\d+\.\s+.+?)(?=\n\d+\.|\Z)"
    clauses = re.findall(pattern, text, re.DOTALL)
    return [c.strip() for c in clauses if len(c.strip()) > 60]

# def extract_entities(text):
#     return {
#         "Dates": re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text),
#         "Amounts": re.findall(r"(₹|\$)\s?\d+(?:,\d+)*(?:\.\d+)?", text),
#         "Jurisdiction": re.findall(r"jurisdiction of ([A-Za-z ]+)", text, re.I),
#         "Parties": re.findall(r"between\s+(.+?)\s+and\s+(.+?)[,\n]", text, re.I)
#     }

def extract_entities(text):
    # Amounts must have currency OR comma format
    amount_pattern = r"""
        (?:
            (?:₹|\$|Rs\.?|INR)\s?\d{1,3}(?:,\d{2,3})*(?:\.\d+)?   # ₹50,000 | Rs. 1,00,000
            |
            \d{1,3}(?:,\d{2,3})+                                 # 50,000 | 1,00,000
        )
    """

    amounts = re.findall(amount_pattern, text, re.VERBOSE)

    return {
        "Dates": re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text),
        "Amounts": [a.strip() for a in amounts],
        "Jurisdiction": re.findall(r"jurisdiction of ([A-Za-z ]+)", text, re.I),
        "Parties": re.findall(r"between\s+(.+?)\s+and\s+(.+?)[,\n]", text, re.I)
    }



def classify_clause(clause):
    clause = clause.lower()
    if any(w in clause for w in ["shall", "must", "is required to"]):
        return "Obligation"
    if any(w in clause for w in ["may", "entitled to"]):
        return "Right"
    if any(w in clause for w in ["shall not", "prohibited", "restricted"]):
        return "Prohibition"
    return "Neutral"
