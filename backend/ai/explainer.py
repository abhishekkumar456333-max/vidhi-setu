import os
import requests

HF_API_TOKEN = os.getenv("HF_API_KEY")
HF_MODEL_ID = "microsoft/phi-3-mini-4k-instruct"
HF_ENDPOINT = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"

def explain_flag(flag_data: dict) -> str:
    default_response = (
        f"This clause poses a potential risk under {flag_data['law']} "
        f"({flag_data['section']}) due to {flag_data['reason']}."
    )

    if not HF_API_TOKEN:
        return default_response

    legal_prompt = f"""
    You are a legal assistant explaining Indian contract law to a layman.
    
    Context:
    Act: {flag_data['law']}
    Section: {flag_data['section']}
    Reason for flag: {flag_data['reason']}
    
    Provide a 2-3 sentence explanation of why this is a risk.
    Do not offer specific legal advice. Keep it simple.
    """

    request_payload = {
        "inputs": legal_prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.2,
            "return_full_text": False
        }
    }

    try:
        api_response = requests.post(
            HF_ENDPOINT,
            headers={"Authorization": f"Bearer {HF_API_TOKEN}", "Content-Type": "application/json"},
            json=request_payload,
            timeout=10
        )

        if api_response.status_code != 200:
            return default_response

        data = api_response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"].strip()

        return default_response

    except Exception:
        return default_response
