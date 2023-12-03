# Misskey Random Sentence Bot
## How to run
1. clone repo
2. make venv
```
python3 -m venv venv
source ./venv/bin/activate
```
3. install modules
```
pip install -r requirements.txt
```
4. change setting
```
# copy example setting file
cp setting_example.py setting.py

# edit setting file
vim setting.py
```
- `instance_address`: address of misskey instance that your bot will run
- `access_token`: API access token of your bot account
- `google_api_json`: your google api access json file
- `spread_sheet_url`: URL of spread sheet that include sentences as:

![](https://r2.worldc.one/media/fa04a9ba-e50e-4b63-81c3-73416f1481b7.webp)

5. RUN
```
python main.py
```