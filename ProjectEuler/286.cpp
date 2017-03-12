#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
typedef vector<int> combo;

double prob(int x, int q) 
{
	return 1 - (x / q);
}

double[] probs(int q) 
{
	double[] arr = new double[];
	for (int i = 1, i <= 50, ++i)
	{
		arr[i] = prob(i, q)
	}
}

vector<combo> combos(int size, int N)
{
	int[] base;
	for (int i = 0; i < size; ++i)
	{
		base[i] = i + 1;
	}
	vector<combo> combos;
	
	do_combos(combos, base, size, N);
	
	return combos;
}




double p_t(int q)
{
	double p = 0;
	double[] probs = probs(q);
	
	
	return p;
}

int main(int argc, char *argv[])
{
	double q = 100;
	
	
	
	
	
	
	
	
	
	cout << input << " " << divisor << endl;
}
	