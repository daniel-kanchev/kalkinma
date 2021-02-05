BOT_NAME = 'kalkinma'
SPIDER_MODULES = ['kalkinma.spiders']
NEWSPIDER_MODULE = 'kalkinma.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'kalkinma.pipelines.DatabasePipeline': 300,
}
