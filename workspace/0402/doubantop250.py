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
		print('Ready: ')

	def get_url(self, cur_page):
		'''
		得到每页的页码
		'''
		#page = (25 * (cur_page -1))
		#url = self.url
		url = self.url.format(page = (25 * (cur_page -1)))            #页码需要更新   format 函数
		
		print(url)
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
			if '&nbsp;' in item:
				temp_data.append('Top ' + str(self.num) + ':' + item)       #self.num
				self.num += 1
		self.name.extend(temp_data)       #append -> extend
			
	
	def spider_start(self):
		while(self.page <= 10):
			my_url = self.get_url(self.page)      #self.get_url
			my_data = self.get_data(my_url)        #self.get_data(my_url)  two error   :一个少了self，一个多了self
			movie_name = self.add_name(my_data)
			self.page += 1
	
def main():
	my_spider = Douban()
	my_spider.spider_start()
	'''
	for item in my_spider.name:
		print(item)
	'''
	print("""
		go ->
	""")
	with open('E:/python/0402/movie02.txt', 'w+') as f:
		f.write("\n".join(my_spider.name).encode('gbk', 'ignore').decode('gbk'))        # 保存进txt，并且换行
	print('finish')
if __name__ == '__main__':             #  ==
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	