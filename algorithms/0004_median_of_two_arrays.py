def findMedianSortedArrays_slow(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    combined_array = []
    i = 0
    total_num_1_len = len(nums1)
    j = 0
    total_num_2_len = len(nums2)
    if_more = True
    while if_more:
        if i >= total_num_1_len and j >= total_num_2_len:
            break
        if j >= total_num_2_len or i < total_num_1_len and nums1[i] < nums2[j]:
            combined_array.append(nums1[i])
            i += 1
        elif i >= total_num_1_len or j < total_num_2_len and nums2[j] <= nums1[i]:
            combined_array.append(nums2[j])
            j += 1
    total_combined_array_len = len(combined_array)
    print(combined_array)
    if total_combined_array_len % 2 == 1:
        return combined_array[total_combined_array_len // 2]
    else:
        return (
            combined_array[total_combined_array_len // 2]
            + combined_array[total_combined_array_len // 2 - 1]
        ) * 0.5
