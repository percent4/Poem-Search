# -*- coding: utf-8 -*-


import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from pymongo import MongoClient
from poet_intro import PoetSearch

# 连接MongoDB
conn = MongoClient('mongodb://localhost:27017/')
coll = conn["test"].poem

#定义端口为8000
define("port", default=8000, help="run on the given port", type=int)

# GET请求
class TestHandler(tornado.web.RequestHandler):
    # get函数
    def get(self):
        title = "Home Page"
        header = "Books that are great"
        books = ['book'+str(i) for i in range(100)]
        self.render('test.html', title=title, header=header, books=books)

# GET请求
class QueryHandler(tornado.web.RequestHandler):
    # get函数
    def get(self):
        self.render('query.html')

# POST请求
# POST请求参数：query_string
class ResultHandler(tornado.web.RequestHandler):
    # post函数
    def post(self):
        query = self.get_argument('query_string')
        if query:
            res = list(coll.find({'content': {'$regex': query}}))
            self.render('result.html', query=query, res=res)
        else:
            res = []
            self.render('result.html', query=query, res=res)

class PoetHandler(tornado.web.RequestHandler):
    # get函数
    def get(self):
        poet = self.get_argument("poet")
        introduction = PoetSearch(poet).search()
        image_src = PoetSearch(poet).search_image()
        self.render('poet.html', poet=poet, intro=introduction, image_src=image_src)

# 主函数
def main():
    tornado.options.parse_command_line()
    # 定义app
    app = tornado.web.Application(
            handlers=[(r'/query', QueryHandler),
                      (r'/result', ResultHandler),
                      (r'/poetIntro', PoetHandler),
                      (r'/test', TestHandler)], #网页路径控制
            template_path=os.path.join(os.path.dirname(__file__), "templates") # 模板路径
          )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

main()