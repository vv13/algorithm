const fs = require('fs');
const path = require('path');

// 按照规则寻找文件，并且执行相应的操作
const revealFile = (rule, action) => {
  const executor = root => {
    fs.readdir(root, (err, files) => {
      files.forEach(filename => {
        const realPath = path.join(root, filename);
        fs.stat(realPath, (_, stats) => {
          if (stats.isDirectory()) {
            executor(realPath, rule, action);
          }
          if (rule.test(filename)) {
            action(realPath);
          }
        });
      });
    });
  };
  return executor;
};

const finder = revealFile(/_CN\.md$/, filepath => {
  fs.unlinkSync(filepath);
  console.log(`success delete ${filepath}`);
});
finder(path.join(__dirname, '../leetcode'));
