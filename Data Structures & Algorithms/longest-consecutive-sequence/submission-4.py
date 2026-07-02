class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_ls = sorted(nums)
        group = defaultdict(list)
        if not nums:
            return 0
        elif len(nums)==1:
            return 1
        def find_chain(index, num,ls):
            next_num = num+1
            if next_num in sort_ls:
                group[index].append(next_num)
                return find_chain(index, next_num,sort_ls)
        index = 0
        for i in sort_ls:   
            group[index].append(i)        
            find_chain(index,i,sort_ls)
            index+=1

        max_vals = []
        print(group)
        for val in group.values():
            max_vals.append(len(val))
        print(max_vals)
        return int(max(max_vals))