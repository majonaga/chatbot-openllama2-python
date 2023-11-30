import replicate

training = replicate.trainings.create(
  version="meta/llama-2-7b:73001d654114dad81ec65da3b834e2f691af1e1526453189b7bf36fb3f32d0f9",
  input={
    # "train_data": "https://gist.githubusercontent.com/nateraw/055c55b000e4c37d43ce8eb142ccc0a2/raw/d13853512fc83e8c656a3e8b6e1270dd3c398e77/samsum.jsonl",
    "train_data": "https://replicate.delivery/pbxt/JxrmMON9snikjXFOknmwh6iHH0XRNirZXnpsOKlhRpfDuxAf/data.jsonl",
    "num_train_epochs": 3
  },
  destination="majonaga/llama2-refugio-test"
)

print(training)