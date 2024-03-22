## Web Scraping and Analysis with Selenium and Pandas
This repository contains a Python script that automates the process of scraping a file name from a website using Selenium, downloading the file asynchronously using ThreadPoolExecutor, and performing analysis on the downloaded data using Pandas.

### How It Works
#### Scraping with Selenium:
`Selenium` is used to automate the process of navigating to a website and extracting the file name.

#### Asynchronous Download:
The file name obtained from scraping is used to construct the download URL.
`ThreadPoolExecutor` is utilized to download the file `asynchronously`, allowing for efficient handling of multiple downloads simultaneously.

#### Analysis with Pandas:
Once the file is downloaded, `Pandas` is employed to analyze its content including cleansing and transformation.

### Usage
Run `main.py` to scrape the file name, construct the download URL, and asynchronously download the file and to perform analysis on the downloaded data using Pandas.


This README provides a high-level overview of how the scraping and analysis process works using Selenium and Pandas.
