// 读取特朗普吐槽内容数组.json文件内容
const fs = require('fs');

try {
    // 读取JSON文件内容
    const data = fs.readFileSync('特朗普吐槽内容数组.json', 'utf8');
    const comments = JSON.parse(data);
    
    // 获取DOM元素
    const postContainer = document.getElementById('post-container');
    let currentIndex = 0;
    
    // 初始显示第一条评论
    if (comments.length > 0) {
        postContainer.innerHTML = comments[0];
    }
    
    // 设置定时器，每20秒切换一条评论
    setInterval(() => {
        currentIndex = (currentIndex + 1) % comments.length;
        postContainer.innerHTML = comments[currentIndex];
    }, 20000);
    
    console.log('特朗普吐槽定时发布功能已启动');
} catch (err) {
    console.error('加载吐槽内容时出错:', err);
}
