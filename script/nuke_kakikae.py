# 全卓組をチェックし、抜け番の表記を「nuke」→「--」に変更
# また、調整戦 (抜け番あり卓組の最終戦) に何も書かれていない場合、「--」を追加
# https://github.com/tomii9273/mahjong_takugumi/pull/41

import os
import sys

root_path = "..\\public"

dirs = [
    d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))
]

tg_path = []  # 全卓組ファイルのパス
for d in dirs:
    tg_path += [os.path.join(root_path, d, f) for f in os.listdir(os.path.join(root_path, d)) if f.endswith(".txt")]

# print(dirs)

for path in tg_path:
    has_nuke = False
    with open(path, "r") as f:
        ar = []
        for line in f.readlines():
            ar.append(list(line.split()))
            if "nuke" in ar[-1]:
                has_nuke = True

    if not has_nuke:
        continue

    max_len = max([len(line) for line in ar])
    for line in ar:
        for i in range(len(line)):
            if line[i] == "nuke":
                line[i] = "--"
        assert len(line) in (max_len-1, max_len)
        if len(line) == max_len-1:
            line += ["--"]
    # print(ar)

    with open(path, "w") as f:
        for i in range(len(ar)):
            for j in range(len(ar[i])):
                f.write(ar[i][j])
                f.write("\t")
            f.write("\n")
    # break
