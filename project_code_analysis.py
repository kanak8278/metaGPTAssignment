import os
import subprocess
import ast

def run_pylint(file_path):
    try:
        result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
        return f"Pylint analysis for {file_path}:\n{result.stdout}"
    except Exception as e:
        return f"Error running Pylint for {file_path}: {e}"

def run_pep8(file_path):
    try:
        result = subprocess.run(['pycodestyle', file_path], capture_output=True, text=True)
        return f"PEP8 analysis for {file_path}:\n{result.stdout}"
    except Exception as e:
        return f"Error running PEP8 for {file_path}: {e}"

def analyze_ast(file_path):
    result = []
    try:
        with open(file_path, 'r') as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not node.body:
                    result.append(f"Empty function {node.name} in {file_path}")
        return "\n".join(result)
    except Exception as e:
        return f"Error in AST parsing for {file_path}: {e}"

def check_incomplete_code(file_path):
    result = []
    incomplete_keywords = ['TODO', 'FIXME', 'TBD']
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for keyword in incomplete_keywords:
                if keyword in line:
                    result.append(f"Incomplete code found in {file_path} at line {i+1}: {line.strip()}")
    return "\n".join(result)

if __name__ == "__main__":
    project_dir = "./workspace/new/sudoku_game_02"  # Replace with the path to your generated project
    analysis_results = []  # List to store all analysis results

    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                analysis_results.append(run_pylint(file_path))
                # analysis_results.append(run_pep8(file_path))
                analysis_results.append(analyze_ast(file_path))
                analysis_results.append(check_incomplete_code(file_path))

    # Write all analysis results into a single file
    analysis_file_path = os.path.join(project_dir, "analysis_report.txt")
    with open(analysis_file_path, 'w') as f:
        f.write("\n".join(analysis_results))
