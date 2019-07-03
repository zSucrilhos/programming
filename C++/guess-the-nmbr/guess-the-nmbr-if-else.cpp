#include <iostream>
using namespace std;

int main() {
    const number {251};
    int user_choice {0};
    int program_ok {0};

    cout << "Guess the number game." << endl;
    cout << "I have one number between 0 and 1000, guess it!" << endl;
    
    cout << "? ";
    cin >> user_choice;
    while(program_ok == 0){
        switch(number){
            case number < 0:
                cout << "Your number is less than zero, try again!" << endl;
                cout << endl;
                main();
            case number > 1000:
                cout << "Your number is greater than zero, try again!" << endl;
                cout << endl;
                main();
            case number == user_choice:
                cout << "You guessed it! Excellent!" << endl;
                cout << endl;
                break;
            case number > user_choice:
                cout << "Too low, try again!" << endl;
                cout << endl;
                main();
            case number < user_choice:
                cout << "Too high, try again!" << endl;
                cout << endl;
                main();
            default:
                cout << "Invalid input. Try again!" << endl;
                cout << endl;
                main();
        }
    }
}
