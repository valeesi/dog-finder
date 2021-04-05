from pyquery import PyQuery as pq
import hashlib

sites_to_monitor = {
    'hundarutanhem': 'https://hundarutanhem.se/hundar/',
    'hundarsokerhem': 'https://hundarsokerhem.se/hundar-som-soker-hem/',
    'hundstallet': 'https://hundstallet.se/soker-hem/'
}
# 'hundstallet': 'https://hundstallet.se/soker-hem/',
# 'dogrescue': 'https://www.dogrescue.se/hundar-soker-hem/',
# 'hundhjalpen': 'https://hundhjalpen.se/hundar-for-adoption/',
# 'hundrondellen': 'https://hundhjalpen.se/hundar-for-adoption/',
# 'sosanimals': 'https://www.sos-animals.se/dogs/'
dogs_found = {}


def add_dog(dog_list):
    for dog in dog_list:
        element = dog.__str__().replace("\t", "").replace("\n", "")
        dogs_found[hash_this(element.encode("utf-8"))] = element


def load_current_dogs():
    for name, url in sites_to_monitor.items():
        d = pq(url)
        if name == 'hundarutanhem':
            add_dog(
                d.find('article').find('a').filter(lambda i, this: pq(this).attr('rel') != 'bookmark').items()
            )
        elif name == 'hundarsokerhem':
            add_dog(
                d.find('.arkivhund').find('a').filter(lambda i, this: pq(this).text() == '').items()
            )
        elif name == 'hundstallet':
            add_dog(
                d.find(".small-12").find('a').filter(
                    lambda i, this: pq(this).text().__contains__('Mer') is False).items()
            )


def hash_this(str):
    return hashlib.sha224(str).hexdigest()
