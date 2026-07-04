import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found!")

genai.configure(api_key=API_KEY)

def get_best_model():
    try:
        models = [m.name for m in genai.list_models() 
                 if 'generateContent' in m.supported_generation_methods]
        print(f"✅ Models available: {models}")
        
        priority = ['gemini-1.5-flash', 'gemini-2.0-flash', 'gemini-pro']
        for p in priority:
            for model in models:
                if p in model:
                    return model
        return models[0] if models else "gemini-pro"
    except:
        return "gemini-1.5-flash"

model_name = get_best_model()
print(f"🚀 Using: {model_name}")

model = genai.GenerativeModel(model_name)
response = model.generate_content("Tulis 1 ide produk digital untuk pemula.")

with open("produk_terbaru.md", "w", encoding="utf-8") as f:
    f.write("# Ide Produk Digital\n\n")
    f.write(response.text)

print("✅ Done!")
