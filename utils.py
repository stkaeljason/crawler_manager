import os
import time

def is_dev():
	return True if os.getenv('img_crawl_env') == 'dev' else False

def time_to_timestamp(t):
	st = time.strptime(t, '%Y-%m-%d %H:%M')
	source_timestamp = str(time.mktime(st))
	point_index = source_timestamp.index('.')
	return int(source_timestamp[:point_index])