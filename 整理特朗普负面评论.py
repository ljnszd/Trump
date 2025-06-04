# 读取特朗普负面评论库.md文件内容
with open('特朗普负面评论库.md', 'r', encoding='utf-8') as file:
    content = file.read()

# 分割评论为列表
comments = []
for line in content.split('\n'):
    if line.startswith('“') and line.endswith('”'):
        comments.append(line.strip('“”'))

# 去重
unique_comments = list(set(comments))

# 筛选符合尖锐讽刺语气的评论
filtered_comments = []
for comment in unique_comments:
    # 检查评论是否包含尖锐讽刺的关键词
    if any(keyword in comment for keyword in ['闹剧', '跳梁小丑', '无耻', '白痴', '令人作呕', '冷血动物', '祸害']):
        filtered_comments.append(comment)

# 按主题分类
categories = {
    '经济政策': [],
    '抗疫表现': [],
    '外交关系': [],
    '个人品行': [],
    '其他': []
}

for comment in filtered_comments:
    if any(keyword in comment for keyword in ['关税', '经济', '税收', '失业']):
        categories['经济政策'].append(comment)
    elif any(keyword in comment for keyword in ['抗疫', '疫情', '死了']):
        categories['抗疫表现'].append(comment)
    elif any(keyword in comment for keyword in ['外交', '盟友', '国际形象']):
        categories['外交关系'].append(comment)
    elif any(keyword in comment for keyword in ['自私', '任性', '孩子', '无耻', '冷血']):
        categories['个人品行'].append(comment)
    else:
        categories['其他'].append(comment)

# 生成结构化吐槽内容
structured_content = "# 特朗普负面评论结构化列表\n\n"
for category, comments in categories.items():
    if comments:
        structured_content += f"## {category}\n\n"
        for i, comment in enumerate(comments, 1):
            structured_content += f"{i}. “{comment}”\n\n"

# 保存结果
output_file = '特朗普负面评论结构化列表.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(structured_content)

print(f"文件 {output_file} 已成功保存。")