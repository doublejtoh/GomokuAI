import tensorflow as tf
import numpy as np
import dqn
import RuleBasedAi
import game
import random
from collections import deque

input_size = 19 * 19
output_size = 19 * 19
board = np.zeros([19, 19])
turn = 1 # DQN 차례 turn이 2이면 rulebased 차

dis = 0.9
REPLAY_MEMORY = 50000

def replay_train(mainDQN, targetDQN, train_batch):
    x_stack = np.empty(0).reshape(0, mainDQN.input_size)
    y_stack = np.empty(0).reshape(0, mainDQN.output_size)
    for state, action, reward, next_state, done in train_batch:
        Q = mainDQN.predict(state)
        if done:
            Q[0, action] = reward

        else:
            Q[0, action] = reward + dis * np.max(targetDQN.predict(next_state))

        y_stack = np.vstack([y_stack, Q])
        x_stack = np.vstack([x_stack, state])
    return mainDQN.update(x_stack, y_stack)

def get_copy_var_ops(*, dest_scope_name="target", src_scope_name="main"):
    op_holder = []
    src_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=src_scope_name)
    dest_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=dest_scope_name)

    for src_var, dest_var in zip(src_vars, dest_vars):
        op_holder.append(dest_var.assign(src_var.value()))
    return op_holder

def get_random_action_pos(board):
    zeros = np.where(board == 0)
    rand = np.random.randint(len(zeros[0]))
    return (zeros[0][rand], zeros[1][rand])

def get_reward_done(turn):
    if turn == 3: # DQN 승리
        print("DQN 승리")
        return (50, True)
    elif turn == 4: # RULE BASED AI 승리
        print("RULE AI 승리")
        return (-50, True)
    else:
        return (0, False)
def main():
    global turn
    max_episodes = 5000
    replay_buffer = deque()

    with tf.Session() as sess:
        mainDQN = dqn.DQN(sess, input_size, output_size, name='main')
        targetDQN = dqn.DQN(sess, input_size, output_size, name='target')
        tf.global_variables_initializer().run()

        copy_ops = get_copy_var_ops(dest_scope_name="target", src_scope_name="name")
        sess.run(copy_ops)

        for episode in range(max_episodes):
            turn = 1
            e = 1. / ((episode / 10) + 1)
            done = False
            step_count = 0
            board = np.zeros([19, 19])
            while not done:
                state = np.reshape(board, [1, 19 * 19])
                if turn == 1: # DQN 차례
                    if np.random.rand(1) < e:
                        action_xpos, action_ypos = get_random_action_pos(board)
                        board[action_xpos][action_ypos] = 1
                    else:
                        max_q_reshaped = np.reshape(mainDQN.predict(board), [19, 19])
                        max_q_action_xpos, max_q_action_ypos = np.unravel_index(np.argmax(max_q_reshaped, axis=None),
                                                                                max_q_reshaped.shape)
                        if (board[max_q_action_xpos][max_q_action_ypos] != 0): # 만약 max q 2차원 좌표에 이미 돌이 있다면,
                            max_q_action_xpos, max_q_action_ypos = get_random_action_pos(board) # 랜덤 액션.
                        board[max_q_action_xpos][max_q_action_ypos] = 1
                elif turn == 2: # RULE BASED 차례
                    RuleBasedAi.rulebased(board, turn)
                turn = game.finishcheck(board, turn)
                next_state = np.reshape(board, [1, 19 * 19])
                reward, done = get_reward_done(turn)
                replay_buffer.append((state, action_xpos * 19 + action_ypos, reward, next_state, done))
                if len(replay_buffer) > REPLAY_MEMORY:
                    replay_buffer.popleft()
                step_count += 1
                if turn == 1:
                    turn = 2
                elif turn == 2:
                    turn = 1
            print("Episode: {} steps: {}".format(episode, step_count))

            if episode % 10 == 1:
                for _ in range(50):
                    minibatch = random.sample(replay_buffer, 10)
                    loss, _ = replay_train(mainDQN, targetDQN, minibatch)
                print("loss: ", loss)
                sess.run(copy_ops)

if __name__ == "__main__":
    main()