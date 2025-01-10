#!/bin/bash

# 変更をステージングエリアに追加
git add .

# 現在の日付と時刻を取得
NOW=`date +"%Y-%m-%d %H:%M:%S"`

# コミット作成。メッセージには上記で取得した日付と時刻を使用。
git commit -m "$NOW"

# リモートリポジトリにプッシュ
git push origin main

git fetch origin main
git merge origin/main
git push origin main