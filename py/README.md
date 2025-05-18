# 1. Create a virtual environment:

Windows:

```
py -m venv .venv
```

Unix/macOS:

```
python3 -m venv .venv
```

# 2. Activate a virtual environment:

Windows:

```
.venv\Scripts\activate
```

Unix/macOS:

```
source .venv/bin/activate
```

# 3. Install the required packages

```
pip install -r requirements.txt
```

# 4. Run

```
AWS_PROFILE=dixon python3 src/images/titan/generate.py
```

```
source deactivate
```
