const countStudents = require('./3-read_file_async');

countStudents('database.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.error(error.message);
  });

console.log('After!');
