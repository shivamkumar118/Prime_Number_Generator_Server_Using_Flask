# Prime_Number_Generator_Server_Using_Flask
Part-1 : Prime Number Generator Python Program
that gives all prime numbers in the range between two numbers provided by the user (e.g. user gives 1 and 10 and it will return "2, 3, 5, 7").

Input : 10 20
Output : "11,13,17,19"

Input : 101 909
Output : "101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907"


Part-2 : Prime Number Generator Server Using Flask

Using the code from part 1 as the generation engine, a server application (in the same programming language Python as above) giving the user the chance to use prime number generator over a REST API over HTTP. 

For all users, each execution in a database, its frequency ,each timestamp, and number of primes is recorded and stored in database.

flask, flask_sqlalchemy, datetime and math modules are used.
