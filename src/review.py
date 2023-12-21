import hashlib
import os
import subprocess


def review(config):
    path_source = config['path_source']

    comments = []

    file_path = os.path.join(path_source, 'CMakeLists.txt')
    if not __run_cmake_format(file_path, config['config']):
        path_relative = file_path.replace(path_source, "")[1:]
        comments.append({
            "id": __generate_md5(file_path),
            "comment": f"Formatação incorreta no arquivo {path_relative}",
            "position": {
                "language": "cmake",
                "path": path_relative,
                "startInLine": 1,
                "endInLine": 1,
                "snipset": False
            }
        })

    return comments


def __run_cmake_format(file_path, config_file_path):
    comando = ['cmake-format', '-c', config_file_path, '--check', file_path]
    resultado = subprocess.run(comando, capture_output=True, text=True)

    return resultado.returncode == 0


def __generate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))

    return md5_hash.hexdigest()
