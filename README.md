# 🗂 Mini Version Control System (VCS)

A lightweight Version Control System implemented in Python.

This project simulates the core behavior of a real VCS (like Git) by creating content-based snapshots of a directory and storing them using SHA-256 hashes.

The purpose of this project is to demonstrate understanding of:

- File system traversal
- Cryptographic hashing
- Snapshot-based versioning
- Binary serialization
- Content-addressable storage design

---

## 🚀 Features

- Initialize a VCS repository
- Create full directory snapshots
- Content-based snapshot hashing (SHA-256)
- Ignore internal storage directory
- Store snapshot data using binary serialization
- Deterministic snapshot IDs
- Basic file tracking system

---

## 🧠 How It Works

### 1️⃣ Initialization

When `init_vcs()` is called, the system creates a hidden directory:

```bash
.vcs_storage/
```

This folder stores all snapshot data.

---

### 2️⃣ Snapshot Creation

When `snapshot(directory)` is executed:

1. The system recursively walks through all files.
2. It ignores:
   - `.git`
   - `.vcs_storage`
   - The VCS script itself
3. Each file is read in binary mode.
4. File contents are hashed using SHA-256.
5. A global snapshot hash is computed.
6. Snapshot data is serialized and stored.

Each snapshot is saved as:

```bash
.vcs_storage/<sha256_hash>
```

The filename itself acts as the snapshot ID.

---

### 3️⃣ Snapshot Structure

Each snapshot file contains:

```python
{
    "files": {
        "relative/path/file1.txt": b"...file bytes...",
        "relative/path/file2.py": b"...file bytes...",
    },
    "file_list": ["file1.txt", "file2.py"]
}
```

Snapshots are stored using Python's `pickle` module.

---

## 🔐 Why SHA-256?

SHA-256 ensures:

- Deterministic snapshot identification
- Content-based uniqueness
- No duplicate snapshots for identical content
- Strong collision resistance

This mirrors how Git generates commit hashes using content-addressable storage.

---

## 📂 Project Structure

```bash
project/
│
├── vcs.py
├── your_project_files...
└── .vcs_storage/
      ├── 9f1a2c...
      ├── 4e7bd1...
```

---

## 🛠 Example Usage

```python
from vcs import init_vcs, snapshot

init_vcs()
snapshot(".")
```

---

## ⚠️ Current Limitations (By Design)

This mini VCS intentionally does not implement:

- Incremental diffs
- Branching
- Commit metadata
- Staging area
- Restore functionality
- Remote repositories

It stores full snapshots for learning purposes.

---

## 📚 Educational Purpose

This project was built to understand:

- How version control systems manage data internally
- How hashing enables content-addressable storage
- How file systems can be abstracted into structured snapshots
- Why Git is architected the way it is

---

## 🔮 Future Improvements

- Add restore command
- Implement diff-based storage
- Add commit messages
- Implement branching
- Replace pickle with a custom object store
- Add CLI interface

---

## 👨‍💻 Author

Built as a systems-learning project in Python to explore low-level repository mechanics and storage architecture.
