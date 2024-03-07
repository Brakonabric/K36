#include "Graph.h"
#include <vector>
#include <map>
#include <iostream>
#include <queue>
using namespace std;


Graph::~Graph()
{
    for (auto& temp : nodes)
    {
        delete temp.second;
    }
}


void Graph::addNode(int id, int number, int level, int p1_score, int p2_score)
{
    if (level % 2 != 0)
    {
        if (number % 2 == 0) p1_score++;
        else if (p1_score > 0) p1_score--;
    }
    else
    {
        if (number % 2 == 0) p2_score++;
        else if (p2_score > 0) p2_score--;
    }
    nodes[id] = new GraphNode(id, number, level, p1_score, p2_score);
}


void Graph::addEdge(int srcId, int endId)
{
    nodes[srcId]->ChildNodes.push_back(nodes[endId]);
}


void Graph::printNodes() //debug
{
    for (auto temp1 = nodes.begin(); temp1 != nodes.end(); temp1++)
    {
        cout << "|" << temp1->second->p1_score << " " << temp1->second->number << " " << temp1->second->p2_score << "|" << endl;
        for (auto temp2 = temp1->second->ChildNodes.begin(); temp2 != temp1->second->ChildNodes.end(); temp2++)
        {
            cout << "|" << (*temp2)->p1_score << " " << (*temp2)->number << " " << (*temp2)->p2_score << "|" << " ";
        }
        cout << endl;
    }
}


void Graph::generateGraph(int startNum)
{
    int maxNum = 1000;
    int nodeID = 0;
    //root node
    nodes[nodeID] = new GraphNode(nodeID, startNum, 0, 0, 0);
    queue <GraphNode*> nQueue;
    nQueue.push(nodes[nodeID]);

    while (!nQueue.empty())
    {
        GraphNode* currentNode = nQueue.front();
        nQueue.pop();

        if (currentNode->number < maxNum)
        {
            addNode(nodeID + 1, currentNode->number * 2, currentNode->level + 1, currentNode->p1_score, currentNode->p2_score);
            nQueue.push(nodes[nodeID + 1]);
            addNode(nodeID + 2, currentNode->number * 3, currentNode->level + 1, currentNode->p1_score, currentNode->p2_score);
            nQueue.push(nodes[nodeID + 2]);


            addEdge(currentNode->id, nodeID + 1);
            addEdge(currentNode->id, nodeID + 2);

            nodeID += 2;
        }
    }
}