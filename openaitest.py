import os
import openai
from config import apikey
openai.api_key= apikey


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "write an email to boss for  my resignation"
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
{
  "id": "chatcmpl-7ahYmLmfY6aS6Mk5E6zL0hybPIAeP",
  "object": "chat.completion",
  "created": 1688981608,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Dear [Boss's Name],\n\nI hope this email finds you well. I am writing to inform you of my decision to resign from my position at [company name]. Please consider this email as my official resignation letter, with my last working day being [date].\n\nI have carefully considered this decision and it was not made lightly. I have truly enjoyed my time at [company name] and the opportunities it has provided for my professional growth. I am grateful for the guidance, support, and valuable experiences I have gained during my tenure here.\n\nHowever, after careful thought and consideration, I have decided to pursue a new opportunity that aligns more closely with my long-term career goals. This decision was not easy for me, as I have developed strong relationships with my colleagues and have a great deal of respect for the work we do together. I am confident, though, that this change is the right move for me at this point in my career.\n\nI am committed to making this transition as smooth as possible. I am willing to assist with the handover of my responsibilities and projects to ensure a seamless transition for my successor. Please let me know how I can be of assistance during this period.\n\nI would like to take this opportunity to express my sincere gratitude to you and the entire team at"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 256,
    "total_tokens": 276
  }
}
'''
