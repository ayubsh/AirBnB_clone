#!/usr/bin/python3
""" initializes file storage """


from models.engine.file_storage import FileStorage

storage = FileStorage()
if __name__ == "__main__":
    storage.reload()
