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
- OpenAI API key is optional for preview mode, required for real API measurements.
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
export OPENAI_API_KEY="your-key"
export OPENAI_MODEL="gpt-4.1-mini"
```
Optional pricing overrides:
```bash
export INPUT_PRICE_PER_MILLION="0.40"
export OUTPUT_PRICE_PER_MILLION="1.60"
```
The notebook defaults to the published GPT-4.1 mini standard rates checked 31 Oct 2026. Verify model availability and rates before execution/submission:
https://developers.openai.com/api/docs/models/gpt-4.1-mini
https://developers.openai.com/api/docs/pricing

## Run
```bash
jupyter notebook
```
Open `EduAssist_LLMOps_Assignment2.ipynb` and run all cells from top to bottom. With `OPENAI_API_KEY` set, it makes 15 live calls (3 prompt versions × 5 questions). Without the key, it runs in preview mode; preview values are not live measurements.

## MLflow UI
In another terminal:
```bash
mlflow ui --backend-store-uri ./mlruns --port 5000
```
Open http://127.0.0.1:5000 and select experiment `eduassist_llmops_assignment`. Inspect the three prompt runs and their metrics. If your MLflow version supports GenAI Prompt Registry, inspect the three successive versions under the `eduassist_academic_qa` prompt name and the `production` alias. The notebook prints registry status; do not assume alias creation succeeded without confirmation.

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
- API: OpenAI Responses API via the official Python SDK.
- Model default: `gpt-4.1-mini`.
- Currency: USD.
- Pricing reference date: 31 October 2026; rates are configurable and must be rechecked before final submission.
