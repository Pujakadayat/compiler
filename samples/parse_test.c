/*
* this is a test for the AST
* the root of the tree should have the "if statement"
* three children should also develop
* first child: the conditional
* second child: the if body
* third child: the else body
*/

int main(void) {

  int a = 2;
  int b = 3;
  int c;

	if (a < b)
  {
    c = 2;
    return c;
  }
  else {
    c = 3;
  }

	return 0;
}
