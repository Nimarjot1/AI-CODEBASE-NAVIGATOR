import os
import shutil
from git import Repo

REPO_FOLDER = "repos"

ALLOWED_EXTENSIONS = (".py", ".js", ".ts", ".java", ".cpp", ".c", ".go")


def clone_repo(repo_url):

    if not os.path.exists(REPO_FOLDER):
        os.makedirs(REPO_FOLDER)

    repo_name = repo_url.split("/")[-1]
    local_path = os.path.join(REPO_FOLDER, repo_name)

    if os.path.exists(local_path):
        print(f"⚠️ Repo already exists, deleting old copy: {local_path}")
        shutil.rmtree(local_path)

    print(f"⬇️ Cloning repo: {repo_url}")
    Repo.clone_from(repo_url, local_path)

    return local_path


def load_code_files(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        # skip heavy folders
        dirs[:] = [d for d in dirs if d not in ["node_modules", ".git", "__pycache__"]]

        for file in files:

            if file.endswith(ALLOWED_EXTENSIONS):

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                        if len(content.strip()) < 50:
                            continue

                        code_files.append({
                            "file_path": file_path,
                            "content": content
                        })

                except Exception:
                    pass

    print(f"\n✅ Total files loaded: {len(code_files)}")

    return code_files
