import { test, expect } from "@playwright/test";

test("navigation test", async ({ page }) => {
  await page.goto("http://localhost:3000/");

  // Navigate to Hire Me page
  await page.click('a:has-text("Hire Me")');

  // Navigate to Let's Talk page
  await page.click('a:has-text("Let\'s Talk")');

  // Navigate to Services page
  await page.click('a:has-text("Services")');

  // Navigate to Projects page
  await page.click('a:has-text("Projects")');

  // Navigate to About page
  await page.click("text=About");

  // Navigate to Resume page
  await page.click('a:has-text("Resume")');

  // Navigate to Privacy page
  await page.click('a:has-text("Privacy")');
});
