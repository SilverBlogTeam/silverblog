最近忙里偷闲完成了这款简单的wiki 系统，现在发布出来，欢迎各位提出意见。

## 简介
**SmartWiki** 是一个简单的，基于文件的 CMS 系统。SmartWiki 采用 Markdown 作为编辑语言，无需任何数据库。与同类产品相比，有着更高的性能。只要您拥有1MB 的PHP虚拟主机空间就可以搭建一个 CMS 系统。

## 注意
以下信息需要根据需要修改。

* 您需要更改 `config` 文件夹下的 `config.json` 文件，该文件为本程序的配置文件。 `Title` 为网站标题，`FooterInfo` 为页脚信息。我们希望您能保留 `Powered by SmartWiki.` 字样以证明您在自豪的使用 Smartwiki 建立网站。

```
{
 "Title":"SmartWiki",
 "FooterInfo":"&copy; Company 2015"
}
```

* 您可以根据您的需要修改 `config` 文件夹下的 `pages.json` 文件，该数组将为程序提供导航信息。其中的 `index` 为 Markdown 文档文件的文件名。您必须编写一个 `index.md` 文件作为本网站的首页。

您可以选择使用一个数组来表示一个分类下的子分类。例如：

```
{
	"index":"主页",
	"example":
	{
		"Title":"example",
		"the one":"page1"
	}
}
```

其中的 `example` 代表这个分类的类名称，所有该分类的Markdown文件需要以 `分类名称(example)/子分类名称(page1).md`的方式来存放。子分类数组中必须包含一个名为 `Title` 的键来描述这个分类所要显示的名称。

* 在 md 文档中，您可以在首个分割线之前定义本页的标题与副标题。例如：

```
#标题
副标题
***
```

您需要将以上代码写在文件的顶部，以便能够正确的解析到这些信息。

## 感谢
感谢优秀的开源 Markdown 库 `php-markdown` 以及优秀的前端框架 `Bootstrap`.

* [php-markdown](https://github.com/michelf/php-markdown)
* [Bootstrap](https://github.com/twbs/bootstrap)
* [amazeui](https://github.com/allmobilize/amazeui/)


## 参与开发
我们欢迎您在 SmartWiki 项目的 GitHub 上报告 issue 或者 pull request。

如果您还不熟悉GitHub的Fork and Pull开发模式，您可以阅读GitHub的文档（https://help.github.com/articles/using-pull-requests）获得更多的信息。

如果你想在这里显示您的副本，请联系 Email：qwe7002@hotmail.com

感谢 [@Rakume](https://github.com/kunr) 同学的优化。

## 版权
采用MIT协议分发

>Copyright (C) <year> <copyright holders>

>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

仓库地址：https://github.com/qwe7002/smartwiki( bootstrap 版本)
