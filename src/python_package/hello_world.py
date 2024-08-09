import asyncio
from aiohttp import web,web_request
from khl import Bot,Message
import json
from typing import Union


#import neuro_bot.hello_nero as hello_nero
def open_file(path: str):
    """打开path对应的json文件"""
    with open(path, 'r', encoding='utf-8') as f:
        tmp = json.load(f)
    return tmp

#todo 打开config要从父级目录开始选取
config = open_file("./config/config.json")
## websocket
bot = Bot(token = config['token'])
## 初始化节点
routes = web.RouteTableDef()




## 请求routes的根节点
@routes.get('/')
async def hello_world(request:web_request.Request):
    return web.Response(body="hello")

## 添加routes到app中
app = web.Application()
app.add_routes(routes)

#test command
# @bot.command(name = "nero")
# async def hello(msg:Message):
#     print("hello,i'm nero")

def test_rules(msg: Message):
    """这是一个命令规则，只有命令中包含khl才能被执行"""
    if 'kind' in msg.content:
        return True
    return False

@bot.command(name="neuro",rules=[test_rules])
async def test_func_cmd(msg: Message,text:str): # 以字符串匹配一个命令参数
    """测试命令"""
    try:
        print(f"get test func cmd from",msg.author_id)
        await msg.reply(f"fck window!")
    except:
        print("test func cmd",traceback.format_exc())

## 同时运行app和bot
HOST,PORT = '0.0.0.0',14725
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(
        asyncio.gather(web._run_app(app, host=HOST, port=PORT), bot.start()))
