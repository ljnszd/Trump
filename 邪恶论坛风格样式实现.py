# 读取邪恶论坛风格视觉元素资料.md文件
with open('邪恶论坛风格视觉元素资料.md', 'r', encoding='utf-8') as file:
    style_data = file.read()

# 读取邪恶风格页面设计.html文件
with open('邪恶风格页面设计.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 创建CSS样式
css_style = """
/* 基础样式 */
body {
    background-color: #121212;
    color: #fff;
    font-family: 'Courier New', monospace;
    margin: 0;
    padding: 20px;
    line-height: 1.6;
}

/* 霓虹字体效果 */
.neon-text {
    color: #fff;
    text-shadow: 
        0 0 7px #fff,
        0 0 10px #fff,
        0 0 21px #fff,
        0 0 42px #0fa,
        0 0 82px #0fa,
        0 0 92px #0fa,
        0 0 102px #0fa,
        0 0 151px #0fa;
    animation: flicker 1.5s infinite alternate;
}

/* 霓虹闪烁动画 */
@keyframes flicker {
    0%, 18%, 22%, 25%, 53%, 57%, 100% {
        text-shadow: 
            0 0 4px #fff,
            0 0 11px #fff,
            0 0 19px #fff,
            0 0 40px #0fa,
            0 0 80px #0fa,
            0 0 90px #0fa,
            0 0 100px #0fa,
            0 0 150px #0fa;
    }
    20%, 24%, 55% {
        text-shadow: none;
    }
}

/* 帖子容器样式 */
.post-container {
    background-color: rgba(37, 40, 42, 0.7);
    border: 1px solid #0fa;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(15, 255, 170, 0.5);
}

/* 帖子标题样式 */
.post-title {
    font-size: 1.5em;
    margin-bottom: 10px;
    color: #0fa;
}

/* 帖子内容样式 */
.post-content {
    font-size: 1em;
    margin-bottom: 10px;
}

/* 帖子时间样式 */
.post-time {
    font-size: 0.8em;
    color: #888;
    text-align: right;
}

/* 高亮边框效果 */
.highlight-border {
    position: relative;
    padding: 20px;
    border-radius: 8px;
    background-color: rgba(255, 255, 255, 0.05);
}

.highlight-border::before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 8px;
    padding: 2px;
    background: linear-gradient(45deg, #0fa, #ff00ff);
    -webkit-mask: 
        linear-gradient(#fff 0 0) content-box, 
        linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}

/* 导航栏样式 */
.navbar {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    margin-bottom: 20px;
    border-bottom: 1px solid #0fa;
}

.navbar a {
    color: #0fa;
    text-decoration: none;
    padding: 5px 10px;
    transition: all 0.3s ease;
}

.navbar a:hover {
    text-shadow: 0 0 5px #0fa;
}

/* 响应式设计 */
@media (max-width: 768px) {
    body {
        padding: 10px;
    }
    
    .post-container {
        padding: 10px;
    }
}
"""

# 将CSS样式保存到文件
with open('邪恶论坛风格样式.css', 'w', encoding='utf-8') as file:
    file.write(css_style)

print("文件 邪恶论坛风格样式.css 已成功保存。")

# 更新HTML文件，添加CSS链接
updated_html = html_content.replace('</head>', f'<link rel="stylesheet" href="邪恶论坛风格样式.css">\n</head>')

# 保存更新后的HTML文件
with open('邪恶风格页面设计.html', 'w', encoding='utf-8') as file:
    file.write(updated_html)

print("文件 邪恶风格页面设计.html 已成功更新。")