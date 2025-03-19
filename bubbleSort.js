function bubbleSort(array) {
  const length = array.length;
  for (let i = 0; i < length - 1; i++) {
    let swapped = false;
    for (let j = 0; j < length - 1 - i; j++) {
      if (array[j] > array[j + 1]) {
        const arrayJ = array[j];
        array[j] = array[j + 1];
        array[j + 1] = arrayJ;
        swapped = true;
      }
    }
    if (!swapped) break;
  }
  return array;
}

const array = [5, 3, 7, 1, 4, 2];
console.log(bubbleSort(array));
