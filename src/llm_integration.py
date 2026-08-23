# LLM APIs & Prompt Engineering (Phase 4)

## LLM API Basics
```python
# Using OpenAI API (compatible with most LLM providers)
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what is machine learning in 2 sentences."}
    ]
)

print(response.choices[0].message.content)
```

## Conversations with Memory
```python
class ChatWithMemory:
    def __init__(self, system_prompt):
        self.messages = [{"role": "system", "content": system_prompt}]

    def ask(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages,
            max_tokens=500,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

bot = ChatWithMemory("You're a Python tutor.")
print(bot.ask("What is the difference between lists and tuples?"))
print(bot.ask("Can you give a coding example?"))
```

## Prompt Engineering Essentials
- **Zero-shot:** Direct instruction without examples
- **Few-shot:** Include 2–3 examples before querying
- **Chain-of-Thought:** Ask model to "think step by step"
- **Temperature:** Lower (0.2) = deterministic, Higher (0.8) = creative
- **Max Tokens:** Controls response length; watch token limits

## Token Management
```python
import tiktoken

def count_tokens(text, model="gpt-4o-mini"):
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    return len(tokens), enc.decode(tokens[:5])  # Sample first 5 tokens

n, sample = count_tokens("Hello, how are you?")
print(f"Token count: {n}, Sample tokens: {sample}")
```

## Exercises
1. Build a simple Q&A bot for a personal knowledge base
2. Implement a few-shot prompt classifier for sentiment analysis
3. Add token counting and truncation to your chat memory

**Goal**: Integrate modern LLMs into AI applications with robust prompting