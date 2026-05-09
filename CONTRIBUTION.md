# Contributing Guide 

Thank you for contributing to the Docker Python Challenges project!

This repository contains intentionally broken Docker + Python projects designed for learning, debugging, and improving DevOps skills.

---

# How To Contribute

## 1. Fork The Repository

Click the **Fork** button on GitHub.

---

## 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/docker-python-challenges.git
```
## 3. Create A New Branch
```bash
git checkout -b fix/challenge-1
```
## Fixing Challenges

Each challenge is intentionally broken.

Your task is to:

- Identify the issue
- Fix the Docker/Python problem
- Ensure the container works correctly
- Follow Docker best practices

# Verify Your Solution

Before submitting your fix:

## Build

```bash
docker build -t test-image .
```
## Run
```
docker run -p 5000:5000 test-image

docker run --rm test-image
```

## Contribution Rules
### DO

- Keep fixes focused
- Follow Docker best practices
- Keep images minimal
- Add comments if useful
- Improve security where possible

### DO NOT

- Remove the challenge entirely
- Rewrite unrelated code
- Add unnecessary dependencies
- Commit secrets or credentials

## Push Your Changes
```
git add .
git commit -m "fix: solve challenge3 multi-stage build issue"
git push origin fix/challenge-3
```
## Open A Pull Request

Go to GitHub and open a Pull Request from your branch.

### Include:

- What was broken
- What you fixed
- Any improvements made


## Example 
## Fixed

- Corrected broken CMD
- Improved Docker layer caching
- Added non-root user
- Reduced image size

## Result

Container now builds and runs successfully.

## Happy Debugging

