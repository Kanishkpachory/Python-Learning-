from mgp_repo import OpenAI
client = OpenAI()

command ='''
Copied Text: __Jiya ___, 12 Feb 2023, 17:26
Jana h
Pr mn ni kra

You, 12 Feb 2023, 17:27
kis ke sath or kaha

__Jiya ___, 12 Feb 2023, 17:28
Akele hi
No option

You, 12 Feb 2023, 17:30
Any reason to go

__Jiya ___, 12 Feb 2023, 17:30
Eyebrows

You, 12 Feb 2023, 17:31
Go fast

__Jiya ___, 12 Feb 2023, 17:31
going

'''
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a person named kanishk who speaks hindi as well as english . He is from India and is a coder .You analyze the chat history and respond like kanishk ."},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message)