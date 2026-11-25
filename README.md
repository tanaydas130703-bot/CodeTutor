# CodeTutor

An interactive Python tutoring prototype exploring adjustable feedback detail.

## Project status

Implemented: three programming exercises, AST-based checking, adjustable feedback, attempt history, progress tracking and session reflection.

Simulated: AI tutoring behaviour using predefined rules.

Not implemented: live LLM integration, automatic personalisation and full user evaluation.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Testing

```bash
python -m unittest -v
```

## Technology

Python, Streamlit and the Python abstract syntax tree module.

## AI assistance

ChatGPT assisted with initial implementation, interface design and automated test creation. Local verification and development decisions must be documented before submission.
