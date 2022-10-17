<?php

//Runtime: 28 ms, faster than 100.00% of PHP online submissions for Build Array from Permutation.
//Memory Usage: 15.7 MB, less than 73.33% of PHP online submissions for Build Array from Permutation.
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
	function buildArray($nums) {
		$getNum = function ($ind) use ($nums) { 
			return $nums[$nums[$ind]];
		};
        	return array_map($getNum, range(0, count($nums) - 1));
    	}
};

$test = array(1,3,0,2);
$solution = new Solution;
print_r($solution->buildArray(array(1,3,0,2)) == array(3,2,1,0));
print_r($solution->buildArray(array(0,2,1,5,3,4)) == array(0,1,2,4,5,3));
print_r($solution->buildArray(array(5,0,1,2,3,4)) == array(4,5,0,1,2,3));
