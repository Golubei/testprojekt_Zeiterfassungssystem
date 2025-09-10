# Zeiterfassungssystem

**Zeiterfassungssystem** is a web application for time tracking, statistics, data export, and change audit.  
The project is written in Python (Flask) and provides an interactive interface for viewing and filtering work time data.

---

## 📦 Installation (Local)

### 1. Clone the repository

```bash
git clone https://github.com/Golubei/testprojekt_Zeiterfassungssystem.git
cd testprojekt_Zeiterfassungssystem
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```
or (if using Flask CLI):

```bash
flask run
```

---

## ⚙️ Project Structure

- `main.py` — main entry point (Flask server, logic for time tracking and auditing)
- `requirements.txt` — Python dependencies
- `templates/` — HTML interface templates
- `static/` — static files (CSS, JS, images)
- `Статистика.txt` — HTML example for statistics and audit section
- Other `.py` files — additional modules

---

## 🛠️ Features

- **Time tracking**
- **Statistics by month, client, and employee**
- **Export data to XLSX**
- **Change audit with filters and reset option**
- **Filtering and search by various parameters**

---

## 🧑‍💻 How can others run your project?

1. Clone the repository to their machine.
2. Install Python ≥3.8 and dependencies using `pip install -r requirements.txt`.
3. Run the app: `python main.py` or `flask run`.
4. Open a browser and navigate to the address shown by Flask (e.g., http://127.0.0.1:5000).

---

## 📝 Additional Notes

- If your project uses a database, check the relevant files for setup instructions or contact the author.
- For environment variables (e.g., secrets, passwords), create a `.env` file in the project root (use `.env.example` as a template, if available).

---

## ❓ Questions / Feedback

Create an issue in this repository or contact the author via [GitHub](https://github.com/Golubei).

---

## License

MIT
