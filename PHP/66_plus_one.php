<!-- You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits. -->

<!-- 
Psudo logic:
Reverse the array s as not to stress with negative indexes
take item 0 and +1
if greater than 10, subtract 10 and update the item
add 1 to next item 

if less than 10, update item and return

n.b. I made this more robust, although less efficient to allow for looping if we wanted to add 1 multiple times
-->



<?php
class Solution
{

    /**
     * @param  Integer[] $digits
     * @return Integer[]
     */
    function plusOne($digits)
    {
        $increasing = true;
        $reverse_digits = array_reverse($digits);
        $increased_digit = $reverse_digits[0] + 1;
        $index = 0;
        while($increasing){
            if($increased_digit >= 10) {
                $reverse_digits[$index] = $increased_digit - 10;
                $increased_digit = $reverse_digits[$index + 1] + 1;
                $index ++;
            }
            else{
                $reverse_digits[$index] = $increased_digit;
                $digits_new = array_reverse($reverse_digits);
                return $digits_new;
            }
        }
    }
}
?>
