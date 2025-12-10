import os 
import hashlib
import pickle

SNAPSHOT_DIR = ".vcs_storage"


def init_vcs():
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    print("VCS initialized.")


def snapshot(directory):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {"files": {}}

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in (".git", SNAPSHOT_DIR.lstrip("./"))]

        for file in files:
            file_path = os.path.join(root, file)

            if os.path.abspath(file_path) == os.path.abspath(__file__):
                continue

            with open(file_path, "rb") as f:
                content = f.read()

            snapshot_hash.update(content)
            rel_path = os.path.relpath(file_path, directory)
            snapshot_data["files"][rel_path] = content

    hash_digest = snapshot_hash.hexdigest()
    snapshot_data["file_list"] = list(snapshot_data["files"].keys())

    snapshot_path = os.path.join(SNAPSHOT_DIR, hash_digest)
    with open(snapshot_path, "wb") as f:
        pickle.dump(snapshot_data, f)

    print(f"Snapchot created with hash {hash_digest}")



def revert_to_snapshot(snapshot_id):
    snapshot_path = os.path.join(SNAPSHOT_DIR, snapshot_id)

    if not os.path.exists(snapshot_path):
        print("Snapshot not found.")
        return

    with open(snapshot_path, "rb") as f:
        snapshot_data = pickle.load(f)

    files_dict = snapshot_data.get("files", {})

    for rel_path, content in files_dict.items():
        if rel_path == ".git" or rel_path.startswith(".git/") or "/.git/" in rel_path:
            continue

        full_path = os.path.join(".", rel_path)
        os.makedirs(os.path.dirname(full_path) or ".", exist_ok=True)

        with open(full_path, "wb") as file:
            file.write(content)

    print(f"Reverted to snapshot {snapshot_id}.")



if __name__ == "__main__":
    import sys
    command = sys.argv[1]

    if command == "init":
        init_vcs()
    elif command == "snapshot":
        snapshot(".")
    elif command == "revert":
        revert_to_snapshot(sys.argv[2])
    else:
        print("Unknown command!")
