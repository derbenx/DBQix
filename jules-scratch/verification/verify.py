import pytest
from playwright.sync_api import Page, expect

def test_qix_game_loads_without_errors(page: Page):
    """
    This test verifies that the Qix game page loads without any console errors.
    """

    # 1. Arrange: Listen for console errors.
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

    # 2. Act: Go to the index.html page.
    page.goto("http://localhost:8000/index.html")

    # 3. Wait for the scene to load.
    page.wait_for_timeout(5000)

    # 4. Assert: Check for console errors.
    assert len(errors) == 0, f"Console errors found: {errors}"

    # 5. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")
