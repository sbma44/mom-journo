import os, os.path, re

re_img_src = re.compile(r' src="https://content.journohq.com/(.*?)(_preview)?\.jpg"')
re_date = re.compile(r'<div class="entry-date">(.*?)</div>')

HEADER = open('header.html').read()
FOOTER = open('footer.html').read()
SIDEBAR_TARGET = '<!-- sidebar -->'

dates = []
date_map = {}
for fn in sorted(os.listdir('./docs/orig')):
    if fn.split('.')[-1] != 'html':
        continue
    with open(os.path.join('./docs/orig', fn)) as f:
        html = f.read()
        m = re_date.search(html)
        if m:
            parts = [x.lower() for x in m.group(1).split()]
            months = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
            new_fn = '{:4d}-{:02}-{:02d}'.format(int(parts[2]), months.index(parts[0]) + 1, int(parts[1]))
            existing = len([x for x in dates if x[1].split('-')[:3] == new_fn.split('-')[:3]])
            new_fn = '{}-{:02d}.html'.format(new_fn, existing + 1)

            dates.append((m.group(1), new_fn))
            date_map[fn] = new_fn

ul = '\n<ul class="nav">' + '\n'.join(['<li><a href="{}">{}</a></li>'.format(x[1], x[0]) for x in dates]) + '</ul>'

for fn in sorted(os.listdir('./docs/orig')):
    if fn.split('.')[-1] != 'html':
        continue
    with open(os.path.join('./docs/orig', fn)) as f:
        html = f.read()

        new_html = HEADER + re_img_src.sub(' src="http://sbma44.s3-website-us-east-1.amazonaws.com/mom-journo/\\1.jpg"', html) + FOOTER
        new_html = new_html.replace(SIDEBAR_TARGET, ul)

        with open(os.path.join('./docs', date_map[fn]), 'w') as f2:
            f2.write(new_html)