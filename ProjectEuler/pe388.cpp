#include <iostream>
#include <math.h>

using namespace std;

struct v3
{
	int X;
	int Y;
	int Z;
};

v3 getNormal(int X, int Y, int Z)
{
	int vlen = sqrt((X * X) + (Y * Y) + (Z * Z));
	v3 result;
	result.X = X/vlen;
	result.Y = Y/vlen;
	result.Z = Z/vlen;
	return result;
}

