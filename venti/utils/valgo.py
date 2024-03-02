class MergeSorter:
    def sort(self, input_list):
        if len(input_list) <= 1:
            return input_list
        else:
            mid = len(input_list) // 2
            left_half = input_list[:mid]
            right_half = input_list[mid:]
            return self.merge(self.sort(left_half), self.sort(right_half))

    def merge(self, left_half, right_half):
        merged = []
        while len(left_half) > 0 and len(right_half) > 0:
            if left_half[0] < right_half[0]:
                merged.append(left_half.pop(0))
            else:
                merged.append(right_half.pop(0))
        while len(left_half) > 0:
            merged.append(left_half.pop(0))
        while len(right_half) > 0:
            merged.append(right_half.pop(0))
        return merged
