import streamlit as st
import json
from parser import extract_text
from nlp_rules import extract_clauses, extract_entities, classify_clause
from risk_engine import assess_risk, overall_risk
from llm_reasoning import explain_clause

st.set_page_config("Contract Risk Analyzer", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.caption("SME-friendly legal risk analysis (Python 3.14 compatible)")

uploaded = st.file_uploader("Upload Contract (PDF / DOCX / TXT)", type=["pdf","docx","txt"])

if uploaded:
    text = extract_text(uploaded)
    clauses = extract_clauses(text)
    entities = extract_entities(text)

    st.subheader("🔍 Extracted Contract Details")
    st.json(entities)

    risks = []

    st.subheader("⚠️ Clause-by-Clause Analysis")

    for i, clause in enumerate(clauses, 1):
        risk = assess_risk(clause)
        clause_type = classify_clause(clause)
        risks.append(risk)

        with st.expander(f"Clause {i} | {risk} Risk | {clause_type}"):
            st.write(clause)
            st.info(explain_clause(clause, risk, clause_type))

    final_risk = overall_risk(risks)

    st.subheader("📊 Overall Contract Risk")
    st.success(final_risk)

    audit = {
        "file": uploaded.name,
        "overall_risk": final_risk,
        "clauses": [
            {"clause_no": i+1, "risk": risks[i]}
            for i in range(len(risks))
        ]
    }

    with open("audit_log.json", "a") as f:
        json.dump(audit, f)
        f.write("\n")

    st.download_button(
        "📥 Download Risk Report",
        json.dumps(audit, indent=2),
        file_name="contract_risk_report.json"
    )
