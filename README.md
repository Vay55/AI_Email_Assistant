# AI Email Assistant

## Overview

This project is an AI-powered command-line email assistant that helps users process and respond to emails more efficiently. It uses a local large language model (LLM) to perform multiple tasks such as summarization, reply generation, tone improvement, and email analysis.

---

## Why I Built This

I built this project to explore how large language models can be integrated into real-world productivity tools. I was particularly interested in how prompt design and system structure affect the quality and reliability of AI outputs.

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
  * Urgency level (low, medium, high)
  * Action items

* **Hybrid Reasoning (AI vs Rule-Based)**
  Compares LLM-based urgency detection with a rule-based keyword system to highlight differences in reasoning.

* **Self-Evaluation System**
  The AI evaluates its own generated replies for clarity, tone, and possible improvements.

* **Stateful Memory System**
  Stores the last output so it can be reused or refined.

* **Multi-Step Workflows**
  Outputs can be reused as new inputs, enabling iterative transformations (e.g., generate → improve → summarize).

---

## Tech Stack

* Python
* Ollama (local LLM runtime)
* Phi-3 model
* Command Line Interface (CLI)

---

## How to Run

1. Install Ollama:
   https://ollama.com

2. Pull and run the model:

   ```bash
   ollama run phi3
   ```

3. Run the application:

   ```bash
   python3 main.py
   ```

---

## Example Workflow

1. Paste an email
2. Generate a reply
3. Improve the tone
4. Reuse the output as new input
5. Summarize the result

This demonstrates a multi-step AI pipeline rather than a single one-time response.

---

## Experiments and Observations

### 1. Prompt Specificity

* Vague prompts led to incorrect behavior (e.g., rewriting instead of summarizing)
* Adding constraints like “one sentence” significantly improved output quality

### 2. Tone and Length Control

* Without constraints, replies were inconsistent
* Specifying tone and sentence limits produced more realistic outputs

### 3. Rule-Based vs AI Reasoning

* Rule-based systems are consistent but limited
* LLMs handle context better but may vary in output
* Combining both provides useful insights into system behavior

### 4. Self-Evaluation

* The model can critique its own responses
* This enables a feedback loop for improving output quality without retraining

---

## Limitations

* The model does not learn over time (no persistent training)
* Rule-based logic is limited to predefined keywords
* Output quality depends heavily on prompt design

---

## Future Improvements

* Convert to a web application (Streamlit)
* Add persistent memory (file/database storage)
* Support multiple tones (casual, friendly, strict)
* Add email classification (spam, important, etc.)

---

## Conclusion

This project demonstrates how LLMs can be integrated into structured systems to perform useful real-world tasks. By combining prompt engineering, rule-based logic, and multi-step workflows, the assistant surpasss simple text generation to provide more intelligent and flexible functionality.
