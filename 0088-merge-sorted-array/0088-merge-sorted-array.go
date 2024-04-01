func merge(nums1 []int, m int, nums2 []int, n int)  {
    arr:=nums1[:m]
    arr1:=nums2[:n]
    arr=append(arr,arr1...)
    sort.Ints(arr)
    fmt.Println(arr)
}