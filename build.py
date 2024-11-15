import json


def get_music_html():
    base = '''
        <a style='background:{{BACKGROUND}}; color: {{TEXT_COLOUR}}' href='{{HREF}}'>
            {{SONG_NAME}}
        </a>
    '''

    f = open('items/songs.json')
    songs = json.load(f)
    f.close()

    result = ''
    for song in songs:
        html = base\
            .replace('{{BACKGROUND}}', song['background'])\
            .replace('{{SONG_NAME}}', song['name'])\
            .replace('{{HREF}}', song['link'])\
            .replace('{{TEXT_COLOUR}}', song['text-colour'])

        result += html
    
    return result


def get_store_html():
    f = open('items/store.json')
    items = json.load(f)
    f.close()

    result = ''
    for item in items:
        result += f'''
            <a class="store-item" href="{item['link']}">
                <img src="{item['image']}" alt="{item['name']}">
                <div class="item-name">{item['name']}</div>
                <div class="item-price">{item['price']}</div>
            </a>
        '''
    
    return result


def build():
    f = open('pages.json')
    pages = json.load(f)
    f.close()

    f = open('items/now-playing.json')
    nowPlaying = json.load(f)
    f.close()

    f = open('unrendered/template.html')
    template = f.read()
    f.close()

    cssFiles = ['nav.css', 'music.css', 'store.css']

    css = ''
    for file in cssFiles:
        f = open(f'unrendered/css/{file}')
        css += f.read()
        f.close()

    template = template.replace('{{MAIN_CSS}}', f'<style>{css}</style>').replace('{{SONG_NAME}}', nowPlaying['name']).replace('{{SONG_FILE}}', nowPlaying['src'])

    f = open('items/socials.json')
    socials = json.load(f)
    f.close()
    social_html = ''
    for social in socials:
        social_html += f'''
            <a href="{social['link']}">
                <img src="{social['icon']}" alt="">
            </a>
        '''
    template = template.replace('{{SOCIALS}}', social_html)

    pageContents = {}

    for page in pages:
        f = open('unrendered/' + page['id'] + '.html')
        contents = f.read()
        if page['id'] == 'music':
            contents = contents.replace('{{MUSIC_LIST}}', get_music_html())
        if page['id'] == 'store':
            contents = contents.replace('{{STORE_ITEMS}}', get_store_html())
        pageContents[page['id']] = contents
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