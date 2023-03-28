# Chat with data POC

"chat with data" example using `Llama_index` library and OpenAI.

For this to work you need to setup OpenAI API key. It is free for the first 18$ worth of tokens!

Define env variable:
```
export OPENAI_API_KEY=""
```

Create the index for `server_documentation` data:

```
python create_index.py
```

Ask the index a question:

```
python ask_documentation.py

Ask a question: What software is Big Bank Server running?

- Apache HTTP Server version 2.4.51
- MySQL version 8.0.27
- PHP version 8.0.14
- Redis version 6.2.6
- Elasticsearch version 7.16.3
```

Please note, that this is not a full chat bot loop implementation. To read more about full "chat bot" implementation go to: https://gpt-index.readthedocs.io/en/latest/guides/building_a_chatbot.html