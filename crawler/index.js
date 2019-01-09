require('dotenv').config();
const request = require('superagent');
const fs = require('fs');
const path = require('path');
const config = require('./config');

function writeQuestionDictionary(dirname) {
  const dirPath = path.join(config.PATH_QUESTION, dirname);
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

function writeQuestionDescription(dirname, content) {
  const filePath = path.join(config.PATH_QUESTION, dirname, 'README.md');
  console.log('create: ' + filePath);
  fs.writeFileSync(filePath, content.content);
}

(async function() {
  const { text } = await request
    .get(config.API_PROBLEMS)
    .set('Accept', 'text/html');
  const data = JSON.parse(text);
  data.stat_status_pairs.forEach(async pair => {
    const {
      difficulty: { level },
      stat: { frontend_question_id, question__title_slug }
    } = pair;
    if (
      !(
        process.env.QUESTION_FROM <= frontend_question_id &&
        process.env.QUESTION_TO >= frontend_question_id
      )
    ) {
      return;
    }
    const {
      body: {
        data: { question }
      }
    } = await request
      .post(config.API_GRAPHQL)
      .send(config.questionDataQL(question__title_slug));
    const dictionaryName = `${frontend_question_id}_${question__title_slug}_${
      config.levelMap[level]
    }`;
    writeQuestionDictionary(dictionaryName);
    writeQuestionDescription(dictionaryName, question);
  });
})();
