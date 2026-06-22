class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit1 = -1
        fruit2 = -1

        start_idx = 0
        end_idx = 0
        mx_len = -1

        """
            The algorithm is simple.
            We keep track of fruits and the last occured indexes with them.
            If it is repeating like 6,6 then its best to track the first index since from there we want to start our traversal.
            If it i 1,2,1,2,3 then we need to constantly update the 1 and 2 positions to get the most latest position.
            In this way we operate a sliding window and keep the max length.
        """

        lkup = {}

        while end_idx < len(fruits):
            # If fruit is present and then 
            if fruits[end_idx] in lkup and len(lkup.items()) <= 2:

                # If the index are repeating then don't update the index.
                # Else update the index.
                if fruits[end_idx - 1] != fruits[end_idx]:
                    lkup[fruits[end_idx]] = end_idx 
                mx_len = max(mx_len, end_idx - start_idx + 1)
            
            elif fruits[end_idx] not in lkup and len(lkup.items()) <= 1:
                lkup[fruits[end_idx]] = end_idx
                mx_len = max(mx_len, end_idx - start_idx + 1)
            
            else:
                # In this case the fruit is a third fruit.
                lst = lkup.values()
                mx = -1
                for i in lst:
                    mx = max(mx, i)

                lkup = {}
                start_idx = mx
                end_idx = mx

                print(mx, lst)
                continue
            
            end_idx += 1

        return mx_len
