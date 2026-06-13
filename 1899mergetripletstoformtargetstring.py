class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        left_cnt = 0
        mid_cnt = 0
        right_cnt = 0

        """
            The logic of the problem is straight.
            We traverse through the array and compare if we can make left, mid and right elements from the elements.
            Now at the end we count if possible for those triplets.
            If possible then return True or else return False.
        """

        for each_triplet in triplets:

            left, mid, right = each_triplet[0], each_triplet[1], each_triplet[2]

            if left == target[0] and mid <= target[1] and right <= target[2]:
                left_cnt+=1
            
            if mid == target[1] and left <= target[0] and right <= target[2]:
                mid_cnt +=1

            if right == target[2] and left <= target[0] and mid <= target[1]:
                right_cnt+=1
            
        if left_cnt > 0 and mid_cnt > 0 and right_cnt > 0:
            return True
        
        return False
