// @ts-check
const { test, expect } = require("@playwright/test");

const localUrl = "http://localhost:3000/";

// Checking hero sections main sentence
test("Check for hero section h1 main sentence", async ({ page }) => {
  const elianTitle = "Hi, I'm Elian Morales Pina";

  await page.goto(process.env.URL || localUrl);

  const h1Selector = `h1:has-text("${elianTitle}")`;
  await expect(page.locator(h1Selector)).toBeVisible();
  await expect(page.locator(h1Selector)).toHaveText(elianTitle);
});

// Checking hero sections slogan
test("Check for hero section sub slogan", async ({ page }) => {
  const elianPosition = "Data Scientist and Web Devlopment Student";

  await page.goto(process.env.URL || localUrl);

  const h3Selector = `h3:has-text("${elianPosition}")`;
  await expect(page.locator(h3Selector)).toBeVisible();
  await expect(page.locator(h3Selector)).toHaveText(elianPosition);
});
