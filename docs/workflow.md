# Development Workflow

This project follows a structured Git workflow to ensure clean history and collaborative development.

1. **Branching Strategy:**
   - `main`: Stores production-ready releases.
   - `development`: Used for ongoing integration of features.
   - Feature/bug-fix branches (e.g., `feature/auth`, `bugfix/login`): Used for developing isolated changes.

2. **Commit Management:**
   - Small, incremental commits.
   - Clear and meaningful commit messages explaining the 'why' and 'what'.

3. **Pull Requests and Code Review:**
   - All feature branches are merged into `development` via Pull Requests.
   - PRs must have descriptive titles and body content.
   - At least one code review is required before merging. Review comments must be addressed with new commits on the branch.
   
4. **Releases:**
   - Merging `development` into `main` signifies a stable release, which is then tagged (e.g., `v1.0.0`).
