"""Builds style-a/b/c from index.html: same markup and text, theme CSS appended.
Run from the repo root: python3 themes/build.py"""
import os, re

FONTS = {
    'a-sage': 'family=Frank+Ruhl+Libre:wght@500;700&family=Heebo:wght@300;400;500;600;700',
    'b-night': 'family=Bellefair&family=Assistant:wght@300;400;600;700',
    'c-warm': 'family=Varela+Round&family=Assistant:wght@300;400;600;700',
}
OUT = {'a-sage': 'style-a', 'b-night': 'style-b', 'c-warm': 'style-c'}

src = open('index.html', encoding='utf-8').read()
for theme, folder in OUT.items():
    css = open(f'themes/{theme}.css', encoding='utf-8').read()
    h = re.sub(r'https://fonts\.googleapis\.com/css2\?[^"]+',
               f'https://fonts.googleapis.com/css2?{FONTS[theme]}&display=swap', src, count=1)
    h = h.replace('</style>', css + '\n</style>', 1)
    h = h.replace('src="assets/', 'src="../assets/')
    h = h.replace('<head>', '<head>\n<meta name="robots" content="noindex, nofollow">', 1)
    os.makedirs(folder, exist_ok=True)
    open(f'{folder}/index.html', 'w', encoding='utf-8').write(h)
    print(folder, 'ok')
