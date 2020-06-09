# -*- coding: utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

def parse_xml(web_data):          #解析传入的xml数据
    if len(web_data) == 0:        #数据为空
        return None
    xmlData = ET.fromstring(web_data)       #转化成可操作文本
    msg_type = xmlData.find('MsgType').text   #看Msg类型
    if msg_type == 'text':          #如果是文本类型，就调用文本处理操作
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    elif msg_type == 'voice':
	return VoiceMsg(xmlData)

class Msg(object):                  #对转化后的文本进行统一的基本操作
    def __init__(self, xmlData):                                  
        self.ToUserName = xmlData.find('ToUserName').text      #用户名
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text    #创建时间
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text
	

class TextMsg(Msg):        #如果是文本类型的数据
    def __init__(self, xmlData):    
        Msg.__init__(self, xmlData)   
        self.Content = xmlData.find('Content').text.encode("utf-8")   #文本内容获取（文本内容读取方式）

class VoiceMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.Recognition = xmlData.find('Recognition').text.encode("utf-8")

class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
