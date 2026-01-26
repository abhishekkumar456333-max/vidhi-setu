# Vidhi Setu 🇮🇳

**Privacy-First AI Contract Risk Analysis Grounded in Indian Law**

Vidhi Setu is an intelligent LegalTech platform designed specifically for the Indian creative community, freelancers, and early-stage startups. It bridges the gap between complex legal jargon and fair professional agreements by providing jurisdiction-aware risk assessment anchored in **The Indian Contract Act, 1872**.

---

## 🚀 Key Features

### ⚖️ Jurisdiction-Aware Legal Engine

- **Statutory Grounding**: Every risk flag is mapped to specific Indian statutes like the Indian Contract Act, 1872 or the Copyright Act, 1957.
- **Jurisdiction Lock**: Hard guardrails that block non-Indian legal concepts (e.g., Delaware law, at-will employment) to ensure 100% domestic compliance.

### 🛡️ Privacy & Security (Zero-Logging)

- **PII Tokenization**: Automatically detects and replaces names, emails, and company names with privacy tokens (e.g., `[PERSON_1]`, `[COMPANY_A]`) before analysis.
- **Ephemeral Processing**: Contracts are processed in-memory and never stored permanently on our servers.
- **User-Controlled Purge**: Users can permanently delete their session data from server memory with a single click.

### 🧠 Intelligent Analysis

- **Statutory Risk Scoring**: A deterministic 0-100 score based on legal severity.
- **ELI5 Explanations**: Complex clauses are translated into simple, plain English summaries.
- **Template Deviation Check**: Compares contract clauses against a baseline of "fair" industry standards to detect unfair terms.

---

## 🛠️ Technology Stack

- **Frontend**: React (Vite), Tailwind CSS, Framer Motion (for high-end animations), Lucide React.
- **Backend**: FastAPI (Python), Regular Expression Legal Engines, OpenAI (for explainability layer).
- **Design**: Premium dark/glassmorphism aesthetic with a citation-first user experience.

---

## 🏁 Getting Started

### Backend Setup

1. Navigate to the `backend/` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your environment variables:
   - `OPENAI_API_KEY`: For the QA and explanation layers.
   - `HF_API_KEY`: (Optional) Fallback explanation model.
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend/` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

---

## 🧪 Testing the Platform (Jury Guide)

To evaluate the full depth of Vidhi Setu's legal intelligence:

1. Access the **Dashboard** via the "Get Started" button.
2. Click **"Test with Sample"** to load a pre-configured high-risk contract.
3. Observe the **Section 27 (Non-Compete)** detection and the **Jurisdiction Guardrail** blocking Delaware law references.
4. Notice the **PII protection badge** indicating names and emails have been tokenized.

---

## ⚠️ Disclaimer

Vidhi Setu is an assistive tool intended to improve legal awareness and understanding. It does **not** provide legal advice. Users should always consult a qualified legal professional before signing any agreement.

---

**Vidhi Setu** - _Clarity over contracts, grounded in Indian Law._
