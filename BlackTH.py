#此插件开源，禁止商业用途、非授权转载和非授权二次开发！
#引入模块
import json
import os
import mc

#变量声明
configf = 'plugins/BlackTH/config.json'
blacklistf = 'plugins/home/blacklist.json'
path = 'plugins/BlackTH'
ver = 1.0

#读取配置文件
def readconfig():
    try:
        with open(configf,'r',encoding='UTF-8') as f:
            d = f.read()
            global config
            config = json.loads(d)
            print('[INFO][BlackTH]BlackTH已经读取完毕配置文件！')
    except:
        print('[INFO][BlackTH]BlackTH读取配置文件错误，使用内置Config.Json')
        config = {"Autoupdatelist": False,"Autoupdateplugin": False}

#读取玩家黑名单
def readblacklist():
    try:
        with open(blacklistf,'r',encoding='UTF-8') as f:
            d = f.read()
            global blacklist
            blacklist = json.loads(d)
            print('[INFO][BlackTH]BlackTH已经读取完毕玩家黑名单！')
    except:
        blacklist = {}

#二次读取配置文件
def readconfig():
    try:
        with open(configf,'r',encoding='UTF-8') as f:
            d = f.read()
            global config
            config = json.loads(d)
    except:
        print('[INFO][BlackTH]BlackTH读取配置文件错误，使用内置Config.Json')
        config = {"maxhome": 6,"lastpos": False}

#二次读取玩家黑名单
def readblacklist():
    try:
        with open(blacklistf,'r',encoding='UTF-8') as f:
            d = f.read()
            global blacklist
            blacklist = json.loads(d)
    except:
        blacklist = {}

#写入文件
def Write_File(typea):
    with open(configf,'w',encoding='utf-8') as f:
        f.write(json.dumps(config,sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
    with open(blacklistf,'w',encoding='utf-8') as f:
        f.write(json.dumps(blacklist,sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
    read_config()
    read_blacklist()

#文件夹函数
def createFolder(Folderpath):
    try:
        fd = os.path.exists(Folderpath)
        if not fd:
            os.makedirs(Folderpath)
    except:
        print('[INFO][BlackTH]'+Folderpath+'创建失败...')




#首次启动创建文件
def firststart():
    if os.path.isfile(configf):
        readconfig()
    else:
        with open(configf,'w') as f:
            f.write(json.dumps({"Autoupdatelist": False,"Autoupdateplugin": False},sort_keys=True, 
                indent=4, 
                separators=(',', ': ')))
            print('[INFO][BlackTH]配置文件已经创建成功！')
    if os.path.isfile(blacklistf):
        readblacklist()
    else:
        with open(blacklistf,'w') as f:
            f.write('{}')
            print('[INFO][BlackTH]空白黑名单已经创建成功，请在minebbs上下载最新的黑名单！')
    print('[INFO][BlackTH]插件已成功加载！  作者：Chsmalldo18  Version:'+str(ver))
    print('[INFO][BlackTH]此插件禁止商业用途、非授权转载和非授权二次开发！此项目为公益项目！')

         

#获取玩家列表
def getPlayerNameList(e):
    global totalPlayer
    global playerNameList
    global playerList
    playerList = []
    playerNameList = []
    playerList = mc.getPlayerList()
    for i in playerList:
            playerNameList.append(i.name)
    totalPlayer = len(playerNameList)
mc.setListener('onPlayerJoin',getPlayerNameList)



#判断玩家与踢出玩家
while True:
    def kickPlayerNameisequaltoPlayerNameName():
        with open("temp.json",'r', encoding='UTF-8') as f:
            load_dict = json.load(f)
            key_value = blacklist(a.keys())
while True:
            if set(blacklist).intersection(set(playerNamelist)):
                mc.runcmd("kick" + mostAppearPlayerName + " 你是一名云黑玩家或被本服服主禁止进入服务器的玩家！")
            else:
                pass
            
#此插件开源，禁止商业用途、非授权转载和非授权二次开发！
#此插件开源，禁止商业用途、非授权转载和非授权二次开发！
#此插件开源，禁止商业用途、非授权转载和非授权二次开发！
