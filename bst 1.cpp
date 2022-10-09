#include<bits/stdc++.h>
using namespace std;
class node {
	public:
		int value;
		node* left;
		node* right;
};
class tree{
	public:
		node* root;
		tree(){root=NULL;}
        void inorder(){ inorder(root);}
		void inorder(node *p);
		void preorder(){preorder(root);}
		void preorder(node *p);
		void postorder(){postorder(root);}
		void postorder(node *p);
		int search(int x);
		void insert(int x);
		node* deleten(node *p,int k);
		node* inpre(){ inpre(root->left);}
		node* inpre(node *p);
		node* insucc(){ insucc(root->right);}
		node* insucc(node *p);
		int height(){height(root);}
		int height(node *p);
};
node* tree::deleten (node *p,int k){
	if(p==NULL) {return NULL;
	}
	node *q;
	if(p->left==NULL && p->right==NULL){
		if(p==root){
			root=NULL;
		}
		delete(p);
		return NULL;
	}
	if(k<p->value){
		p->left=deleten(p->left,k);
	}else if(k>p->value){
		p->right=deleten(p->right,k);
	}else{ 
	         if(height(p->right)>height(p->left)){
	         	q=insucc(p->right);
	         	p->value=q->value;
	         	p->right=deleten(p->right,q->value);
			 }
			 else{
			 q=inpre(p->left);
			 p->value=q->value;
			 p->left=deleten(p->left,q->value);     
	}	
}
return p;}
int tree::height(node *p){
	int x,y;
	if(p==NULL){
		return 0;
	}
	y=height(p->right);
	x=height(p->left);
	return x>y?x+1:y+1;
}
node* tree::inpre(node *p){
	if(p==NULL){
		return p;
	}else{
	
	while(p && p->right!=NULL){
     p=p->right;
	}
	return p;}
} 
node* tree::insucc(node *p){
	if(p==NULL){
		return p;
	}
	else{
	
	while(p && p->left!=NULL){
     p=p->left;
	}
	return p;}
} 
void tree :: insert(int x){
		node *n=new node;
	n->value=x;
	n->right=NULL;
	n->left=NULL;
	if(root==NULL){
		root=n;
		return;
	}
	node* r;
	node* t=root;
	while(t!=NULL){
		r=t;
		if(x>t->value){ t=t->right;}
		else if(x<t->value) t=t->left;
		else return;
	}
	if(x>r->value){
		r->right=n;
	}
	else r->left=n;

}
void tree::inorder(node *p){
	if(p){
	    inorder(p->left);
		cout<<p->value<<" ";
		inorder(p->right);
	}
} 
void tree::preorder(node *p){
	if(p){
		cout<<p->value<<" ";
	    preorder(p->left);
		preorder(p->right);
	}
} 

void tree::postorder(node *p){
	if(p){
	    postorder(p->left);
		postorder(p->right);
		cout<<p->value<<" ";
	}
} 
int tree::search(int x){
	 node *t=root;
while(t!=NULL)
{
if(x==t->value)
return x;
else if(x<t->value)
t=t->left;
else
t=t->right;
}
return -1;
}	
int main(){
	tree t;
	vector<int> a={30,20,40,10,25,35,45,42,43};
	for(auto v:a){
		t.insert(v);
	}
	t.preorder();
	cout<<endl;
	t.inorder();
	cout<<endl;
	t.postorder();
	cout<<endl;
	int y=t.search(3);
	if(y!=-1) cout<<"YES";
	else cout<<"NO";
	node *s = t.inpre();
	cout<<"\n"<<s->value<<endl;
	s=t.insucc();
	cout<<s->value<<endl;
	int x=t.height();
	cout<<x<<endl;
	t.deleten(t.root,30);
	t.preorder();  
	cout<<endl;
	return 0;
}