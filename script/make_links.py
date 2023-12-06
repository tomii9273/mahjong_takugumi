# 3 人麻雀用
# https://github.com/tomii9273/mahjong_takugumi/pull/32

for n_taku in range(3, 31):
    n_taisen = n_taku if n_taku % 2 == 1 or n_taku == 4 else n_taku - 1
    # print(f'<a href="3g_3team_sen/{n_taku}taku_{n_taku * 3}nin_{n_taisen}sen_3team.txt">{n_taku}卓{n_taku * 3}人{n_taisen}戦</a><br />')  # 3 チーム戦

    # print(f'<a href="3g_kojin_sen/{n_taku}taku_{n_taku * 3}nin_{n_taisen}sen_kojin.txt">{n_taku}卓{n_taku * 3}人{n_taisen}戦</a><br />')  # 個人戦
    if n_taku not in [3,5,9,11,13,17,19,25]:
        print(f"copy 3g_3team_sen\{n_taku}taku_{n_taku * 3}nin_{n_taisen}sen_3team.txt 3g_kojin_sen\{n_taku}taku_{n_taku * 3}nin_{n_taisen}sen_kojin.txt")
