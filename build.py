
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
    index = tmpl.render(title = 'Music Notes', root = root, main = index, part = False)

    with open(os.path.join(DEST, 'index.html'), 'w') as fout:
        fout.write(index)

def _build_parts(root = ROOT):
    logging.info('Building parts')

    # online
    tmpl = env.get_template('content/music-theory-part-1.html')
    part = tmpl.render(root = root)
    tmpl = env.get_template('templates/layout.html')
    part = tmpl.render(title = 'Music Theory Part 1', root = root, main = part, part = True)
    with open(os.path.join(DEST, 'music-theory-part-1.html'), 'w') as fout:
        fout.write(part)

    # print
    tmpl = env.get_template('content/music-theory-part-1.html')
    part = tmpl.render(root = '../'+root)
    tmpl = env.get_template('templates/print.html')
    part = tmpl.render(title = 'Music Theory Part 1', root = '../'+root, main = part)
    with open(os.path.join(DEST, 'print/music-theory-part-1.html'), 'w') as fout:
        fout.write(part)

# main
_build_index()
_build_parts()
