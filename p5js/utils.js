
function range(start, stop, step) {
  if (typeof stop == 'undefined') {
      // one param defined
      stop = start;
      start = 0;
  }

  if (typeof step == 'undefined') {
      step = 1;
  }

  if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
      return [];
  }

  var result = [];
  for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
      result.push(i);
  }

  return result;
};

function searchForArray(haystack, needle){
  var stringifiedHaystack = JSON.stringify(haystack);
  var stringifiedNeedle = JSON.stringify(needle);
  return stringifiedHaystack.indexOf(stringifiedNeedle) >= 0;
}

function easeInOutN(t, power){
  return t < 0.5 ? 0.5 * pow(2 * t, power) : 1 - 0.5 * pow(2 * (1 - t), power);
}

function timeCycle(totalframes, offset) {
  var step = (frameCount + offset) % totalframes / totalframes;
  return step;
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
