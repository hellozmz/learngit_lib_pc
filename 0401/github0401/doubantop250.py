import urllib.request
import re 

class Douban(object):
	'''
		page 页码
		url 页面url
		num 排名
		name 保存名字的数组
	'''
	def __init__(self):
		self.page = 1
		self.url = 'https://movie.douban.com/top250?start={page}&filter=&type='
		self.name = []
		self.num = 1

	def get_url(self, cur_page):
		'''
		得到每页的页码
		'''
		page = 25 * (cur_page -1)
		url = self.url
		return url

	def get_data(self, cur_url):
		'''
		得到每页数据，utf8
		'''
		cur_data = urllib.request.urlopen(cur_url).read()
		data = cur_data.decode('utf8')
		
		return data
		
	def add_name(self, cur_data):
		'''
		将名字加入数组
		'''
		temp_data = []
		movie_items = re.findall(r'<span class="title">(.*?)</span>', cur_data)    #why r'  '
		for item in movie_items:
			if '&nbsp;' not in item:
				temp_data.append('Top ' + str(num) + ':' + item)
				num += 1
		name.append(tmp_name)
			
	
	def spider_start(self):
		while(self.page <= 10):
			my_url = get_url(self.page)
			my_data = get_data(self.my_url)
			movie_name = add_name(self.my_data)
			self.page += 1
	
def main():
	my_spider = Douban()
	my_spider.spider_start()
	for item in my_spider.name:
		print(item)
	
if __name__ == '__main__':             #  ==
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	