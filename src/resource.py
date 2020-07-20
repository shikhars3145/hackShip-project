import sys
import os


def getResource(name: str) -> str:
    """Get resource path."""
    try:
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath("./src/assets/")
    return os.path.normpath(
        os.path.join(
            basePath,
            name,
        )
    )
