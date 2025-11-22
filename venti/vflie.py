# -*- coding: UTF-8 -*-
import hashlib

class Vfile:
    @staticmethod
    def file_sha256(file_path, chunk_size=4096):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

    @staticmethod
    def file_read(file_path, chunk_size=4096):
        with open(file_path, "rb") as f:
            while 1:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk