
```uv add flake8```

```uv run flake8```

or

```uv run flake8 main.py```


## remove .venv/ files from flake8 linting

```uv run flake8 --exclude=.venv```


or 


touch .flake8

[flake8]
exclude =
    .venv,
    __pycache__


uv run flake8




