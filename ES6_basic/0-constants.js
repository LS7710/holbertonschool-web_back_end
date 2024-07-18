// Modify taskFirst to use const
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

// Keep getLast unchanged
export function getLast() {
  const last = ' is okay';  // Use const here as well
  return last;
}

// Modify taskNext to use let
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();
  return combination;
}
