import src.conways as conways
import src.fibonacci as fibonacci
import src.mysinh as mysinh
import src.mystats as mystats


def main() -> None:
    mysinh.test_factorial()
    mysinh.test_sinh()
    fibonacci.test_fibonacci()
    mystats.test_mean()
    mystats.test_mode()
    mystats.test_median()
    mystats.test_standard_deviation()
    # conways.test_conways()
    return


if __name__ == "__main__":
    main()
