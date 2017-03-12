#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

int leastPrime(int n)
{
	if (n == 2) return 2;
	if (n == 3) return 3;
	if (n % 2 == 0) return 2;
	if (n % 3 == 0) return 3;
	int i = 5;
	int w = 2;
	while (i*i <= n)
	{
		if (n % i == 0)
			return i;
		i += w;
		w = 6 - w;
	}
	return n;
}

bool isPrime(int n)
{
	return leastPrime(n) == n;
}

//vector<int> primeFactors(int n)
//{
//	vector<int> result;
//	while (n > 1)
//	{
//		int a = leastPrime(n);
//		result.push_back(a);
//		while (n % a == 0) 
//		{
//			n /= a;
//		}
//	}
//	return result;
//}

int totient(int n)
{
	int lp = leastPrime(n);
	if (n == lp) return n - 1;
	if (gcd(n, lp) == 1)
		return totient(lp) * totient(n/lp);
	int product = n;
	int p = leastPrime(n);
	while (p > 1)
	{
		product *= (1.0f - 1.0f/(float)p);
		while (n % p == 0)
		{
			n /= p;
		}
		p = leastPrime(n);
	}
	return (int)product;
}
	
int main(int argc, char* argv[])
{
	char *endptr;
	long int MAX = strtol(argv[1], &endptr, 10);
	int p_sum = 0;
	map<int, int> chain_length;
	//map<int, int> totients = getTotients(MAX);
	chain_length[2] = 2;
	for (int i = 4; i < MAX; i += 2)
	{
		if (i % 1000000 == 0) cout<< i <<endl;
		int tot = totient(i);
		int len_i = chain_length[tot] + 1;
		chain_length[i] = len_i;
		if (len_i == 24 && isPrime(i + 1)) 
		{
			p_sum += i + 1;
		}
	}
	cout<< "sum = " << p_sum <<endl;
}


