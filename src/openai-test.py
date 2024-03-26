from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert on textiles and garments production and export."},
        {"role": "user", "content": "I could not deliver on time, what will happen"}
    ]
)

print(completion.choices[0].message)