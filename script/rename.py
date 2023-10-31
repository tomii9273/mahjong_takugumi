# 卓組のファイル名を分かりやすいものに変換するスクリプト
# ref: https://github.com/tomii9273/mahjong_takugumi/pull/12
# public フォルダで実行する

import os
import re
import sys

DIR_BEFORE = "nuke8"
DIR_AFTER = "nukeari_8and1_sen"
# SUFFIX_AFTER = "souatari"

os.makedirs(DIR_AFTER, exist_ok=True)


def rewrite_line(line):
    """html の 1 行を書き換え、ファイル名の変更も行う"""
    # match = re.match(rf'        <a href="{DIR_BEFORE}/(\d+){DIR_BEFORE}\.txt">(\d+)卓(\d+)人(\d+)戦</a><br />\n', line)  # 個人戦など
    # match = re.match(
    #     rf'        <a href="{DIR_BEFORE}/(\d+){DIR_BEFORE}\.txt">(\d+)卓(\d+)人(\d+)トリオ (\d+)戦</a><br />\n', line
    # )  # ペア戦など
    # match = re.match(
    #     rf'        <a href="{DIR_BEFORE}/(\d+)taku(\d+)nin8and1sen\.txt">(\d+)卓(\d+)人</a><br />\n', line
    # )  # 抜け番あり
    match = re.match(rf'        <a href="3ma/(\d+)sou3ma\.txt">(\d+)卓(\d+)人(\d+)戦</a><br />\n', line)  # サンマ

    if match:
        print(match.groups())
        # num1, num2, num3, num4 = match.groups()  # 個人戦など
        # num1, num2, num3, num4, num5 = match.groups()  # ペア戦など
        # num1, num2, num3, num4 = match.groups()  # 抜け番あり
        # assert num1 == num3 and num2 == num4  # 抜け番あり
        num1, num2, num3, num4 = match.groups()  # サンマ

        # if int(num1) >= 14:
        #     return line

        # 個人戦など
        # new_format = f'        <a href="{DIR_AFTER}/{num2}taku_{num3}nin_{num4}sen_{SUFFIX_AFTER}.txt">{num2}卓{num3}人{num4}戦</a><br />\n'
        # os.rename(
        #     f"{DIR_BEFORE}/{num1}{DIR_BEFORE}.txt", f"{DIR_AFTER}/{num2}taku_{num3}nin_{num4}sen_{SUFFIX_AFTER}.txt"
        # )

        # ペア戦など
        # path_after = f"{DIR_AFTER}/{num2}taku_{num3}nin_{num5}sen_{num4}pair.txt"
        # new_format = f'        <a href="{path_after}">{num2}卓{num3}人{num4}トリオ {num5}戦</a><br />\n'
        # os.rename(f"{DIR_BEFORE}/{num1}{DIR_BEFORE}.txt", path_after)

        # 抜け番あり
        # path_after = f"{DIR_AFTER}/{num1}taku_{num2}nin_8and1sen.txt"
        # new_format = f'        <a href="{path_after}">{num3}卓{num4}人</a><br />\n'
        # os.rename(f"{DIR_BEFORE}/{num1}taku{num2}nin8and1sen.txt", path_after)

        # サンマ
        path_after = f"3ma/{num2}taku_{num3}nin_{num4}sen.txt"
        new_format = f'        <a href="{path_after}">{num2}卓{num3}人{num4}戦</a><br />\n'
        os.rename(f"3ma/{num1}sou3ma.txt", path_after)

        # sys.exit()
        return new_format
    else:
        return line


# テスト
# line = '<a href="k/4k.txt">4卓16人5戦</a><br />'
# print(rewrite_line(line))

html_name = "index.html"

# 元のHTMLファイルを読み込む
with open(html_name, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 各行にrewrite_line関数を適用する
new_lines = [rewrite_line(line) for line in lines]

# 結果を新しいファイルに保存する
with open(html_name, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("完了")
