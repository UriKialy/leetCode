#include <iostream>
#include <bitset>
#include <cstdint>
#include <string>
#include <vector>
#include <set>
#include <math.h>
#include <algorithm>
using namespace std;

string addBinary(string a, string b)
{
    int x = stoi(a);
    int y = stoi(b);
    while (y != 0)
    {
        int carry = (~x) & y;
        x = x ^ y;
        y = (unsigned int)carry << 1;
    }
    return to_string(x);
}

uint32_t reverseBits(uint32_t n)
{
    string bits = bitset<32>(n).to_string();
    string reversedBits = "";
    for (int i = bits.size() - 1; i >= 0; i--)
    {
        reversedBits += bits[i];
    }
    return static_cast<uint32_t>(bitset<32>(reversedBits).to_ullong());
}

int hammingWeight(int n)
{

    int count = 0;
    string bits = bitset<32>(n).to_string();
    for (char c : bits)
    {
        if (c == '1')
        {
            count++;
        }
    }
    return count;
}

int singleNumber(vector<int> &nums)
{
    int result = 0;
    for (int i : nums)
    {
        result = result ^ i;
    }
    return result;
}
int subarrayBitwiseORs(vector<int> &arr)
{
    set<int> s;
    set<int> prev;
    for (int a : arr)
    {
        set<int> curr;
        curr.insert(a);
        for (int x : prev)
        {
            curr.insert(x | a);
        }
        s.insert(curr.begin(), curr.end());
        prev = move(curr);
    }
    return s.size();
}

char findKthBit(int n, int k)
{
    string s = "0";
    for (int i = 2; i <= n; ++i)
    {
        string inverted;
        inverted.reserve(s.size());
        for (char c : s)
        {
            inverted.push_back(c == '0' ? '1' : '0');
        }
        reverse(inverted.begin(), inverted.end());
        s = s + '1' + inverted;
    }
    return s[k - 1];
}

int main()
{
    char c = findKthBit(4, 11);
    cout << c << endl;
}

// 011100110110001
// 011100110110001