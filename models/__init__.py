#!/usr/bin/python3
__all__ = ["base_model"]
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
