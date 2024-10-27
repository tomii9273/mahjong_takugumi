# リンクミス修正スクリプト
# https://github.com/tomii9273/mahjong_takugumi/pull/48

import os

# フォルダのパスを指定
folder_path = "."

# 置換前と置換後の文字列
old_string = 'guest_method.html"'
new_string = '../guest_method.html#cost_value"'

cnt = 0
# フォルダ内のすべてのHTMLファイルを対象に処理
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        # ファイルの内容を読み込んで文字列を置換
        with open(file_path, "r", encoding="utf-8") as file:
            file_data = file.read()

        # 置換処理
        new_data = file_data.replace(old_string, new_string)

        # 上書き保存
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_data)

        # cnt += 1
        # if cnt == 5:
        #     break

print("置換が完了しました。")
