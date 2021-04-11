#include <iostream>
#include "IntArray.cpp"

using namespace std;

int main()
{
    cout << "Creating empty array" << endl;
    IntArray a{};
    cout << a.Size() << endl;
    cout << a.IsEmpty() << endl;

    IntArray b{10};
    cout << b.Size() << endl;
    cout << b.IsEmpty() << endl;

    b[0] = 100;
    cout << b[0] << endl;
}
