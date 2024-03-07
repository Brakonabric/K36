#pragma once
#include <vector>
#include <map>
using namespace std;


class Graph
{
private:
	// ��������� ���� �����
	struct GraphNode
	{
		int id;
		int number;
		int level;
		int p1_score;
		int p2_score;
		vector<GraphNode*> ChildNodes;

	//����������� ����
		GraphNode(int id, int number, int level, int p1_score, int p2_score) : id(id), number(number), level(level), p1_score(p1_score), p2_score(p2_score) {}
	};
	//����� �����
	map<int, GraphNode*> nodes;
public:
	//����������� �����
	Graph() {}
	//���������� �����
	~Graph();
	//����� ����������� � ����� ����� ����� ���� (���������� ������� generateGraph())
	void addNode(int id, int number, int level, int p1_score, int p2_score);
	//����� ��������� ���� �����(srcId) � �����(endId)
	void addEdge(int srcId, int endId);
	//����� ������� � ������� ���� �����(debug)
	void printNodes();
	//����� ������� ���� �������� ��������� �����
	void generateGraph(int startNum);
};

