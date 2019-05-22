# -*- coding: utf-8 -*-
__author__ = 'Administrator'
# 导入模块
# 日志设置
import  logging;logging.basicConfig(level=logging.INFO)
# 导入基础模块
import asyncio,os,json,time
from datetime import datetime
# 导入异步http
from aiohttp import  web

# 定义函数首页
def index(request):
    return web.Response(body=b'<h1>my blog</h1>',headers={'content-type':'text/html'})

# 定义初始化
@asyncio.coroutine
def init(loop):
    # 获得项目app服务器
    app=web.Application(loop=loop)
    # 获取路由
    app.router.add_route('GET','/',index)
    srv=yield  from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop=asyncio.get_event_loop();
loop.run_until_complete(init(loop))
loop.run_forever()