from bs4 import BeautifulSoup
import requests
import json


def get_verses_from_page(link):
  verses = get_verses(link[53:])
  r = requests.get(link)
  soup = BeautifulSoup(r.text, 'html.parser')
  for verse in verses:
    html = soup.find_all(id=verse)[0]
    html.span.decompose()
    help_text = {'verse': verse[1:], 'text': ''}
    try:
      while True:
        html.sup.decompose()
    except AttributeError:
      pass
    help_text['text'] = html.get_text()
    output_file.write(json.dumps(help_text))


def get_verses(link):
  verse_block = link.split('.')[1].split('?')[0]
  if '-' in verse_block:
    start, finish = verse_block.split('-')
    return [f'p{v}' for v in range(int(start), int(finish) + 1)]
  elif ',' in verse_block:
    return [f'p{v}' for v in verse_block.split(',')]
  else:
    return [f'p{verse_block}']


if __name__ == '__main__':
  input_file = open('help_text.txt')
  output_file = open('help_text.json', 'w')
  links = [link for link in input_file.read().splitlines()]
  for link in links:
    get_verses_from_page(link)
  output_file.close()
