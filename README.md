# 📄 Contract Analysis & Risk Assessment Bot

A **GenAI-powered legal assistant** that helps Indian SMEs understand contracts, identify legal risks, and receive actionable advice in **plain business language**.

This project was built as part of a **hackathon problem statement** focused on contract analysis, risk scoring, and explainability — without relying on external legal databases.

---

## 🚀 Features

* 📂 Upload contracts in **PDF, DOCX, or TXT** format
* 🧠 Automatic **clause-by-clause analysis**
* ⚠️ **Risk scoring** for each clause (Low / Medium / High)
* 📊 **Overall contract risk assessment**
* 🧾 Entity extraction:

  * Parties
  * Dates
  * Monetary amounts (₹ / INR / Rs)
  * Jurisdiction
* 🗣️ **Plain-language explanations** suitable for non-legal users
* 📥 Downloadable **JSON risk report** for legal review
* 📝 Audit trail generation
* ✅ Fully compatible with **Python 3.14** (spaCy-free)

---

## 🛠️ Tech Stack

* **Language:** Python 3.14
* **UI:** Streamlit
* **Text Extraction:** pdfplumber, python-docx
* **NLP (Rule-based):** Regex & heuristics
* **Language Detection:** langdetect
* **LLM (Optional):** GPT-4 / Claude 3 (for reasoning only)

> ⚠️ No external legal databases, case law, or APIs are used.

---

## 📁 Project Structure

```
contract_bot/
├── app.py                # Streamlit UI
├── parser.py             # File parsing (PDF/DOCX/TXT)
├── nlp_rules.py          # Clause & entity extraction (rule-based)
├── risk_engine.py        # Risk scoring logic
├── llm_reasoning.py      # Plain-language explanations (LLM-ready)
├── requirements.txt
├── audit_log.json        # Auto-generated audit trail
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

---

## 🧪 Sample Inputs

Sample contracts (service agreements, employment contracts) are provided in plain text format for easy testing. These contracts include common clauses such as termination, penalties, indemnity, jurisdiction, and non-compete.

---

## 📊 Example Output

* Clause-by-clause risk classification
* Plain English explanation of legal impact
* Overall contract risk (Low / Medium / High)
* Downloadable JSON report for legal consultation

---

## 🎯 Intended Users

* Small & Medium Business Owners (SMEs)
* Startup founders
* Legal consultants
* Compliance teams

---

## 🏆 Hackathon Highlights

* Focus on **explainability over black-box AI**
* SME-centric risk interpretation
* Stable, demo-friendly architecture
* Clear audit trails and exportable outputs

---

## 📌 Disclaimer

This tool provides **informational insights only** and does not constitute legal advice. Users are encouraged to consult a qualified legal professional before making contractual decisions.

---

## 👩‍💻 Author

Built with ❤️ for hackathons and real-world SME problems.
