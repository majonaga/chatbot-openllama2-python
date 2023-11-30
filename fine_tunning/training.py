import replicate

training = replicate.trainings.create(
  version="meta/llama-2-13b-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
  input={
    "train_data": "https://raw.githubusercontent.com/majonaga/chatbot-openllama2-python/main/fine_tunning/data.jsonl",
  },
  destination="majonaga/llama2-refugio-test"
)

print(training)