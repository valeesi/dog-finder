import hashlib
from pyquery import PyQuery as pq

sites_to_monitor = {
    'hundarutanhem': 'https://hundarutanhem.se/hundar/',
    'hundarsokerhem': 'https://hundarsokerhem.se/hundar-som-soker-hem/',
    'hundstallet': 'https://hundstallet.se/soker-hem/',
    'amigosmios': 'https://www.amigosmios.se/hundar-soker-hem/'
}
# 'dogrescue': 'https://www.dogrescue.se/hundar-soker-hem/',
# 'hundhjalpen': 'https://hundhjalpen.se/hundar-for-adoption/',
# 'hundrondellen': 'https://hundhjalpen.se/hundar-for-adoption/',
# 'sosanimals': 'https://www.sos-animals.se/dogs/'
current_dogs = {}
new_dogs = {}


def add_dog(dog_list):
    for dog in dog_list:
        element = dog.__str__().replace("\t", "").replace("\n", "")
        hashed = hash_this(element.encode("utf-8"))
        if hashed not in current_dogs:
            new_dogs[hashed] = element
        current_dogs[hashed] = element


def scan_for_dogs():
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
        elif name == 'amigosmios':
            add_dog(
                d.find(".overlay").find('a').items()
            )


def hash_this(element):
    return hashlib.sha224(element).hexdigest()
