function solution(sequence, k) {
  var answer = [0, 1000000];

  let start = 0;
  let end = 0;
  let sum = sequence[start];

  while (end < sequence.length) {
    if (sum === k) {
      if (answer[1] - answer[0] > end - start) {
        answer = [start, end];
      }
      sum -= sequence[start];
      start += 1;
      end += 1;
      sum += sequence[end];
    }

    if (sum > k) {
      sum -= sequence[start];
      start += 1;
    } else if (sum < k) {
      end += 1;
      sum += sequence[end];
    }
  }

  return answer;
}
