import gym

env = gym.make('MsPacman-v0')

episodes = 1000

for episode in range(1, episodes + 1):

    state = env.reset()
    done = False
    G, reward = 0, None

    while not done:
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        G += reward
        env.render()

    if episode % 100 == 0:
        print('Episode = {:,}\tRewards = {}'.format(episode, G))

print('Total rewards {} after {:,} episodes'.format(G, episodes))
