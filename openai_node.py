from openai import OpenAI
import uuid

class OpenAI_API:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "1girl"
                }),
                "api_url": ("STRING", {
                    "multiline": False,
                    "default": "https://api.openai.com/v1/completions"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "model": ("STRING", {
                    "multiline": False,
                    "default": "gpt-4o-0806"
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.1,
                    "round": 0.01,
                    "display": "number"
                }),
                "top_p": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1,
                    "round": 0.01,
                    "display": "number"
                }),
                "frequency_penalty": ("FLOAT", {
                    "default": 0.0,
                    "min": -2.0,
                    "max": 2.0,
                    "step": 0.1,
                    "round": 0.01,
                    "display": "number"
                }),
                "presence_penalty": ("FLOAT", {
                    "default": 0.0,
                    "min": -2.0,
                    "max": 2.0,
                    "step": 0.1,
                    "round": 0.01,
                    "display": "number"
                }),
                "sys_prefix": ("STRING", {
                    "multiline": True,
                    "default": "You are a prompt generation AI. your task is to take a user input for a flux.1-dev diffusion prompt and output and expand the supplied prompt in a difusion format to provide better output. Do not deviate from the format. Do not output anything other than a diffusion prompt."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "get_completion"

    CATEGORY = "api/openai"

    def get_completion(self, prompt, api_url, api_key, sys_prefix, temperature, top_p, frequency_penalty, presence_penalty, model):
        client = OpenAI(
            api_key=api_key,
            base_url=api_url,
        )

        unique_request_id_sq = str(uuid.uuid4())
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "x-ms-client-request-id": unique_request_id_sq,
        }

        messages = [{"role": "system", "content": sys_prefix},{"role": "user", "content": prompt}]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty = presence_penalty,
            stream=False,
            extra_headers=headers
        )

        return (response.choices[0].message["content"],)
