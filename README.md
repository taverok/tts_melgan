## install on ubuntu 18

- apt installs
```
sudo apt get update
sudo apt install python3-pip libsndfile1
pip3 install gdown
pip install -U pip
```

- clone repo and cd to project directory
- download weights
```
gdown --id 10Z_TLISbHEp0f4l4wlqV9J9Mp63XrSv- -O weight/fastspeech-150k.h5
gdown --id 1TYk56ZyA3C3CA1fsFs8Hp9X-a-kJvZcx -O weight/melgan-1M6.h5
```

- pip installs
```
pip3 install ./tts_app/vendor/TensorflowTTS/
pip3 install -r ./tts_app/requirements.txt
```

- run falsk
```
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=80
```
