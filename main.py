import subprocess

memory = {
    "last_output": None
}

def ask_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()


def summarize(text):
    return ask_llm(
        f"Summarize the following email in ONE short sentence. Do not rewrite it.\n\n{text}"
    )


def generate_reply(text):
    return ask_llm(
        f"Write a short, polite, and professional reply (max 3 sentences). Do not repeat the original email.\n\n{text}"
    )


def improve_tone(text):
    return ask_llm(
        f"Rewrite this message to be more formal and professional. Keep it concise.\n\n{text}"
    )


def analyze_email_ai(text):
    return ask_llm(
        f"""Analyze this email and provide:
1. Intent
2. Urgency (low, medium, high)
3. Action items

Keep it short.

{text}
"""
    )


def analyze_urgency_rules(text):
    text = text.lower()

    if "not urgent" in text or "no rush" in text:
        return "Low"

    high_keywords = [
        "urgent", "asap", "as soon as possible",
        "immediately", "right away", "without delay"
    ]

    medium_keywords = [
        "soon", "shortly", "in the near future",
        "before long", "in the next few days",
        "at your earliest convenience"
    ]

    for word in high_keywords:
        if word in text:
            return "High"

    for word in medium_keywords:
        if word in text:
            return "Medium"

    return "Low"


def compare_analysis(text):
    rule_result = analyze_urgency_rules(text)
    ai_result = analyze_email_ai(text)

    return f"""Rule-based urgency: {rule_result}

AI Analysis:
{ai_result}
"""


def evaluate_reply(text):
    reply = generate_reply(text)

    evaluation = ask_llm(
        f"""Evaluate the following email reply:
- Is it polite?
- Is it clear?
- Can it be improved?

Reply:
{reply}
"""
    )

    return f"""Generated Reply:
{reply}

Evaluation:
{evaluation}
"""


def improve_last_output():
    if memory["last_output"]:
        return ask_llm(
            f"Improve this text to be more professional and clear:\n\n{memory['last_output']}"
        )
    else:
        return "No previous output found."


def main():
    print("📧 AI Email Assistant (Advanced)\n")

    user_input = input("Paste your email:\n")
    current_input = user_input

    while True:
        print("\nCurrent input:")
        print("-------------------------")
        print(current_input[:200] + ("..." if len(current_input) > 200 else ""))
        print("-------------------------")

        print("\nChoose an option:")
        print("1. Summarize")
        print("2. Generate Reply")
        print("3. Improve Tone")
        print("4. Analyze Email (AI)")
        print("5. Compare AI vs Rules")
        print("6. Evaluate Reply")
        print("7. Improve Last Output (Memory)")
        print("8. Use Last Output as New Input")
        print("0. Exit")

        choice = input("\nEnter number: ")

        print("\n-------------------------")

        if choice == "1":
            output = summarize(current_input)
            print("📌 SUMMARY\n")
            print(output)

        elif choice == "2":
            output = generate_reply(current_input)
            print("✉️ REPLY\n")
            print(output)

        elif choice == "3":
            output = improve_tone(current_input)
            print("📝 IMPROVED VERSION\n")
            print(output)

        elif choice == "4":
            output = analyze_email_ai(current_input)
            print("🧠 AI ANALYSIS\n")
            print(output)

        elif choice == "5":
            output = compare_analysis(current_input)
            print("⚖️ AI vs RULES\n")
            print(output)

        elif choice == "6":
            output = evaluate_reply(current_input)
            print("🔍 REPLY EVALUATION\n")
            print(output)

        elif choice == "7":
            output = improve_last_output()
            print("♻️ IMPROVED LAST OUTPUT\n")
            print(output)

        elif choice == "8":
            if memory["last_output"]:
                current_input = memory["last_output"]
                print("✅ Now using last output as new input.")
            else:
                print("❌ No previous output found.")
            continue

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")
            continue

        memory["last_output"] = output

        print("\n-------------------------")


if __name__ == "__main__":
    main()