import java.io.*;
import java.util.ArrayList;

// A binary tree node
class Node {
	
	int data;
	Node left, right;
	
	Node(int d) {
		data = d;
		left = right = null;
	}
}

class BinarySearchTree
{
	
	// Root of BST
	Node root;

	// Constructor
	BinarySearchTree() {
		root = null;
	}
	
	// Inorder traversal of the tree
	void inorder()
	{
		inorderUtil(this.root);
	}
	
// Utility function for inorder traversal of the tree
void inorderUtil(Node node)
{
	if(node==null)
		return;
		
	inorderUtil(node.left);
	System.out.print(node.data + " ");
	inorderUtil(node.right);
}
	

	// A Utility Method that stores inorder traversal of a tree
	public ArrayList<Integer> storeInorderUtil(Node node, ArrayList<Integer> list)
	{
		if(node == null)
			return list;
		
		//recur on the left child
		storeInorderUtil(node.left, list);
		
		// Adds data to the list
		list.add(node.data);
		
		//recur on the right child
		storeInorderUtil(node.right, list);
		
		return list;
	}
	
	// Method that stores inorder traversal of a tree
	ArrayList<Integer> storeInorder(Node node)
	{
		ArrayList<Integer> list1 = new ArrayList<>();
		ArrayList<Integer> list2 = storeInorderUtil(node,list1);
		return list2;
	}

	// Method that merges two ArrayLists into one.
	ArrayList<Integer> merge(ArrayList<Integer>list1, ArrayList<Integer>list2, int m, int n)
	{
		// list3 will contain the merge of list1 and list2
		ArrayList<Integer> list3 = new ArrayList<>();
		int i=0;
		int j=0;
		
		//Traversing through both ArrayLists
		while( i<m && j<n)
		{
			// Smaller one goes into list3
			if(list1.get(i)<list2.get(j))
			{
				list3.add(list1.get(i));
				i++;
			}
			else
			{
				list3.add(list2.get(j));
				j++;
			}
		}
		
		// Adds the remaining elements of list1 into list3
		while(i<m)
		{
			list3.add(list1.get(i));
			i++;
		}
	
		// Adds the remaining elements of list2 into list3
		while(j<n)
		{
			list3.add(list2.get(j));
			j++;
		}
		return list3;
	}
	
	// Method that converts an ArrayList to a BST
	Node ALtoBST(ArrayList<Integer>list, int start, int end)
	{
		// Base case
		if(start > end)
			return null;
	
		// Get the middle element and make it root	
		int mid = (start+end)/2;
		Node node = new Node(list.get(mid));

		/* Recursively construct the left subtree and make it
		left child of root */
		node.left = ALtoBST(list, start, mid-1);
		
		/* Recursively construct the right subtree and make it
		right child of root */
		node.right = ALtoBST(list, mid+1, end);
	
	return node;
	}
	
	// Method that merges two trees into a single one.
	Node mergeTrees(Node node1, Node node2)
	{
		//Stores Inorder of tree1 to list1
		ArrayList<Integer>list1 = storeInorder(node1);
		
		//Stores Inorder of tree2 to list2
		ArrayList<Integer>list2 = storeInorder(node2);
		
		// Merges both list1 and list2 into list3
		ArrayList<Integer>list3 = merge(list1, list2, list1.size(), list2.size());
		
		//Eventually converts the merged list into resultant BST
		Node node = ALtoBST(list3, 0, list3.size()-1);
		return node;
	}

	// Driver function
	public static void main (String[] args)
	{

		BinarySearchTree tree1 = new BinarySearchTree();
		tree1.root = new Node(100);
		tree1.root.left = new Node(50);
		tree1.root.right = new Node(300);
		tree1.root.left.left = new Node(20);
		tree1.root.left.right = new Node(70);
		
		/* 
    EXAMPLE :
    
    Creating following tree as second balanced BST
				80
				/ \
			40 120
		*/
    
    
		BinarySearchTree tree2 = new BinarySearchTree();
		tree2.root = new Node(80);
		tree2.root.left = new Node(40);
		tree2.root.right = new Node(120);
			
			
		BinarySearchTree tree = new BinarySearchTree();
		tree.root = tree.mergeTrees(tree1.root, tree2.root);
		System.out.println("The Inorder traversal of the merged BST is: ");
		tree.inorder();
	}
}

