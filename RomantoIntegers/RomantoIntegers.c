#include <stdio.h>

int romanToInt(char* s);
int findValue(char s);

int main(void){

    char* s = "LVIII";

    int num = romanToInt(s); 
    // printf("%d\n", num);

    return 0;
}

int romanToInt(char *s){

    //I is 1
    //V is 5
    //X is 10
    //L is 50
    //C is 100
    //D is 500
    //M is 1000

    int sum = 0;
    int i = 0;
    int p1 = 0;
    int p2 = 0;

    if(s[1] == '\0'){
        return findValue(s[0]);
    }

    while(s[i] != '\0'){
        p1 = findValue(s[i]);
        if(s[i+1] != '\0'){
            p2 = findValue(s[i+1]);
            // printf("%d\n", p2);
            if(p1 < p2){
                // printf("dif %d\n", p2-p1);
                sum += (p2 - p1);
                i += 2;
            }
            else{
                sum += p1;
                // printf("sum %d\n", sum);
                i++;
            }
        }
        else{
            sum+=p1;
            i++;
        }
    }

    return sum;
}

int findValue(char s){
        if(s == 'I'){
            return 1;
        }
        else if(s == 'V'){
            return 5;
        }
        else if(s == 'X'){
            return 10;
        }
        else if(s == 'L'){
            return 50;
        }
        else if(s == 'C'){
            return 100;
        }
        else if(s == 'D'){
            return 500;
        }
        else{
            return 1000;
        }
}