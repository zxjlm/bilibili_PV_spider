# bilibili_PV_spider
这是一个实现bilibili播放量增长的爬虫项目.

详细的代码形成思路可以参看[我的博客](http://www.harumonia.top/index.php/archives/215/)

### 2020年06月06日 更新内容
将列表从手动录入变为自动爬取

### 使用说明
1. 在 settings.py 文件中录入 cookies 的信息
2. (每隔一段时间运行一次即可)运行 info_getter.py 文件,获取tt的视频清单,清单将存储到本地,有效降低爬虫访问频率
3. 运行 simple_spider.py 文件,开始愉快地爬虫之旅~

### 后续更新
1. 完成对指定up主的所有视频(或者该up主的某个频道下的所有视频)的播放量增长爬虫
2. 基于模拟登陆的用户池
