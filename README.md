# **Masto OSINT Tool**

<img width="999" alt="Masto_logo" src="https://user-images.githubusercontent.com/104733166/200212151-c5eea622-adfe-4209-ad43-f667f743e5fd.png">

<br>

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 <img width="77" src="https://user-images.githubusercontent.com/104733166/201745432-e10240ca-a742-40d8-98e4-1b83a011d159.png">
[![security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![MIT License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/C3n7ral051nt4g3ncy/Masto/blob/master/LICENSE) 
<img src="https://img.shields.io/github/v/tag/C3n7ral051nt4g3ncy/Masto?color=bright%20green&label=Version&logo=github">
[![HitCount](http://hits.dwyl.com/C3n7ral051nt4g3ncy/Masto.svg)](http://hits.dwyl.com/C3n7ral051nt4g3ncy/Masto) 
<img src="https://img.shields.io/github/stars/C3n7ral051nt4g3ncy/Masto?color=bright%20green&logo=github">
<img src="https://img.shields.io/github/forks/C3n7ral051nt4g3ncy/Masto?color=bright%20green&logoColor=white&logo=github">
<img src="https://img.shields.io/github/last-commit/C3n7ral051nt4g3ncy/MAsto?color=bright%20green&label=Last%20commit">
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

</div>


## 🐘 **About Masto**

**Masto provides information/intelligence on [Mastodon.social](https://mastodon.social) users and fediverse instances (servers).** 

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

```git clone https://github.com/C3n7ral051nt4g3ncy/Masto```
<br>
<br>
```pip3 install -r requirements.txt```

<br>

## 👨‍💻 **Usage**

- Help:
```python3 masto.py -h```

- Searching for a user
```python3 masto.py -u {username}```

- Searching for an instance
```python3 masto.py -i {instance}```

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

- Featured in [Week in OSINT](https://sector035.nl/articles/2022-45) `#2022-45` by [@Sector035](https://github.com/Sector035)
- Part of the [OSINT Stuff Tool Collection](https://cipher387.github.io/osint_stuff_tool_collection/) by [@cipher387](https://github.com/cipher387)
- Mentionned on [D1 H4ck](https://www.facebook.com/techmaleficent)



<br>

## 🙏 **Thanks**!

<img width="33" src="https://user-images.githubusercontent.com/104733166/201990127-2b7b4f03-ba6a-43fa-a8ef-7ba164685ee2.png"> Huge thanks to [@EduardSchwarzkopf](https://github.com/EduardSchwarzkopf) for all his contributions to **Masto OSINT Tool**.

<img width="33" src="https://user-images.githubusercontent.com/104733166/201990241-3dfd2022-7eab-4c57-88e5-3567376b84fa.png">  Thanks to [@Webbreacher](https://github.com/WebBreacher) for his input, help and ideas. I learn a great deal from him, and he is a great instructor & inspiring person.

<img width="33" src="https://user-images.githubusercontent.com/104733166/204681183-8702ba59-3419-4f8d-a3a3-18f5b7b441a3.png"> Thanks to [sthierolf](https://github.com/sthierolf) for contributing

<img width="33" src="https://user-images.githubusercontent.com/104733166/201990360-337c1d05-031a-4210-ae34-80503bae1981.png">  Thanks to [@Roman-Kasianenko](https://github.com/Roman-Kasianenko) for his help.


<br>

## 📝 **License**

[MIT License](https://opensource.org/licenses/MIT) <br>
*Tool made for the OSINT and Cyber community, feel free to contribute  **```code```** .*

<img width="66" src="https://user-images.githubusercontent.com/104733166/200310377-be6d8187-8366-4968-b730-a5c215b310ec.png">
