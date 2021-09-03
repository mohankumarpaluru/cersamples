from PIL import Image
from pathlib import Path

extension_list = [".jpeg", ".jpg", ".png"]


def image_compression(input_dir, final_quality=85, scale_down_ratio=None):
    for image_file in Path(input_dir).iterdir():
        if image_file.is_file() and image_file.suffix.lower() in extension_list:
            foo = Image.open(image_file)
            if scale_down_ratio:
                h, w = foo.size
                foo = foo.resize(
                    (int(h * scale_down_ratio / 100), int(w * scale_down_ratio / 100)),
                    Image.ANTIALIAS,
                )
            new_name = image_file.stem
            extension = image_file.suffix
            new_image_path = Path(input_dir).joinpath(
                new_name + "_compressed" + extension
            )
            foo.save(new_image_path, optimize=True, quality=final_quality)


DIR = "C:\\Users\\mohan.kumar.paluru\\test\\Saved Pictures"
scale_down = 80
final_quality = 70

image_compression(DIR, scale_down, final_quality)
