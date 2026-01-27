#include <iostream>
#include <regex>
#include <string>
using namespace std;

int main() {
    string code = R"(
        // Single line comment
        int a = 10;
        float b = 20.5;
        /* Multi-line
           comment */
        char str[] = "Hi this is Mohit this side ";
    )";

    regex singleLineComment("//.*");
    regex multiLineComment("/\\*[\\s\\S]*?\\*/");
    regex stringLiteral("\".*?\"");
    regex floatNum("\\b\\d+\\.\\d+\\b");
    regex integerNum("\\b\\d+\\b");
    regex identifier("\\b[a-zA-Z_][a-zA-Z0-9_]*\\b");

    cout << "Single-line Comments:\n";
    for (sregex_iterator it(code.begin(), code.end(), singleLineComment), end; it != end; it++)
        cout << it->str() << endl;

    cout << "\nMulti-line Comments:\n";
    for (sregex_iterator it(code.begin(), code.end(), multiLineComment), end; it != end; it++)
        cout << it->str() << endl;

    cout << "\nString Literals:\n";
    for (sregex_iterator it(code.begin(), code.end(), stringLiteral), end; it != end; it++)
        cout << it->str() << endl;

    cout << "\nFloating Numbers:\n";
    for (sregex_iterator it(code.begin(), code.end(), floatNum), end; it != end; it++)
        cout << it->str() << endl;

    cout << "\nIntegers:\n";
    for (sregex_iterator it(code.begin(), code.end(), integerNum), end; it != end; it++)
        cout << it->str() << endl;

    cout << "\nIdentifiers:\n";
    for (sregex_iterator it(code.begin(), code.end(), identifier), end; it != end; it++)
        cout << it->str() << endl;

    return 0;
}
