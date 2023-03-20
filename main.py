import html
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET

XML_PATH = ''
TARGET_FILE = '2023-03-20.xml'


def cleanRegex(string):
    # pattern = r'\[(cmsmasters_|/cmsmasters_).*\]'
    pattern = r'\[(cmsmasters_|/cmsmasters_).*?\]'
    htmlText = re.sub(pattern, "", string)
    return htmlText


def XMLparse(path: str):
    with open(path, 'r') as f:
        data = f.read()

    bs = BeautifulSoup(data, 'lxml')

    for tag in bs.find_all('content:encoded'):
        truncated = cleanRegex(str(tag))
        tag.string = (html.unescape(truncated)
                      .replace('<content:encoded>', "")
                      .replace('</content:encoded>', ''))

    # for meta in bs.find_all('wp:meta_key'):
    #     truncated = cleanRegex(meta.text)
    #     meta.string = str(truncated).replace(']', '[]]')

    mod_xml = html.unescape(bs.prettify())
    with open(TARGET_FILE, "w") as f:
        f.write(mod_xml)


def modifyXMLandSave(path: str):
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    for child in root.iter():
        print(child.text)
    # tree.write("movies.xml")


if __name__ == '__main__':
    XMLparse(path=XML_PATH)
    # modifyXMLandSave(path=TEST_PATH)
