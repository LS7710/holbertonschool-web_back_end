export default function iterateThroughObject(reportWithIterator) {
  let result = [];
  for (const employee of reportWithIterator) {
    result.push(employee);
  }
  return result.join(' | ');
}
