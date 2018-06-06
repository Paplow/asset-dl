#!/usr/bin/python3

"""
*********************************************************
 _______                      __
|       \                    |  \
| $$$$$$$\ ______    ______  | $$  ______   __   __   __
| $$__/ $$|      \  /      \ | $$ /      \ |  \ |  \ |  \
| $$    $$ \$$$$$$\|  $$$$$$\| $$|  $$$$$$\| $$ | $$ | $$
| $$$$$$$ /      $$| $$  | $$| $$| $$  | $$| $$ | $$ | $$
| $$     |  $$$$$$$| $$__/ $$| $$| $$__/ $$| $$_/ $$_/ $$
| $$      \$$    $$| $$    $$| $$ \$$    $$ \$$   $$   $$
 \$$       \$$$$$$$| $$$$$$$  \$$  \$$$$$$   \$$$$$\$$$$
                   | $$
                   | $$
                    \$$
*********************************************************
"""

from urllib import request as req
from bs4 import BeautifulSoup
from shutil import copyfileobj
from re import search
import argparse
import sys
import os


def main():
    # Command line parser
    parser = argparse.ArgumentParser(description="Smart Asset Downloader",
                                     argument_default=sys.argv[0] + " -u URL -p PATH",
                                     epilog="This tool downloads all assets on a page and saves them by directory structure.")
    required = parser.add_argument_group("Required arguments")
    required.add_argument("-u", "--url", type=str, help="Target site url")
    required.add_argument("-p", "--path", type=str, help="The absolute path to save assets")

    # Print help if no provided arguments
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Put all passed arguments in args variable
    args = parser.parse_args()

    try:
        res = req.urlopen(req_obj(args.url))
        soup = BeautifulSoup(res.read().decode('utf-8'), 'html.parser')
        urls = []
        for link in soup.find_all('link'):
            urls.append(link.get('href'))
        for script in soup.find_all('script'):
            urls.append(script.get('src'))
        for img in soup.find_all('img'):
            urls.append(img.get('src'))
        download_asset(urls, args)
    except Exception as error:
        sys.stderr.write(str(error) + "\r\n")


# The Download Request function / method
def req_obj(url):
    return req.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
    )


# Download assets
def download_asset(urls, args):
    try:
        basepath = args.path
    except IndexError:
        basepath = os.path.dirname(os.path.abspath(__file__))

    line = "#" * 20
    sys.stdout.write(line + " Downloading " + line + "\r\n")
    for url in urls:
        if not url or not search("(\.[a-zA-Z0-9]+)$", url):
            continue

        path = search("/([a-zA-Z0-9/\-_]+)/", url).group()[1:] if search("/([a-zA-Z0-9/\-_]+)/", url) else ''
        fullpath = os.path.join(basepath, path)
        os.system("mkdir -p " + fullpath)

        file = url[2:] if url[:2] == './' else url
        url = url if not search("^(\.\/|\/|(?!(http|www)))", url) else search("(http(s|)://(www.|)([a-zA-Z0-9-.]+))",
                                                                              args.url).group() + '/' + file

        with req.urlopen(req_obj(url)) as res_data, open(fullpath + url.split('/')[-1], 'wb') as asset:
            copyfileobj(res_data, asset)

        sys.stdout.write(str(url) + "\r\n")
    sys.stdout.write(line + " Completed " + line + "\r\n")


if __name__ == '__main__':
    main()
