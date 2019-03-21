# pyBeiHangClassTable
![](https://img.shields.io/badge/BUAAHub-qualified-brightgreen.svg)

pyBeiHangClassTable是一个获取北航学生的课程表，并将其转换成可被各种日历服务导入的日历文件的工具。

## 安装与运行
pyBeiHangClassTable 依赖 `selenium` 运作。
```console
$ pip install selenium
```
欲运行，在终端键入
```console
$ python main.py
```
根据提示操作，便能生成课程表文件，保存为 `classCal.ics`。

## 配置文件
修改 `config.py` 的内容，便能做到自动登录，选择课表等不同特性。

```python
# Edit this file to change settings
CONFIG = {
    'beginDate': '2019-02-25',
    # 学期的起始日期，格式为 %Y-%m-%d
    # 无论你实际上什么时候开学，这里都应当填入第一周的周一。

    # 'userName': 'yourUsername',
    # 'passWord': 'yourPassword',

    # 取消userName与passWord的注释，并填入用户名与密码，便能自动登录。
    # 如你所见，账户与密码都是明文保存的，因此不推荐使用自动登录。

    'default': True

    # default设置项用于决定是否默认下载最后一学期的课表。
    # 如果他为 False， 程序运行时，你需要手动选择学期。
}
```

## 我该如何导入
生成的日历文件可以导入任何一个网络日历提供商（一般来说他同时是邮件提供商），请进入你的邮箱找到日历功能，按提示操作。在导入时，推荐建立一个新的日历防止污染。

## 已知问题
由于没有什么高级 API，课表的解析是完全依靠正则表达式分析文本完成的。这意味着，如果课表本身出现了非标准的情况，他就会大概率死掉。

- 由于1873系第一学期课表过于复杂（不标准），解析会出现很大问题。
- 体育课无法获得精确的时间

因此，在添加课表到你的日历前，请务必仔细对照，以免不小心漏了什么课。