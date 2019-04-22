int mult(int a, int b) {
	return a * b;
}

int sum(int a, int b) {
	return a + b;
}

int div(int a, int b) {
	return a / b;
}

int sub(int a, int b) {
	return a - b;
}

int main() {
	int a = sum(3, 2);
	int b = a;

	if (b == 4) {
		b = 20;
	} else {
		b = 30;
	}

	int c = div(b, 10);
	int d = 100;

	while (c > 0) {
		d++;
		c--;
	}

	return d;
}
