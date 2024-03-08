#pragma once
#include <vector>
#include <map>
using namespace std;

class Graph
{
private:
	// Struct defining properties of a graph node
	struct GraphNode
	{
		int id;                 // Node ID
		int number;             // Arbitrary number associated with the node
		int level;              // Level of the node in the graph hierarchy
		int p1_score;           // Score associated with player 1
		int p2_score;           // Score associated with player 2
		vector<GraphNode*> ChildNodes; // Child nodes of this node

		// Constructor to initialize the node
		GraphNode(int id, int number, int level, int p1_score, int p2_score) : id(id), number(number), level(level), p1_score(p1_score), p2_score(p2_score) {}
	};

	// Map to store nodes with their IDs as keys
	map<int, GraphNode*> nodes;

public:
	// Constructor
	Graph() {}

	// Destructor
	~Graph();

	// Function to add a new node to the graph
	void addNode(int id, int number, int level, int p1_score, int p2_score);

	// Function to add an edge between two nodes in the graph
	void addEdge(int srcId, int endId);

	// Function to print information about all nodes in the graph
	void printNodes();

	// Function to generate a graph starting from a specified number
	void generateGraph(int startNum);
};
