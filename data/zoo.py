from pyquery import PyQuery as pq
import hashlib

sites_to_monitor = {
    'hundarutanhem': {
        'url': 'https://hundarutanhem.se/hundar/',
        'tag': 'a'
    },
    'hundarsokerhem': {
        'url': 'https://hundarsokerhem.se/hundar-som-soker-hem/',
        'tag': '.arkivhund'
    }
}
# 'hundstallet': 'https://hundstallet.se/soker-hem/',
# 'dogrescue': 'https://www.dogrescue.se/hundar-soker-hem/',
# 'hundhjalpen': 'https://hundhjalpen.se/hundar-for-adoption/',
# 'hundrondellen': 'https://hundhjalpen.se/hundar-for-adoption/',
# 'sosanimals': 'https://www.sos-animals.se/dogs/'
dogs_found = {''}


def add_dog(url, tag_for_list, additional_tag=None):
    d = pq(url)
    for dog in d.items(tag_for_list):
        if additional_tag is None:
            dog_entry = dog
        else:
            dog_entry = dog.find(additional_tag)
        dogs_found.add(
            hash_dog(dog_entry.__str__().encode("utf-8"))
        )


def load_current_dogs():
    for site, value in sites_to_monitor.items():
        if site == 'hundarutanhem':
            add_dog(value['url'], 'article', additional_tag='a')
        elif site == 'hundarsokerhem':
            add_dog(value['url'], value['tag'])


def hash_dog(str):
    return hashlib.sha224(str).hexdigest()
