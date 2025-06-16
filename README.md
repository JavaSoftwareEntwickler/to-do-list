# ✅ To-Do List App – Flask + SQLite

Questa è una semplice **applicazione To-Do List** sviluppata con Python (Flask) e SQLite. L’interfaccia è costruita con HTML, CSS e JS. L’obiettivo è fornire una base solida per una web app CRUD minimale, facilmente estendibile.

---

## 🚀 Funzionalità

- 📋 Aggiunta di nuovi task
- ✅ Toggle completamento di un task
- 🗂️ Lista dinamica dei task con salvataggio persistente via SQLite
- 🔁 Routing gestito tramite Flask Blueprint
- 🛠️ ORM SQLAlchemy per l’accesso al database

---

## 🧠 Architettura del Progetto

```

to-do-list/
│   run.py
│   requirements.txt
│   app.db  ← creato automaticamente
│
└───app/
│   **init**.py
│   models.py
│   routes.py
│
├───static/
│   ├───css/
│   │       styles.css
│   └───js/
│           scripts.js
│
└───templates/
index.html

````

---

## 💻 Istruzioni per l’installazione

### 1. 🔁 Clona il repository

Apri il terminale (cmd) e digita:

```bash
git clone https://github.com/JavaSoftwareEntwickler/to-do-list.git
cd to-do-list
````

### 2. 🧪 Crea un ambiente virtuale

```bash
python -m venv venv
```

### 3. 📦 Attiva l’ambiente virtuale (solo Windows)

```bash
venv\Scripts\activate
```

⚠️ Se ricevi un errore sui criteri di esecuzione, esegui:

```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

E poi riattiva l’ambiente.

---

### 4. 📥 Installa le dipendenze

```bash
pip install -r requirements.txt
```

---

### 5. ▶️ Avvia il server

```bash
python run.py
```

Apri il browser su: [http://localhost:5000](http://localhost:5000)

---

## 🧩 Dipendenze principali

Le dipendenze si trovano nel file `requirements.txt`. Le principali sono:

* `Flask`
* `Flask-SQLAlchemy`

---

## 📁 File Principali

* `run.py`: punto d’ingresso dell'app
* `app/__init__.py`: factory Flask e registrazione blueprint
* `app/routes.py`: logica delle route
* `app/models.py`: definizione del modello `Task`
* `app/templates/index.html`: interfaccia HTML
* `app/static/css/styles.css`: stile base
* `app/static/js/scripts.js`: codice JS (se presente)

---

## 📌 Note per estensioni future

* Autenticazione utenti con Flask-Login o OAuth2
* API RESTful con Flask-Restx
* UI migliorata con Bootstrap o Tailwind
* Frontend reattivo con Vue.js o React

---

## 🧑‍💻 Autore

**Max** – [GitHub](https://github.com/JavaSoftwareEntwickler)

---

## 📄 Licenza

Distribuito con licenza MIT. Sentiti libero di riutilizzare e modificare il progetto.

```