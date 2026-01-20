#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream file("input.cpp");
    string line;
    int characters = 0, words = 0, lines = 0;

    while (getline(file, line)) {
        lines++;
        characters += line.length();

        bool inWord = false;
        for (char c : line) {
            if (isspace(c)) {
                inWord = false;
            } else if (!inWord) {
                words++;
                inWord = true;
            }
        }
    }

    file.close();

    cout << "Characters: " << characters << endl;
    cout << "Words: " << words << endl;
    cout << "Lines: " << lines << endl;

    return 0;
}
