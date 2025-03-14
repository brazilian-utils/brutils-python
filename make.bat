@echo off

SET 	@PYTHONDONTWRITEBYTECODE=1 poetry run python3 -m unittest discover tests\ -v

IF /I "%1"=="install" GOTO install
IF /I "%1"=="shell" GOTO shell
IF /I "%1"=="run-python" GOTO run-python
IF /I "%1"=="format" GOTO format
IF /I "%1"=="check" GOTO check
IF /I "%1"=="test" GOTO test
GOTO error

:install
	@git config --local core.hooksPath .githooks/
	GOTO :EOF

:shell
	@poetry shell
	GOTO :EOF

:run-python
	@poetry run python
	GOTO :EOF

:format
	@poetry run ruff format .
	@poetry run ruff check --fix .
	GOTO :EOF

:check
	@poetry run ruff format --check .
	@poetry run ruff check .
	GOTO :EOF

:test
	@PYTHONDONTWRITEBYTECODE=1 poetry run python3 -m unittest discover tests/ -v
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
