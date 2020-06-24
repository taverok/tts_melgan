## install on ubuntu 18
- apt installs
```
sudo apt get update
sudo apt install gdown python3-pip
```
- clone repo and cd to project directory
- download weights
```
gdown --id 10Z_TLISbHEp0f4l4wlqV9J9Mp63XrSv -O weight/fastspeech-150k.h5
gdown --id 1TYk56ZyA3C3CA1fsFs8Hp9X-a-kJvZcx -O weight/melgan-1M6.h5
```
- pip installs
```
pip install ./tts_app/vendor/TenserflowTTS
pip install -r ./tts_app/requirements.txt
```
- run falsk
```$xslt
export FLASK_APP=app.py
flask run
```
