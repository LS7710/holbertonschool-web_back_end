export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;

    if (trueOrFalse) {
        const innerTask = true;
        const innerTask2 = false;
        console.log(innerTask, innerTask2);
    }

    return [task, task2];
}