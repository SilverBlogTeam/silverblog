import asyncio
import json
import os
import shutil
import time

from common import console, file, page, post_map

@asyncio.coroutine
def async_build_page(file_name, system_config, page_info, menu_list, template_config):
    return page.build_page(file_name, system_config, page_info, menu_list, template_config)

@asyncio.coroutine
def build_post_page(filename, page_name_list, page_list, system_config, menu_list, template_config):
    if filename.endswith(".md"):
        file_name = filename.replace(".md", "")
        console.log("Build", "Processing file: ./static_page/post/{0}.html".format(file_name))
        page_info = None
        if file_name in page_name_list:
            this_page_index = page_name_list.index(file_name)
            page_info = page_list[this_page_index]
        content = yield from async_build_page(file_name, system_config, page_info, menu_list,
                                              template_config)
        if content is not None:
            yield from file.async_write_file("./static_page/post/{0}.html".format(filename.replace(".md", "")), content)

def publish():
    page_list = json.loads(file.read_file("./config/page.json"))
    menu_list = json.loads(file.read_file("./config/menu.json"))
    page_name_list = list()
    for item in page_list:
        page_name_list.append(item["name"])
    page_list = list(map(post_map.add_post_header, page_list))
    menu_list = list(map(post_map.add_post_header, menu_list))
    system_config = json.loads(file.read_file("./config/system.json"))
    for item in page_list:
        page_list[page_list.index(item)]["time"] = str(post_map.build_time(item["time"], system_config))
    template_config = None
    if os.path.exists("./templates/{0}/config.json".format(system_config["Theme"])):
        template_config = json.loads(file.read_file("./templates/{0}/config.json".format(system_config["Theme"])))

    if not os.path.isdir("./static_page"):
        os.mkdir("./static_page")
    os.system("cd ./static_page && rm -rf *")
    console.log("Build", "Processing file: ./static_page/index.html")
    content, row = page.build_index(1, system_config, page_list, menu_list, template_config)
    file.write_file("./static_page/index.html", content)
    if row != 1:
        os.mkdir("./static_page/index/")
        file.write_file("./static_page/index/1.html", "<meta http-equiv='refresh' content='0.1; url=/'>")
        for page_id in range(2, row + 1):
            console.log("Build", "Processing file: ./static_page/index/{0}.html".format(str(page_id)))
            content, row = page.build_index(page_id, system_config, page_list, menu_list, template_config)
            file.write_file("./static_page/index/{0}.html".format(str(page_id)), content)
    os.mkdir("./static_page/post/")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [
        build_post_page(filename, page_name_list, page_list, system_config,
                        menu_list, template_config)
        for filename in os.listdir("./document/")]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    shutil.copyfile("./document/rss.xml", "./static_page/rss.xml")
    shutil.copytree("./templates/{0}/static".format(system_config["Theme"]),
                    "./static_page/static/{0}/".format(system_config["Theme"]))
    if os.path.exists("./templates/static/user_file"):
        shutil.copytree("./templates/static/user_file", "./static_page/static/user_file")
    console.log("Success", "Create Github Page Success!")

    localtime = time.asctime(time.localtime(time.time()))
    import git
    if not os.path.exists("./static_page/.git"):
        console.log("Error", "[./static_page/] Not a git repository.")
        return False
    try:
        repo = git.Repo("./static_page")
        if not repo.is_dirty():
            console.log("Success", "Done")
            return True
        repo.git.add("--all")
        repo.git.commit("-m Publish Time：{0}".format(localtime))
    except git.exc.GitCommandError as e:
        console.log("Error", e.args[2].decode())
        return False
    console.log("Info", "Submitted to the remote.")
    remote = repo.remote()
    remote.push()
    console.log("Success", "Done")
    return True
