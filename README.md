# TaskFlow

TaskFlow is a beginner-friendly, 100% Python task management application that helps individuals and small teams organize, track, and prioritize their daily tasks and activities.

---

## Features

- **Task Creation** – Quickly create tasks with a name and description.
- **Task Tracking** – Monitor the status of each task (Pending / Done).
- **Dashboard View** – Render a clear overview of all tasks and their current status.
- **User Authentication** – Basic username/password authentication to protect access.

---

## Prerequisites

- **Python 3.8+** – [Download Python](https://www.python.org/downloads/)
- **pip** – Comes bundled with Python; used to install dependencies.

---

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/MaryamCodeHub/TaskFlow.git
   cd TaskFlow
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   ```

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** A `requirements.txt` file has not yet been added to this repository. Once it is available, run the command above to install all project dependencies.

---

## Running the Application

The main entry point is `src/main.py`. You can run it with:

```bash
python src/main.py
```

This will print a welcome message. Full application functionality is still under development.

---

## Running Tests

Tests are located in the `tests/` directory. To run them use:

```bash
python -m pytest tests/
```

> Make sure you have `pytest` installed (`pip install pytest`) before running this command.

---

## Project Structure

```
TaskFlow/
├── docs/
│   └── project_overview.md   # High-level project overview
├── src/
│   ├── auth.py               # User authentication logic
│   ├── dashboard.py          # Task dashboard rendering
│   ├── main.py               # Application entry point
│   └── task.py               # Task model and creation helpers
├── tests/
│   └── test_main.py          # Unit tests
├── .gitignore
├── Jenkinsfile
└── README.md
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository and create your branch from `development`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** and ensure existing tests still pass.
3. **Add tests** for any new functionality you introduce.
4. **Commit** your changes with a clear, descriptive message:
   ```bash
   git commit -m "Add: brief description of your change"
   ```
5. **Push** your branch and open a **Pull Request** targeting the `development` branch.
6. Your PR will be reviewed and merged once approved.

---

## License

License: Not specified.
