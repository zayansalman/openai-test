from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert on textiles and garments production and export."},
        {"role": "user", "content": "what is the recommended method for dyeing"}
    ]
)

print(response.choices[0].message)