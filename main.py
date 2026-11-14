import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts"))

from data_loader import load_all


def define_env(env):
    data = load_all()
    env.variables["data"] = data
    # Keep the download links in one place: the same names build.py writes.
    stem = data["profile"]["name"].replace(" ", "-")
    env.variables["pdf_name"] = f"{stem}-CV.pdf"
