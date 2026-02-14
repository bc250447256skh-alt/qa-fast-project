import { test, expect } from '@playwright/test';
import { LoginPage } from '../ui/login.page';

test('Valid user can add item to cart', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.navigate();
  await loginPage.login('standard_user', 'secret_sauce');

  await page.click('.inventory_item button');
  await expect(page.locator('.shopping_cart_badge')).toHaveText('1');
});

test('Locked user cannot login', async ({ page }) => {
  const loginPage = new LoginPage(page);

  await loginPage.navigate();
  await loginPage.login('locked_out_user', 'secret_sauce');

  await expect(page.locator('[data-test="error"]')).toBeVisible();
});
