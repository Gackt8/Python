# %%
from PIL import Image, ImageDraw, ImageFont
from os import listdir
from datetime import date


def create_super_image(image_path: str, logo_path: str, qr_code_path: str, output: str, im_width=800):
    image_path = Image.open(image_path)
    logo_path = Image.open(logo_path)
    qr_code_path = Image.open(qr_code_path)

    assert im_width >= 480, RuntimeError("Small size")
    im_height = im_width * image_path.size[1] // image_path.size[0]
    image_path = image_path.resize((im_width, im_height), Image.ANTIALIAS)

    lo_width = im_width // 10
    lo_height = lo_width * logo_path.size[1] // logo_path.size[0]
    logo_path = logo_path.resize((lo_width, lo_height), Image.ANTIALIAS)

    qr_code_path = qr_code_path.resize((100, 100), Image.ANTIALIAS)

    if image_path.size[1] > image_path.size[0]:
        image_path = image_path.rotate(270)

    idraw = ImageDraw.Draw(image_path)

    dates = date.today()

    text = "Опарина Алёна MC-32"
    font = ImageFont.truetype("arial.ttf", size=18)
    idraw.text((im_width // 2 - 125, im_height - 25), f"{text} {dates}", font=font)

    image_path.paste(logo_path, (im_width - lo_width, 0), logo_path)
    image_path.paste(qr_code_path, (0, 0))

    image_path.save(output)



# %%
files = listdir('cat')
for file in files[:]:
    if '.jpg' not in file:
        files.remove(file)
    else:
        create_super_image(f'cat/{file}', 'cat/bamboo.png', 'cat/qr.png', f'cat/out/{file}', im_width=1000)