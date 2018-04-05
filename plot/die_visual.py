import pygal

from pack.die import Die

die1 = Die()
die2 = Die()
results = []

for i in range(0, 100):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_sides = die1.num_sides + die2.num_sides

for k in range(2, max_sides+1):
    frequency = results.count(k)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Results of rolling two Die6 dice 100 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequcencies of Result'

hist.add('D6+D6', frequencies)#add()方法接受一个标签和一个列表参数，列表即为每个Bar显示的信息
hist.render_to_file('dice_visual.svg')
