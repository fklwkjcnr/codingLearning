//1 1 2 3 5 8 13 21 34 55 89 144
function fib(n){
    if(n==1){
       return 1;
    }
    if(n==2){
        return 1;
    }
    return fib(n-1)+fib(n-2);
}