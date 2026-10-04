"""Build a local preview of the site into _preview/ (approximates GitHub Pages' rendering).
Run:  python3 _tools/preview.py   then open _preview/index.html in a browser."""
import os, re, html, datetime, yaml, markdown
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '_preview')
os.makedirs(OUT, exist_ok=True)
menu = yaml.safe_load(open(os.path.join(ROOT, '_data/menu.yml'), encoding='utf-8'))
up = os.path.relpath(ROOT, OUT)  # '..' : assets/images/documents are read from the site folder itself
def local(u): return u if '://' in u or u.startswith('mailto:') or u.endswith('.html') else up + '/' + u
today = datetime.date.today().strftime('%B %-d, %Y')
for f in sorted(os.listdir(ROOT)):
    if not f.endswith('.md') or f == 'README.md': continue
    t = open(os.path.join(ROOT, f), encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', t, re.S)
    fm, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, t)
    body = re.sub(r'\\\\\n', '<br>\n', body)
    h = markdown.markdown(body, extensions=['extra', 'attr_list', 'md_in_html'])
    h = re.sub(r'(src|href)="(?!https?:|mailto:|#)([^"]+)"', lambda m: '%s="%s"' % (m.group(1), local(m.group(2))), h)
    here = f[:-3] + '.html'
    nav = ''
    for s in menu:
        nav += '<div class="menu-section"><div class="menu-head">%s</div><ul>' % html.escape(s['section'])
        for it in s['items']:
            cur = ' class="current"' if it['url'] == here else ''
            nav += '<li><a href="%s"%s>%s</a></li>' % (local(it['url']), cur, html.escape(it['title']))
        nav += '</ul></div>'
    title = fm.get('title', '')
    page = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Tryphon T. Georgiou (preview)</title>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;1,400&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}/assets/style.css"></head><body><div class="wrap"><nav class="menu">{nav}</nav>
<main class="content">{h}<footer>Updated {today} &middot; local preview</footer></main></div></body></html>'''
    open(os.path.join(OUT, here), 'w', encoding='utf-8').write(page)
    print('wrote', here)
