    #JS EXERCISE EXCERPT 1---------------------------------------------------------

    # const getName = () => {
    #   let name = prompt("what is your name?");
    #   return name;
    # };

#GET NAME EXERCISE 1---------------------------------------------------------

# name = input("what is your name?")
# print(name)

    #JS EXERCISE EXCERPT 2---------------------------------------------------------

    # const reverseIt = () => {
    #   let string = "a man, a plan, a canal, frenemies!";

    #   let reverse = "";

    #   for (let i=0; i < string.length; i++) {
    #     reverse += string[string.length - (i+1)];
    #   };

    #   alert(reverse);
    # };

#REVERSE IT EXERCISE 2---------------------------------------------------------------------

# def reverseIt():
#     string = "a man, a plan, a canal, frenemies!"
#     reverse = ""

#     for i in range(len(string)):
#         reverse += string[len(string) - (i+1)]

#     print(reverse)

# reverseIt()

    #JS EXERCISE EXCERPT 3---------------------------------------------------------

    # const swapEm = () => {
    #   let a = 10;
    #   let b = 30;
    #   let temp;

    #   temp = b;
    #   b = a;
    #   a = temp;

    #   alert("a is now " + a + ", and b is now " + b);
    # };

#SWAP EM EXERCISE 3---------------------------------------------------------------------

# def swapEm():
#     a = 10
#     b = 30

#     temp = b
#     b = a
#     a = temp

#     print("a is now " + str(a) + ", and b is now " + str(b))

# swapEm()

    #JS EXERCISE EXCERPT 4-------------------------------------------------------------------------

    # const multiplyArray = (ary) => {
    #     if (ary.length == 0) { return 1; };

    # let total = 1;
    # // let total = ary[0];

    # for (let i=0; i < ary.length; i++) {
    #     total = total * ary[i];
    # };

    # return total;
    # };

#MULTIPLY ARRAY/LIST EXERCISE 4---------------------------------------------------------------------

# def multiplyArray (ary):
#     if len(ary) == 0:
#         return 1
#     total = 1
#     total = ary[0]

#     for i in range(len(ary)):
#         total = total * ary[i]

#     print(total)

# multiplyArray([1,2,4,5,6])

    #JS EXERCISE EXCERPT 5-------------------------------------------------------------------------

    # const fizzbuzzer = (x) => {
    #     if( x%(3*5) == 0 ) {
    #         return 'fizzbuzz'
    #     } else if( x%3 == 0 ) {
    #         return 'fizz'
    #     } else if ( x%5 == 0 ) {
    #         return 'buzz'
    #     } else {
    #         return 'archer'
    #     }
    # }

#FIZZBUZZER EXERCISE 5-------------------------------------------------------------------------------

# def fizzbuzzer(x):
#     if x%(3*5) == 0:
#         return 'fizzbuzz'
#     elif x%3 == 0:
#         return "fizz"
#     elif x%5 == 0:
#         return 'buzz'
#     else:
#         return 'archer'
    
# print (fizzbuzzer(23))

    #JS EXERCISE EXCERPT 6-----------------------------------------------------------------------------
    # const nthFibonacciNumber = () => {
    #     let fibs = [1, 1];
    #     let num = prompt("which fibonacci number do you want?");

    #     while (fibs.length < parseInt(num)) {
    #         let length = fibs.length;
    #         let nextFib = fibs[length - 2] + fibs[length - 1];
    #         fibs.push(nextFib);
    #     }

    #     alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
    # };

#NTH FIBONACCI NUMBER EXERCISE 6-------------------------------------------------------------------------

# def nthFibonacciNumber():
#     fibs = [1,1]
#     num = int(input("which fibonacci number do you want?"))

#     while len(fibs) < int(num):
#         nextFib = fibs [- 2] + fibs [-1]
#         fibs.append(nextFib)

#         print(str(fibs[-1]) + " is the fibonacci number at position" + str(num))

# nthFibonacciNumber()

    #JS EXERCISE EXCERPT 7-----------------------------------------------------------------------------
    # const searchArray = (array, value) => {
    #     for(let i = 0; i < array.length-1; i++) {
    #         if(array[i] == value) {
    #         return true;
    #         break;
    #         }
    #     }
    #     return -1;
    #     };

#SEARCH ARRAY/LIST EXERCISE 7-------------------------------------------------------------------------
# def searchArray(array, value):
#     for i in range (len(array)):
#         if array[i] == value:
#             return True
       
#     return False
# print(searchArray([1,2,3,4,5,6], 4))

#     #JS EXERCISE EXCERPT 8-----------------------------------------------------------------------------
#     const isPalindrome = (str) => {
#         for(let i = 0; i < str.length/2; i++){
#             if(str[i] != str[str.length-i-1]){
#                 return false;
#                 break;
#             }
#         }
#         return true;
#     };

#PALINDROME EXERCISE 8-------------------------------------------------------------------------

# def isPalindrone(str):
#     for i in range(len(str)//2):
#         if str[i] !=str[len(str)-i-1]:
#             return False
#     return True
# print(isPalindrone("racecar"))

    #JS EXERCISE EXCERPT 9-----------------------------------------------------------------------------
    
    # const hasDupes = (arr) => {
    #     let obj = {};
    #     for (i = 0; i < arr.length; i++) {
    #         if(obj[arr[i]]) {
    #         return true;
    #         }
    #         else {
    #         obj[arr[i]] = true;
    #         }
    #     }
    #     return false;
    # };

#HASDUPES EXERCISE 9----------------------------------------------------------------------------

# def hasDupes(arr):
#     obj = {}
#     for i in range(len(arr)):
#         if obj.get(arr[i]):
#             return True
#         else:
#             obj[arr[i]] = True
#     return False
# print(hasDupes([1,2,3,4,5,6,7,8,9,10,10]))

