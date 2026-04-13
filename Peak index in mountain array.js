var peakIndexInMountainArray = function(arr) {
  let low=0
  let  high=arr.length-1
  while (low<high){
   mid=low+Math.floor((high-low)/2)
  if (arr[mid]<arr[mid+1]){
    low=mid+1
  }
  else if(arr[mid]>arr[mid+1]){
    high=mid
  }
  } 
  return low
};
