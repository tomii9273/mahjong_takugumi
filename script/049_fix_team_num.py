import os

root_path = "..\\public"

dirs = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]

target_path = []  # チーム戦の卓組 html ファイルのパス
for d in dirs:
    target_path += [
        os.path.join(root_path, d, f)
        for f in os.listdir(os.path.join(root_path, d))
        if f.endswith(".html") and "team" in f
    ]


for path in target_path:
    print("path:", path)

    with open(path, "r", encoding="utf-8") as f:
        ar = []
        for line in f.readlines():
            ar.append(line)
    n_player = -1
    for line in ar:
        if '      <tr align="right">' in line:
            n_player += 1

    if "4team" in path:
        n_game = 4
    elif "3team" in path:
        n_game = 3
    else:
        raise ValueError("Invalid path")

    assert n_player % n_game == 0 and n_player > 0

    n_1team = n_player // n_game
    print("n_player:", n_player)

    cnt = -1
    ind = 0
    while ind < len(ar):
        line = ar[ind]
        if '      <tr align="right">' in line:
            if cnt == -1:
                cnt = 0
                ind += 1
            else:
                ar[ind + 1] = f"        <td>{cnt//n_1team+1}</td>\n"
                cnt += 1
                ind += 2
        else:
            ind += 1

    with open(path, "w", encoding="utf-8") as f:
        for line in ar:
            f.write(line)
    # break
