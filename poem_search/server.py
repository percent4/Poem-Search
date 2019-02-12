# -*- coding: utf-8 -*-

import random
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017/')
coll = conn["test"].poem

#定义端口为8000
define("port", default=8000, help="run on the given port", type=int)

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
        res = list(coll.find({'content': {'$regex': query}}))

        if len(res) > 0:
            result = random.sample(res, 1)[0]
            del result["_id"]
            title = result['title']
            dynasty = result['dynasty']
            poet = result['poet']
            content = result['content']
        else:
            title = ''
            dynasty = ''
            poet = ''
            content = ''

        self.render('result.html', query=query, title=title, dynasty=dynasty, poet=poet, content=content)

# 主函数
def main():
    tornado.options.parse_command_line()
    # 定义app
    app = tornado.web.Application(
            handlers=[(r'/query', QueryHandler), (r'/result', ResultHandler)], #网页路径控制
            template_path=os.path.join(os.path.dirname(__file__), "templates") # 模板路径
          )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

main()