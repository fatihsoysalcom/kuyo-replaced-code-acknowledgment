def filter_even_numbers_legacy(numbers):
    """
    Filters even numbers from a list using a traditional loop.
    This represents an older implementation that might be less efficient
    or harder to read than newer alternatives.
    """
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def filter_even_numbers_modern(numbers):
    """
    Filters even numbers from a list using a modern list comprehension.
    This represents an improved, more concise, and often more Pythonic
    implementation.
    """
    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":
    data = list(range(1, 21)) # Example data

    print("Original data:", data)
    print("-" * 40)

    # --- The "Kuyō" Moment for Deleted Code ---
    # This section illustrates the article's core concept: acknowledging
    # and respectfully phasing out old code, much like a memorial service.
    print("Acknowledging 'filter_even_numbers_legacy' (the old code):")
    print("This function once served its purpose well but has been superseded.")
    print("Instead of silent deletion, we pause to acknowledge its past contribution.")
    print("In a real project, this function would now be marked for deprecation,")
    print("or commented out, before its eventual final removal from the codebase.")
    print("----------------------------------------")

    # Demonstrate the old way (for comparison, or if still temporarily in use
    # during a transition phase, though no longer the primary path).
    print("\nDemonstrating the *legacy* function (for comparison/context):")
    legacy_result = filter_even_numbers_legacy(data)
    print("Result from legacy function:", legacy_result)
    print("-" * 40)

    # Demonstrate the new, preferred way
    print("\nUsing the *modern*, improved function (the current solution):")
    modern_result = filter_even_numbers_modern(data)
    print("Result from modern function:", modern_result)
    print("-" * 40)

    print("\nThis example simulates the transition where 'filter_even_numbers_legacy'")
    print("is the 'deleted code' being honored, while 'filter_even_numbers_modern'")
    print("is its successor.")
