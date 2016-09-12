# birdspider
web scrawler for a birds website.

## Description
This project is base on [Scrapy](https://scrapy.org/). 

## Install
`pip install Scrapy`, `virtualenv` is highly recommended. If you encounter any problem, please refer to the official document of [Scrapy Installation](http://doc.scrapy.org/en/latest/intro/install.html).

## Usage
1. `cd` to the `root` directory
2. run `scrapy runspider myspider.py` in shell
3. find the `birds.json` file in the same directory, all scrawled data are in it
4. enjoy :)

## Modification
Change target website and target scrawl pages by change [this line](https://github.com/yrxwin/birdspider/blob/e6e12b2f6b5939c9733dc305fe36febad26ffa3a/birdspider/myspider.py#L8).

