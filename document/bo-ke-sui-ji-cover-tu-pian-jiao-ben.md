以下是2015-10-02的更新

服务器程序开源了！现在直接上 Github 就能下载到安装程序。

https://github.com/qwe7002/OneAnime

为了提高网站效率，特别设计了一个 python 版本

首先你需要安装Wand扩展，使用 JPG 格式可以节约流量带宽和提高加载速度。

<code>pip install wand</code>

您需要安装以下支持：

<code>apt-get install libmagickwand-dev</code>

然后你可以使用 git clone 或者 wget 等方法把仓库下载下来

<code>git clone https://github.com/qwe7002/OneAnime.git</code>

具体安装以及使用说明请参考README.md文件

感谢 Deluxghost 的程序重写
<hr>
最近嫌自己博客的顶部图片过于单调，于是就开了个坑。做了个自动随机显示图片的php程序。以下是源代码。将这个文件保存为index.php并建立一个名为 img的子目录，在下面放上你想随机显示的图片就可以了。

<pre><code>&lt;?php
function getFileList($directory) {
    $files = array();
    if(is_dir($directory)) {
        if($files = scandir($directory)) {
          $files = array_slice($files,2);
        }
}
    return $files;
}
$file=getFileList('img/'); //获取目录文件列表 
$random=rand(0,count($file)-1); //取一个随机数，最大值为文件数量-1 
if(substr($file[$random],-3)=='jpg'||substr($file[$random],-3)=='jpeg') header("Content-type:image/jpeg"); //检测文件格式，输出正确的文件信息
if(substr($file[$random],-3)=='png') header("Content-type: image/png"); 
readfile("img/".$file[$random]); //读取文件
?&gt; </code></pre>
