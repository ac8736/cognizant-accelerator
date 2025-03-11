from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

print("Welcome to the Text Completion AI! Enter 'Exit' to quit.")
sequences = int(input("How sequences would you like to generate? "))
maxLength = int(input("What is the maximum length of each sequence? "))

while True:
    text = input("Enter a prompt: ")
    if text.lower() == "exit":
        break
    output = generator(text, max_length=maxLength, num_return_sequences=sequences, truncation=True)
    for i, sequence in enumerate(output):
        print(f"Generated text {i+1}: {sequence['generated_text']}")
