#include <stdio.h>
#include <stdbool.h>

char* longestCommonPrefix(char** strs, int strSize);

int main(void){
    char** strs = {"flower", "flow", "flight"};
    int size = 3;
    char* prefix = longestCommonPrefix(strs, size);
    int i = 0;
    while(prefix[i] != '\0'){
        printf("%c", prefix[i]);
        i++;
    }

}

char* longestCommonPrefix(char** strs, int strSize){
    bool samePref = true;
    int j = 0;
    char* prefix;

    while(samePref){
        for(int i = 0 ; i < strSize ; i++){
            char letter = strs[0][i];
            if(strs[i][j] != letter){
                samePref = false;
                return prefix;
            }
            else{
                prefix[j] = letter;
            }
        }
        j++;
    }


    return "";
}