# GitHub Codespaces PoC

## Overview

This repository contains a To Do List app, based in Python. The purpose of this repository is to investigate the use of GitHub Codespaces and demonstrate best practices when working with Python in ONS.

## Contents

- [GitHub Codespaces PoC](#github-codespaces-poc)
  - [Overview](#overview)
  - [Contents](#contents)
  - [Tech Stack](#tech-stack)
  - [Project Scope](#project-scope)
  - [Output](#output)
  - [Getting Started](#getting-started)
    - [Codespace Running (Recommended)](#codespace-running-recommended)
    - [Local Running](#local-running)
      - [With Devcontainer](#with-devcontainer)
      - [Without Devcontainer](#without-devcontainer)
  - [Linting, Formatting, and Testing](#linting-formatting-and-testing)
    - [Linting and Formatting (Python)](#linting-and-formatting-python)
    - [Testing](#testing)
    - [Security Checks](#security-checks)
    - [Markdown Linting](#markdown-linting)
  - [GitHub Actions](#github-actions)

## Tech Stack

The project uses Streamlit for the web application, Poetry for dependency management, and includes various tools for linting, formatting, and testing to ensure code quality. These include:

- **Black** for code formatting
- **Flake8** for linting
- **Isort** for import sorting
- **Mypy** for type checking
- **Pytest** for unit testing
- **Bandit** for security checks
- **Markdownlint** for Markdown file linting

The repository also contains a range of housekeeping documentation to fit ONS development best practices, including a `CONTRIBUTING.md` file, a `CODE_OF_CONDUCT.md` and various issue and pull request templates to guide contributions.

## Project Scope

- To evaluate the feasibility and effectiveness of using GitHub Codespaces for Python projects.
- To create a sample repository containing all best practices for Python development on GitHub.

## Output

A write-up of the findings and recommendations are available within the [Output Report](./output_report.md). This report includes the general experience of using GitHub Codespaces, the benefits and drawbacks of using Codespaces, and recommendations for future use.

This report is also available in MS Word Format (`.docx`). This file is available within the repository's releases.

*(See [`pandoc.yaml`](./.github/workflows/pandoc.yaml) for how this gets generated).*

## Getting Started

### Codespace Running (Recommended)

1. Open the repository in GitHub Codespaces.
2. Wait for the Codespace to initialize and install the required dependencies.
3. Once the Codespace is ready, open a terminal in the Codespace.
4. Run the application:

    ```bash
    poetry run streamlit run src/app.py
    ```

5. Go to the Local URL provided in the terminal to view the To Do List app (cmd + click or ctrl + click).

### Local Running

#### With Devcontainer

This method requires a Docker daemon running on your machine and a copy of VS Code with the Devcontainer extension installed.

1. Clone the repository:

    ```bash
    git clone https://github.com/ONSdigital/codespace-poc.git
    ```

2. Open the repository in Visual Studio Code.

3. When prompted, select "Reopen in Container" to open the project in a Devcontainer.

    > If you do not see the prompt, you can manually reopen in a container by clicking on the green button in the bottom left corner of VS Code and selecting "Reopen in Container".

4. Wait for the Devcontainer to build and install the required dependencies.

5. Once the Devcontainer is ready, open a terminal in VS Code.

6. Run the application:

    ```bash
    poetry run streamlit run src/app.py
    ```

#### Without Devcontainer

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

## Linting, Formatting, and Testing

### Linting and Formatting (Python)

To ensure code quality, this project uses Black, Flake8, Isort and Mypy for linting and formatting. You can run these tools using the following command:

```bash
make lint
```

### Testing

To run the unit tests, you can use the following command:

```bash
make test
```

### Security Checks

To run security checks, you can use the following command:

```bash
make security
```

### Markdown Linting

To ensure the Markdown files are well-formatted, you can use the following command:

```bash
make md_lint
```

## GitHub Actions

This repository makes use of GitHub Actions for CI. Actions are available within `.github/workflows`.

The following Actions are available:

- `py_lint.yaml` | Python Linting
- `md_lint.yaml` | Markdown Linting
- `security.yaml` | Security Checks
- `testing.yaml` | Unit Testing

The above actions will run automatically on push and pull requests to the `main` branch, ensuring that code quality and security standards are maintained.
