#include <iostream>

// class Solution {
// 	public:
// 		string run(int N, int M);
// };

// string Solution::run(int N, int M) {
// 	//
// 	// Write your code below; return type and arguments should be according to the problem\'s requirements
// 	//
int main() {

	//
	// Write your code below; return type and arguments should be according to the problem\'s requirements
	//
	int N = 0;
	int M = 10;
	//std::string sequence = "";
	// for (int i = N; i == M; ++i) {
	// 	if (i%3 == 0) && (i%5 == 0) {
	// 		//sequence = sequence + "FizzBuzz";
	// 		std::cout << "FizzBuzz" << std::endl;
	// 	}
	// 	if (i%3 == 0) {
	// 		//sequence = sequence + "Fizz";
	// 		std::cout << "Fizz" << std::endl;
	// 	} else if (i%5 == 0) {
	// 		//sequence = sequence + "Buzz";
	// 		std::cout << "Buzz" << std::endl;
	// 	} else {
	// 		//sequence = sequence + (std::to_string(i));
	// 		std::cout << i << std::endl;
	// 	}
	// }
	int i = N;
	do {
		if ((i % 3 == 0) && (i % 5 == 0)) {
			//sequence = sequence + "FizzBuzz";
			std::cout << "FizzBuzz" << std::endl;
		}
		if (i%3 == 0) {
			//sequence = sequence + "Fizz";
			std::cout << "Fizz" << std::endl;
		} else if (i%5 == 0) {
			//sequence = sequence + "Buzz";
			std::cout << "Buzz" << std::endl;
		} else {
			//sequence = sequence + (std::to_string(i));
			std::cout << i << std::endl;
		}
		i ++;
	} while (i <= M);

	//std::cout << sequence;
}