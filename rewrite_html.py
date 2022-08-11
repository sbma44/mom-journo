import os, os.path, re

re_img_src = re.compile(r' src="https://content.journohq.com/(\w+)_preview.jpg"')

for fn in os.listdir('./html/orig'):
    if fn.split('.')[-1] != 'html':
        continue
    with open(fn) as f:
        html = f.read()
        new_html = re_img_src.subn(' src="img/\1.jpg"', html)
        with open(os.path.join('./html', os.path.basename(fn), 'w') as f2:
            f2.write(new_html)
