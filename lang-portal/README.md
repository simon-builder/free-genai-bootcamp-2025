# Setup Backend

Navigate to backend

```
cd .\backend-fastapi\
```

Create a virtual environment

```
python -m venv venv
```

Activate the virtual environment

```
.\venv\Scripts\activate.ps1
```

Install dependencies

```
pip install -r requirements.txt
```

Run the FastAPI application

```
fastapi dev app/main.py
```

Check FastAPI docs for endpoint documentation

```
http://127.0.0.1:8000/docs
```


