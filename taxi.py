import gym

def main():
    # load basic taxi environment
    env = gym.make("Taxi-v2")

    # initialize the environment
    env.reset()

    # total possible state
    print('{:,}'.format(env.observation_space.n))
    
    # Visualize current state
    env.render()
    

if __name__ == '__main__':
    main()
