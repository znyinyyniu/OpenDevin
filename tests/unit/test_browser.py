from opendevin.runtime.browser.browser_env import BrowserEnv


def test_browse():
    browser = BrowserEnv()
    asked_url = 'https://www.baidu.com'
    action_str = f'goto("{asked_url}")'
    obs = browser.step(action_str)
    print(obs['screenshot'])
