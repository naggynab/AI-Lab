# run.ps1 -- load a Prolog file and drop into the interactive ?- toplevel
#   .\run.ps1 family.pl          -> consult family.pl, then you get the ?- prompt
#   .\run.ps1 family.pl main     -> consult, run goal `main`, then exit
param(
    [Parameter(Mandatory = $true)][string]$File,
    [string]$Goal
)

$swipl = 'C:\Program Files\swipl\bin\swipl.exe'
if (-not (Test-Path $swipl)) { Write-Error "swipl.exe not found at $swipl"; exit 1 }
if (-not (Test-Path $File))  { Write-Error "No such file: $File"; exit 1 }

if ($Goal) {
    & $swipl -g $Goal -t halt $File
} else {
    & $swipl $File
}
