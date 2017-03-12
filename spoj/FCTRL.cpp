#include <cstdio>
#include <cmath>

using namespace std;

int z(int n)
{
	int res = 0;
	int a = 5;
	int ex = 1;
	while (a <= n)
	{
		res += n / a;
		ex += 1;
		a = pow(5, ex);
	}
	return res;
}

int main()
{
	int l, n;
	scanf("%d", &l);
	while(l--)
	{
		scanf("%d", &n);
		printf("%d\n", z(n));
	}
	return 0;
}



