#include <iostream>
#include <math.h>
using namespace std;

int n, count; 
int main (){
	cin >> n;
    for (int a = 1; a < n; a++){
        for (int b = a; b < n; b++){
            int aux  = ((a * a) + (b * b));
            int c = sqrt(aux);
            if((c*c == (aux)) && (c <= n)){
                count += 1;
            }else if(c > n)
                break;
        }
    }
    cout << count << endl;
}
