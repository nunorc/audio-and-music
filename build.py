
import os, jinja2, json, logging

logging.basicConfig(level = logging.INFO)

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='./'))

ROOT = '.'
DEST = 'docs'
CONTENT = 'content'
PAGES = 'pages'

if not os.path.exists(DEST):
    os.mkdir(DEST)
if not os.path.exists(DEST + '/print'):
    os.mkdir(DEST + '/print')

def _build_index(root = ROOT):
    logging.info('Building index')

    tmpl = env.get_template('templates/index.html')
    index = tmpl.render(root = root)
    tmpl = env.get_template('templates/layout.html')
    index = tmpl.render(title = 'A & M', root = root, main = index, part = False)

    with open(os.path.join(DEST, 'index.html'), 'w') as fout:
        fout.write(index)

def _slug(title):
    slug = title.replace('Notes', '')

    return slug

def _build_part(title, file, root = ROOT):
    logging.info('Building ' + title)

    slug = _slug(title)
    # online
    tmpl = env.get_template(f"content/{ file }.html")
    part = tmpl.render(root = root)
    tmpl = env.get_template('templates/layout.html')
    part = tmpl.render(title = title, slug = slug, root = root, main = part, part = True)
    with open(os.path.join(DEST, f"{ file }.html"), 'w') as fout:
        fout.write(part)

    # print
    tmpl = env.get_template(f"content/{ file }.html")
    part = tmpl.render(root = '../'+root)
    tmpl = env.get_template('templates/print.html')
    part = tmpl.render(title = title, slug = slug, root = '../'+root, main = part)
    with open(os.path.join(DEST, f"print/{ file }.html"), 'w') as fout:
        fout.write(part)

# main
_build_index()

content = [
    ('Music Theory Part 1', 'music-theory-part-1'),
    ('Music Theory Part 2', 'music-theory-part-2')
]
for c in content:
    _build_part(c[0], c[1])
