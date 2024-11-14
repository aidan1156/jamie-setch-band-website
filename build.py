import json

def build():
    f = open('pages.json')
    pages = json.load(f)
    f.close()

    f = open('unrendered/template.html')
    template = f.read()
    f.close()

    cssFiles = ['nav.css']

    css = ''
    for file in cssFiles:
        f = open(f'unrendered/css/{file}')
        css += f.read()
        f.close()

    template = template.replace('{{MAIN_CSS}}', f'<style>{css}</style>')

    pageContents = {}

    for page in pages:
        f = open('unrendered/' + page['id'] + '.html')
        pageContents[page['id']] = f.read()
        f.close()

    for page in pages:
        contents = ''
        for key in pageContents.keys():
            content = pageContents[key].replace('{{HIDDEN}}', ' hidden ')
            if key == page['id']:
                content = pageContents[key].replace('{{HIDDEN}}', '')
            showNav = [page['show-nav'] for page in pages if page['id'] == key]
            content = content.replace('{{SHOW_NAV}}', showNav[0])
            contents += content
        
        contents = template.replace('{{MAIN_CONTENT}}', contents)
        contents = contents.replace('{{NAV_SIZE}}', page['show-nav'])

        f = open('rendered/' + page['id'] + '.html', 'w+')
        f.write(contents)
        f.close()

        if page['id'] == 'home':
            f = open('rendered/index.html', 'w+')
            f.write(contents)
            f.close()


build()