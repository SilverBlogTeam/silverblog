由于研究内网穿透用到了 vpn，由于各种原因，pptp 连接并不是很稳定，所以本人就想了个办法来解决这个问题。
由于我们知道，pptp 的连接用到了 ppp 的支持，所以说，只要写一个程序来监控 ppp 的进程就可以达到 pptp 断线重拨的效果。由于 linux 有个特点，就是当进程在运行的时候，会生成一个 pid 文件。所以我们只要监控这个 pid 文件是否存在。就可以了解 pptp 的状态。
以下是一段很短的代码：

<pre><code>
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
pf ="/var/run/ppp0.pid"
if not(os.path.exists(pf)):
    os.system("echo disconnet pptp")
    os.system("echo restart")
    log_file = open('/home/log/pptpd.log','a')
    today = time.strftime('%Y-%m-%d')
    print >>log_file,'时间：{0}  重置 pptp 连接'.format(today)
    os.system("sudo pptpsetup --create server --server vpn地址  --username vpn用户名 --password vpn密码 --encrypt --start")
</code></pre>

将上面的代码保存为*.py 文件，并且在 root 的 crontab 中设定每分钟执行一次，就可以检测断线和自动重拨了。如果您在使用 pppoe 虚拟拨号上网的话，那么请修改 pf 的文件名称。
2015-02-21更新
以上代码会有一个问题，就是同个 vpn 下的主机只能和 pptp 服务器联通而无法和其他主机互相访问。经过研究发现是默认网关的设置没有更新导致的。所以需要增加默认网关修改的部分。代码如下：
<code>os.system("route add default gw vpn服务器内网地址")</code>
<code>os.system("route del default gw 原默认网关地址")</code>
这样设置就能将所有流量发送至 pptp。同时，vlan 内的其他主机也能正常访问了。
