from sympy import symbols, Eq, solve

# Define the variables
x1, x2, lam = symbols('x1 x2 lambda', real=True)

# Define the objective function's gradient
grad_f = [2*x1, 2*x2]

# Define the constraint's gradient
grad_g = [2*(x1 - 4), 2*(x2 - 3)]

# Equating gradient of f to lambda times gradient of g
eq1 = Eq(grad_f[0], lam * grad_g[0])
eq2 = Eq(grad_f[1], lam * grad_g[1])


# Solve for x1 and x2 in terms of lambda
x1_sol = solve(eq1, x1)[0]
x2_sol = solve(eq2, x2)[0]

# Constraint equation
constraint_eq = Eq((x1 - 4)**2 + (x2 - 3)**2, 1)

# Substitute x1 and x2 into the constraint equation
constraint_substituted = constraint_eq.subs({x1: x1_sol, x2: x2_sol})

# Solve for lambda
lambda_solutions = solve(constraint_substituted, lam)

# Calculate x1 and x2 for each solution of lambda
solutions = [(x1_sol.subs(lam, sol), x2_sol.subs(lam, sol)) for sol in lambda_solutions]
print(min(solutions))