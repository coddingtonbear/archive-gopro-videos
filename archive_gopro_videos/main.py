import os
import shutil

from . import exceptions


def copy_files_from_to(volume_name, destination):
    if not os.path.exists(volume_name):
        raise exceptions.VolumeNotPresent()
    if not os.path.exists(destination):
        raise exceptions.DestinationNotPresent()

    for filename in os.listdir(volume_name):
        shutil.move(
            os.path.join(volume_name, filename),
            os.path.join(destination, filename)
        )
