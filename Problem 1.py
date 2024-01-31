from ortools.linear_solver import pywraplp

n, m = map(int, input().split())
D = []

for i in range(n):
    ai, bi = map(int, input().split())
    D.append([ai, bi])

c = list(map(int, input().split()))
L = []
U = []

for i in range(m):
    l, u = map(int, input().split())
    L.append(l)
    U.append(u)

A = []
for i in range(m):
    a = list(map(int, input().split()))
    A.append(a)
def solve(n, m, D, c, L, U, A):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    X = [solver.IntVar(D[i][0], D[i][1], "") for i in range(n)]

    for u in range(m):
        constraint = solver.Constraint(L[u], U[u])
        for i in range(n):
            constraint.SetCoefficient(X[i], A[u][i])
    Objective = solver.Objective()

    for i in range(n):
        Objective.SetCoefficient(X[i], c[i])
    Objective.SetMaximization()
    result_status = solver.Solve()
    if result_status == pywraplp.Solver.OPTIMAL:
        print(int(solver.Objective().Value()))
    else:
        print('NOT_FOUND')
solve(n, m, D, c, L, U, A)