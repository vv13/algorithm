const fs = require('fs');
const path = require('path');

// 根据目录查找fetch ids，更新题库
(function () {
  const dirs = fs.readdirSync(path.join(__dirname, '../leetcode'));
  console.log(
    dirs
      .filter(dirname => dirname.includes('.'))
      .map(dirname => dirname.split('.')[0])
      .join(',')
  );
})();
