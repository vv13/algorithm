const path = require('path')

module.exports = {
  PATH_QUESTION: path.resolve(__dirname, '../question'),
  API_PROBLEMS: 'https://leetcode.com/api/problems/all/',
  API_GRAPHQL: 'https://leetcode.com/graphql',
  questionDataQL: titleSlug => ({
    operationName: 'questionData',
    variables: { titleSlug },
    query:
      'query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { likes dislikes content similarQuestions stats }}'
  }),
  levelMap: {
    1: 'Easy',
    2: 'Medium',
    3: 'Hard'
  }
};
