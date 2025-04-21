# Simple phone recognition service

## Install requirements

```commandline
pip3 install -r requirements.txt
```

## Download phones data

do to https://opendata.digital.gov.ru/registry/numeric/downloads and download files in some folder.

set env variable with loaded filenames like this:

```commandline
export PHONES_DATA_FILENAMES=/Users/.../DEF-9xx.csv,/Users/.../ABC-4xx.csv,/Users/.../ABC-8xx.csv,/Users/.../ABC-3xx.csv
```

## Run backend

```commandline
cd src/phone_number_recognizer
python3 manage.py runserver 8000
```

## Front

```commandline
cd src/front
python3 -m http.server 8845
```

Open browser on `localhost:8845` and you'll see form)