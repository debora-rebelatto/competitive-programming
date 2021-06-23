#include <bits/stdc++.h>
typedef long long ll;
typedef long double ld;
#define fr(i, a, b) for (ll i = a; i < b; i++)
#define rf(i, a, b) for (ll i = a; i >= b; i--)
typedef std::vector<long long> vi;
#define F first
#define S second
#define fast                      \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
#define mod 1000000007
#define PB push_back
#define MP make_pair
#define PI 3.14159265358979323846
#define all(a) a.begin(), a.end()
#define mx(a) *max_element(all(a))
#define mn(a) *min_element(all(a))
const ll INF = LLONG_MAX / 2;
const ll N = 2e5 + 1;
using namespace std;
void solve()
{
    ll n, i, j = 0;
    std::cin >> n;
    ll a[n];
    fr(i, 0, n)
            cin >>
        a[i];
    ll maxi = *max_element(a, a + n), mini = *min_element(a, a + n), maxii, minii;
    fr(i, 0, n)
    {
        if (a[i] == maxi)
            maxii = i + 1;
        if (a[i] == mini)
            minii = i + 1;
    }
    ll c = maxii, d = minii;
    if (c < d)
        swap(c, d);
    cout << min({n - (c - d - 1), n - d + 1, c}) << "\n";
}
int main()
{
    fast;
    ll _ = 1, counti = 0;
    std::cin >> _;
    while (_--)
    {
        // counti++;
        // cout << "Case #" << counti << ": ";
        solve();
    }
}