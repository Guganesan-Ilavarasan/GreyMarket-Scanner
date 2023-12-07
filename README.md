# GreyMarket-Scanner</br>

### A study to scan grey markets to trace recent trends in antiquity sales, with an outlook to expand further for tracking illicit trafficked art in black markets.</br>
</br>
<div align="justify">

The study aims to collect data from an antiquities (grey) market and analyse its recent trends in sales, which could be further taken up to understand contemporary cultural value. For the data source, after considering e-commerce sites dealing with antiquity sales, it was decided to embark on higher transacted markets like auction houses and their e-bids and sales of lots. Hence, [Christie's](https://www.christies.com) proved more informative and easily accessible for data collection. The data was requested by web scrapping with Selenium and was cleaned and tokenised using NLTK.</br>
</div>

<div align="justify">

### High-Level Overview:</br>

1. #### ``src``
    src/webscraping:</br>

     - [``webscraper.py``](src/webscraping/webscraper.py) is used to scrape data by applying the Selenium library. The scraped data, [<i>scrape_data.csv</i>](data/scrape_data), is in the data folder.</br>

     - ``geckodriver.log`` is the driver that needed to be installed to run Selenium.</br>
2.  #### ``word_analysis``
    The only module here is [``word_counter.py``](word_analysis/word_counter.py), which does NLP operations on the retrieved data. The inputs of this module are the scraped parameters of the antiquities, e.g. period, object name, etc.
3.  #### ``data``
    The folder contains the raw scraped data and <i>.txt</i> files used in the NLP analysis done in ``src/word_anlysis/word_counter.py``. The scraped output <i>.csv</i> file contains object names, the value of the sale, the period of antiquity,       and the link of the object. The data is then split and saved as individual parameters, e.g. [objnames.txt](data/objnames.txt), to perform NLP to find the most used terms.</br>
    </div>

### Run order:</br>
</br>

````
webscraper.py -> word_counter.py
````
<div align="justify">

### Analysis:</br>

The word counter generates the fifty most used words, revealing the culture and materials with the highest occurrence in the lot, popular among buyers. A dictionary is compiled from these most used terms to perform subsequent analysis. Accordingly, in the scraped database, two reference columns are added, one for the dynasty of the artefact and the other for its material. Consequently, using the dictionary, a partial textual match is detected on the object name's column by conditional if statements with wildcards to populate the reference columns. The data in these columns act as ordinal data indicators for the classification of data, which would further assist in visualisations.</br>
</div>

</br>

> Example of an analysis: A heat map for the sum of prices of artefacts of different dynastical cultures and material composition.</br>


![image](https://github.com/Guganesan-Ilavarasan/GreyMarket-Scanner/assets/85569213/614073a2-ad4f-4cfd-a77d-71c1d6e4e672)

