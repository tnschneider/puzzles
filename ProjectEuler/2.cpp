#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int input = (int)argv[1];
	int best;
	int divisor = 2;
	for (;;)
	{
		if (input % divisor == 0)
		{
			input = input / divisor;
			best = divisor;
		}
		divisor++;
}
	