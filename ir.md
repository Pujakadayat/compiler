int add(int a, int b) {
	return a - b;
}

int main() {
	int x = 4;
	int y = 5;
	int z;

	z = add(x, y);

	if (z > 7) {
		x = y * ( z + 1);
	} else {
		x = y / z;
	}

	return x;
}

BECOMES, IN IR:

.Add(int a, int b)
r1 <- a + b
ret r1

.Main()
x <- 4
y <- 5
z <- call Add(x, y)
r1 <- z > 7
if r1 GOTO branch1 ELSE branch2

branch1:
r2 = z + 1
x = y * r2
GOTO branch3

branch2:
x <- y / z
GOTO branch3

branch3:
ret x


Constant Propogation : replace variables with constants forward until var is re-assigned
Dead code elimination : check for gotos and delete unused branches
Function inlining : replace short function calls as straight operations in the current scope

Need to keep indeces of branches and functions by name (dict)
Convert parse tree nodes to IR
Helper function to generate new unused variable names (like lodash)
