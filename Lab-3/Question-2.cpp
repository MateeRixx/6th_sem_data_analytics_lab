#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <cctype>
#include <string>
using namespace std;

bool isKeyword(string s) {
    string keywords[] = {"int", "float", "if", "else", "while", "return"};
    for (string k : keywords)
        if (s == k) return true;
    return false;
}

int main() {
    ifstream file("Sample_for_q2.cpp");   // input file
    string line, token;
    int lineNo = 0;

    map<string, vector<int>> symbolTable;

    while (getline(file, line)) {
        lineNo++;
        token = "";

        for (int i = 0; i <= line.length(); i++) {
            char ch = line[i];

            if (isalnum(ch) || ch == '_') {
                token += ch;
            } else {
                if (!token.empty()) {
                    if (isKeyword(token)) {
                        cout << token << " -> Keyword at line " << lineNo << endl;
                    } else {
                        cout << token << " -> Identifier at line " << lineNo << endl;
                        symbolTable[token].push_back(lineNo);
                    }
                    token = "";
                }
            }
        }
    }

    cout << "\nSymbol Table\n";
    cout << "Identifier\tLine Numbers\n";
    for (auto &entry : symbolTable) {
        cout << entry.first << "\t\t";
        for (int ln : entry.second)
            cout << ln << " ";
        cout << endl;
    }

    file.close();
    return 0;
}
