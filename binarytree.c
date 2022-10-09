#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *ladd;
    struct node *radd;
};
struct node *root=NULL,*New;
struct node * create();
void inorder();
void preorder();
void postorder();
void leafnode();
void leftleafnode();
void rightleafnode();
void NodeWhoseLefNodeIsNull();
void NodeWhoseRightNodeIsNull();
void NodewhoseEitherLeftNodeOrRightNodeIsNull();
void insert();
void search();
int main(){
    int ch,n;
    do{
        printf("\n\n--------------------------BINARY TREE------------------\n");
        printf("enter 1 to create a binary tree\n");
        printf("enter 2 to display binary tree in accending order\n");
        printf("enter 3 to display binary tree in preorder\n");
        printf("enter 4 to display binary tree in post order\n");
        printf("enter 5 to know leaf nodes\n");
        printf("enter 6 to get the value of leftmost leaf node\n");
        printf("enter 7 to get the value of righttmost leaf node\n");
        printf("enter 8 to get value of node whose left node is empty\n");
        printf("enter 9 to get node whose right node is empty\n");
        printf("enter 10 to get the values of all node who has either left node or right node\n");
        printf("enter 11 to insert\n");
        printf("enter 12 to search an element\n");
        printf("enter 13 to exit\n");
        printf("enter your choice-->");
        scanf("%d",&ch);
        switch(ch){
            case 1:
            printf("enter a value-->");
            scanf("%d",&n);
            while(n!=0){
                root= create(root,n);
                printf("enter next value-->");
                scanf("%d",&n);
            }
            break;
            case 2:
            inorder(root);
            break;
            case 3:
            preorder(root);
            break;
            case 4:
            postorder(root);
            break;
            case 5:
            leafnode(root);
            break;
            case 6:
            leftleafnode(root);
            break;
            case 7:
            rightleafnode(root);
            break;
            case 8:
            NodeWhoseLefNodeIsNull(root);
            break;
            case 9:
            NodeWhoseRightNodeIsNull(root);
            break;
            case 10:
            NodewhoseEitherLeftNodeOrRightNodeIsNull(root);
            break;
            case 11:
            printf("enter a value-->");
            scanf("%d",&n);
            insert(root,n,root);
            break;
            case 12:
            printf("enter the value ");
            scanf("%d",&n);
            search(root,n);
            break;
            case 13:
            break;
            default:
            printf("enter a valid choice");
            break;
        }
    }while(ch!=13);
    return 0;
}

struct node * create(struct node *p,int n){
    if(p==NULL){
        p=(struct node*) malloc(sizeof(struct node));
        p->data=n;
        p->ladd=NULL;
        p->radd=NULL;
    }
    else{
        if(n<p->data){
            p->ladd=create(p->ladd,n);
        }
        else if(n>p->data){
            p->radd=create(p->radd,n);
        }
        else{
            printf("a binary tree cant have same values");
        }
    }
    return(p);
}
void inorder(struct node *p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            inorder(p->ladd);
            printf("%d ||",p->data);
            inorder(p->radd);
        }
    }
} 
void preorder(struct node *p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            printf("%d ||",p->data);
            preorder(p->ladd);
            preorder(p->radd);
        }
    }
}
void postorder(struct node *p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            postorder(p->ladd);
            postorder(p->radd);
            printf("%d ||",p->data);
        }
    }
}

void leafnode(struct node *p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            leafnode(p->ladd);
            leafnode(p->radd);
            if(p->ladd==NULL&&p->radd==NULL){
                printf("%d ||",p->data);
            }
        }
    }
}

void leftleafnode(struct node*p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            leftleafnode(p->ladd);
            if(p->ladd==NULL&&p->radd==NULL){
                printf("%d ||",p->data);
            }
        }
    }
}
void rightleafnode(struct node*p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            rightleafnode(p->radd);
            if(p->ladd==NULL&&p->radd==NULL){
                printf("%d ||",p->data);
            }
        }
    }
}

void NodeWhoseLefNodeIsNull(struct node*p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            NodeWhoseLefNodeIsNull(p->ladd);
            if(p->ladd==NULL&&p->radd!=NULL){
                printf("%d ||",p->data);
            }
            NodeWhoseLefNodeIsNull(p->radd);
        }
    }
}

void NodeWhoseRightNodeIsNull(struct node *p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            NodeWhoseRightNodeIsNull(p->ladd);
            if(p->radd==NULL&&p->ladd!=NULL){
                printf("%d ||",p->data);
            }
            NodeWhoseRightNodeIsNull(p->radd);
        }
    }
}
void NodewhoseEitherLeftNodeOrRightNodeIsNull(struct node *p){
    if(root== NULL){
        printf("please create a binary tree first");
    }
    else{
        if(p!=NULL){
            NodewhoseEitherLeftNodeOrRightNodeIsNull(p->ladd);
            if(p->ladd!=NULL || p->radd!=NULL){
                printf("%d ||",p->data);
            }
            NodewhoseEitherLeftNodeOrRightNodeIsNull(p->radd);
        }
    }
}
void insert(struct node *p,int n,struct node*c){
    if(root==NULL){
        printf("please create binary tree first..");
    }
    else{
        if(p!=NULL){
            if(n<p->data){
                insert(p->ladd,n,p);
            }
            else if(n>p->data){
                insert(p->radd,n,p);
            }
            else{
                printf("invalid value");
            }
        }
        else{
            New=(struct node*) malloc(sizeof(struct node));
            New->data=n;
            New->ladd=NULL;
            New->radd=NULL;
            if(n>c->data){
                c->radd=New;
            }
            else if(n<c->data){
                c->ladd=New;
            }
        }

    }
}

void search(struct node *p,int n){
    if(root == NULL){
        printf("please create a binary tree first.....");
    }
    else{
        if(p!=NULL){
            if(n==p->data){
                printf("element found at %x node and value is %d",p,p->data);
            }
            else if(n<p->data){
                search(p->ladd,n);
            }
            else if(n>p->data){
                search(p->radd,n);
            }
        }
        else{
            printf("element is not in binary tree");
        }
    }
}