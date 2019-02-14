function main(fn, input, config = {}) {
  console.time('程序耗时')
  const result = fn.apply(null, input);
  console.log('运行结果:', result);
  console.timeEnd('程序耗时')
}

module.exports = main
