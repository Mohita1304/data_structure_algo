# Find the number of digits in the given number , given n>0.
from llama_index.core.workflow.utils import import_module_from_qualified_name


# define the function
def count_digit(x):
    count=0
    while x >0:
        x=x//10
        count=count+1
    return count


# execution
if __name__ == "__main__":
    number= 790
    print(count_digit(number))