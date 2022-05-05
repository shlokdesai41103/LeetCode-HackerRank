#include <stdio.h>
#include <stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize);

int main(void){
    int nums[4] = {0,4,3,0};
    int returnSize[2];
    twoSum(nums, 4, 0, returnSize);
    return 0;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int sum = 0;
    //the calloc function allocates a specific amount of memory to the array res and initializes it to 0
    int* res = calloc((*returnSize = 2), sizeof(int)); 
    for(int i  = 0 ; i < numsSize ; i++){
            sum = nums[i];
            for(int j = 0 ; j < numsSize ; j++){
                if(j != i){
                    sum += nums[j];
                    if(sum == target){
                        res[0] = i;
                        res[1] = j;
                        return res;
                    }
                }
                sum = nums[i];
            }
    }
    return res;
}