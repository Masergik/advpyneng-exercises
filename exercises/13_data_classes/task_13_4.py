# -*- coding: utf-8 -*-
"""
Задание 13.4

Создать класс IPv4Network с использованием dataclass. У экземпляров класса должны быть
доступны:
* переменные: network, broadcast, hosts, allocated, unassigned
* метод allocate

Пример создания экземпляра класса:

In [3]: net1 = IPv4Network('10.1.1.0/29')

После этого, должна быть доступна переменная network:
In [6]: net1.network
Out[6]: '10.1.1.0/29'


Broadcast адрес должен быть записан в атрибуте broadcast:

In [7]: net1.broadcast
Out[7]: '10.1.1.7'

Также должен быть создан атрибут allocated в котором будет
храниться список с адресами, которые назначены на каком-то
устройстве/хосте. Изначально атрибут равен пустому списку:

In [8]: print(net1.allocated)
[]


Атрибут hosts должен возвращать список IP-адресов, которые входят в сеть,
не включая адрес сети и broadcast:

In [9]: net1.hosts
Out[9]: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5', '10.1.1.6']

Метод allocate ожидает как аргумент IP-адрес. Указанный адрес
должен быть записан в список в атрибуте net1.allocated и удален из списка unassigned:

In [10]: net1 = IPv4Network('10.1.1.0/29')

In [11]: print(net1.allocated)
[]

In [12]: net1.allocate('10.1.1.6')

In [13]: net1.allocate('10.1.1.3')

In [14]: print(net1.allocated)
['10.1.1.6', '10.1.1.3']


Атрибут unassigned возвращает возвращает список со свободными адресами:

In [15]: net1 = IPv4Network('10.1.1.0/29')

In [16]: net1.allocate('10.1.1.4')
    ...: net1.allocate('10.1.1.6')
    ...: net1.allocate('10.1.1.8')
    ...:

In [17]: net1.unassigned
Out[17]: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.5']

"""
