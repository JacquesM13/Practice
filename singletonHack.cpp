#include <algorithm>
#include <list>
#include <vector>

class Solution {
	public:
		int run(vector<int> student_list);
};

int Solution::run(vector<int> student_list) {
	//
	// Write your code below; return type and arguments should be according to the problem\'s requirements
	//
	std::list<int> myList;
	std::vector<int> myList2;
	int j;

	for (int number : student_list) {
		myList.push_back(number);
	}

	myList.sort();

	// for (int k : myList) {
	// 	std::cout << k << ", ";
	// }

	for (int num : myList) {
		if (num != j) {
			myList2.push_back(num);
		} else myList2.pop_back();
		j = num;
	}

	// for(int k : myList2) {
	// 	std::cout << k << std::endl;
	// }

	int single_student_number = myList2[0];
	return single_student_number;
}
