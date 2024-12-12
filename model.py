import torch
import re
import textwrap
from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer

device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')

model = GPT2LMHeadModel.from_pretrained(
    'sberbank-ai/rugpt3small_based_on_gpt2',
    output_attentions=False,
    output_hidden_states=False,
)

model.to('cpu')
model.load_state_dict(torch.load('model_weights.pt', map_location=torch.device('cpu')))


def get_prediction(prompt):
    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = model.generate(
        input_ids=prompt,
        max_length=70,
        num_beams=5,
        do_sample=True,
        temperature=1.3,
        top_k=50,
        top_p=0.7,
        no_repeat_ngram_size=2,
        num_return_sequences=10,
    ).cpu().numpy()
    for out_ in out:
        txt = textwrap.fill(tokenizer.decode(out_))
        txt = re.sub("\n", " ", txt)
        if 'рожден' not in txt:
            prediction = '.'.join(txt.split('.')[:-1]) + '.'
            return prediction
            break