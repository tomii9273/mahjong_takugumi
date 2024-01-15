from bs4 import BeautifulSoup


def make_header(title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="keyword" content="麻雀, 卓組" />
    <title>{title} - 麻雀大会用卓組表</title>
    <link rel="stylesheet" href="../takugumi.css" type="text/css" />
  </head>
  <body bgcolor="#e0ffe0">
"""


def make_footer() -> str:
    return """  </body>
</html>
"""


def txt_to_list(path: str) -> list:
    with open(path, "r") as f:
        takugumi = []
        for item in f.readlines():
            takugumi.append(list(item.split()))
    return takugumi


def list_to_table(takugumi: list) -> str:
    table_str = '    <table border="1" style="border-collapse: collapse">\n'

    table_str += '      <tr align="right">\n'
    table_str += "        <td></td>\n"
    for taisen_ind in range(len(takugumi[0])):
        table_str += f"        <td>{taisen_ind + 1}戦目</td>\n"
    table_str += "      </tr>\n"

    for player_ind, row in enumerate(takugumi):
        table_str += '      <tr align="right">\n'
        table_str += f"        <td>選手{player_ind + 1}</td>\n"
        for col in row:
            table_str += "        <td>" + col + "</td>\n"
        table_str += "      </tr>\n"
    table_str += "    </table>\n"
    return table_str


def takugumi_to_html(takugumi_path: str, title: str) -> str:
    print("start", takugumi_path, title)
    return (
        make_header(title) + list_to_table(txt_to_list(takugumi_path)) + make_footer()
    )


with open("../public/index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

links = soup.find_all("a")
# print(link)
for link in links:
    href = link["href"]
    text = link.get_text()
    if href.endswith(".txt"):
        takugumi_path = "../public/" + href
        with open(takugumi_path[:-4] + ".html", "w", encoding="utf-8") as f:
            f.write(takugumi_to_html(takugumi_path, text))
        # break
