#include <stdio.h>
#include <stdbool.h>

bool isValid(char* s);
bool isValidHelper(char* s, int i, int current);

int main(void){
    char *s = "()[]{}";
    printf("%d\n", '{');
    printf("%d\n", '}');
    printf("%s", isValid(s)?"true":"false");

    return 0;
}

bool isValid(char* s){

    //( 40
    //) 41
    //[ 91
    //] 93
    //{ 123
    //} 125

    return isValidHelper(s, 0, s[0]);
}

bool isValidHelper(char* s, int i, int current){
    
        if(current == 123 || current == 91 || current == 40){
            if(s[i+1] == s[i]+1 || s[i+1] == s[i]+2){
                return isValidHelper(s, i+2, s[i+2]);
            }
            else if(s[i+1] == 123 || s[i+1] == 91 || s[i+1] == 40){
                return isValidHelper(s, i+1, s[i+1]);
            }
            else{
                return false;
            }
        }
    
}