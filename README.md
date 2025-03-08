# **Masto OSINT Tool**

<img width="999" alt="Masto_logo" src="https://user-images.githubusercontent.com/104733166/200212151-c5eea622-adfe-4209-ad43-f667f743e5fd.png">

<br>

## Stargazers over time
[![Stargazers over time](https://starchart.cc/C3n7ral051nt4g3ncy/Masto.svg?variant=adaptive)](https://starchart.cc/C3n7ral051nt4g3ncy/Masto)

<br>

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 <img width="77" src="https://user-images.githubusercontent.com/104733166/201745432-e10240ca-a742-40d8-98e4-1b83a011d159.png">
[![security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![MIT License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/C3n7ral051nt4g3ncy/Masto/blob/master/LICENSE)
<img src="https://img.shields.io/github/v/tag/C3n7ral051nt4g3ncy/Masto?color=bright%20green&label=Version&logo=github">
<img src="https://img.shields.io/github/stars/C3n7ral051nt4g3ncy/Masto?color=bright%20green&logo=github">
<img src="https://img.shields.io/github/forks/C3n7ral051nt4g3ncy/Masto?color=bright%20green&logoColor=white&logo=github">
<img src="https://img.shields.io/github/last-commit/C3n7ral051nt4g3ncy/MAsto?color=bright%20green&label=Last%20commit">
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![PyPI version](https://badge.fury.io/py/masto.svg)](https://badge.fury.io/py/masto)

</div>

<br>

## 🐘 **About Masto**

**Masto provides information/intelligence on [Mastodon.social](https://mastodon.social) users and fediverse instances (servers).** <br>
Masto OSINT Tool has been added as a Python package on PyPI --> https://pypi.org/project/masto/ 
- Latest version --> https://pypi.org/project/masto/2.0.5/

<br>

## 🚀 **Masto capabilities**
**Masto OSINT Tool** helps to:
- Find user ID
- Find exact username match across instances (the tool currently pulls many accounts with the username **```OSINT```**, whereas the mastodon.social (browser search bar) returns one result, as well as returning unreliable results, such as accounts that only start with ```osint```
- Find all accounts belonging to a user without logging in to Mastodon (**Mastodon requires users to log in and after 5 results you get**: ```401 Search queries pagination is not supported without authentication```
- Find username correlation (can't be found by browser)
- Check if the user is a bot
- Check if the account is a group
- Check if the account is locked
- Check if the user opted to be listed on the profile directory
- Get avatar link with an **additional choice** of opening the avatar within your browser
- Get profile creation date
- Get number of followers & following
- Get number of posts
- Get user last status date
- Get user's bio

### **Additional instance (server) feature**
**This is a nice feature**, if you type ```social.network.europa.eu``` on [Mastodon.social](https://mastodon.social/search) , you won't get a result as the instance is set to ```not discoverable```. <br>

**This function helps to**:
- Get information on an instance
- Get instance Admin ID
- Get instance email
- Get a short description
- Get server thumbnail link
- Get instance creation date
- Get instance language used
- Get instance admin count of followers and following
- Get instance admin last status date
- Get header image link and avatar link
- Get instance display name
- Get admin url
- Get admin avatar
- Check if instance admin account is locked
- Check if registration is required and if the admin needs to approve the request
- Check if the admin is a bot

<br>

## Masto Workflow

<img width="933" src="https://user-images.githubusercontent.com/104733166/201748872-60872350-3c70-4988-b3c0-31e3ca194a27.png">

<br>

![](assets/workflow.png)

<br>

## 🛠️ **Installation**

### Using PyPI

https://pypi.org/project/masto/

```pip install masto==2.0.5```

<br>

### Using GitHub

```bash
git clone https://github.com/C3n7ral051nt4g3ncy/Masto.git
cd masto
python3 setup.py install
```

<br>

## 👨‍💻 **Usage**


- Help:
```masto -h``` 

- Search for user
```masto -user {username}```

- Search for instance
```masto -instance {instance_name}```

<br>

## ⭐ **Tool use cases**

| **Use case 1**    | **Searching for a user and bypassing the profile directory opt-out**|
| ----------------  |:------------------------------------------------------------------:|

- Tried searching via browser both terms `Webbreacher` and `@Webbreacher` **1 result** --> `@Webbreacher@mastodon.social`
- Searched `Webbreacher` on **Masto**: **3 results** --> ✅ 3 accounts found
- On the `counter.social` profile, `@Webbreacher's` settings are --> user opted to be on the profile directory = `False`, this is why the browser search didn't find the counter.social profile!

🪄 **Masto successful outcome**: **Masto found all 3 accounts**.

<br>
<br>

|**Use case 2**    | **Searching without getting a 401 error**|
| ---------------- |:----------------------------------------:|

- Many people don't want an account on Mastodon, and if you don't have an account, you can search on Mastodon, but you will only get 5 results.
- Clicking on `load more` will give you a 401 error and request for the user to log in.

🪄 **Masto successful outcome**: **You can use Masto without logging in to Mastodon**, you won't get a 401 error.

<br>
<br>

|**Use case 3**    | **Getting information on locked instances**:|
| ---------------- |:-------------------------------------------:|

- Tried searching for the instance [0sint.social](https://0sint.social/about), there isn't much information via a browser search because it's locked.

🪄 **Masto successful outcome**: **Masto found more information on the instance and on the admin, including email address.**

<br>
<br>

|**Use case 4**    | **Conducted a username search for Defcon**:|
| ---------------- |:-------------------------------------------:|

- Conducted a search with Masto for the username ```defcon```, the Mastodon API returned 2 user accounts.

🪄 **Masto successful outcome**: **Masto OSINT Tool picked up after the initial API search by doing a full scan and found 4 accounts.**

<br>

## 🐘 **Mastodon.social understanding**
The **same username** can be found across different instances(servers):
- example: ```@osint@mastodon.social``` | ```@osint@mstdn.social``` | ```@osint@counter.social```
- Finding the same username on different instances does not prove it's the same person behind each account.
- Each instance can only have **one unique username** in the server. Tip: verify your account with the `<a rel="me"` attribute which confirms you are behind the account, and will help avoid or detect impersonators.

<br>


## 👤 **Testing on known users and instances**

- For a username test, try: ```python3 masto.py -u Gargron```, the founder of [Mastodon.social](https://mastodon.social), this pulls a wopping 11 accounts!!! (keep in mind that the same username doesn't prove the 11 accounts belong to @Gargron {Gargron is the Mastodon Dev}).
- For an instance test, try: ```python3 masto.py -i social.network.europa.eu```

<br>

## :white_circle: **Mastodon API reliability issues**
- You may know of a valid user & have the link to the user's profile, you input the username on Masto but get no result.
- I asked the Mastodon Team about this api issue, they replied:
> There is no global search, the server will reply with what it knows about. If it has not encountered the account, it will not return it in search results.

- 🟢 **Masto v2.0 fixes this**, the scan of Masto's own json instances list comes in support of Mastodon's API and picks up on things the API missed.
- **v2.0 is 100% reliable** if the server is listed in the Masto ```fediverse_instances.json``` file.
- This fix is thanks to [@Webbreacher](https://github.com/WebBreacher) who suggested this feature.

<br>

## Community mentions about Masto

- <img width="33" src="https://user-images.githubusercontent.com/104733166/216791505-929a73be-cd20-4f6d-a6ac-a36c25426edd.png"> Featured on the [UK OSINT](https://www.uk-osint.net/mastodon.html) website. UK OSINT is headed by [Neil Smith](https://twitter.com/UKOSINT), a true OSINT legend who has been using the internet as an investigative tool for well over 20 years.


- <img width="33" src="https://user-images.githubusercontent.com/104733166/210180709-87e0bc2e-a228-4b05-b026-6119b6c19073.png"> Featured in [Week in OSINT](https://sector035.nl/articles/2022-45) `#2022-45` by [@Sector035](https://github.com/Sector035) 

- <img width="33" src="https://user-images.githubusercontent.com/104733166/210180760-3e26b745-8796-4a0d-a723-8aa313731346.png"> Featured in the [OSINT Stuff Tool Collection](https://cipher387.github.io/osint_stuff_tool_collection/) by [@cipher387](https://github.com/cipher387) 

-  <img width="33" src="https://user-images.githubusercontent.com/104733166/210180596-6f3efce3-6966-4759-91fa-f31020383bcd.png"> Mentionned by [@DailyOsint](https://twitter.com/DailyOsint/status/1604827757426475008?s=20&t=W0v5uwWLaXgtQ1Ncn3G0Qg) 

- <img width="33" src="https://user-images.githubusercontent.com/104733166/210181085-67d0a680-a725-4cfc-8b55-1839aa930d60.png"> Mentionned by [@Treadstone71](https://twitter.com/Treadstone71LLC) 

- <img width="33" src="https://user-images.githubusercontent.com/104733166/212393361-84eb5aef-4565-4d87-9417-4ceee927c5c1.png"> Mentionned in this [Secjuice investigation](https://www.secjuice.com/mastodon-child-porn-pedophiles)  

- <img width="33" src="https://user-images.githubusercontent.com/104733166/224481685-a49857be-090e-4e36-99e7-ede1937fdd00.png"> Mentionned in [MAG'OSINT March 2023 Issue](https://www.aege.fr/global/gene/link.php?news_link=2023113354_mag-osint-13-aege.pdf&fg=1)  



<br>

## 🙏 **Thanks**!

<img width="33" src="https://github.com/user-attachments/assets/5ed20401-76dd-49c9-8184-0690607ac7f6"> A great big thanks to [@hippiiee](https://github.com/hippiiee) for radically changing Masto's speed, by adding asynchronous functions to run multiple requests at the same time ! 

<img width="33" src="https://user-images.githubusercontent.com/104733166/201990127-2b7b4f03-ba6a-43fa-a8ef-7ba164685ee2.png"> Huge thanks to [@EduardSchwarzkopf](https://github.com/EduardSchwarzkopf) for all his contributions to **Masto OSINT Tool**.

<img width="33" src="https://user-images.githubusercontent.com/104733166/201990241-3dfd2022-7eab-4c57-88e5-3567376b84fa.png">  Thanks to [@Webbreacher](https://github.com/WebBreacher) for his input, help and ideas. I learn a great deal from him, and he is a great instructor & inspiring person.

<img width="33" src="https://user-images.githubusercontent.com/104733166/204681183-8702ba59-3419-4f8d-a3a3-18f5b7b441a3.png"> Thanks to [sthierolf](https://github.com/sthierolf) for contributing

<img width="33" src="https://user-images.githubusercontent.com/104733166/201990360-337c1d05-031a-4210-ae34-80503bae1981.png">  Thanks to [@Roman-Kasianenko](https://github.com/Roman-Kasianenko) for his help.


<br>

## 📝 **License**

[MIT License](https://opensource.org/licenses/MIT) <br>
*Tool made for the OSINT and Cyber community, feel free to contribute  **```code```** .*

<img width="66" src="https://user-images.githubusercontent.com/104733166/200310377-be6d8187-8366-4968-b730-a5c215b310ec.png">

---

## **Maltego Transform**

A Maltego transform was made at the beginning of March 2025, and you can find the instructions here: https://github.com/C3n7ral051nt4g3ncy/Masto_Maltego_Transform
