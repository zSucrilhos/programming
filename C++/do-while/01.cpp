#include <iostream>
using namespace std;

int main() {
	string user_type = "";

	cout << "Do-while test :)" << endl;
	
	do {
		cout << "Type 'exit' to exit" << endl;
        cin >> user_type;
	} while (user_type != "exit");
        cout << "Do-while" << endl;

	return 0;
}



