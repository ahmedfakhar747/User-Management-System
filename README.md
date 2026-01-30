
---
# 👥 User Management System (CLI)

A modern, interactive **Command-Line User Management System** built with Python and **Rich**.  
This project demonstrates clean architecture, solid data handling, and a polished CLI user experience.

---

## ✨ Features

- ➕ Add users with **unique username and email**
- 🔍 Search users by username
- ✏️ Update user information (partial updates supported)
- 🗑️ Delete users
- 👁️ View all users in a formatted table
- 🎨 Beautiful, colorized CLI using **Rich**
- ✅ Case-insensitive validation
- 📧 Email format validation
- 🧱 Clean project structure (separation of concerns)
- 🛑 Graceful error handling

---

## 🧠 Design Decisions

- **Username & Email Uniqueness**  
  Both are enforced to prevent identity conflicts and ensure data integrity.

- **Case-Insensitive Matching**  
  Usernames and emails are normalized internally for consistent behavior.

- **Sorted Storage**  
  Users are stored alphabetically by username for predictable output.



---

## 📁 Project Structure

  - `models.py` → Core functionality / User and UserDatabase classes
  - `cli.py` → Command-line interface logic
  - `theme.py` → presentation / styling
  - `main.py` → application entry point

---
## 🚀 Getting Started

### Requirements
- Python 3.10+
- pip

### Install Dependencies
```bash
pip install rich readchar
````

### Run the Application

```bash
python main.py
```

---

## 🖥️ CLI Preview

* Color-coded messages for success, errors, and info
* Emoji-enhanced menu for better UX
* Clean tables for displaying users
* Keyboard-friendly navigation

---

## 🧪 Testing

Basic unit tests were written using **pytest** to validate:

* User insertion
* Sorting logic
* Username uniqueness
* Email uniqueness
* Search behavior

Run tests with:

```bash
python -m pytest
```

---

## 🔮 Future Improvements

* 💾 Persistent storage (JSON / SQLite)
* 🔐 Authentication & roles
* ⚡ Faster lookups using dictionaries
* 📦 Packaging as a reusable CLI tool
* 🧪 Expanded test coverage

---


## 👤 Author

**Ahmed Fakhar**
Aspiring Software / AI Engineer
Focused on writing clean, practical, and scalable Python applications.

---

## 📜 License

This project is open-source and free to use for learning and experimentation.

---