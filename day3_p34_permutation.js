// 튜터 사이트에서 디버깅용
var permute = function (nums) {
  const result = [];

  const dfs = (i, nums) => {
    console.log(' '.repeat(i*3), 'start(i=',i,')``````')
    if (i === nums.length) {
      result.push(nums.slice());
      console.log(' '.repeat(i*3), 'result:', result)
      console.log(' '.repeat(i*3), 'i0=' + i)
      return
    }
    for (let j = i; j < nums.length; j++) {

      [nums[i], nums[j]] = [nums[j], nums[i]]
      console.log('\n',' '.repeat(i*3), 'for i/j 변경(i:',i,',j:',j,') 후 -> 함수 호출')
      dfs(i + 1, nums);

      [nums[i], nums[j]] = [nums[j], nums[i]];
      console.log(' '.repeat(i*3), '______돌아와서 i/j 변경(i:',i,',j:',j,') 후 close')
    }
  }
  dfs(0, nums);
  return result;
}
console.log(permute([1, 2, 3]))