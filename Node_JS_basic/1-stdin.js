console.log('Welcome to Holberton School, what is your name?\r');

process.stdin.on('data', (input) => {
  const name = input.toString().trim();
  console.log(`Your name is: ${name}\r`);
  process.exit(0);
});

process.on('exit', () => {
  console.log('This important software is now closing\r');
});