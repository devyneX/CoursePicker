from collections import defaultdict
import pandas as pd


def make_ds(data):
    follow_up = defaultdict(list)
    prereq_count = defaultdict(int)
    start = []

    for i, row in data.iterrows():
        follow_up[i] = []
        prereq_count[i] = 0

    for i, row in data.iterrows():
        for col in data.loc[i]:
            if col == '':
                continue
            follow_up[col].append(i)
            prereq_count[i] += 1
        if prereq_count[i] == 0:
            start.append(i)

    return follow_up, prereq_count, start


def reset_completed(data):
    for i, row in data.iterrows():
        data.loc[i, 'FINISHED'] = False


def dfs_util(graph, course, completed, pre_requisite_count, pre_requisite_completed, unlocked):
    for follow_up in graph[course]:
        if not completed.loc[follow_up, 'Finished']:
            pre_requisite_completed[follow_up] += 1
            if pre_requisite_completed[follow_up] == pre_requisite_count[follow_up]:
                unlocked.append(follow_up)
            continue
        dfs_util(graph, follow_up, completed, pre_requisite_count,
                 pre_requisite_completed, unlocked)


def dfs(graph, start, completed, pre_requisite_count):
    pre_requisite_completed = defaultdict(int)
    unlocked = []
    for course in start:
        if not completed.loc[course, 'Finished']:
            unlocked.append(course)
            continue
        dfs_util(graph, course, completed, pre_requisite_count,
                 pre_requisite_completed, unlocked)

    unlocked.sort()

    return unlocked


def get_unlocked_course(data, completed):
    course_structure, pre_requisite_count, starting_course = make_ds(data)

    unlocked_courses = dfs(course_structure, starting_course,
                           completed, pre_requisite_count)

    return unlocked_courses
