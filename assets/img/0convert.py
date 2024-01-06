import os
import asyncio
from PIL import Image


QUALITY = 80


def get_png_files(path='.'):
    files = []
    for filename in os.listdir(path):
        if filename.endswith('.png'):
            files.append(os.path.join(path, filename))
    return files


async def convert(file):
    image = Image.open(file)
    image = image.convert('RGB')
    new_file = file.replace('Screenshot', 'Clip').replace('.png', '.jpg')
    image.save(
        new_file,
        'JPEG', quality=QUALITY
    )

    # sleep for 10 seconds before removing the file
    await asyncio.sleep(10)
    os.remove(file)
    return print('Converted {} to {}'.format(file, new_file))


# Convert png to jpg and slim it
if __name__ == '__main__':
    fs = get_png_files()
    if not fs:
        exit(0)
    tasks = []
    for f in fs:
        tasks.append(convert(f))
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    asyncio.run(asyncio.wait(tasks))
