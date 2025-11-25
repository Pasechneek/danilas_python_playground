class AggregateSum:

    def calculate_sum_1(input_list: list[int]) -> int:
        if not input_list:
            return 0
        aggregate_sum: int = 0
        for item in input_list:
            if item % 3 == 0:
                aggregate_sum += item
        return aggregate_sum

    def calculate_sum_2(coll):
        sum = 0
        for num in coll:
            if num % 3 == 0:
                sum += num
        return sum