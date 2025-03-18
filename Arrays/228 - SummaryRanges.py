char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    int a = 0, b = 0;
    *returnSize = 0;
    char** ans = (char**)malloc(numsSize * sizeof(char*));
    
    while (b < numsSize) {
        if (b + 1 < numsSize && nums[b] + 1 == nums[b + 1]) {
            b++;
        } else {
            ans[*returnSize] = (char*)malloc(25 * sizeof(char));
            if (a == b) {
                sprintf(ans[*returnSize], "%d", nums[a]);
            } else {
                sprintf(ans[*returnSize], "%d->%d", nums[a], nums[b]);
            }
            (*returnSize)++;
            b++;
            a = b;
        }
    }
    
    return ans;
}
