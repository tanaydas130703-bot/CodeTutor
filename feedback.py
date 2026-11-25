import ast

TASKS = {
    "Functions": {
        "question": "Write a function add(a, b) that returns the sum of two numbers.",
        "starter": "def add(a, b):\n    print(a + b)",
        "solution": "def add(a, b):\n    return a + b",
        "hint": "Use return to pass the sum back to the caller."
    },
    "Conditionals": {
        "question": "Write is_positive(n) to return True when n is greater than zero.",
        "starter": "def is_positive(n):\n    print(n > 0)",
        "solution": "def is_positive(n):\n    return n > 0",
        "hint": "Compare n with zero and return the Boolean result."
    },
    "Loops": {
        "question": "Write total(numbers) using a for loop to return the sum of a list.",
        "starter": "def total(numbers):\n    result = 0\n    for n in numbers:\n        result += n\n    print(result)",
        "solution": "def total(numbers):\n    result = 0\n    for n in numbers:\n        result += n\n    return result",
        "hint": "Return the accumulated result after the loop."
    }
}


def check_code(task, code, detailed=False):
    correct = False
    evidence = ""
    explanation = ""

    try:
        tree = ast.parse(code)
        expected = ast.parse(TASKS[task]["solution"])

        if ast.dump(tree) == ast.dump(expected):
            correct = True
            issue = "Your code matches the supported solution."
            suggestion = "No changes are required."
            explanation = "The function returns the expected expression using the required structure."
            next_step = "Try another exercise."

        elif not any(isinstance(n, ast.Return) for n in ast.walk(tree)):
            issue = "No return statement was detected."
            suggestion = TASKS[task]["hint"]
            explanation = "Printing displays a value, whereas returning makes it available to the function caller. For example, return 5 passes a value back to the caller."
            next_step = "Revise your code and submit again."

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print":
                    evidence = ast.get_source_segment(code, node) or ""
                    break
        else:
            issue = "The checker cannot verify this solution."
            suggestion = TASKS[task]["hint"]
            explanation = "Different implementations can be valid. This prototype recognises limited syntax patterns and does not execute submitted code."
            next_step = "Review the requirements or consult a tutor."

    except SyntaxError as error:
        issue = "Python syntax error."
        suggestion = f"Check line {error.lineno}: {error.msg}."
        explanation = "Python must be able to parse the program before its structure can be analysed."
        next_step = "Correct the syntax and retry."

    if detailed:
        suggestion += "\n\n" + explanation

    return {
        "correct": correct,
        "issue": issue,
        "suggestion": suggestion,
        "next_step": next_step,
        "evidence": evidence
    }
