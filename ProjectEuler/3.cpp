#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
	char *endptr;
	long int input = strtol(argv[1], &endptr, 10);
	long int best;
	long int divisor = 2;
	for (;;)
	{
		if (input == divisor)
		{
			break;
		}
		else if (input % divisor == 0)
		{
			input /= divisor;
			cout << input << endl;
		}
		else divisor += 2;
	}
	cout << input << " " << divisor << endl;
}
	