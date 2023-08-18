import random
import requests
import re


url = 'http://www.66ip.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


def get_page_size():
    response = requests.request(method='GET', url=url, headers=headers)
    response.encoding='gb2312'
    html_content = response.text
    # print(html_content)
    # 使用正则表达式匹配id为PageList的div标签及其内容
    div_pattern = r'<div[^>]*id="PageList"[^>]*>(.*?)</div>'
    div_match = re.search(div_pattern, html_content, re.DOTALL)  # 使用re.DOTALL标志匹配跨行的内容
    if div_match:
        div_content = div_match.group(1)  # 提取div标签的内容

        # 使用正则表达式匹配倒数第二个a标签的内容
        a_pattern = r'<a[^>]*>(.*?)</a>'
        a_matches = re.findall(a_pattern, div_content)

        if len(a_matches) >= 2:
            second_last_a_content = a_matches[-2]  # 提取倒数第二个a标签的内容
            # print(second_last_a_content)
            return second_last_a_content
        else:
            print("未找到足够的a标签")
            exit(0)
    else:
        print("未找到id为PageList的div标签")
        exit(0)


def get_ip_list():
    ip_list=[]
    i = random.randint(1,5)
    target_url = 'http://www.66ip.cn/{0}.html'.format(i)
    response = requests.request(method='GET', url=url, headers=headers)
    response.encoding='gb2312'
    html_content = response.text
    #print(html_content)
    # 使用正则表达式匹配<table>标签及其内容
    table_pattern = r'<table[^>]*width=\'100%\'[^>]*border="2px"[^>]*cellspacing="0px"[^>]*bordercolor="#6699ff"[^>]*>(.*?)</table>'
    table_match = re.search(table_pattern, html_content, re.DOTALL)  # 使用re.DOTALL标志匹配跨行的内容
    if table_match:
        table_content = table_match.group(1)  # 提取<table>标签的内容

        # 使用正则表达式匹配第二个<tr>标签到最后一个<tr>标签的内容
        tr_pattern = r'<tr[^>]*>(.*?)</tr>'
        tr_matches = re.findall(tr_pattern, table_content, re.DOTALL)

        if len(tr_matches) >= 2:
            tr_content = tr_matches[1:]  # 提取第二个<tr>标签到最后一个<tr>标签的内容

            # 遍历每个<tr>标签的内容
            for tr in tr_content:
                # 使用正则表达式匹配<tr>标签下的所有<td>标签的内容
                td_pattern = r'<td[^>]*>(.*?)</td>'
                td_matches = re.findall(td_pattern, tr, re.DOTALL)

                # 提取<td>标签的内容
                td_content = [re.sub(r'<.*?>', '', td) for td in td_matches]
                ip_list.append(td_content)
        else:
            print("未找到足够的<tr>标签")
    else:
        print("未找到<table>标签")
    return ip_list

if __name__=='__main__':

    ip_list = get_ip_list()
    print(ip_list[0][0])




