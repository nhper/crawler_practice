# crawler_practice
爬虫练习
```
本仓库中是对 https://scrape.center/ 网站的所有爬虫的练习
```
### ssr1 电影数据网站，无反爬，数据通过服务端渲染，适合基本爬虫练习。 -- ssr1.py
### ssr2 电影数据网站，无反爬，无 HTTPS 证书，适合用作 HTTPS 证书验证。
### ssr3 电影数据网站，无反爬，带有 HTTP Basic Authentication，适合用作 HTTP 认证案例，用户名密码均为 admin。
### ssr4 电影数据网站，无反爬，每个响应增加了 5 秒延迟，适合测试慢速网站爬取或做爬取速度测试，减少网速干扰。
### spa1 电影数据网站，无反爬，数据通过 Ajax 加载，页面动态渲染，适合 Ajax 分析和动态页面渲染爬取。
### spa2 电影数据网站，无反爬，数据通过 Ajax 加载，数据接口参数加密且有时间限制，适合动态页面渲染爬取或 JavaScript 逆向分析。
### spa3 电影数据网站，无反爬，数据通过 Ajax 加载，无页码翻页，下拉至底部刷新，适合 Ajax 分析和动态页面渲染爬取。
### spa4 新闻网站索引，无反爬，数据通过 Ajax 加载，无页码翻页，适合 Ajax 分析和动态页面渲染抓取以及智能页面提取分析。
### spa5 图书网站，无反爬，数据通过 Ajax 加载，有翻页，适合大批量动态页面渲染抓取。
### spa6 电影数据网站，数据通过 Ajax 加载，数据接口参数加密且有时间限制，源码经过混淆，适合 JavaScript 逆向分析。
### captcha1 对接滑动拼图验证码，适合滑动拼图验证码分析处理。
### captcha2 对接图标点选验证码，适合图标点选验证码分析处理。
### captcha3 对接图文点选验证码，适合图文点选验证码分析处理。
### captcha4 对接语序分析验证码，适合语序分析验证码分析处理。
### captcha5 对接空间推理验证码，适合空间推理验证码分析处理。
### captcha6 对接九宫格识图验证码，适合九宫格识图验证码分析处理。
### captcha7 对接普通图像验证码，干扰较少，适合 OCR 识别。
### captcha8 对接普通图像验证码，干扰较多，适合打码平台或深度学习处理。
### login1 模拟登录网站，登录时用户名和密码经过加密处理，适合 JavaScript 逆向分析。
### login2 对接 Session + Cookies 模拟登录，适合用作 Session + Cookies 模拟登录练习。
### login3 对接 JWT 模拟登录方式，适合用作 JWT 模拟登录练习。
### antispider1 对接 WebDriver 反爬，检测到使用 WebDriver 就不显示页面，适合用作 WebDriver 反爬练习。
### antispider2 对接 User-Agent 反爬，检测到常见爬虫 User-Agent 就会拒绝响应，适合用作 User-Agent 反爬练习。
### antispider3 对接文字偏移反爬，所见顺序并不一定和源码顺序一致，适合用作文字偏移反爬练习。
### antispider4 对接字体文件反爬，显示的内容并不在 HTML 内，而是隐藏在字体文件，设置了文字映射表，适合用作字体反爬练习。
### antispider5 限制单个 IP 访问频率 5 分钟最多 10 次，如果过多则会封禁 IP 10 分钟。
### antispider6 限制单个账号访问频率 5 分钟最多 10 次，如果过多则会暂停访问 10 分钟。
### antispider7 限制单个 IP 访问频率 5 分钟最多 10 次，同时限制单个账号访问频率 5 分钟最多 10 次，如果过多则会封禁 IP 或账号 10 分钟。
### antispider8 JavaScript 反爬，增加了接口处的无限 debugger 和定时循环 debugger。

