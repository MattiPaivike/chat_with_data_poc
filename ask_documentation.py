from llama_index import QuestionAnswerPrompt, GPTSimpleVectorIndex

question = input("Ask a question: ")

QA_PROMPT_TMPL = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question in bullet point format with a new line after each point and cross reference any data cited in the document.\n"
    "warn the user if any information seems off: {query_str}\n"
)

QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

index = GPTSimpleVectorIndex.load_from_disk('index.json')

response = index.query(
    question,
    text_qa_template=QA_PROMPT
)

print(response.response)

# use this to get the source for the document:
#print(response.get_formatted_sources())