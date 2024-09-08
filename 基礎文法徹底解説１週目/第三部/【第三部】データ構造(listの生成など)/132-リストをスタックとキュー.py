from collections import deque

fukui = []
fukui.append('fukui')
fukui.append('sakai')
fukui.append('maruoka')
fukui.append('harue')
fukui.append('awara')
fukui.append('mikuni')
fukui.append('matsuoka')
fukui.append('eiheiji')
fukui.append('kamishihi')
fukui.append('katsuyama')
fukui.append('oono')
fukui.append('izumi')

fukuis = deque(fukui)
print(fukuis.popleft())
print(fukuis.popleft())
print(fukuis.popleft())
print(fukuis.popleft())
print(fukuis)
print(fukui)