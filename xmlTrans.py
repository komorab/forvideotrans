# 尝试解析xml文档，提取文本信息，过滤特定用户或者内容

from xml.dom.minidom import parse
import xml.dom.minidom


class XmlTree:
    """be used to build a tree about xml file"""
    def __init__(self, filename:str, filepath:str):
        self.filename = filename
        self.filepath = filepath
        pass


# 以下内容源自up主virworks，作为参考，有时间再写这个
domTree = parse("./aaa.xml")  # 读入XML文件
rootNode = domTree.documentElement
scs = rootNode.getElementsByTagName("sc")
ds = rootNode.getElementsByTagName("d")

for d in ds:  # 对于d类节点，是普通弹幕，把普通弹幕里的固定弹幕都修改成滚定弹幕
    temp = d.getAttribute("p").split(',')  # 将p属性的值用“，”隔开生成列表
    temp[1] = "1"  # 将弹幕类型改成滚动
    d.setAttribute("p", ','.join(temp))

for sc in scs:  # 对于sc类节点，根据信息生成d类节点
    new_node = domTree.createElement("d")  # 创建新的d类节点
    # 下一行设置弹幕的参数，字号放大到38号，颜色设置为红色，后面的参数都是乱写的，不影响
    new_node.setAttribute("p", sc.getAttribute("ts")+",4,38,16711680,1631362154590,0,165836540,0")
    # 下一样设置弹幕内容，在源内容前面加上【SC】
    text_value = domTree.createTextNode("【SC】" + sc.childNodes[0].data)
    # 下面三行完成节点创建并连接到根上
    new_node.appendChild(text_value)
    rootNode.appendChild(new_node)
    sc.parentNode.removeChild(sc)

with open('new.xml', 'w', encoding='utf-8') as f:  # 将新的XML文件保存好
    domTree.writexml(f, addindent='  ', encoding='utf-8')