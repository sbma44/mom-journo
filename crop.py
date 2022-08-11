import sys, os, os.path
from PIL import Image

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        im = Image.open(f)
        p = os.path.splitext(os.path.basename(sys.argv[1]))[0]
        idx = p.split('_')[-1]
        new_name = 'screenshots/cropped/journo_{:03d}.png'.format(int(idx))
        im.crop((110, 218, im.width - 1610, im.height - 160)).save(new_name)