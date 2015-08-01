#include<iostream>
#include<string>
using namespace std;

template <typename T>
int Compare(const T &v1,const T &v2)
{
 if(v1>v2) return -1;
 if(v1<v2) return 1;
 return 0;
}

int main()
{
cout<<Compare(1,10)<<endl;
string s1="a";
string s2="b";
cout<<Compare(s1,s2)<<endl;
return 0;
}
