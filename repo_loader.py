import os
from git import Repo

# Folder where repositories will be stored
REPO_FOLDER = "repos"


def clone_repo(repo_url):
    """
    Clone a GitHub repository to local machine
    """

    # create repo folder if it does not exist
    if not os.path.exists(REPO_FOLDER):
        os.makedirs(REPO_FOLDER)

    # extract repo name from URL
    repo_name = repo_url.split("/")[-1]

    local_path = os.path.join(REPO_FOLDER, repo_name)

    # clone only if repo not already downloaded
    if not os.path.exists(local_path):
        Repo.clone_from(repo_url, local_path)

    return local_path


def load_code_files(repo_path):
    """
    Read all code files from repository
    """

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith((".py", ".js", ".ts", ".java", ".cpp", ".c", ".go")):

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:

                        code_files.append({
                            "file_path": file_path,
                            "content": f.read()
                        })

                except:
                    pass

    return code_files