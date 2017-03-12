#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <stdio.h>

using namespace std;

double endingBalance(double f, double starting_balance, int num_trials, int wins)
{
	return starting_balance * pow (1 + 2*f, wins) * pow (1 - f, num_trials - wins);
}

int winsNeeded(double f, double starting_balance, int num_trials, double target, double error)
{
	int guess = floor(num_trials / 2); 
	int ub = num_trials;
	int lb = 0;
	double result = endingBalance(f, starting_balance, num_trials, guess);
	
	while(abs(result - target) > error)
	{
		cout << fixed << "guess: " << guess << endl;
		cout << fixed << "result: " << result << endl;
		cout << fixed << "error: " << abs(result - target) << endl;
		if (result < target)
		{
			lb = guess;
			guess = floor((guess + ub) / 2);
		}
		else
		{
			ub = guess;
			guess = floor((guess + lb) / 2);
		}
		result = endingBalance(f, starting_balance, num_trials, guess);
	}
	
	return guess;
}

int main(int argc, char *argv[])
{
	double f, starting_balance, ending_balance;
	int num_trials, wins;
	
	/*sscanf(argv[1], "%lf", &f);
	sscanf(argv[2], "%lf", &starting_balance);
	sscanf(argv[3], "%d", &num_trials);
	sscanf(argv[4], "%d", &wins);*/
	
	//ending_balance = endingBalance(f, starting_balance, num_trials, wins);
	int wins_needed = winsNeeded(.25, 1, 1000, 1000000000, .1);
	
	cout << wins_needed << endl;
}