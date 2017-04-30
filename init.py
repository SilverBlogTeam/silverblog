import json
import os.path

import memcache
from flask import Flask, abort

from common import file, page, console

# Global Var
system_config = None
menu_list = None
rss = None
restful_switch = False
page_name_list = list()
template_config = None
cache_switch = False
page_list = None
mc = None
cache_list = list()
app = Flask(__name__)


@app.route('/manage/reload_config')
def load_config():
    global system_config, menu_list, rss, restful_switch, page_name_list, template_config, cache_switch, mc, page_list
    console.log("info", "Loading configuration")
    system_config = json.loads(file.read_file("./config/system.json"))
    system_config["API_Password"] = None

    page_list = json.loads(file.read_file("./config/page.json"))

    if os.path.exists("./config/menu.json"):
        menu_list = json.loads(file.read_file("./config/menu.json"))

    if os.path.exists("./document/rss.xml"):
        rss = file.read_file("document/rss.xml")

    if "Restful_API" in system_config:
        if system_config["Restful_API"]:
            restful_switch = True

    for item in page_list:
        page_name_list.append(item["name"])

    cache_switch = system_config["Cache"]
    if cache_switch:
        console.log("info", "Connect memcache...")
        mc = memcache.Client([system_config["Memcached_Connect"]], socket_timeout=500, debug=0)
        console.log("info", "Clear the Memcache data")
        mc.flush_all()

    if os.path.exists("./templates/{0}/config.json".format(system_config["Theme"])):
        template_config = json.loads(file.read_file("./templates/{0}/config.json".format(system_config["Theme"])))
    console.log("Success", "load the configuration file successfully")
    return "Reload the configuration file successfully"


load_config()


# Subscribe
@app.route("/rss")
@app.route("/feed")
def load_krss():
    return rss, 200, {'Content-Type': 'text/xml; charset=utf-8'}


@app.route("/")
@app.route("/<file_name>")
@app.route("/<file_name>/")
@app.route('/index/p/<int:page_index>')
@app.route('/index/p/<int:page_index>/')
def route(file_name="index", page_index=1):
    result = None
    page_index_url=""
    if file_name=="index":
        page_index_url = "/p/{0}".format(str(page_index))
    page_url = "/{0}{1}".format(file_name, page_index_url)

    if cache_switch and page_url in cache_list:
        console.log("info", "Trying to get cache: {0}".format(page_url))
        result = mc.get(page_url)

    if result is None:
        console.log("info", "Trying to build: {0}".format(page_url))
        if restful_switch:
            result = page.build_restful_result(file_name, system_config, page_list, page_name_list, menu_list)
        else:
            if file_name == "index":
                result, row = page.build_index(page_index, system_config, page_list, menu_list, False, template_config)
            if os.path.exists("document/{0}.md".format(file_name)):
                result = page.build_page(file_name, system_config, page_list, page_name_list, menu_list, False,
                                         template_config)

    if result is not None:
        if cache_switch and page_url not in cache_list:
            console.log("info", "Writing to cache: {0}".format(page_url))
            cache_list.append(page_url)
            mc.set(page_url, result)
        console.log("Success", "Get success: {0}".format(page_url))
        return result
    console.log("Error", "Can not build: {0}".format(page_url))
    abort(404)
