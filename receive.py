# -*- coding: utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

def parse_xml(web_data):   #解析传入的xml数据
    if len(web_data) == 0:       #如果为空
        return None
    xmlData = ET.fromstring(web_data)    #转换为可处理格式
    msg_type = xmlData.find('MsgType').text  #看是什么类型的数据
    if msg_type == 'text':       #如果是文本消息，则调用文本处理方法
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    elif msg_type == 'voice':
	return VoiceMsg(xmlData)

class Msg(object):     #对数据的基本处理
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text
	

class TextMsg(Msg):    #如果是文本消息
    def __init__(self, xmlData):   
        Msg.__init__(self, xmlData)  
        self.Content = xmlData.find('Content').text.encode("utf-8")   #获取文本内容

class VoiceMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.Recognition = xmlData.find('Recognition').text.encode("utf-8")

class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
