# codespace-poc

An example Python project to demonstrate the use of GitHub Codespaces.

## Contents

- [codespace-poc](#codespace-poc)
  - [Contents](#contents)
  - [Overview](#overview)
  - [Project Scope](#project-scope)
  - [To Do List](#to-do-list)
    - [Getting Started](#getting-started)
      - [Local Running](#local-running)
    - [Codespace Running](#codespace-running)

## Overview

This repository contains a To Do List app, based in Python. The purpose of this repository is to investigate the use of GitHub Codespaces and demonstrate best practices when working with Python in ONS.

The repository contains the following features:

- Example To Do List App
- All required GitHub Housekeeping features, including the use of:
  - A README and /docs.
  - A Pull Request template, Issue template, CONTRIBUTING and CODE_OF_CONDUCT files.
  - LICENSE and SECURITY files.
  - A .gitignore and CODEOWNERS.
- GitHub Action Workflows for automated CI processes.
- A .devcontainer configuration for Codespace setup.

## Project Scope

- To evaluate the feasibility and effectiveness of using GitHub Codespaces for Python projects.
- To create a sample repository containing all best practices for Python development on GitHub.

## To Do List

### Getting Started

#### Local Running

1. Clone the repository:

    ```bash
    git clone https://github.com/ONSdigital/codespace-poc.git
    ```

2. Navigate to the project directory:

    ```bash
    cd codespace-poc
    ```

3. Install the required dependencies:

    ```bash
    poetry install
    ```

4. Run the application:

    ```bash
    poetry run streamlit run src/app.py
    ```

5. Open your web browser and navigate to `http://localhost:8501` to view the To Do List app.

### Codespace Running

1. Open the repository in GitHub Codespaces.
2. Wait for the Codespace to initialize and install the required dependencies.
3. Once the Codespace is ready, open a terminal in the Codespace.
4. Run the application:

    ```bash
    poetry run streamlit run src/app.py
    ```

5. Go to the Local URL provided in the terminal to view the To Do List app (cmd + click or ctrl + click).

### Linting, Formatting, and Testing

#### Linting and Formatting (Python)

To ensure code quality, this project uses Black, Flake8, Isort and Mypy for linting and formatting. You can run these tools using the following command:

```bash
make lint
```

#### Testing

To run the unit tests, you can use the following command:

```bash
make test
```

#### Security Checks

To run security checks, you can use the following command:

```bash
make security
```

#### Markdown Linting

To ensure the Markdown files are well-formatted, you can use the following command:

```bash
make md_lint
```

### GitHub Actions

This repository makes use of GitHub Actions for CI. Actions are available within `.github/workflows`.

The following Actions are available:

- `py_lint.yaml` | Python Linting
- `md_lint.yaml` | Markdown Linting
- `security.yaml` | Security Checks
- `testing.yaml` | Unit Testing

The above actions will run automatically on push and pull requests to the `main` branch, ensuring that code quality and security standards are maintained.
