from cfd import mesh

def main() -> None:
    test_length = 12345
    cfd_mesh = mesh.discretize_1d_even(length=test_length)

if __name__ == "__main__":
    main()