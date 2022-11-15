#!/usr/bin/python
# -*- coding: utf-8 -*-
# Code style         : Black
# Tool name          : Masto (v2.0)
# File name          : masto.py
# Author             : C3n7ral051nt4g3ncy(@OSINT_Tactical)


# Modules
import time
import json
from tqdm import tqdm
import sys
import webbrowser
import requests
import argparse
from w3lib.html import remove_tags


class Masto:
    def __init__(self) -> None:
        self.silent_mode = False
        self.__init_args()

    def __print_output(self, output: str):
        divider = "\033[32m-" * 77
        print(divider)
        print(output)
        print(divider)

    def __loading_bar(self):
        if not self.silent_mode:
            for _ in tqdm(range(10)):
                time.sleep(0.03)

    def __arg_list(self) -> list:
        return [
            {
                "flag": "u",
                "long_flag": "username",
                "help": "\033[32m\033[1m\ntarget username search across hundreds of Mastodon instances\033[0m",
                "action": "store",
            },
            {
                "flag": "i",
                "long_flag": "instance",
                "help": "\033[32m\033[1m\ninstance (server)\033[0m",
                "action": "store",
            },
            {
                "flag": "s",
                "long_flag": "silent_mode",
                "help": "\033[32m\033[1m\nsilent mode, just print the results\033[0m",
                "action": "store_true",
            },
        ]

    def __init_args(self):
        parser = argparse.ArgumentParser(
            description="Masto OSINT Tool help --> "
            "\033[32m\033[1m[For username]\033[0m: input without @ symbol |"
            "\033[32m\033[1m [For server]\033[0m: input without https in"
            " front | example: \033[35m\033[1minfosec.exchange\033[0m"
        )

        arg_list = self.__arg_list()

        for arg in arg_list:
            parser.add_argument(
                f"-{arg['flag']}",
                f"--{arg['long_flag']}",
                help=arg["help"],
                action=arg["action"],
            )

        # args settings
        args = parser.parse_args()

        for arg in arg_list:
            attr = arg["long_flag"]
            parse_arg = getattr(args, attr)
            setattr(self, attr, parse_arg)

    @staticmethod
    def intro():

        # banner
        print(
            """\033[34m
        ███╗   ███╗ █████╗ ███████╗████████╗ ██████╗
        ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗
        ██╔████╔██║███████║███████╗   ██║   ██║   ██║
        ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██║   ██║
        ██║ ╚═╝ ██║██║  ██║███████║   ██║   ╚██████╔╝
        ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝v2.0\033[0m"""
        )
        print("\033[34m\033[1mMastodon OSINT Tool\033[0m")
        print("by @C3n7ral051nt4g3ncy ")
        print(
            "https://ko-fi.com/tacticalintelanalyst\n"
            "BTC: bc1q66awg48m2hvdsrf62pvev78z3vkamav7chusde\n"
        )

    # search mastodon instances (servers)
    def instance_search(self):
        headers = {
            "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US;q=0.9,en,q=0,8",
            "accept-encoding": "gzip, deflate",
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
            "Chrome/104.0.0.0 Safari/537.36",
        }
        inst_url = f"https://{self.instance}/api/v1/instance.json"
        try:
            response = requests.request("GET", inst_url, headers=headers)
            inst_data = json.loads(response.text)
        except Exception as e:
            inst_data = {}

        self.__loading_bar()

        if not inst_data:
            print(
                f"\n\033[31mMastodon instance\033[1m [{self.instance}]\033[0m\033[31m NOT found!\033[0m"
            )
            return

        name = inst_data["uri"]
        print("\ninstance (server): ", name)
        title = inst_data["title"]
        print("title: \033[32m\033[1m", title)
        s_description = inst_data["short_description"]
        s_description = remove_tags(s_description)
        print("\033[0mdescription: ", s_description)
        det_descript = inst_data["description"]
        invalid_tags = [
            "<strong>",
            "</strong>",
            "<a href=",
            "target=",
            "</a>",
            "<a>",
            "_blank",
            ">",
            "<",
            '"',
            "br /",
            "|",
        ]
        for invalid_tag in invalid_tags:
            det_descript = det_descript.replace(invalid_tag, "")
        print("detailed description: ", det_descript)
        e_mail = inst_data["email"]
        print("\ninstance email: \033[32m\033[1m", e_mail)
        thumb = inst_data["thumbnail"]
        print("\033[0mserver thumbnail:", thumb)
        lang = inst_data["languages"]
        print("instance languages: ", lang)
        reg = inst_data["registrations"]
        print("registration needed: ", reg)
        reg_approve = inst_data["approval_required"]
        print("admin approval required: ", reg_approve)
        print("\ninstance admin information:")
        admin_data = inst_data["contact_account"]
        for key in [
            "id",
            "username",
            "acct",
            "display_name",
            "followers_count",
            "following_count",
            "statuses_count",
            "last_status_at",
            "locked",
            "bot",
            "discoverable",
            "group",
            "created_at",
            "url",
            "avatar",
            "header",
        ]:
            print(f"{key}: {admin_data[key]}")

    # search username with Mastodon API
    def username_search_api(self):
        url = f"https://mastodon.social/api/v2/search?q={self.username}"
        response = requests.request("GET", url)
        data = json.loads(response.text)

        self.__loading_bar()

        if response.text == ('{"accounts":[],"statuses":[],"hashtags":[]}'):
            print(
                f"\n\033[1m\033[31mTarget username: [{self.username}] NOT found using the Mastodon API!\033[0m"
            )
            return
        time.sleep(1)

        data = filter(
            lambda x: x.get("username").lower() == self.username.lower(),
            data["accounts"],
        )
        for index, intelligence in enumerate(list(data), start=1):

            if not self.silent_mode:
                print("\n\n══════════")
                print(f"\033[32m\033[1mAccount: {index}\033[0m")
                print("══════════\n")

            identity = intelligence["id"]
            lock = intelligence["locked"]
            pro_url = intelligence["url"]
            target_username = intelligence["username"]
            account = intelligence["acct"]
            dispn = intelligence["display_name"]
            creation_date = intelligence["created_at"]
            bot = intelligence["bot"]
            dscvr = intelligence["discoverable"]
            fwers = intelligence["followers_count"]
            fwing = intelligence["following_count"]
            posts = intelligence["statuses_count"]
            lastm = intelligence["last_status_at"]
            group = intelligence["group"]
            note = intelligence["note"]
            avt = intelligence["avatar"]

            print("user ID:\033[32m\033[1m", identity)
            print("\033[0mprofile url:", pro_url)
            print("account locked:", lock)
            print("username:", target_username)
            print("\033[0maccount:\033[32m\033[1m", account)
            print("\033[0mdisplay Name:\033[32m\033[1m", dispn)
            print("\033[0mprofile creation date:", creation_date)
            print("user is a bot:", bot)
            print("user opted to be listed on the profile directory:", dscvr)
            print("followers:", fwers)
            print("following:", fwing)
            print("number of posts:", posts)
            print("user last message date:", lastm)
            print("user is a group:", group)

            bad_tags = [
                "<p>",
                "</p>",
                "</a>",
                "</span>",
                "<span>",
                "<a href",
                '"',
                "<",
                ">",
                "class=",
                "rel=tag",
                "=",
                "relnofollow",
                "noopener",
                "noreferrer",
                "target_blankspan",
                "target_blank",
                "span",
                "invisible",
                "\u003e\u003c/a\u003e.",
                "\u003cbr",
            ]
            for bad_tag in bad_tags:
                note = note.replace(bad_tag, "")
            print("user bio:", note)
            print("user's avatar link:", avt)

            if not self.silent_mode:

                choice = input("\033[1mopen avatar in browser | [Y|N]: \033[0m")
                if choice in ["y", "Y", "YES", "yes"]:
                    webbrowser.open(avt)
                if choice in ["n", "N", "NO", "no"]:
                    continue

    # username search with the Masto OSINT Tool servers database
    def username_search(self):

        if not self.silent_mode:
            print("\n")
            print(
                f"Preparing to scan for target -->\033[32m\033[1m {self.username}\033[0m on the \033[32m\033[1m"
                f"Masto OSINT Tool servers database\033[0m\033[0m\n"
            )

        time.sleep(6)
        self.__loading_bar()

        headers = {
            "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US;q=0.9,en,q=0,8",
            "accept-encoding": "gzip, deflate",
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
            "Chrome/104.0.0.0 Safari/537.36",
        }

        response = requests.get(
            "https://raw.githubusercontent.com/C3n7ral051nt4g3ncy/Masto/master/fediverse_instances.json"
        )
        sites = response.json()["sites"]
        is_any_site_matched = False
        for site in sites:
            uri_check = site["uri_check"]
            site_name = site["name"]
            uri_check = uri_check.format(account=self.username)

            try:
                res = requests.get(uri_check, headers=headers)

                estring_pos = res.text.find(site["e_string"]) > 0

            except Exception as e:
                continue

            if res.status_code == 200 and estring_pos:
                is_any_site_matched = True

                if not self.silent_mode:
                    self.__print_output(
                        f"""\033[32m[+] \033[1mTarget found\033[0m\033[32m ✓ on:\033[1m{site_name}\033[0m\n\033[32m[+] Profile URL:\033[1m{uri_check}\033[0m"""
                    )
                else:
                    print(uri_check)

        if not is_any_site_matched:
            if not self.silent_mode:
                print(
                    f"\n\033[1m\033[31mTarget username: [{self.username}] NOT found on the Masto OSINT Tool servers database!\033[0m"
                )
        return is_any_site_matched


# main
if __name__ == "__main__":

    if len(sys.argv) == 1:
        Masto.intro()
        print(
            "You did not pass an argument | For Help --> \033[32m\033[1mpython3 masto.py -h\033[0m"
        )
        sys.exit(1)

    masto = Masto()

    if not masto.silent_mode:
        Masto.intro()

    # Loop Instance Search
    if masto.instance:
        while True:
            instance_found = masto.instance_search()

            yes_no = input("\nCheck another instance? [yes|no]: ")
            if yes_no.lower() == "no":
                break
            else:
                setattr(masto, "instance", input("type new instance: "))

    # Loop target username search across all instances with API and Masto OSINT tool database
    if masto.username:
        while True:
            api_user_found = masto.username_search_api()
            user_found = masto.username_search()

            yes_no = input("\nTry another username? [yes|no]: ")
            if yes_no.lower() == "no":
                break
            else:
                setattr(masto, "username", input("Type new username: "))
