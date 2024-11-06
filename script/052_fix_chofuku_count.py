import os
from itertools import combinations

from bs4 import BeautifulSoup


def fix_chohuku_count(file_path):
    print("start", file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # BeautifulSoupでHTMLをパース
    soup = BeautifulSoup(html, "html.parser")

    # テーブルを取得
    table = soup.find("table")

    # 行を取得
    rows = table.find_all("tr")

    data = []

    # ヘッダー行をスキップしてデータ行を処理
    for row in rows[1:]:
        # セルを取得
        cells = row.find_all("td")
        # 行ラベルをスキップしてデータを抽出
        row_data = [int(cell.get_text()) for cell in cells[1:]]
        data.append(row_data)

    print(data)

    n_guest = 0
    lines = html.splitlines()
    for line in lines:
        if f"ゲスト{n_guest+1}" in line:
            n_guest += 1

    p = len(data)
    pre_s = len(data[0])
    assert all(len(row) == pre_s for row in data)

    s = pre_s
    if n_guest == 1:
        s -= 1
    elif n_guest >= 2:
        s -= n_guest + 1

    chofuku4 = [[] for _ in range(s + 1)]
    chofuku3 = [[] for _ in range(s + 1)]
    chofuku2 = [[] for _ in range(s + 1)]
    doutaku2 = [[0] * p for _ in range(p)]

    for p0, p1, p2, p3 in combinations(range(p), 4):
        cnt = 0
        for s0 in range(s):
            if data[p0][s0] == data[p1][s0] == data[p2][s0] == data[p3][s0]:
                cnt += 1
        chofuku4[cnt].append((p0, p1, p2, p3))

    for p0, p1, p2 in combinations(range(p), 3):
        cnt = 0
        for s0 in range(s):
            if data[p0][s0] == data[p1][s0] == data[p2][s0]:
                cnt += 1
        chofuku3[cnt].append((p0, p1, p2))

    for p0, p1 in combinations(range(p), 2):
        cnt = 0
        for s0 in range(s):
            if data[p0][s0] == data[p1][s0]:
                cnt += 1
        chofuku2[cnt].append((p0, p1))
        doutaku2[p0][p1] = cnt
        doutaku2[p1][p0] = cnt

    def make_chofuku():
        ans = ""
        # 「重複同卓者の詳細」
        ans += "    <h3>重複同卓者の詳細</h3>\n"

        if (
            all(len(chofuku2[s0]) == 0 for s0 in range(s, 1, -1))
            and all(len(chofuku3[s0]) == 0 for s0 in range(s, 1, -1))
            and all(len(chofuku4[s0]) == 0 for s0 in range(s, 1, -1))
        ):
            ans += "    <p>重複同卓者なし。どの 2 人も互いに 0 ～ 1 回同卓。</p>\n"
        else:
            ans += "    <ul>\n"
            for s0 in range(s, 1, -1):
                if len(chofuku4[s0]) > 0:
                    ans += f"      <li>{s0} 回同卓する 4 人組 ({len(chofuku4[s0])} 組): "
                    for ind, (p0, p1, p2, p3) in enumerate(chofuku4[s0]):
                        ans += f"({p0 + 1}, {p1 + 1}, {p2 + 1}, {p3 + 1})"
                        if ind < len(chofuku4[s0]) - 1:
                            ans += ", "
                    ans += "</li>\n"

                if len(chofuku3[s0]) > 0:
                    ans += f"      <li>{s0} 回同卓する 3 人組 ({len(chofuku3[s0])} 組): "
                    for ind, (p0, p1, p2) in enumerate(chofuku3[s0]):
                        ans += f"({p0 + 1}, {p1 + 1}, {p2 + 1})"
                        if ind < len(chofuku3[s0]) - 1:
                            ans += ", "
                    ans += "</li>\n"

                if len(chofuku2[s0]) > 0:
                    ans += f"      <li>{s0} 回同卓する 2 人組 ({len(chofuku2[s0])} 組): "
                    for ind, (p0, p1) in enumerate(chofuku2[s0]):
                        ans += f"({p0 + 1}, {p1 + 1})"
                        if ind < len(chofuku2[s0]) - 1:
                            ans += ", "
                    ans += "</li>\n"
            ans += "    </ul>\n"

        # 「2 人組の同卓回数」
        ans += "    <h3>2 人組の同卓回数</h3>\n"
        ans += '    <table border="1" style="border-collapse: collapse">\n'

        ans += '      <tr align="right">\n'
        ans += "        <td></td>\n"
        for p0 in range(p):
            player_type = "ゲスト" if p0 < n_guest else "選手"
            ans += f"        <td>{player_type}{p0 + 1}</td>\n"
        ans += "      </tr>\n"

        for p0 in range(p):
            player_type = "ゲスト" if p0 < n_guest else "選手"
            ans += '      <tr align="right">\n'
            ans += f"        <td>{player_type}{p0 + 1}</td>\n"
            for p1 in range(p):
                val = str(doutaku2[p0][p1]) if p0 != p1 else "-"
                ans += "        <td>" + val + "</td>\n"
            ans += "      </tr>\n"
        ans += "    </table>\n"

        ans += "  </body>\n"
        ans += "</html>\n"
        return ans

    with open(file_path, "w", encoding="utf-8") as f:
        lines = html.splitlines()
        for line in lines:
            if "<h3>重複同卓者の詳細</h3>" in line:
                break
            f.write(line + "\n")
        f.write(make_chofuku())

    print("end", file_path)


root_path = "..\\public\\guest"
target_path = [os.path.join(root_path, f) for f in os.listdir(root_path)]  # 卓組 html ファイルのパス

for file_path in target_path:
    fix_chohuku_count(file_path)
