top_heights = [6, 9, 5, 7, 4]

#[0, 0, 0, 0, 0]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)   # [0, 0, 0, 0, 0]
    while heights:  # heigts가 빈상태가 아닐 때
        height = heights.pop()
        #[6, 9, 5, 7]
        for idx in range(len(heights) - 1, -1, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
