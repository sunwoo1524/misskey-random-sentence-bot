from src.setting import google_api_json, spread_sheet_url
import gspread, random

# authentication to google spread sheet
gc = gspread.service_account(google_api_json)


# choose random sentence in google spread sheet
def chooseSentence() -> str:
    # get all sentences
    sheet = gc.open_by_url(spread_sheet_url)
    work_sheet = sheet.get_worksheet(0)
    sentences = work_sheet.col_values(1)

    # choice random sentence
    return random.choice(sentences)
