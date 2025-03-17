int findClosestNumber(int* nums, int numsSize) {
    int closest = nums[0];
    for(int i=0; i< numsSize; i++){
        int current = nums[i];
        if(abs(current) < abs(closest)){
            closest = current;
        }
        else if(abs(current) == abs(closest) && current > closest){
            closest = current;
        }

    }
    return closest;
}
