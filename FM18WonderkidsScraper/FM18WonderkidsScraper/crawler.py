# -*- coding: utf-8 -*-
import scrapy
from scrapy import spiderloader
from scrapy.utils import project
from scrapy.crawler import CrawlerProcess
from scrapy.exporters import CsvItemExporter
from FM18WonderkidsScraper.spiders import AMCSpider

process = CrawlerProcess()

# Exporting the data to CSVs
def ExportToCSV(pSpiderName):
        file_to_save = open((pSpiderName + '.csv'), 'w+t')
        files = [pSpiderName]
        files[pSpiderName] = file_to_save
        exporter = CsvItemExporter(file_to_save)
        exporter.start_exporting()

def Crawl(pSpiderName):
        process.crawl(pSpiderName)
        ExportToCSV(pSpiderName)

# Getting all spiders
settings = project.get_project_settings()
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
spiders = spider_loader.list()
classes = [spider_loader.load(name) for name in spiders]

#for name in spider_loader.list():
#   Crawl(name)