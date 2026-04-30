# AI Email Assistant

## Overview

This project is an AI-powered email assistant designed to help users process and respond to emails more efficiently. It integrates a local Large Language Model (LLM) using Ollama and provides both a command-line interface and a web-based interface for interacting with the system.

The assistant performs multiple tasks such as summarization, reply generation, tone improvement, and email analysis, while supporting multi-step workflows and memory reuse.

---

## DEMO

[![App_video](EmailAI.mp4)](https://github.com/user-attachments/assets/34cd484a-f454-409a-94b0-c2fa1ec65934)

---

## Why I Built This

I built this project to explore how large language models can be integrated into real-world productivity tools. I was particularly interested in how prompt design, system structure, and output handling affect the quality and reliability of AI-generated responses.

This project also allowed me to experiment with transitioning from a simple CLI-based system to a full-stack web application.

---

## Features

### Core Features

* **Email Summarization**
  Generates a clear, one-sentence summary of long emails.

* **Reply Generation**
  Produces short, polite, and professional responses.

* **Tone Improvement**
  Rewrites messages to sound more formal and concise.

---

### Advanced Features

* **Email Intent Analysis**
  Identifies:

  * Intent (what the sender wants)
  * Key action points

* **Urgency Detection**
  Determines urgency level using:

  * AI-based reasoning
  * Rule-based keyword detection

* **Hybrid Reasoning (AI vs Rule-Based)**
  Compares LLM-generated analysis with rule-based logic to highlight differences in interpretation.

* **Stateful Memory System**
  Stores the last output so it can be reused or refined.

* **Multi-Step Workflows**
  Outputs can be reused as new inputs, enabling iterative transformations (e.g., generate → improve → summarize).

---

## Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **LLM Runtime:** Ollama
* **Model:** Phi-3 (with optional support for Llama 3)

---

## Project Structure

```bash
ai-email-assistant/
│
├── server.py        # Flask backend (LLM calls)
├── index.html       # Frontend UI
├── script.js        # Frontend logic 
├── main.py          # CLI testing environment for LLM
└── README.md
```

---

## About `main.py`

`main.py` was used as a **testing file in the terminal** to evaluate the capabilities of the LLM before implementing it in a web application.

It includes:

* Early versions of all features
* A menu-based CLI system
* Prompt experimentation and testing

This step was important to validate functionality and refine prompts before integrating the system into Flask and the frontend UI.

---

## How to Run

### 1. Install Ollama

https://ollama.com

---

### 2. Run a Model

```bash
ollama run phi3
```

---

### 3. Start the Backend

```bash
python3 server.py
```

---

### 4. Open the Application

Open `index.html` in your browser.

---

## Example Workflow

1. Paste an email
2. Generate a reply
3. Improve the tone
4. Reuse the output as new input
5. Summarize the result

This demonstrates a **multi-step AI pipeline** rather than a single one-time response.

---

## Experiments and Observations

### 1. Prompt Specificity

* Vague prompts led to incorrect behavior (e.g., rewriting instead of summarizing)
* Adding constraints like “one sentence” significantly improved output quality

### 2. Output Stability

* Smaller models sometimes produced repetition or formatting issues
* Post-processing (cleaning output) improved reliability

### 3. Rule-Based vs AI Reasoning

* Rule-based systems are consistent but limited
* LLMs handle context better but may vary in output
* Combining both provides more insight into system behavior

### 4. Multi-Step Processing

* Reusing outputs enables more advanced workflows
* Demonstrates how LLMs can be chained instead of used once

---

## Limitations

* The model does not learn over time (no persistent training)
* Output quality depends heavily on prompt design
* Smaller models may produce unstable or repetitive outputs
* Rule-based logic is limited to predefined keywords

---

## Future Improvements

* Deploy the application online
* Add persistent memory (database storage)
* Improve UI/UX further
* Support multiple tones (casual, formal, strict)
* Add email classification (spam, priority, etc.)
* Upgrade to more advanced models

---

## Conclusion

This project demonstrates how LLMs can be integrated into structured systems to perform useful real-world tasks. By combining prompt engineering, rule-based logic, output processing, and multi-step workflows, the assistant goes beyond simple text generation to provide more controlled and practical functionality.

---

## Status

✔ Completed
✔ Fully functional
✔ Available on GitHub

