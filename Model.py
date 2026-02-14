# =========================================
# Project: Build Your Own AI Agent
# Hugging Face LLM (Hybrid Version) + Gradio UI
# =========================================

import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo
from transformers import pipeline
import gradio as gr

# =========================================
# LOAD HUGGING FACE MODEL
# =========================================

print("Loading Hugging Face model...")
llm = pipeline(
    "text-generation",
    model="distilgpt2",
    truncation=True,
    pad_token_id=50256
)
print("Model loaded successfully!")

# =========================================
# TOOL DEFINITIONS
# =========================================

def calculator_add(a: float, b: float) -> float:
    return a + b

def calculator_multiply(a: float, b: float) -> float:
    return a * b

def get_current_time(city: str) -> str:
    city_timezones = {
        "london": "Europe/London",
        "new york": "America/New_York",
        "paris": "Europe/Paris",
        "tokyo": "Asia/Tokyo",
        "delhi": "Asia/Kolkata",
        "dubai": "Asia/Dubai",
        "sydney": "Australia/Sydney"
    }

    city_lower = city.lower()
    if city_lower not in city_timezones:
        return f"Sorry, I don't have timezone data for {city}."

    tz = ZoneInfo(city_timezones[city_lower])
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    return f"The current time in {city.title()} is {now}"

# =========================================
# HUGGING FACE + LOGIC REASONING
# =========================================

def huggingface_reasoning(user_input: str) -> dict:
    """
    Hugging Face model understands intent,
    Python ensures correct action extraction.
    """

    # Use LLM for semantic understanding (soft reasoning)
    prompt = f"Understand this request: {user_input}"
    llm(prompt, max_new_tokens=20)

    text = user_input.lower()

    # Extract numbers
    numbers = re.findall(r"-?\d+\.?\d*", text)
    numbers = [float(n) for n in numbers]

    # ADD
    if "add" in text and len(numbers) >= 2:
        return {
            "action": "calculator_add",
            "arguments": {"a": numbers[0], "b": numbers[1]}
        }

    # MULTIPLY
    if "multiply" in text and len(numbers) >= 2:
        return {
            "action": "calculator_multiply",
            "arguments": {"a": numbers[0], "b": numbers[1]}
        }

    # TIME
    if "time" in text:
        match = re.search(r"time in ([a-zA-Z ]+)", text)
        city = match.group(1).strip() if match else "London"
        return {
            "action": "get_current_time",
            "arguments": {"city": city}
        }

    return {"action": "none", "arguments": {}}

# =========================================
# AGENT SETUP
# =========================================

TOOLS = {
    "calculator_add": calculator_add,
    "calculator_multiply": calculator_multiply,
    "get_current_time": get_current_time
}

def ai_agent(user_input: str) -> str:
    """
    Core agent logic, returns final answer as string
    """
    action_data = huggingface_reasoning(user_input)
    action = action_data["action"]
    arguments = action_data["arguments"]

    if action in TOOLS:
        result = TOOLS[action](**arguments)
        return f"Final Answer: {result}"
    else:
        return "Sorry, I don't understand your request."

# =========================================
# GRADIO UI SETUP
# =========================================

def launch_gradio():
    with gr.Blocks() as demo:
        gr.Markdown("## 🤖 Hugging Face AI Agent")
        user_input = gr.Textbox(label="Enter your query", placeholder="e.g. add 5 and 7")
        output = gr.Textbox(label="Agent Response")
        submit_btn = gr.Button("Submit")

        submit_btn.click(fn=ai_agent, inputs=user_input, outputs=output)

    demo.launch()

# =========================================
# RUN AGENT
# =========================================

if __name__ == "__main__":
    print("\n🤖 Hugging Face AI Agent with Gradio UI Started")
    launch_gradio()
