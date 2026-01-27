#include <iostream>
#include <string>
#include <cctype>
#include <fstream>
#include <sstream>
using namespace std;

bool isKeyword(string s) {
    string keywords[] = {"int", "float", "if", "else", "while", "return"};
    for (string k : keywords)
        if (s == k) return true;
    return false;
}

bool isIdentifier(string s) {
    if (!isalpha(s[0]) && s[0] != '_') return false;
    for (char c : s)
        if (!isalnum(c) && c != '_') return false;
    return true;
}

int main(int argc, char* argv[]) {
    string code;
    string filename = (argc > 1) ? argv[1] : "Mohit_Kumar_sample.txt";
    ifstream in(filename);
    if (in) {
        ostringstream ss;
        ss << in.rdbuf();
        code = ss.str();
        cout << "Read input from file: " << filename << "\n";
    } else {
        cout << "Could not open file '" << filename << "'. Enter a line of C-like code (EOF to finish):\n";
        string line;
        while (getline(cin, line)) {
            code += line;
            code += '\n';
        }
    }

    string token = "";
    for (size_t i = 0; i <= code.length(); i++) {
        char ch = (i < code.length()) ? code[i] : ' ';

        if (isalnum((unsigned char)ch) || ch == '_') {
            token += ch;
        } else {
            if (!token.empty()) {
                if (isKeyword(token))
                    cout << token << " -> Keyword\n";
                else if (isIdentifier(token))
                    cout << token << " -> Identifier\n";
                token = "";
            }

            if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
                cout << ch << " -> Arithmetic Operator\n";
            else if (ch == '<' || ch == '>')
                cout << ch << " -> Relational Operator\n";
            else if (ch == ';' || ch == ',' || ch == '(' || ch == ')' || ch == '{' || ch == '}')
                cout << ch << " -> Delimiter\n";
        }
    }
    return 0;
}
