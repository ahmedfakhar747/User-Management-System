
# ℹ️ Architecture (`ARCHITECTURE.md`)

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

# 🧠 Architecture & Design Decisions

### Core Components
- **User Class** - data model
- **UserDatabase Class** - CRUD + JSON persistence
- **CLI Module** - menu + input validation
- **Theme Module** - consistent UI styling

### Design Highlights
- Username & Email uniqueness
- Case-insensitive matching
- Sorted storage
- Separation of concerns

---
