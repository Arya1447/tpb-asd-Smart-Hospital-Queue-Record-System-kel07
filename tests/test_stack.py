import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

from src.data_structures.stack import Stack

# TEST STACK

stack = Stack()

# push data
stack.push('Periksa tekanan darah')

stack.push('Pemberian obat')

stack.push('Rontgen')

print(
    '\n=== ISI STACK ==='
)

current = stack.top

while current:

    print(
        current.data
    )

    current = current.next


print(
    '\n=== POP ==='
)

removed = stack.pop()

print(
    'Data dihapus:',
    removed
)

print(
    '\n=== STACK SETELAH POP ==='
)

current = stack.top

while current:

    print(
        current.data
    )

    current = current.next


print(
    '\nTop Stack:',
    stack.peek()
)

print(
    'Total data:',
    stack.size
)