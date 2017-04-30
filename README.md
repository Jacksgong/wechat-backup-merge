# Wechat Backup Merge

> You can use this tool to merge and migrate Wechat backup files to another folder.

[中文文档](https://github.com/Jacksgong/wechat-backup-merge/blob/master/README-ZH.md)

P.S. This script is only tested on Mac.

## Dropbox Case

I use this tool to merge and migrate Wechat backup files to the Dropbox auto-backup folder to make it on cloud after backed up chat logs through Wechat Mac client each time.

## How To Use?

#### Step 1. Config On First Time

You need create the `path.conf` on the current tool directory file, below is the demonstrate which also on the `example_path.conf` file.

```bash
# src path
src=~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/Backup
# target path
target=~/Dropbox/wechat-backup/Backup
```

#### Step 2. Backup with Wechat Mac client and Execute tool

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
