from misskey import Misskey
import random

from src.setting import instance_address, access_token
from src.choose_sentence import chooseSentence
from src.generate_sentence import generateSentence

# authentication to misskey
misskey = Misskey(address=instance_address, i=access_token)


def writeRandomSentenceNote():
    choice_methods = [
        chooseSentence,
        generateSentence
    ]

    # choose method and get sentence
    sentence: str = random.choice(choice_methods)()

    # change newline-character to be valid
    sentence = sentence.replace("\\n", "\n")

    # write note
    random_sentence_note = misskey.notes_create(text=sentence)
    note_id = random_sentence_note["createdNote"]["id"]
    note_text = random_sentence_note["createdNote"]["text"]
    print(f"{note_id} | {note_text}")


if __name__ == "__main__":
    writeRandomSentenceNote()
