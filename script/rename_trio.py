# トリオ戦のファイル名が pair になっていたので trio に修正
# index.html のリンクは手動で修正
# ref: https://github.com/tomii9273/mahjong_takugumi/pull/46


import os

root_path = "..\\public\\trio_sen"

target_path = [os.path.join(root_path, f) for f in os.listdir(root_path)]  # 卓組 html・txt ファイルのパス

print(target_path)

for path in target_path:
    os.rename(path, path.replace("pair", "trio"))
