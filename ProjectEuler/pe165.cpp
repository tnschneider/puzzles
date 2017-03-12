#include <iostream>
#include <math.h>

using namespace std;

class bssSeq
{
	private:
	int s;
	int m1;
	int m2;
	
	public:
	bssSeq(int seed, int mod1, int mod2)
	{
		s = seed;
		m1 = mod1;
		m2 = mod2;
	}
	int iter()
	{
		s = (s*s) % m1;
		cout << s << endl;
		return s % m2;
	}
};

class lineSeg
{
	private:
	int x1;
	int y1;
	int x2;
	int y2;
	
	public:
	lineSeg() { }
	lineSeg(int X1, int Y1, int X2, int Y2)
	{
		x1 = X1; y1 = Y1; x2 = X2; y2 = Y2;
	}
	double length()
	{
		int x = x2 - x1;
		int y = y2 - y1;
		return sqrt(x*x + y*y);
	}
};

int main()
{
	const int NUM_SEGMENTS = 1950;
	bssSeq s = bssSeq(290797, 50515093, 500);
	int i = 0;
	lineSeg segments[NUM_SEGMENTS];
	while (i < NUM_SEGMENTS)
	{
		int x1 = s.iter();
		int y1 = s.iter();
		int x2 = s.iter();
		int y2 = s.iter();
		lineSeg seg = lineSeg(x1, y1, x2, y2);
		segments[i] = seg;
		i++;
	}
}
