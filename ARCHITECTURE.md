
# ℹ️ Architecture (`ARCHITECTURE.md`)

## 📁 Project Structure

```
User-Management-System/
├── assets/
│   ├── MainAnimation.gif       # Full CLI walkthrough (startup → exit)
│   ├── AddAnimation.gif        # Adding a new user with validation
│   ├── SearchAnimation.gif     # Searching users by username/email
│   ├── UpdateAnimation.gif     # Updating user fields (partial updates)
│   ├── DeleteAnimation.gif     # Deleting a user safely
│   └── ListAnimation.gif       # Listing all users in sorted order
│
├── src/ums/
│   ├── __init__.py
│   ├── main.py                 # Application entry point & global error handling
│   ├── theme.py                # Rich-based styling (colors, headers, messages)
│   └── core/
│       ├── models.py           # Core domain logic (User, UserDatabase, invariants)
│       └── cli.py              # Interactive CLI menu & command routing
│
├── data/
│   └── users.json              # Persistent JSON-backed user storage
│
├── tests/
│   ├── __init__.py
│   └── tests.py                # Unit tests for CRUD, validation & persistence
│
├── README.md                   # Project documentation
│
├── USAGE.md                    # How to use the CLI (commands, flows, examples)
├── ARCHITECTURE.md             # System design, data flow, and design decisions
└── TESTS.md                    # Testing strategy, test cases, and coverage


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
