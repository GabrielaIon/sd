#include <iostream>

using namespace std;

struct Nod {
    int cheie;
    bool exista;
    Nod *left;
    Nod *next;

    Nod() :
            left(nullptr), next(nullptr) {}

    Nod(int key_, Nod *left_, Nod *next_) :
            cheie(key_), left(left_), next(next_) {}

    void addChild(Nod *n) {
        if (left == nullptr)
            left = n;
        else {
            n->next = left;
            left = n;
        }
    }
};

bool Empty(Nod *n) {
    return (n == nullptr);
}

int FindMin(Nod *n) {
    return n->cheie;
}

Nod *Merge(Nod *n, Nod *m) {
    if (n == nullptr) return m;
    if (m == nullptr) return n;
    if (n->cheie < m->cheie) {
        n->addChild(m);
        return n;
    } else {
        m->addChild(n);
        return m;
    }
}

int root(Nod *n) {
    return n->cheie;
}

Nod *Push(Nod *node, int key) {
    return Merge(node, new Nod(key, nullptr, nullptr));
}

Nod *TwoPassMerge(Nod *n) {
    if (n == nullptr || n->next == nullptr)
        return n;
    else {
        Nod *nod1, *nod2, *newNode;
        nod1 = n;
        nod2 = n->next;
        newNode = n->next->next;

        nod1->next = NULL;
        nod2->next = NULL;

        return Merge(Merge(nod1, nod2), TwoPassMerge(newNode));
    }
}

Nod *Pop(Nod *node) {  // sterge elem min
    return TwoPassMerge(node->left);
}

void Delete(Nod *n, int x){
    if (n -> cheie == x && ){
        n -> exista = false;
    }
    if(n->next != nullptr)
        Delete(n->next, x);
    if(n->left != nullptr)
        Delete(n->left, x);
}

struct PairHeap {
    Nod *root;

    PairHeap() :
            root(NULL) {}

    bool Empty(void) {
        return ::Empty(root);
    }

    int Top(void) {
        return ::root(root);
    }

    void Push(int key) {
        root = ::Push(root, key);
    }

    void Pop(void) {
        root = ::Pop(root);
    }

    void Join(PairHeap other) {
        root = ::Merge(root, other.root);
    }

    void lazy(int x) {
        ::Delete(root, x);
    }
};

int main(void) {

    PairHeap heap1, heap2;
    heap1.Push(5);
    heap1.Push(3);

    heap2.Push(4);
    heap2.Push(2);

    heap1.Join(heap2);
    cout << heap1.Top() << endl;

    heap1.Pop();
    cout << heap1.Top() << endl;

    heap1.lazy(3);
    cout << heap1.Top() << endl;


    return 0;
}
