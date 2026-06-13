# 🤖 The Agentic Testing Harness

An automated CI/CD evaluation pipeline that continuously audits an AI Agent's **accuracy** and **safety** using an LLM-as-a-judge framework. Built with Python, the Gemini API, and GitHub Actions.

Every time you push code or open a Pull Request, this harness forces the agent to complete a 50-question test suite. A secondary, highly advanced LLM Judge scores the outputs. If the overall score drops below **90%**, the pipeline fails, blocking unsafe or regressive code from merging.

---

## 🏗️ Architecture & Flow

1. **Developer Pushes Code:** A change is made to the agent's prompts or core logic.
2. **GitHub Actions Triggers:** The pipeline installs dependencies and sets up the environment securely.
3. **The Exam Begins:** The harness feeds 50 evaluation test cases to the Agent (`gemini-2.5-flash`).
4. **The Audit:** The Judge (`gemini-2.5-pro`) grades the agent's response against pre-defined strict accuracy or safety criteria.
5. **The Gateway:** The pipeline calculates the final score. $\text{Score} \ge 90\%$ passes; anything lower fails the build.

---

## 🛠️ Project Structure

```text
agentic-testing-harness/
├── .github/workflows/
│   └── eval-pipeline.yml  # GitHub Actions CI/CD pipeline
├── agent/
│   └── core.py            # Agent logic (powered by gemini-2.5-flash)
├── data/
│   └── test_cases.json    # 50 accuracy & safety test profiles
├── tests/
│   └── run_evals.py       # Evaluation framework & LLM Judge
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
