# Pruebas de Software UCR 2025 II Ciclo

## Students

Paula Camacho González C21570 

Yeshúa Ramírez Alfaro C26230

Jose Daniel Ramírez C16339

Valeria Rodríguez Ramírez C16696

Christian Vargas Álvarez C18174

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download the repository**
```bash
   cd path/to/behave-pruebas-2025
```

2. **Create a virtual environment**

   **Windows (PowerShell/CMD):**
```powershell
   python -m venv .venv
```

   **Linux/Mac/WSL:**
```bash
   python3 -m venv .venv
```

3. **Activate the virtual environment**

   **Windows PowerShell:**
```powershell
   .venv\Scripts\Activate.ps1
```

   **Git Bash (Windows):**
```bash
   source .venv/Scripts/activate
```

   **Linux/Mac/WSL:**
```bash
   source .venv/bin/activate
```

4. **Install dependencies**
```bash
   pip install -r requirements.txt
```

### Running the Tests

Navigate to the `behave_atm` directory:
```bash
cd behave_atm
```
then run:
```bash
python -m behave
```

### Deactivating the Virtual Environment

When you're done testing:
```bash
deactivate
```

## Introduction
This repository demonstrates an ATM domain model and its behavior-driven tests using Behave. It shows how banking operations such as deposits, withdrawals, transfers, and PIN management can be described in business-readable Gherkin scenarios and exercised via Python step definitions.

## Technologies
- Python 3.12 for the ATM implementation and test glue code.
- Behave for BDD-style feature execution.
- Gherkin syntax for readable feature specifications.

## Project Structure
```text
behave_atm/
├── atm.py
├── behave.ini
├── __pycache__/
│   └── atm.cpython-312.pyc
└── features/
    ├── atm.feature
    ├── environment.py
    └── steps/
        └── test_atm_steps.py
```
- `behave_atm/atm.py` — Core ATM domain class with balance tracking, withdrawals, transfers, PIN changes, and custom exceptions.
- `behave_atm/behave.ini` — Behave configuration file.
- `behave_atm/features/atm.feature` — Gherkin feature file covering balance checks, deposits, withdrawals, transfers, history, PIN updates, and daily limits.
- `behave_atm/features/environment.py` — Testing environment initialization.
- `behave_atm/features/steps/test_atm_steps.py` — Step definitions that map Gherkin phrases to Python code invoking `ATM` and asserting results.