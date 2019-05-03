class Sol:
    def intersecr_of_2_arr(self,arr1,arr2):
        return list(set(arr1) & set(arr2))


if __name__ == '__main__':
    p1=Sol()
    print(p1.intersecr_of_2_arr([1,4,5],[6,2,4]))
