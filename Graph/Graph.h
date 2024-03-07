#pragma once
#include <vector>
#include <map>
using namespace std;


class Graph
{
private:
	// Структура узла графа
	struct GraphNode
	{
		int id;
		int number;
		int level;
		int p1_score;
		int p2_score;
		vector<GraphNode*> ChildNodes;

	//конструктор узла
		GraphNode(int id, int number, int level, int p1_score, int p2_score) : id(id), number(number), level(level), p1_score(p1_score), p2_score(p2_score) {}
	};
	//карта графа
	map<int, GraphNode*> nodes;
public:
	//конструктор графа
	Graph() {}
	//деструктор графа
	~Graph();
	//метод добавляющий в карту графа новый узел (вызывается методом generateGraph())
	void addNode(int id, int number, int level, int p1_score, int p2_score);
	//метод соеденяет узел графа(srcId) с узлом(endId)
	void addEdge(int srcId, int endId);
	//метод выводит в консоль узлы графа(debug)
	void printNodes();
	//метод создает граф принимая начальное число
	void generateGraph(int startNum);
};

