
---
# 👥 User Management System (CLI)

A modern, interactive **Command-Line User Management System** built with Python and **Rich**.  
This project demonstrates clean architecture, solid data persistence, input validation, and a polished CLI user experience.

---

## ✨ Features

- ➕ **Add Users** - Register new users with username, name, and email
- 🔍 **Search Users** - Find users by username with instant lookup
- ✏️ **Update Users** - Modify user information with validation
- 🗑️ **Delete Users** - Remove users from the system
- 👁️ **View All Users** - Display users in a beautifully formatted table
- 💾 **Persistent Storage** - All data automatically saved to JSON
- 🎨 **Rich CLI Styling** - Color-coded messages, emoji indicators, and formatted tables
- ✅ **Robust Validation** - Case-insensitive username/email matching, preventing duplicates
- 📧 **Email Validation** - Regex-based email format verification
- 🛑 **Error Handling** - Graceful error messages and recovery
- ⌨️ **Keyboard-Friendly** - Menu-driven navigation with numeric shortcuts

---

## 🧠 Architecture & Design Decisions

### Core Components

- **`User` Class** - Simple data model representing a user (username, name, email)
- **`UserDatabase` Class** - Manages CRUD operations with JSON persistence
- **CLI Module** - Interactive menu system with input validation
- **Theme Module** - Centralized styling for consistent UI

### Design Highlights

- **Username & Email Uniqueness**  
  Both are enforced at the database level to prevent identity conflicts and ensure data integrity.

- **Case-Insensitive Matching**  
  Despite case preservation, lookups are case-insensitive (e.g., "john" matches "John" or "JOHN").

- **Sorted Storage**  
  Users are maintained alphabetically by username for predictable, consistent output.

- **Separation of Concerns**  
  Business logic (models), CLI logic, and presentation (theme) are cleanly separated.

---

## 📁 Project Structure

```
User-Management-System/
├── src/ums/
│   ├── main.py              # Application entry point with error handling
│   ├── theme.py             # Rich-based styling and formatting utilities
│   └── core/
│       ├── models.py        # User & UserDatabase classes (CRUD operations)
│       └── cli.py           # Interactive CLI menu and command handling
├── data/
│   └── users.json           # Persistent user data storage
├── tests/
│   ├── __init__.py
│   └── tests.py             # Comprehensive unit tests
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

---
## 🚀 Getting Started

### Prerequisites
- **Python 3.10+** (for type hints support)
- **pip** (Python package manager)

### Installation

1. **Clone or navigate to the repository:**
   ```bash
   cd User-Management-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or manually install:
   ```bash
   pip install rich>=13.0 readchar>=4.0 pytest>=8.0
   ```

### Running the Application

Start the interactive CLI:

```bash
python src\ums\main.py
```

The main menu will display with numbered options (1-6) for navigation.

---

## 🖥️ CLI Preview

### Main Menu

━━━━━━━━━━━ ⚙️  USER MANAGEMENT SYSTEM ⚙️  ━━━━━━━━━━━
Welcome to the User Management System!

----------------👥 User Management System ----------------
| # | Command                |  Description                                  |
|---|----------------------|-----------------------------------------------|
| 1 | ➕  Add User           | Add a new user to the system                  |
| 2 | 🔍  Search User        | Search for a user by username                |
| 3 | 🗑️  Delete User        | Remove a user from the system                |
| 4 | ✏️  Update User        | Update user information                      |
| 5 | 👁️  View All Users    | Display all registered users                 |
| 6 | ⛔ Exit               | Exit the application                         |
_________________________________________________________________________________________________


### Operations

**Add User:**
- Input username, full name, and email
- Email format validation with regex
- Prevents duplicate usernames and emails

**Search User:**
- Case-insensitive username lookup
- Returns user details or "not found" message

**View All Users:**
- Displays all registered users in a formatted Rich table
- Users sorted alphabetically by username

**Update User:**
- Modify user information
- Supports partial updates

**Delete User:**
- Remove users by username
- Confirmation message upon deletion

### Design Features
- 🎨 **Color-coded messages** - Red for errors, green for success, blue for info, yellow for warnings
- 🎭 **Emoji indicators** - ✔️ ❌ ℹ️ for quick visual feedback
- ⏸️ **Pause prompts** - "Press any key to continue..." between operations
- 🖥️ **Clear navigation** - Screen clears between commands for focused interaction

---

## 🧪 Testing

Comprehensive unit tests validate core functionality:

### Test Coverage
- ✅ Username uniqueness (case variations)
- ✅ Email uniqueness (case variations)
- ✅ User insertion and retrieval
- ✅ Sorting logic
- ✅ Search behavior
- ✅ Database persistence
- ✅ Email format validation

### Running Tests

```bash
python -m pytest tests/tests.py -v
```

Example output:
```
tests/tests.py::test_duplicate_username_case_variations PASSED
tests/tests.py::test_duplicate_email_case_variations PASSED
tests/tests.py::test_insert_single_user PASSED
...
```

---

## 🔮 Future Improvements

- 🔐 **Authentication & Authorization** - User roles and login system
- 🔄 **Batch Operations** - Import/export users via CSV
- 📊 **Analytics** - User statistics and reports
- 🔍 **Advanced Search** - Filter by name, email, or any field
- 💎 **Database Upgrade** - SQLite/PostgreSQL for larger datasets
- 📦 **Packaging** - Distribute as pip-installable tool
- 🌐 **Web Interface** - REST API and web dashboard
- 🎯 **Fuzzy Search** - Approximate username matching

---


## � Data Format

Users are stored in `data/users.json` with the following structure:

```json
[
    {
        "username": "john_doe",
        "name": "John Doe",
        "email": "john@example.com"
    },
    {
        "username": "jane_smith",
        "name": "Jane Smith",
        "email": "jane@example.com"
    }
]
```

The file is:
- **Auto-created** on first user addition
- **Auto-updated** after every CRUD operation
- **Validated** for JSON integrity on load

---

## 🔧 Validation Rules

| Field | Rules |
|-------|-------|
| **Username** | No duplicates (case-insensitive), cannot be empty |
| **Email** | Valid email format (regex), no duplicates (case-insensitive), cannot be empty |
| **Name** | Cannot be empty, case-preserved |

---

## 📖 Usage Examples

### Basic Workflow

1. **Run the application:**
   ```bash
   python src\ums\main.py
   ```

2. **Add a user** (Select option 1):
   ```
   Enter username: john_doe
   Enter fullname: John Doe
   Enter Email Address: john@example.com
   ✔️ User 'john_doe' added successfully!
   ```

3. **Search for a user** (Select option 2):
   ```
   Enter username: john_doe
   ℹ️ User found!
   Username: john_doe
   Name: John Doe
   Email: john@example.com
   ```

4. **View all users** (Select option 5):
   - Displays formatted table of all registered users

5. **Exit** (Select option 6):
   - Graceful shutdown with goodbye message

---

## 👤 Author

**Ahmed Fakhar**  
Aspiring Software Engineer / AI Developer  
Focused on clean, practical, and scalable Python applications.

---

## 📜 License

This project is open-source and free to use for learning and experimentation.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs or issues
- 💡 Suggest new features
- 🔧 Submit pull requests with improvements
- 📝 Improve documentation

---

## ⭐ Acknowledgments

Built with [Rich](https://github.com/Textualize/rich) - A Python library for rich text and beautiful formatting in the terminal.

---