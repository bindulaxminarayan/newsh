import os

import config
from config import db
import database.models


if __name__ == "__main__":
    if not os.path.exists(config.dbFilename):
        print("Creating database.")
        print db
        db.create_all()
        print("Created database.")
    else:
        print("Database already exists. Nothing to do.")
