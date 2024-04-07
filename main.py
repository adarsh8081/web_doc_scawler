from scrapy.crawler import CrawlerProcess
from scrapy_crawler.scrapy_crawler.spiders.crawling_spider import CrawlingSpider
from indexer.indexer import Indexer

# Run the Scrapy crawler
process = CrawlerProcess()
process.crawl(CrawlingSpider)
process.start()

# Get documents from the crawler
documents = CrawlingSpider.documents

# Build and save TF-IDF index
indexer = Indexer(documents)
indexer.build_tfidf_index()
indexer.save_tfidf_index("tfidf_index.pkl")

# Start Flask app for query processing
from processor.processor import app
app.run(debug=True)
