# GitHub Actions Workflow Setup Example

## Generate TODO and FIXME for whole repo
-  `.github/workflows/*.yml`  
   - In the repository where the action should run, navigate to `Settings` -> `Actions` (under `General`)
   - Locate `Workflow permissions` and enable **"Read and write permissions"**. This permission is required for workflows that generate or modify files, such as tasks that automate "To-Do" lists

## Create Issue from TODO
- see project [TODO to Issue](https://github.com/marketplace/actions/todo-to-issue)
