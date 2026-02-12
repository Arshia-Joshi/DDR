import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_ddr_with_ollama(validated_data):

    structured_json = json.dumps(validated_data, indent=2)

    prompt = f"""
You are a structured diagnostic report generator.

You MUST use only the provided JSON.
You are NOT allowed to infer, reinterpret, or expand beyond it.

CRITICAL RULES:

1. For Severity:
   - Use analysis.severity.severity_level EXACTLY as written.
   - Use analysis.severity.severity_reasoning EXACTLY as written.
   - Do NOT change severity wording.

2. For Missing Information:
   - ONLY list items from validation.missing_information.
   - If the list is empty, write:
     "No major missing information identified."
   - DO NOT treat "N/A" values as missing unless listed in validation.

3. For Conflicts:
   - ONLY mention items from validation.conflicts.

4. Do NOT:
   - Add structural assumptions
   - Add engineering interpretations
   - Add new inspection checklist items
   - Add inferred risks
   - Duplicate sections

Follow EXACT structure once:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Structured JSON:
{structured_json}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "temperature": 0
        }
    )

    return response.json()["response"]
