最近心血来潮，看到好多机油在raspiberry pi上驱动lcd1602等等的点阵字符屏幕，心里痒痒的。但是又怕gpio口接不好导致烧板子。权衡利弊，最后就选择了usb2lcd的方案。经过各种哦焦急等待，屏幕终于来了！由于卖家的教程是一个英文教程，相对于各位英文较差的小白而言阅读起来比较辛苦，这里我就花点时间吧配置教程中文化吧
驱动这个lcd屏幕，我们要安装的就是lcdproc这个软件了，这个软件自带有驱动和程序，只要安装上并且配置好就能够正常的使用。所以我们就先来安装这个程序。输入命令
<pre>
sudo apt-get update
sudo apt-get install lcdproc
</pre>
如果你是使用foroda、arch等yum系的系统的话，可以使用
<pre>
sudo yum update
sudo yum install lcdproc
</pre>
（注意，如果你用root登录的话，sudo就可以免了）等待安装完毕以后，就是本文的重点，配置文件。
首先我们先用nano打开配置文档
<pre>
sudo nano /etc/LCDd.conf
</pre>
然后找到
<pre>
# The following drivers are supported:
#   bayrad, CFontz, CFontz633, CFontzPacket, curses, CwLnx, ea65,
#   EyeboxOne, g15, glcdlib, glk, hd44780, icp_a106, imon, imonlcd,
#   IOWarrior, irman, joy, lb216, lcdm001, lcterm, lirc, lis, MD8800,
#   mdm166a, ms6931, mtc_s16209x, MtxOrb, mx5000, NoritakeVFD, picolcd,
#   pyramid, sed1330, sed1520, serialPOS, serialVFD, shuttleVFD, sli,
#   stv5730, svga, t6963, text, tyan, ula200, xosd
Driver=curses
并且把Driver=curses改为Driver=hd44780

# The following drivers are supported:
#   bayrad, CFontz, CFontz633, CFontzPacket, curses, CwLnx, ea65,
#   EyeboxOne, g15, glcdlib, glk, hd44780, icp_a106, imon, imonlcd,
#   IOWarrior, irman, joy, lb216, lcdm001, lcterm, lirc, lis, MD8800,
#   mdm166a, ms6931, mtc_s16209x, MtxOrb, mx5000, NoritakeVFD, picolcd,
#   pyramid, sed1330, sed1520, serialPOS, serialVFD, shuttleVFD, sli,
#   stv5730, svga, t6963, text, tyan, ula200, xosd
Driver=hd44780
</pre>
之后就是配置hd44780这个驱动了，找到[hd44780]，然后在这下面一共有如下几项，只要对照着改就可以了。注意最后的按钮设定一定要注意前缀，不然有可能出问题
<pre>
[hd44780]
ConnectionType=lcd2usb
Contrast=850
Brightness=800
OffBrightness=0
Keypad=yes
Backlight=yes
Size=16x2
KeyDirect_1=Enter
KeyDirect_2=Down
KeyDirect_3=Escape
</pre>
之后，按ctrl+x，保存配置，然后就大胆的输入reboot重启吧！
重启过后，插入显示屏并且输入
<pre>
sudo LCDd
sudo lcdproc
</pre>
就可以看到效果了。如果想开机启动的话，还可以把这两行命令加到rc.local中实现开机启动！
外部链接：

LCD2USB project: http://www.harbaum.org/till/lcd2usb/index.shtml
LCDProc project: http://www.lcdproc.org
