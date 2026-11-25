# CodeTutor

An interactive Python tutoring prototype exploring adjustable feedback detail.

Approximate prose word count: 340 (excluding headings and commands).

## Project Overview

CodeTutor is a Python learning assistant developed for my Intelligent Interactive Systems assignment. The idea came from my A1 literature review, where I looked at how the level of detail in chatbot responses could affect cognitive load and task performance.

The system allows users to complete basic Python exercises and choose between concise and detailed feedback.

## Project Status

- **Implemented:** Three programming exercises, AST-based checking, adjustable feedback, attempt history, progress tracking and session reflection.
- **Simulated:** AI tutoring behaviour using predefined rules.
- **Not implemented:** Live language model integration, automatic personalisation and formal user evaluation.

## Current Features

- Three exercises covering functions, conditionals and loops.
- Concise and detailed feedback options.
- Feedback based on the structure of submitted Python code.
- Progress tracking and attempt history.
- Mental effort ratings and feedback preferences.
- An option to reset the session.

## How to Run

Run the following commands from the project directory:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    python -m streamlit run app.py

## Development Decisions

I decided to keep the prototype focused on feedback detail rather than building a general-purpose chatbot. This made it easier to compare the two feedback styles while keeping the exercises and feedback structure consistent.

The prototype uses Python's abstract syntax tree (AST) module to examine submitted code without executing it. Predefined rules are used to simulate the behaviour of an AI tutor.

The initial implementation is recorded in commit `11e3786`.

## Testing

Six automated tests were run successfully on my Mac. These covered supported solutions, missing return statements, syntax errors, alternative solutions, empty submissions and differences in feedback detail.

I also ran the Streamlit application locally and checked the feedback and correction process.

To run the automated tests:

    python -m unittest -v

## Limitations

The system does not use a live language model and cannot recognise every correct Python solution. Session information is temporary, and feedback detail is selected manually by the user.

A future version could include a language model, more exercises and automatic adjustment of feedback based on the user's experience.

## AI Assistance

I used ChatGPT to help develop the initial code, organise the interface and prepare automated tests. I ran the application and tests locally and checked the interaction myself.
## Technologies

Python, Streamlit, AST and unittest.