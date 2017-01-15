from lib.parsers.wangyi_parser import WangyiParser

def createParser(name):
    if name == 'wangyi':
        return WangyiParser()
    
    return None