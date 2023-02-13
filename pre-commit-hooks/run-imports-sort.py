try:
    import isort
    isort.file(".")
except ImportError:
    raise ImportError("Por favor instala isort https://pypi.org/project/isort/")