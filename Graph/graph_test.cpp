#include "Graph.h"
using namespace std;

int main()
{
	Graph* g1 = new Graph;
	g1->generateGraph(12);
	g1->printNodes();
	delete g1;
};