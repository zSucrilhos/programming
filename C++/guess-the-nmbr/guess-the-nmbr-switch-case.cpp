#include <iostream>
using namespace std;

int main() {
    int number {251};
    int user_choice {0};
    int program_ok {0};

    cout << "Guess the number game." << endl;
    cout << "I have one number between 0 and 1000, guess it!" << endl;
    
    cout << "? ";
    cin >> user_choice;
    while(program_ok == 0){

        if(user_choice > 1000){
            cout << " Your number is greater than the limit, try again" << endl;
            cout << endl;
            main();
        } else if(user_choice < 0){
            cout << "Your number is less than zero, try again!" << endl;
            cout << endl;
            main();
        } else if(user_choice == number){
            cout << "You guessed it! Excellent!" << endl;
            cout << endl;
            break;

        }
    }
}
