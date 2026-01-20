#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream input("input.cpp");
    ofstream output("output.cpp");
    string line;

    while (getline(input, line)) {
        string cleaned;
        bool space = false;

        for (char c : line) {
            if (c == ' ' || c == '\t') {
                if (!space) {
                    cleaned += ' ';
                    space = true;
                }
            } else {
                cleaned += c;
                space = false;
            }
        }

        if (!cleaned.empty() && cleaned != " ")
            output << cleaned << endl;
    }

    input.close();
    output.close();
    return 0;
}
