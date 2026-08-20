# Prolog setup

**Installed:** SWI-Prolog 10.0.2 (x64) at `C:\Program Files\swipl\bin\swipl.exe`
`C:\Program Files\swipl\bin` was appended to your **user** PATH.

> Open a **new** terminal before `swipl` resolves by name — existing shells still
> have the old PATH.

## Run a program

Interactive toplevel (the normal way to work):

```bash
swipl family.pl
```

Then at the `?-` prompt type a query ending in `.` — e.g. `father(X, aditya).`
Press `;` for the next solution, Enter to stop, `halt.` to quit.

Run one goal and exit (good for quick checks and marking):

```bash
swipl -g main -t halt family.pl
```

Ad-hoc query without editing the file:

```bash
swipl -g "father(X,aditya), format('X = ~w~n',[X])" -t halt family.pl
```

Helper script, same two modes:

```bash
powershell -File run.ps1 -File family.pl -Goal main
```

## Reloading while the toplevel is open

Edit the file, then at the `?-` prompt:

```
make.
```

That recompiles changed files without restarting.

## Notes / gotchas

- **`FATHER-MOTHER` is Turbo/Visual Prolog**, not standard Prolog. Its
  `predicates` / `clauses` / `goal` sections are a Turbo Prolog dialect and
  SWI-Prolog will reject them. `family.pl` is the ported version: drop the
  section headers, declare no types, and replace the `goal` section with a
  `main` predicate.
- **Backslashes are escapes inside quoted atoms.** `'C:\Users\...'` is a syntax
  error in Prolog. Use forward slashes: `'C:/Users/...'`.
- **Standalone `.exe` builds do not work on this SWI build.** `qsave_program/2`
  writes the file, but running it fails with `STATUS_ENTRYPOINT_NOT_FOUND`
  (0xC0000139), with or without `stand_alone(true)`. Use the `swipl -g ... -t halt`
  form above instead — for coursework "compile and run" that is the expected
  workflow anyway.

## Editor

VS Code is installed; the **"VSC-Prolog"** extension (`arthurwang.vsc-prolog`)
gives syntax highlighting, linting and a run command. Not installed — add it
from the Extensions pane if you want it.
