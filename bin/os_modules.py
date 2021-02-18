import os
import shutil


def move_file(filename, source, destination):
    # Moving of the file from source to destination
    # Creating a new folder if in case the folder is already not there.
    print("\tMoving file from " + source + " to " + destination)

    try:
        os.mkdir(destination)
        return shutil.move(source, destination)
    except FileExistsError:
        try:
            return shutil.move(source, destination)
        except shutil.Error as err:
            return shutil.move(source, os.path.join(destination, filename))
    except shutil.Error as err:
        return shutil.move(source, os.path.join(destination, filename))
