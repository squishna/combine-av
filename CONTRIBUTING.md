# Contributing to combine-av

Thank you for your interest in contributing! We welcome all types of help, including bug fixes, new features, and documentation improvements.

## How to Contribute

1.  **Fork the Repository**: Create your own copy of the project on GitHub.
2.  **Clone Locally**:
    ```bash
    git clone https://github.com/squishna/combine-av.git
    cd combine-av
    ```
3.  **Create a Branch**:
    ```bash
    git checkout -b feature/my-new-feature
    ```
4.  **Make Your Changes**: Ensure your code follows the existing style.
5.  **Run Tests**:
    ```bash
    export PYTHONPATH=$PYTHONPATH:.
    python3 -m unittest discover tests
    ```
6.  **Submit a Pull Request**: Explain your changes and why they're useful.

## Development Setup

We use `ruff` for linting. You can run it manually:
```bash
pip install ruff
ruff check src
```

---
Happy coding!
