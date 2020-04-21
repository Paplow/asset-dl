## Smart Asset Downloader.

A CLI tool for downloading assets (image, css and javascript) files contained in a webpage and persisting them locally according to their directory structure.

- [asset-dl](#asset-dl)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contribution](#contribution)
  - [License (MIT)](#license-mit)

## Requirement
-   python >= 3

## Installation
```bash
    git clone https://github.com/kodjunkie/asset-dl.git
    cd asset-dl
    pip install -r requirements.txt
```

## Usage

```bash
python3 ./asset-dl.py -u URL -p PATH
```

```bash
     ___                   __            ____
   /   |  _____________  / /_      ____/ / /
  / /| | / ___/ ___/ _ \/ __/_____/ __  / / 
 / ___ |(__  |__  )  __/ /_/_____/ /_/ / /  
/_/  |_/____/____/\___/\__/      \__,_/_/ 

usage: asset-dl.py [-h] [-u URL] [-p PATH]

Smart Asset Downloader

optional arguments:
  -h, --help            show this help message and exit

Required arguments:
  -u URL, --url URL     Target site url
  -p PATH, --path PATH  Path to save assets

Download all assets on a page and saves them by directory structure.

```

## Contribution

All contributions of any kind are welcome.


## License (MIT)

This project is opened under the [MIT 2.0 License](https://github.com/kodjunkie/asset-dl/blob/master/LICENSE) which allows very broad use for both academic and commercial purposes.
