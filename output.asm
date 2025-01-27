.globl	_main
_main:
pushq %rbp
movq %rsp, %rbp
_L1:
		 # Moving arguments into registers
movl -4(%rbp), %r8d
callq _printf
		 # Saving the return value
movl %eax, -8(%rbp)
		 # Return 0
movl $0, %eax
popq %rbp
retq
_L2:
movl $0, %eax
addq $8, %rsp
popq %rbp
retq