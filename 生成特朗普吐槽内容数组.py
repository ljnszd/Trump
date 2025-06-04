// 读取特朗普负面评论结构化列表.md文件内容
const fs = require('fs');

try {
    // 读取文件内容
    const content = fs.readFileSync('特朗普负面评论结构化列表.md', 'utf8');
    
    // 将内容按行分割成数组，并过滤掉空行
    const comments = content.split('\n').filter(line => line.trim() !== '');
    
    // 将数组保存为JSON文件
    const outputFileName = '特朗普吐槽内容数组.json';
    fs.writeFileSync(outputFileName, JSON.stringify(comments, null, 2));
    
    console.log(`文件 ${outputFileName} 已成功保存。`);
} catch (err) {
    console.error('读取文件时出错:', err);
}