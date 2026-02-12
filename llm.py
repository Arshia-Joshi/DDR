import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_ddr_with_ollama(validated_data):

    structured_json = json.dumps(validated_data, indent=2)

    prompt = f"""
Generate a Detailed Diagnostic Report (DDR) using ONLY the structured data provided below.

Rules:
- Do NOT invent facts.
- If information is missing, write "Not Available".
- Mention conflicts clearly if present.
- Use simple, client-friendly language.

Follow EXACT structure:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information(explicitly mention “Not Available” if needed)

Structured Data:
{structured_json}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
