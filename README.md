# exorium discord bot | Since 2020
----
### exorium information
exorium is a multifunctional bot used for many categories. The main aim for exorium was, and still is social commands. With a variety of commands and more being added regularly, we aim to ensure user experience to be at it's best and try to improve our commands as well as the bot as much as possible.

exorium started off as a small bot named Protogen, which was created by [BluewyDev](https://github.com/BluewyDev/) for own use. Later on the decision was made to give Protogen a new purpose: Social commands for [The Paw Kingdom](https://linktr.ee/pawkingdom). A while later the name was changed to ProtoPaw. Protopaw eventually moved to Heroku as host, where it was made public and [ChosenFate](https://github.com/Chosen-Fate) joined the team as developer. Shortly after [Etile](https://github.com/Etile0) provided us with a vps we could use to host Protopaw, a while after that, we changed the name to exorium.

---
### exorium team
**main developers:**
- [ChosenFate](https://github.com/Chosen-Fate/)

**LTD. developers**
- [Bench](https://github.com/Bench182/)

**Host & provider:**
- [Etile](https://github.com/Etile0/)
---
### contributions
Anyone is free to contribute to exorium as long as they follow the [Contribution guidelines](https://github.com/ThePawKingdom/exorium/blob/master/CONTRIBUTING.md). Contributions can be done through [forks](https://github.com/ThePawKingdom/exorium/network/members). In your fork you can edit, add and remove code. After you did that, you are always free to make a [pull request](https://github.com/ThePawKingdom/exorium/pulls/). They will then be reviewed by one of the [main developers](https://github.com/ThePawKingdom/exorium#exorium-team).

---
## Warning
**exorium is currently being rewritten into [cogs](https://github.com/ThePawKingdom/exorium/tree/cogs/). This could cause more downtime while it's being rewritten, as well as being able to cause more issues and errors. Of course we will try to keep this to the minimal, for as far as what we can do. But we can not guarantee this will go flawless. If you spot an error/issue or there's something else concerning that you think you need to report, please make an [issue](https://github.com/ThePawKingdom/exorium/issues).**

---
### Commands
All available commands are listed here. This list may not be fully up-to-date at all times.
Please report this in an issue if it's not complete, or make a [pull request](https://github.com/ThePawKingdom/exorium/pulls/) With a complete list. Note that for making a pull request you will need to [fork](https://github.com/ThePawKingdom/exorium/network/members) this repository first, and edit the fork's readme. Prefixes of this bot are `p/` and `p?`

* Syntax args surrounded by `<>` are required. 
* Syntax args surrounded by `()` are optional. 
* Any syntax with `...` means you can give several arguments.
* Crossed through commands are currently not working.

Commands, suggestions or features we still plan to add can be seen in our [TO DO project](https://github.com/ThePawKingdom/exorium/projects/1). If a command doesn't work, please make an [issue](https://github.com/ThePawKingdom/exorium/issues/). Furthermore, if you require support with something within exorium, please join our [support server](https://discord.gg/CEHkNky) and ask for support in it's support channel. 

#### Social commands
|Command                                                                      |Syntax                |
| :-------------------------------------------------------------------------: | :------------------: |
|[hug](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L179)     |`?hug <@user>...`     |
|[snuggle](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L173) |`?snuggle <@user>...` |
|[boop](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L191)    |`?boop <@user>...`    |
|[kiss](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L197)    |`?kiss <@user>...`    |
|[pat](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L185)     |`?pat <@user>...`     |
|[cuddle](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L215)  |`?cuddle <@user>...`  |
|[askproto](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L355)|`?askproto <arg>...`  |

|Command                                                                      |Syntax                |  
| :-------------------------------------------------------------------------: | :------------------: |
|[lick](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L203)    |`?lick <@user>...`    |
|[blush](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L251)   |`?blush (@user)...`   |
|[feed](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L266)    |`?feed <@user>...`    |
|[glomp](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L276)   |`?glomp <@user>...`   |
|[happy](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L286)   |`?happy (@user)...`   |
|[highfive](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L301)|`?highfive <@user>...`|
|[wag](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L307)     |`?wag (@user)...`     |

#### Moderation
|Command                                                                        |Syntax                       |description                                      |
| :---------------------------------------------------------------------------: | :-------------------------: | :---------------------------------------------: |
|[ban](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L364)       |`?ban <@user> <@reason>`     |permbans the mentioned user from the guild       | 
|[unban](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L384)     |`?unban <ID>`                |Unbans the provided user                         |
|[softban](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L416)   |`?softban <@user> <@reason>` |Bans and immediately unbans the mentioned user   |
|[kick](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L396)      |`?kick <@user> <@reason>`    |Kicks the mentioned user from the guild          |
|[warn](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L505)      |`?warn <@user> <@reason>`    |Logs a warn for the mentioned user               |
|[delwarn](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L515)   |`?delwarn <@user> <@reason>` |Remove a case from someones warning logs         |
|[warnings](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L528)  |`?warnings <@user>`          |See the mentioned user's logged warnings         |

#### Utility
|Command                                                                        |Syntax                       |Description                                      |
| :-------------------------------------------------------------------------:   | :-------------------------: | :---------------------------------------------: |
|[serverinfo](https://github.com/ThePawKingdom/protogen/blob/master/main.py#L153)|`?serverinfo`                |Shows membercount and guild region               |
|[avatar](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L130)    |`?avatar <@user>`            |Shows the mentioned user's avatar                |
|[random](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L328)    |`?random <arg1> <arg2>...`   |Randomly picks one from the given args           |
|[decide](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L458)    |`?decide <arg>...`           |Lets people choose with :white_check_mark:	or :x:|
|[poll](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L437)      |`?poll <arg1>... (arg10)`    |Host a poll with up to 10 things to pick from    |
|[say2](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L486)      |`?say2 <args>...`            |Repeats what you said without an embed           |
|[say](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L477)       |`?say <args>...`             |Repeats what you said in an embed                |
|[id](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L92)         |`?id <@user/ID/name>`        |Shows the ID of the provided user                |

#### Bot related
|Command                                                                        |Syntax                       |Description                                      |
| :-------------------------------------------------------------------------:   | :-------------------------: | :---------------------------------------------: |
|[invite](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L75)     |`?invite`                    |Invite Protopaw through the given invite link    |
|[stats](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L83)      |`?stats`                     |The statistics of Protopaw (guilds & total users)|
|[links](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L143)     |`?links`                     |Links to things related to Protopaw & TPK        |
|[pings](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L44)      |`?ping`                      |Shows the bot's latency in seconds               |
|[help](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L60)       |`?help`                      |Shows all the commands and the Protopaw team     |
|[info](https://github.com/ThePawKingdom/exorium/blob/master/main.py#L335)      |`?info <command>`            |Shows information about an individual command    |

---
#### Selfhosting
Selfhosting exorium is not endorsed by the exorium team and is not recommended. We will not provide any type of support for editing or compiling the code in this repository. The source code is given here for education purposes, and so users can better contribute themselves as well as see how the bot works. If you do decide to selfhost exorium, please respect the [license](https://github.com/ThePawKingdom/exorium/blob/master/LICENSE)
