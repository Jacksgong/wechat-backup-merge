# Wechat Backup Merge

> 你可以使用这个工具来合并与迁移微信Mac客户端的聊天记录备份文件到另外的文件夹。

[English Doc](https://github.com/Jacksgong/wechat-backup-merge/blob/master/README.md)

P.S. 这个脚本只在Mac下测试过。


## Dropbox的情况

我在每次通过Mac微信客户端备份号聊天记录以后，都会通过这个工具将聊天记录迁移合并到Dropbox可以自动备份到云端的目录。

## 如何使用?

#### 第一步. 第一次使用时创建配置文件

在第一次使用的时候，你需要在这个工具的根目录创建配置文件`path.conf`，下面是`example_path.conf`文件中的例子。

```bash
# src path
src=~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/Backup
# target path
target=~/Dropbox/wechat-backup/Backup
```

#### 第二步. 通过Mac客户端备份，然后执行脚本

![](https://github.com/Jacksgong/wechat-backup-merge/raw/master/arts/demo.gif)

```bash
python merge_wechat_backup.py
```

![](https://github.com/Jacksgong/wechat-backup-merge/raw/master/arts/demo.png)

## License

```
Copyright 2017 Jacks gong.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
