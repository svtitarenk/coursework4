"""
This happens if you are trying to open a file, but your path is a folder.
This can happen easily by mistake.
To defend against that, use:
"""


# import os
# path = r"my/path/to/file.txt"
# assert os.path.isfile(path)
# with open(path, "r") as f:
#     pass