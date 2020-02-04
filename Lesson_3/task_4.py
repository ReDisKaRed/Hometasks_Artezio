"""импорт модуля"""
import xml.etree.ElementTree as ET


def show_node(node):
    """Выполняет преобразование и выводит максимальную вложенность."""
    child_depth = 0
    list_child = []
    for child in node:
        child_result = show_node(child)
        list_child.append(child_result[0])
        child_depth = max(child_depth, child_result[1]+1)
    node_dict = {'name': node.tag, 'children': list_child}
    return node_dict, child_depth


XML_STR = "<root><element1 /><element2 " \
          "/><element3><element4 /></element3></root>"
ROOT = ET.fromstring(XML_STR)
print(show_node(ROOT))
