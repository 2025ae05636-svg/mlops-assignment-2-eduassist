# EduAssist AI — LLMOps Assignment 2

## Contents
- `EduAssist_LLMOps_Assignment2.ipynb` — executable notebook (live API mode or clearly labelled preview mode)
- `latency_tokens_cost.csv` — 15-row sample preview; replace by rerunning notebook with API key
- `prompt_evaluation_results.csv` — per-prompt sample preview; replace after live run
- `outputs/sample_responses.csv` — sample output records
- `report.pdf` — 500–700 word report
- `requirements.txt` — Python dependencies
- `screenshots/` — add genuine screenshots from your MLflow UI after a live run

## Environment
- Python 3.11 or newer recommended
- Required libraries are listed in `requirements.txt`
- Groq API key is optional for preview mode, required for real API measurements.
- Never hard-code or commit the API key.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\\Scripts\\activate     # Windows
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Set the key in the shell (do not put it in the notebook):
```bash
export GROQ_API_KEY="your-key"
export GROQ_MODEL="llama-3.1-8b-instant"
```
Optional pricing overrides:
```bash
export INPUT_PRICE_PER_MILLION="0.05"
export OUTPUT_PRICE_PER_MILLION="0.08"
```
The notebook defaults to Groq llama-3.1-8b-instant rates checked 2 Nov 2026. Verify current rates before submission:
https://groq.com/pricing

## Run
```bash
jupyter notebook
```
Open `EduAssist_LLMOps_Assignment2.ipynb` and run all cells from top to bottom. With `GROQ_API_KEY` set, it makes 15 live calls (3 prompt versions × 5 questions). Without the key, it runs in preview mode; preview values are not live measurements.

## MLflow UI
In another terminal (run from the repo folder):
```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001
```
Open http://127.0.0.1:5001 and select experiment `eduassist_llmops_assignment`. Inspect the three prompt runs and their metrics. Inspect the three versions under the `eduassist_academic_qa` prompt name and the `production` alias in the Prompt Registry tab.

## Screenshots to capture
After a successful live run, save genuine screenshots in `screenshots/`:
1. MLflow experiment with all three runs and metrics.
2. Prompt Registry showing v1, v2, and v3.
3. Prompt comparison/commit history or diff evidence.
4. v3 `production` alias.
5. Any evaluation metric detail needed to substantiate the report.

Do not submit fabricated screenshots. Preview mode is for development only; rerun live and replace the CSV outputs before final submission.

## Output formulas
Input cost = input tokens / 1,000,000 × input USD price per million  
Output cost = output tokens / 1,000,000 × output USD price per million  
Request cost = input cost + output cost  
Monthly projection = average request cost × 10,000

## API and pricing notes
- API: Groq API via the official Groq Python SDK.
- Model default: `llama-3.1-8b-instant`.
- Currency: USD.
- Pricing reference date: 2 November 2026; rates are configurable and must be rechecked before final submission.
