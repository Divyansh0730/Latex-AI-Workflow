<#
.SYNOPSIS
    Latex AI Workflow - Quick PowerShell Builder
.EXAMPLE
    .\build.ps1 -File "templates/technical_specification/main.tex"
    .\build.ps1 -File "templates/technical_specification/main.tex" -Inspect
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$File,

    [switch]$Inspect,

    [string]$Distro = "Ubuntu-22.04"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$workflowPy = Join-Path $scriptDir "latex_workflow.py"

if ($Inspect) {
    python $workflowPy inspect $File --distro $Distro
} else {
    python $workflowPy build $File --distro $Distro
}
