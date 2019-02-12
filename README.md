# Poem-Search
web框架使用tornado, 后端数据库采用MongoDB, 诗词数据集使用爬虫。

### 数据集

&emsp;&emsp;爬取的网址为：https://www.gushiwen.org , 只爬取了该页面中的唐诗三百首、古诗三百、宋词三百、宋词精选，一共大约1144首诗歌。爬虫的代码文件为poem_scrape.py 。

### 数据库

&emsp;&emsp;采用MongoDB作为后端数据库，利用write2mongodb.py将爬取的诗歌CSV文件写入到数据库。

### 前端

&emsp;&emsp;前端框架使用tornado, 代码为server.py 。

### 使用示例

&emsp;&emsp;运行server.py, 在浏览器中输入网址：http://localhost:8000/result ，界面如下：

![](https://github.com/percent4/Poem-Search/blob/master/%E8%AF%97%E6%AD%8C%E6%90%9C%E7%B4%A2%E7%95%8C%E9%9D%A2.png)

在其中输入搜索关键词，比如“白云”，则会显示一条随机的结果，如下：

![](https://github.com/percent4/Poem-Search/blob/master/%E8%AF%97%E6%AD%8C%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C.png)

点击“查询词高亮”，则查询词部门会高亮显示。

### 总结

&emsp;&emsp;仍有很多功能还待完善，待补充~
