import re
import os
import glob
import string
import shutil
import logging


__all__ = [
    "count_words",
    "read_file",
    "read_line",
    "printnl",
    "remove_quotes",
    "remove_nl",
    "remove_spaces",
    "remove_double_spaces",
    "remove_punctuation",
    "remove_end_punctuation",
    "count_sentence_periods",
    "get_sentences",
    "str_to_file_name",
    "str_to_tag_name",
    "format_index",
    "path_exists",
    "list_subpaths",
    "list_file_paths",
    "list_file_paths_sorted",
    "list_file_names",
    "list_file_names_sorted",
    "list_dir_paths",
    "list_dir_paths_sorted",
    "list_dir_names",
    "list_dir_names_sorted",
    "create_dir",
    "remove_dir",
    "copy_file",
    "move_file",
]

LOG = logging.getLogger(__name__)


def count_words(text: str):
    return len(text.split())


def read_file(file_path: str):
    with open(file_path, "r") as f:
        response = f.read()
    return response


def read_line(file_path: str):
    with open(file_path, "r") as f:
        response = f.readline().strip()
    return response


def printnl(text: str):
    print(f"{text}\n")


def remove_quotes(text: str):
    text = text.replace('"', "")
    return text


def remove_nl(text: str):
    text = text.replace("\n", "")
    return text


def remove_spaces(text: str):
    text = text.replace(" ", "")
    return text


def remove_double_spaces(text: str):
    text = text.replace("  ", " ")
    return text


def remove_punctuation(text: str):
    return re.sub(r"[^\w\s]", "", text)


def remove_end_punctuation(text):
    return text.rstrip(string.punctuation)


def count_sentence_periods(text):
    pattern = r"(?<![0-9])\.\s*(?=[A-Z]|$)"
    matches = re.findall(pattern, text)
    return len(matches)


def get_sentences(text: str):
    pattern = r"(?<=[.!?])\s+(?=[A-Z])"
    sentences = re.split(pattern, text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences


def str_to_file_name(text: str):
    return remove_punctuation(text=text).lower().replace(" ", "_")


def str_to_tag_name(text: str):
    return remove_spaces(remove_punctuation(text=text)).lower()


def format_index(index: int, decimals: int = 3):
    return f"{index:0{decimals}d}"


def path_exists(dir_path: str):
    return os.path.exists(dir_path)


def list_subpaths(dir_path):
    return glob.glob(os.path.join(dir_path, "*"))


def list_file_paths(dir_path):
    return [f for f in list_subpaths(dir_path=dir_path) if os.path.isfile(f)]


def list_file_paths_sorted(dir_path):
    return sorted(list_file_paths(dir_path=dir_path))


def list_file_names(dir_path):
    return [os.path.basename(f) for f in list_file_paths(dir_path=dir_path)]


def list_file_names_sorted(dir_path):
    return [os.path.basename(f) for f in list_file_paths_sorted(dir_path=dir_path)]


def list_dir_paths(dir_path):
    return [d for d in list_subpaths(dir_path=dir_path) if os.path.isdir(d)]


def list_dir_paths_sorted(dir_path):
    return sorted(list_dir_paths(dir_path=dir_path))


def list_dir_names(dir_path):
    return [os.path.basename(d) for d in list_dir_paths(dir_path=dir_path)]


def list_dir_names_sorted(dir_path):
    return [os.path.basename(d) for d in list_dir_paths_sorted(dir_path=dir_path)]


# def create_dir(dir_path):
#     os.makedirs(dir_path, exist_ok=True)


# def remove_dir(dir_path):
#     os.system(f"rm -rf {dir_path}")


# def copy_file(src_path, dst_path):
#     os.system(f"cp -r {src_path} {dst_path}")


# def move_file(src_path, dst_path):
#     os.system(f"mv {src_path} {dst_path}")


def create_dir(dir_path):
    """
    Safely create a directory and any intermediate directories if they do not exist.

    :param dir_path: Path of the directory to create.
    """
    try:
        os.makedirs(dir_path, exist_ok=True)
        LOG.info(f"Directory '{dir_path}' created successfully.")
    except Exception as e:
        LOG.error(f"Error creating directory '{dir_path}': {e}")


def remove_dir(dir_path):
    """
    Safely remove a directory and all its contents.

    :param dir_path: Path of the directory to remove.
    """
    try:
        shutil.rmtree(dir_path)
        LOG.info(f"Directory '{dir_path}' and all its contents have been removed.")
    except FileNotFoundError:
        LOG.error(f"Directory '{dir_path}' not found.")
    except PermissionError:
        LOG.error(f"Permission denied when trying to remove '{dir_path}'.")
    except Exception as e:
        LOG.error(f"Error removing directory '{dir_path}': {e}")


def copy_file(src_path, dst_path):
    """
    Safely copy a file or directory into the destination directory.
    If the destination directory exists, the source will be copied inside it.

    :param src_path: Source path of the file or directory.
    :param dst_path: Destination directory where the file or directory should be copied into.
    """
    try:
        if not os.path.exists(dst_path):
            create_dir(dst_path)  # Ensure the destination directory exists

        # If it's a directory, copy its contents into the destination
        if os.path.isdir(src_path):
            # Join the source directory name with the destination directory
            final_dst_path = os.path.join(dst_path, os.path.basename(src_path))
            shutil.copytree(src_path, final_dst_path)
            LOG.info(f"Directory '{src_path}' copied into '{dst_path}'.")
        else:
            # If it's a file, copy it directly into the destination directory
            shutil.copy2(src_path, dst_path)
            LOG.info(f"File '{src_path}' copied into '{dst_path}'.")
    except FileExistsError:
        LOG.error(f"Error: '{src_path}' already exists in '{dst_path}'.")
    except FileNotFoundError:
        LOG.error(f"Error: '{src_path}' not found.")
    except PermissionError:
        LOG.error(f"Permission denied when copying '{src_path}'.")
    except Exception as e:
        LOG.error(f"Error copying '{src_path}' to '{dst_path}': {e}")


def move_file(src_path, dst_path):
    """
    Move a file or directory from src_path to dst_path.

    :param src_path: Source path of the file or directory.
    :param dst_path: Destination path where the file or directory should be moved.
    """
    try:
        shutil.move(src_path, dst_path)
        LOG.info(f"Successfully moved {src_path} to {dst_path}.")
    except FileNotFoundError:
        LOG.error(f"Error: {src_path} not found.")
    except PermissionError:
        LOG.error(f"Error: Permission denied when moving {src_path}.")
    except Exception as e:
        LOG.error(f"An error occurred: {e}")
