#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (auto i : nums) {
        freq[i]++;
    }

    // Min-heap to store pairs of (frequency, element)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

    // Maintain a heap of size k
    for (auto& it : freq) {
        minHeap.push({it.second, it.first});
        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    // Extracting elements from the heap
    vector<int> result;
    while (!minHeap.empty()) {
        result.push_back(minHeap.top().second);
        minHeap.pop();
    }

    return result;
}

int main() {
    // Test Case 1
    vector<int> nums1 = {1, 1, 1, 2, 2, 3,3,3};
    int k1 = 2;
    vector<int> result1 = topKFrequent(nums1, k1);
    cout << "Test Case 1 Result: ";
    for (int num : result1) {
        cout << num << " ";
    }
    cout << endl;

    // Test Case 2
    vector<int> nums2 = {1};
    int k2 = 1;
    vector<int> result2 = topKFrequent(nums2, k2);
    cout << "Test Case 2 Result: ";
    for (int num : result2) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
