import re

# p = 3
p = 4


def make_row_4ma(g, p, w):
    max_or_not = "○" if (g * p - 1) // (p - 1) == w else ""
    return f"""      <tr align="left">
        <td>{g}</td>
        <td>{p}</td>
        <td>{w}</td>
        <td>{max_or_not}</td>
        <td><a href="kojin_sen/{g}taku_{g*p}nin_{w}sen_kojin.html">{g} 卓 {g*p} 人 {w} 戦</a></td>
        <td><a href="kojin_sen_method.html">個人戦 重複同卓なし 卓組作成方法</a></td>
      </tr>"""


def make_row_3ma(g, p, w):
    max_or_not = "○" if (g * p - 1) // (p - 1) == w else ""
    return f"""      <tr align="left">
        <td>{g}</td>
        <td>{p}</td>
        <td>{w}</td>
        <td>{max_or_not}</td>
        <td><a href="3g_kojin_sen/{g}taku_{g*p}nin_{w}sen_kojin.html">{g} 卓 {g*p} 人 {w} 戦</a></td>
        <td><a href="3g_kojin_sen_method.html">3 人麻雀 個人戦 重複同卓なし 卓組作成方法</a></td>
      </tr>"""


def check_and_make_row(line):
    if '<a href="kojin_sen/' in line:
        # if '<a href="3g_kojin_sen/' in line:
        # print(line)
        match = re.match(r".*>(\d+) 卓 (\d+) 人 (\d+) 戦<.*", line.replace("(", "").replace(")", ""))

        if match:
            # print(match.groups())
            g, _, w = match.groups()
            g = int(g)
            w = int(w)
            print(make_row_4ma(g, p, w))
            # print(make_row_3ma(g, p, w))


html_name = "../public/index.html"

# 元のHTMLファイルを読み込む
with open(html_name, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    check_and_make_row(line)

print("完了")
