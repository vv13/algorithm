const fs = require('fs');
const path = require('path');

// 按照规则寻找文件，并且执行相应的操作
const ActionLoader = (rule, action) => {
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

const actions = {
  removeFile: {
    rule: /_CN\.md$/,
    callback: filepath => {
      fs.unlinkSync(filepath);
      console.log(`success delete ${filepath}`);
    },
  },
  renameFile: {
    rule: /solution\.py/,
    callback: filepath => {
      const targetName = filepath.replace('solution.py', 'Solution.py');
      fs.renameSync(filepath, targetName);
      console.log(`success rename file from ${filepath} to ${targetName}`);
    },
  },
  removeAlltestPy: {
    rule: /test\.py$/,
    callback: filepath => {
      fs.unlinkSync(filepath);
      console.log(`success delete ${filepath}`);
    },
  },
};

const executor = ({ rule, callback }) => {
  const action = ActionLoader(rule, callback);
  action(path.join(__dirname, '../leetcode'));
};

executor(actions.renameFile);
