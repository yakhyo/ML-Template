# project-template

## Commit Message Convention

### Commit Message Format

```
<Type>: Short description

Longer description here if necessary

BREAKING CHANGE: only contain breaking change
```
- Any line of the commit message cannot be longer 100 characters!

### Revert
```
revert: commit <short-hash>

This reverts commit <full-hash>
More description if needed
```

### Type
| Syntax      | Description                 | Detailed Description     |
| :---        | :-----                      | :----           |
| `feat`      | Features                    | A new feature   |
| `fix`       | Bug Fixes                   | A bug fix       |
| `docs`      | Documentation               | Documentation only changes      |
| `style`     | Styles                      | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)      |
| `refactor`  | Code Refactoring            | A code change that neither fixes a bug nor adds a feature      |
| `perf`      | Performance Improvements    | A code change that improves performance      |
| `test`      | Tests        | Adding missing tests or correcting existing tests     |
| `build`     | Builds        | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)    |
| `ci`        | Continuous Integrations     | Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)      |
| `chore`     | Chores                      | Other changes that don't modify src or test files      |
| `revert`    | Reverts                     | Reverts a previous commit      |

### Subject
- use the imperative, __present__ tense: "change" not "changed" nor "changes"
- do capitalize the first letter
- no dot (.) at the end

### Body

- use the imperative, __present__ tense: "change" not "changed" nor "changes".
- the motivation for the change and contrast this with previous behavior.

### BREAKING CHANGE
- This commit contains breaking change(s).
- start with the word BREAKING CHANGE: with a space or two newlines. The rest of the commit message is then used for this.