#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        
        for(const auto& c: s){
            if(stack.empty()){
                stack.push(c);
            }else{
                char top = stack.top();
                if( (top == '[') && (c == ']') ){
                    stack.pop();
                }else if( (top == '(') && (c == ')') ){
                    stack.pop();
                }else if( (top == '{') && (c == '}') ){
                    stack.pop();
                }else{
                    stack.push(c);
                }
            }
            
        }
    
        return stack.empty();
    }
};

// Runtime 3ms, beats %40.96
// Memory 7.84MB, beats %46.10
