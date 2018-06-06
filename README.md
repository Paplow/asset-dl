# asset-dl
Smart Asset Downloader.

This CLI tool helps you download all assets (image, css and javascript) files contained in a page 
and saves then according to their directory structure with just one click.

## Requirement
-   python >= 3
-   beautifulsoup4

## Installation

	git clone git@github.com:Paplow/asset-dl.git
	cd asset-dl
	sudo chmod 0755 asset-dl.py
    
	OR:

	Download the latest version at: https://github.com/Paplow/asset-dl/archive/master.zip
	unzip master.zip
	mv asset-dl-master asset-dl
	cd asset-dl
	sudo chmod 0755 asset-dl.py

## Usage
```python3
./asset-dl.py -u URL -p PATH

or

python3 asset-dl.py -u URL -p PATH
```

    -u or --url - Url of the page you want to download assets
    -p or --path - Absolute path to where you want to save assets


ENJOY...