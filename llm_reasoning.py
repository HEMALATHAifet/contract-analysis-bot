def explain_clause(clause, risk, clause_type):
    return f"""
Clause Type: {clause_type}

Risk Level: {risk}

Explanation (Plain Language):
This clause may impact an SME's legal or financial position.
Higher risk clauses are often one-sided or unclear.

Suggested Action:
Consider renegotiating this clause or seeking legal advice
before signing the agreement.
"""
