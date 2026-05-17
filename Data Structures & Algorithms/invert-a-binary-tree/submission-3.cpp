/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr){return nullptr;}
        vector<TreeNode*> que;
        TreeNode *cur, *tmp;
        que.push_back(root);
        while (que.size() > 0)
        {
            cur = que.back();
            que.pop_back();
            tmp = cur->left;
            cur->left = cur->right;
            cur->right = tmp;

            if (cur->right)
            {
                que.push_back(cur->right);
            }
            if (cur->left)
            {
                que.push_back(cur->left);
            }
        }

        return root;
    }
};
