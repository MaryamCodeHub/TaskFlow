def render_dashboard(tasks):
    print("--- Task Dashboard ---")
    for t in tasks:
        status = "Done" if t.completed else "Pending"
        print(f"[{status}] {t.name}")
