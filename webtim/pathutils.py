from pathlib import PurePosixPath


def study_from_path(root, path):
    local_path = path.relative_to(root)
    return local_path.parts[0]
