import pygal
p = [
    {'value': 12000, 'label': 'aa'},
    {'value': 1200, 'label': 'bb'}

]
chart = pygal.Bar()
chart.add('', p)
chart.render_to_file('test.svg')
