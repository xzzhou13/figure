import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'#该URL可直接在浏览器中打开查看数据格式
r = requests.get(url)#调用API请求
print('Status code:', r.status_code)#status_code是响应对象的一个属性，可用来检查API请求是否成功，状态码200表示请求成功
result_dict = r.json()#该Github的API请求返回JSON格式的信息，使用json()方法使之转换成Python字典
print(result_dict.keys())#一般不关key_incomplete_result，此键返回API请求是否完整，若为false，则说明API请求完全搜索

'''处理API响应'''
print('Total repositories:', result_dict['total_count'])#查看仓库总数
repo_dicts = result_dict['items']#字典列表，列表中的每一个元素均为字典
print('python repositories count:', len(repo_dicts))#查看python仓库的数量

'''研究第一个仓库'''
# print('\nThe first python repository information')
# repo_dict = repo_dicts[0]#repo_dicts的第一个字典
# print('\nkeys:', len(repo_dict))
# for key in repo_dict.keys():
#     print(key)

'''研究每一个仓库的某几部分信息'''
# print('\nThe name owner stars repository description of every python repositories')
# for repo_dict in repo_dicts:
#     print('Name:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])
#     print()

'''注意：API调用存在速率限制，即在特定时间内可执行的请求数存在限制，可在浏览器中输入
http://api.github.com/rate_limit查看一下search的速率极限'''

'''研究仓库信息并可视化'''
plot_dicts = []#自定义显示工具，存放显示工具显示的内容，是一个字典列表
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],#项目的星值
        'label': str(repo_dict['description']),#项目的描述性信息，对于有些项目其描述可能为None，它没有decode方法
        'xlink': repo_dict['html_url'],#项目的链接
    }#注意：对于用在条形图上需要显示的内容，只能用字典存储，且字典的键只能是'value','label','xlink'
    plot_dicts.append(plot_dict)
#print(plot_dicts)

'''可视化'''
my_style = LS('#336699', base_style=LCS)#定制Bar的颜色风格，十六进制的RGB颜色，基本样式为LCS

my_config = pygal.Config()#配置图表外观
my_config.x_labels_rotation = 45 #使得x轴标签旋转45°
my_config.show_legend = False#关于图例显示与否的设置
my_config.title_font_size = 24#标题字体大小
my_config.major_label_font_size = 18#主标签字体大小
my_config.label_font_size = 14#副标签字体大小
my_config.truncate_label = 15#将较长的name缩短为15个字符
my_config.show_y_guides = False
#my_config.width = 100#自定义宽度，使图表更充分的利用浏览器可用空间

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most_Starred Python Project on GitHub'
chart.x_labels = names
#chart.add('', stars)#鼠标放在每个条形上，显示一个信息，因为stars是值列表
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
