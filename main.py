from misskey import Misskey
from setting import instance_address, access_token, google_api_json, spread_sheet_url
import gspread
import random

# authentication to misskey
misskey = Misskey(address=instance_address, i=access_token)

# authentication to google spread sheet
gc = gspread.service_account(google_api_json)


def writeRandomSentenceNote():
    # get all sentences
    sheet = gc.open_by_url(spread_sheet_url)
    work_sheet = sheet.get_worksheet(0)
    sentences = work_sheet.col_values(1)

    # choice random sentence
    sentence = random.choice(sentences)

    # write note
    random_sentence_note = misskey.notes_create(text=sentence)
    note_id = random_sentence_note["createdNote"]["id"]
    note_text = random_sentence_note["createdNote"]["text"]
    print(f"{note_id} | {note_text}")


if __name__ == "__main__":
    writeRandomSentenceNote()
