# script used for extracting frames from the videos

import os

from config import CLASSES, RAW_IMAGES_DIR, VIDEO_NAMES_DIR, VIDEOS_DIR
from utils import FrameExtractor

if __name__ == "__main__":
    for class_name in CLASSES:
        print(f"Extracting images for class {class_name}...")
        dest_dir = os.path.join(RAW_IMAGES_DIR, class_name)
        os.makedirs(dest_dir, exist_ok=True)

        fe = FrameExtractor(
            os.path.join(VIDEOS_DIR, VIDEO_NAMES_DIR[class_name])
        )

        fe.extract_frames(
            every_x_frame=50,
            skip_seconds=60,
            img_name=class_name,
            dest_path=dest_dir,
        )

        print("done.")
