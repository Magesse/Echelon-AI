
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

for model in genai.list_models():

    if "generateContent" in model.supported_generation_methods:

        print(model.name)
