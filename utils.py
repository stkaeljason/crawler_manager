import os

def is_dev():
	return True if os.getenv('img_crawl_env') == 'dev' else False