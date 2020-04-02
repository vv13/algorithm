let queue = [];
let running = false;
function start(id) {
  queue.push(id);
  if (running) return;
  next();
}

function next() {
  running = true;
  execute(queue.shift())
    .catch(console.error)
    .then(() => {
      running = false;
      if (queue.length) {
        next();
      }
    });
}

console.log('输出结果:');

for (let i = 0; i < 5; i++) {
  start(i);
}

function sleep(duration) {
  return new Promise(resolve => setTimeout(resolve, duration));
}

function execute(id) {
  let duration = Math.floor(Math.random() * 500);

  return sleep(duration).then(() => {
    console.log('id', id);
  });
}
