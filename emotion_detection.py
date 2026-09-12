import requests
def emotion_detector(text_to_analyze):
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
               #"Content-Type": "application/json"
              }

    body = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=body,
            timeout=30
        )   

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

    return response.text

if __name__ == "__main__":
    result = emotion_detector("I love this new technology.")
    print(result)