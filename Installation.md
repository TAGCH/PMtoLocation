# Prerequisites
Make sure you have Python 3.8, 3.9, 3.10, or 3.11 installed on your system.


# Installation steps

## 1. Clone repository

- Clone this repository to your local computer.

```
git clone https://github.com/TAGCH/PMtoLocation.git
```

## 2. Create file config.py
- Create config.py then put this code inside and please change DB_USER, DB_PASSWD and DB_NAME to your own.
```
OPENAPI_STUB_DIR = 'stub'
DB_HOST = 'iot.cpe.ku.ac.th'
DB_USER = 'Database User'
DB_PASSWD = 'Database Password'
DB_NAME = 'Database Name'
```

## 3. Generate python-flask
- Open [Swagger Editor](https://editor.swagger.io/)
- In file, click import file
- Select file PM.yaml
- In Generate Server, click python-flask
- Extract file that receive from download.

## 4. Create and insert file into stub folder
- Create stub folder
- Open the folder that extract from "Step 3"
- Drag all of item in the extract folder in to stub folder

## 5. Install requirement
Install by typing below code in your another terminal, cmd or powershell.
```
pip install -r requirements.txt
```
