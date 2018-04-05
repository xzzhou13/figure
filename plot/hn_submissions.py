import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'#Hacker News上当前最热门的文章的ID
r = requests.get(url)
print('Status code:', r.status_code)
results_list = r.json()
#print(results)
submission_dicts = []
for paper_id in results_list[:10]:
    url = ('https://hacker-news.firebaseio.com/v0/item/'+str(paper_id)+'.json')
    submission_r = requests.get(url)
    #print(submission_r.status_code)
    result_dict = submission_r.json()

    submission_dict = {
        'title': result_dict['title'],
        'link': 'http://news.ycombinator.com/item?id='+str(paper_id),
        'comments': result_dict.get('descendants', 0)#有些文章ID的返回字典中没有‘descendants’，可以用字典名.get()方法处理
                                                    #当指定键存在时返回与之相关连的值，不存在时返回指定的值，这里是0
    }
    submission_dicts.append(submission_dict)

#submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)#按comments大小进行降序排序
title, plot_dict = [], []
comments = []
for submission_dict in submission_dicts:
    title.append(submission_dict['title'])
    comments.append(submission_dict['comments'])
    label_dict = {
       'value': submission_dict['comments'],
       'xlink': submission_dict['link'],
    }
    plot_dict.append(label_dict)
#print(plot_label)

'''可视化'''
my_style = LS('#336633', base_style=LCS)#定制Bar的颜色风格，十六进制的RGB颜色，基本样式为LCS

my_config = pygal.Config()#配置图表外观
my_config.x_labels_rotation = 45 #使得x轴标签旋转45°
my_config.show_legend = False#关于图例显示与否的设置
my_config.title_font_size = 24#标题字体大小
my_config.major_label_font_size = 18#主标签字体大小
my_config.label_font_size = 14#副标签字体大小
#my_config.truncate_label = 15#将较长的name缩短为15个字符
my_config.show_y_guides = False
#my_config.width = 100#自定义宽度，使图表更充分的利用浏览器可用空间

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Articles on Hacker News'
chart.x_labels = title
#chart.add('', comments)#鼠标放在每个条形上，显示一个信息，因为comments是值列表
chart.add('', plot_dict)
chart.render_to_file('hn.svg')
