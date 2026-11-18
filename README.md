# Ghostwire

**Headless browser session recorder that exports clean, deterministic Playwright test scripts directly from user interaction recordings.**

Writing reliable UI tests by hand is tedious and fragile, requiring constant element locator updates and manual event sequencing. Ghostwire eliminates this friction by recording browser interactions directly and emitting ready-to-run Python Playwright scripts.

## Worked Example

Record a session navigating to example.com and clicking a link, then output the generated Playwright script:

```bash
$ ghostwire record --url https://example.com --output test_example.py
```

Console output:
```
[ghostwire] Starting recording session on https://example.com...
[ghostwire] Browser launched (headless).
[ghostwire] Recording interactions... Press Ctrl+C to stop.
[ghostwire] Captured navigation: https://example.com/
[ghostwire] Captured click: text="More information..."
[ghostwire] Session recording stopped.
[ghostwire] Writing Playwright test script to test_example.py...
[ghostwire] Successfully exported test script (5 events recorded).
```

Generated `test_example.py`:
```python
import re
from playwright.sync_api import Page, expect

def test_recorded_session(page: Page) -> None:
    page.goto("https://example.com/")
    page.get_by_text("More information...").click()
    expect(page).to_have_url(re.compile(r".*iana\.org.*"))
```

## Install

Install in editable mode from a local clone:

```bash
pip install -e .
```

## Usage

- `ghostwire record --url <url> --output <file>`: Record browser session and export Playwright test script.
- `ghostwire check <file>`: Validate a recorded test script against deterministic rules.

## How it works

- Instruments headless browser navigation and DOM events via Playwright inspection hooks.
- Captures click, input, navigation, and assertion events into an intermediate event log.
- Filters out noise, transient hover events, and flaky timing delays.
- Emits idiomatic synchronous Python Playwright test functions with typed page fixtures.

## Limitations

- Only exports Python synchronous Playwright scripts (async and TypeScript exports are not currently supported).
- Does not record complex multi-window or cross-domain popup interactions.
- Relies on headless Chromium; other browser engines are not tested.
