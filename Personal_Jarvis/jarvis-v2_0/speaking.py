from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import random
import string
import soundfile as sf

device = "cuda" if torch.cuda.is_available() else "cpu"

# load the processor
print("loading the processor")
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")

# load the model
print("loading the model")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts").to(device)

# load the vocoder, that is the voice encoder
print("loading the vocoder, that is the voice encoder")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan").to(device)

# we load this dataset to get the speaker embeddings
print("we load this dataset to get the speaker embeddings")
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")


def save_text_to_speech(text, speaker=None):
    # preprocess text
    inputs = processor(text=text, return_tensors="pt").to(device)
    print('test1')
    if speaker is not None:
        # load xvector containing speaker's voice characteristics from a dataset
        print('test3')
        speaker_embeddings = torch.tensor(embeddings_dataset[speaker]["xvector"]).unsqueeze(0).to(device)
        print('test4')
    else:
        # random vector, meaning a random voice
        speaker_embeddings = torch.randn((1, 512)).to(device)
    # generate speech with the models
    try:
        print('test5')
        speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
        print('test6')
        if speaker is not None:
            # if we have a speaker, we use the speaker's ID in the filename
            output_filename = "output_wav_files/answer.mp3"
            print('test7')
        else:
            # if we don't have a speaker, we use a random string in the filename
            # random_str = ''.join(random.sample(string.ascii_letters+string.digits, k=5))
            output_filename = "output_wav_files/answer.mp3"
        # save the generated speech to a file with 16KHz sampling rate
        sf.write(output_filename, speech.cpu().numpy(), samplerate=16000)
        print('test8')
    except RuntimeError as e: 
        # logger.debug(f'{e}')
        print(f'{e}')
    # return the filename for reference
    return output_filename



