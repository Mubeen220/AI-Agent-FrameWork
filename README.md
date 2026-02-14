# AI-Agent-FrameWork
# 🤖 Hybrid AI Agent with Tool Usage

A modular AI agent built with **Python** and **Hugging Face** that interprets natural language commands to execute functional tools. This project demonstrates the implementation of an **Agentic Workflow**, bridging the gap between Generative AI (LLMs) and deterministic logic.

## 🚀 Overview
This agent accepts natural language queries (e.g., *"What is the time in Paris?"* or *"Add 5 and 22"*), identifies the user's intent, and autonomously selects the correct "tool" to perform the action. It features a **Gradio** user interface for real-time interaction.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Model:** Hugging Face `distilgpt2` (Transformers pipeline)
* **Interface:** Gradio (Web UI)
* **Logic:** Regex & `zoneinfo` for argument parsing and timezone handling

## ✨ Key Features
* **Tool Registry:** A scalable dictionary-based system allowing easy addition of new functions.
* **Hybrid Reasoning:** Combines LLM semantic processing with Pythonic logic for accurate argument extraction.
* **Multi-Timezone Support:** Real-time clock handling for major global cities using `ZoneInfo`.
* **Math Engine:** Safe calculation tools decoupled from the LLM to prevent hallucination.

## 📂 Project Structure
* `Model.py`: Contains the core agent loop, tool definitions, and Gradio launch code.
* `Project_Build_AI_Agent.ipynb`: Jupyter Notebook with development steps and documentation.

## 🔧 How to Run
1.  **Install Dependencies:**
    ```bash
    pip install transformers gradio torch
    ```
2.  **Run the Agent:**
    ```bash
    python Model.py
    ```
3.  **Access the UI:**
    Click the local URL provided in the terminal (e.g., `http://127.0.0.1:7860`).

## 📸 Usage Examples
| Query | Action Triggered | Result |
| :--- | :--- | :--- |
| *"Calculate time in Tokyo"* | `get_current_time` | Returns accurate Tokyo time |
| *"Multiply 50 by 10"* | `calculator_multiply` | Returns `500.0` |

---
*Created as part of a Master's project in Mechatronics & AI.*
