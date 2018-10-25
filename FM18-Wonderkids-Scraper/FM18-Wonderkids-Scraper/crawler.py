# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.contrib.exporter import CsvItemExporter

csvFileName = ""

def ExportToCSV(spider):
        file_to_save = open((csvFileName + '.csv'), 'w+t')
        files = [spider]
        files[spider] = file_to_save
        exporter = CsvItemExporter(file_to_save)
        exporter.start_exporting()

process = CrawlerProcess()

process.crawl('AMCSpider')
csvFileName = "amc"
ExportToCSV('AMCSpider')

