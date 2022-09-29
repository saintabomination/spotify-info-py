from dotenv import dotenv_values

ENV_PATH = '.env'

env_file = dotenv_values(ENV_PATH)
access_token = env_file['ACCESS_TOKEN']
print(access_token)

def main():
    print('Hello, World!')

if __name__ == '__main__':
    main()
