import os
import shutil

def copy_source_to_destination(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    
    os.mkdir(destination)

    for item in os.listdir(source):

        item_path = os.path.join(source, item)

        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
        else:
            copy_source_to_destination(item_path, os.path.join(destination, item))