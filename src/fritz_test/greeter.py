def greet(name: str) -> None:
    """Prints a greeting message using the provided name."""
    print(f"Hello, {name}! Welcome to the system.")

if __name__ == "__main__":
    # Example usage demonstrating the fix
    test_name = "Fritz"
    greet(test_name)