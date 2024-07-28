# 全卓組 (html) を確認し、チーム戦・ペア戦・トリオ戦にチーム番号の列を追加
# 選手番号の列は「選手n」から「n」に変更
# https://github.com/tomii9273/mahjong_takugumi/pull/41

import os

root_path = "..\\public"

dirs = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]

target_path = []  # チーム戦・ペア戦・トリオ戦の卓組 html ファイルのパス
for d in dirs:
    target_path += [
        os.path.join(root_path, d, f)
        for f in os.listdir(os.path.join(root_path, d))
        if f.endswith(".html") and ("team" in f or "pair" in f or "trio" in f)
    ]

# print(target_path)
# exit()

for path in target_path:

    # if "4taku_16nin_4sen_4team" not in path:
    #     continue

    with open(path, "r", encoding="utf-8") as f:
        ar = []
        for line in f.readlines():
            ar.append(line)

    cnt = 0
    for ind in range(len(ar)):
        line = ar[ind]
        if "        <td>選手" in line:
            # print("player")
            if "4team" in path:
                team_num = cnt // 4 + 1
            elif "3team" in path or "trio" in path:
                team_num = cnt // 3 + 1
            elif "pair" in path:
                team_num = cnt // 2 + 1
            else:
                raise ValueError("Invalid path")
            ar[ind] = f"        <td>{team_num}</td>\n" + line.replace("選手", "")
            cnt += 1
        elif "        <td></td>" in line:
            if "4team" in path or "3team" in path:
                col = "チーム"
            elif "trio" in path:
                col = "トリオ"
            elif "pair" in path:
                col = "ペア"
            else:
                raise ValueError("Invalid path")
            ar[ind] = f"        <td>{col}番号</td>\n        <td>選手番号</td>\n"

    with open(path, "w", encoding="utf-8") as f:
        for line in ar:
            f.write(line)
            # f.write("\n")
