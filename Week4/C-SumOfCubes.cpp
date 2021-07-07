#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <map>
using namespace std;
#define ll long long

map<ll,ll>mp;

int main() {
  for(ll i = 1; i <= 10000; i++) {
    mp[i * i * i] = 1;
  }

  int t;
  cin >> t;

  while(t--) {
    ll n;
    cin >> n;
    int flag = 0;
    for(ll i = 1; i <= 10000; i++) {
      if(mp[n-i*i*i] == 1) {
        flag = 1;
        break;
      }
    }
    if(flag == 1)
      cout<<"YES"<<endl;
    else
      cout<<"NO"<<endl;
  }

  return 0;
}