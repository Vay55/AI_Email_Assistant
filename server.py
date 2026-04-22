from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import re

memory = {
    "last_output": None
}

app = Flask(__name__)
CORS(app)

import re

def clean_output(text):
    #random terminal characters
    text = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', text)

    #repeating words ykwim
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)

    # random newlines
    text = text.replace("\n", " ")

    return text.strip()


def ask_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    cleaned = clean_output(result.stdout)

    cleaned = cleaned.split("\n\n")[0]

    return cleaned


def summarize(text):
    return ask_llm(
        f"""Summarize this email in ONE short sentence.

STRICT RULES:
- No greetings
- No reply
- No extra text
- No repetition
- Output ONLY the sentence

Email:
{text}
"""
    )


def generate_reply(text):
    return ask_llm(
        f"""Write a short, polite, professional reply (max 2 sentences).

STRICT RULES:
- Do NOT use "Dear"
- Do NOT use placeholders like [Name]
- Do NOT repeat words
- Keep it natural and concise
- Output ONLY the reply

Email:
{text}
"""
    )

def analyze_intent(text):
    return ask_llm(
        f"""Analyze the tone of this email.
Classify it as:
- Polite
- Neutral
- Rude

Also briefly explain why in one short line.

Email:
{text}
"""
    )

def analyze_urgency(text):
    text_lower = text.lower()

    high_keywords = [
        "urgent", "asap", "as soon as possible",
        "immediately", "right away", "without delay",
        "quick", "fast"
    ]

    medium_keywords = [
        "soon", "shortly", "in the near future",
        "before long", "in the next few days",
        "at your earliest convenience", "by the end of this week"
    ]

    found = []

    for word in high_keywords:
        if word in text_lower:
            found.append(word)

    for word in medium_keywords:
        if word in text_lower:
            found.append(word)

    if any(word in text_lower for word in high_keywords):
        level = "High"
    elif any(word in text_lower for word in medium_keywords):
        level = "Medium"
    else:
        level = "Low"

    return f"Urgency: {level}\nKeywords found: {', '.join(found) if found else 'None'}"

def improve_tone(text):
    return ask_llm(
        f"""Rewrite this message to be more polite and professional.

STRICT RULES:
- No greetings
- No placeholders
- No repetition
- Fix any broken sentences
- Keep meaning the same
- Output ONLY the improved text

Message:
{text}
"""
    )


@app.route("/summarize", methods=["POST"])
def summarize_route():
    data = request.json
    result = summarize(data["text"])
    memory["last_output"] = result 
    return jsonify({"result": result})


@app.route("/reply", methods=["POST"])
def reply_route():
    data = request.json
    result = generate_reply(data["text"])
    memory["last_output"] = result 
    return jsonify({"result": result})

@app.route("/intent", methods=["POST"])
def intent_route():
    data = request.json
    result = analyze_intent(data["text"])
    memory["last_output"] = result 
    return jsonify({"result": result})

@app.route("/urgency", methods=["POST"])
def urgency_route():
    data = request.json
    result = analyze_urgency(data["text"])
    memory["last_output"] = result 
    return jsonify({"result": result})

@app.route("/improve", methods=["POST"])
def improve_route():
    data = request.json
    result = improve_tone(data["text"])
    memory["last_output"] = result 
    return jsonify({"result": result})

@app.route("/last", methods=["GET"])
def get_last():
    if memory["last_output"]:
        return jsonify({"result": memory["last_output"]})
    else:
        return jsonify({"result": "No previous output found."})


if __name__ == "__main__":
    app.run(debug=True)

