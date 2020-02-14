# bilibili_PV_spider
如何提高B站(bilibili)的访问量呢？
这就是一个实现bilibili播放量增长的爬虫项目.

详细的代码形成思路可以参看[我的博客](http://www.harumonia.top/index.php/archives/215/)

### settings.py
这里存放了一些爬虫运行的关键信息.比如你想要增长哪些视频的播放量(aid_list,cid_list),你的uid,你的cookie(B站只有登录用户才能反复提高视频的播放量)

### simple_spider.py
这是最初版本的播放量增长爬虫,能够在单一用户模式下实现多个视频的播放量增长.效率很低,但是非常稳定.

### 后续更新
1. 完成对指定up主的所有视频(或者该up主的某个频道下的所有视频)的播放量增长爬虫
2. 基于模拟登陆的用户池
