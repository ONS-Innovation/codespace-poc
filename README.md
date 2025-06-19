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
