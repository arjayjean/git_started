import subprocess
from selenium import webdriver
subprocess.run('clear')

directory = input(f'Name the directory: ').lower()
new_directory = f'FILE/{directory}'


PATH = '/Users/USER/chromedriver'
URL = 'https://github.com/new'
driver = webdriver.Chrome(PATH)
driver.get(URL)

# SIGN IN
github_username = driver.find_element_by_xpath('//*[@id="login_field"]')
github_username.send_keys('') # YOUR USERNAME

github_password = driver.find_element_by_xpath('//*[@id="password"]')
github_password.send_keys('') # YOUR PASSWORD

github_sign_in_button = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
github_sign_in_button.click()

# AUTHENTICATION 
github_authentication = driver.find_element_by_xpath('//*[@id="otp"]')
subprocess.run('clear')
authentication_code = input('Enter the authentication code: ')
github_authentication.send_keys(f'{authentication_code}')

# NEW REPOSITORY
create_repository = driver.find_element_by_xpath('//*[@id="repository_name"]')
create_repository.send_keys(f'{directory}')
create_repository.submit()
driver.quit()

commands = [
    ['mkdir',f'{new_directory}'],
    ['touch',f'{new_directory}/{directory}.py'],
    ['python3', '-m', 'venv', f'{new_directory}/venv'],
    ['git', 'init',f'{new_directory}'],
    ['code', f'{new_directory}/'],
    'clear'
    ]

project_creator = [subprocess.run(command) for command in commands]