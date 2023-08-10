from transformers import pipeline 
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

while True:
    prompt = input("Ask anything: (or type 'break' to exit) \n") 
    if prompt =="break":
        break
    res = generator((prompt), max_length=50, do_sample=True, temperature=0.8) 
    print(res[0]['generated_text'])
