'''绘制世界人口地图'''

from pygal_maps_world import maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
import json
import os

from pack.get_code import get_country_code

path = os.getcwd()
file = path + '\population_data.json'
with open(file) as f:
    pop_data = json.load(f)

cc_pop = {}
country_uncode = []
n = 0
for pip in pop_data:
    if pip['Year'] == '2010':
        country = pip['Country Name']
        population = int(float(pip['Value']))
        code = get_country_code(country)
        if code!='F':
            cc_pop[code] = population

'''根据人口数量将国家分组'''
cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in cc_pop.items():
    if pop < 10000000:
        cc_pop1[cc] = pop
    elif pop < 1000000000:
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))#查看每组有多少个国家

'''改变世界地图的样式（主要是颜色）'''
wm_style = RS('#996633', base_style=LCS)#定制map的颜色风格，十六进制的RGB颜色，基本样式为LCS
'''绘制世界人口地图'''
wm = maps.World(style=wm_style)
wm.title = 'World population in 2010, by country'
wm.add('0-10m', cc_pop1)
wm.add('10,-1bm', cc_pop2)
wm.add('>1bn', cc_pop3)
wm.render_to_file('population.svg')



