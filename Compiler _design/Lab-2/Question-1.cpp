#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream file("input.cpp");
    string line;
    int lineNumber = 1;

    while (getline(file, line)) {
        cout << lineNumber << ": " << line << endl;
        lineNumber++;
    }

    file.close();
    return 0;
}
