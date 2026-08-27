from pathlib import Path
from PIL import Image

source = Path('/home/ubuntu/webdev-static-assets/securechat-icon.png')
targets = [
    Path('/home/ubuntu/securechat-android/assets/images/icon.png'),
    Path('/home/ubuntu/securechat-android/assets/images/splash-icon.png'),
    Path('/home/ubuntu/securechat-android/assets/images/favicon.png'),
    Path('/home/ubuntu/securechat-android/assets/images/android-icon-foreground.png'),
]
image = Image.open(source).convert('RGBA')
image.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
for target in targets:
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, format='PNG', optimize=True, compress_level=9)
print('optimized', image.size)
