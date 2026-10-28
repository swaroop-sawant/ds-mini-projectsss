from collections import deque

def job_scheduling():
    n = int(input("\nEnter number of jobs: "))

    if n <= 0:
        print("Number of jobs must be positive!")
        return

    graph = [[] for _ in range(n)]
    indegree = [0] * n

    m = int(input("Enter number of dependencies: "))

    if m < 0 or m > n * (n - 1):
        print("Invalid number of dependencies!")
        return

    print("\nEnter dependencies as: job1 job2")
    print("(job1 must finish before job2)")

    for _ in range(m):
        try:
            u, v = map(int, input().split())
        except ValueError:
            print("Invalid input! Enter two job numbers.")
            return

        if not (1 <= u <= n and 1 <= v <= n):
            print("Invalid job number!")
            return

        if u == v:
            print("A job cannot depend on itself!")
            return

        graph[u - 1].append(v - 1)
        indegree[v - 1] += 1

    # Find jobs with no prerequisites
    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    # Topological sorting
    while queue:
        job = queue.popleft()
        order.append(job + 1)

        for neighbour in graph[job]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(order) == n:
        print("\nJob Scheduling Order:")
        print(" -> ".join(map(str, order)))
        print("All jobs scheduled successfully!")
    else:
        print("\nCycle detected!")
        print("Jobs cannot be scheduled because of circular dependencies.")


# Main menu
while True:
    print("\n===== JOB SCHEDULING SYSTEM =====")
    print("1. Schedule Jobs")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        try:
            job_scheduling()
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "2":
        print("\nThank you for using the Job Scheduling System!")
        print("Program exited successfully.")
        break

    else:
        print("\nInvalid choice! Please enter 1 or 2.")
