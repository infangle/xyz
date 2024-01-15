class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Initialize two pointers for the left and right ends of the window
        left = right = 0
        # Initialize a dictionary to store the frequency of each fruit type in the window
        freq = {}
        # Initialize a variable to store the maximum number of fruits
        max_fruits = 0
        # Loop through the array until the right pointer reaches the end
        while right < len(fruits):
            # Add the current fruit to the frequency dictionary and increment its count
            fruit = fruits[right]
            freq[fruit] = freq.get(fruit, 0) + 1
            # While the number of distinct fruit types in the window is more than 2
            while len(freq) > 2:
                # Remove the leftmost fruit from the frequency dictionary and decrement its count
                left_fruit = fruits[left]
                freq[left_fruit] -= 1
                # If the count becomes zero, delete the fruit type from the dictionary
                if freq[left_fruit] == 0:
                    del freq[left_fruit]
                # Move the left pointer to the right by one
                left += 1
            # Update the maximum number of fruits with the current window size
            max_fruits = max(max_fruits, right - left + 1)
            # Move the right pointer to the right by one
            right += 1
        # Return the maximum number of fruits
        return max_fruits
