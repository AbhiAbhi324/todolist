# 📝 Smart Todo List Application

A responsive, secure, full-stack Todo application built with Python and Flask. This project strictly follows the **Model-View-Controller (MVC)** design pattern and uses an interconnected SQLite relational database for absolute separation of concerns.

---

### 🏛️ Application Architecture (MVC)

The codebase isolates core functional responsibilities to maximize maintainability and scalability:

*   **`main.py`**: The application server entry-point and launcher script.
*   **`website/__init__.py`**: Initializer factory that instantiates Flask, binds SQLAlchemy, and registers controllers.
*   **`website/models.py`** *(The Model)*: Contains the relational database schemas mapping your Users and Tasks.
*   **`website/views.py`** *(The Controller)*: Manages task creation, status toggles, deletion, and homepage routing.
*   **`website/auth.py`** *(The Controller)*: Isolates secure registration, login credential validation, and user sessions.
*   **`website/templates/`** *(The View)*: Renders dynamic front-end dashboard layouts utilizing Jinja rendering.
*   **`website/static/`**: Houses public CSS asset sheets and interface styling variables.

---

### 📈 Future AI Expansion Road Map
Once the baseline MVC todo system and database collection workflow are completed, this application will be extended to include:
1.  🎯 **Smart Prioritization Engine**: An ML model utilizing user historical completion speeds to dynamically rank tasks.
2.  🏷️ **Auto-Tagging System**: Natural Language Processing (NLP) text categorization to auto-group newly created tasks.

---

### 💻 Installation and Local Setup

1. Clone the repository down to your computer:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the directory and initialize your environment:
   ```bash
   cd todolist
   python -m venv myenv
   ```
3. Activate your virtual environment and launch your dev server:
   ```bash
   # Windows Powershell:
   .\myenv\Scripts\Activate.ps1
   python main.py
   ```


