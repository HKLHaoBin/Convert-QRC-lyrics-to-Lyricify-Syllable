import re
from github import Github
import os

def process_line_fixed(line):
    # 替换首个 [xxxx,yyyy] 为 [0] 或 [6]
    pattern = r'\[\d+,\d+\]'
    match = re.search(pattern, line)
    if match:
        if '((' in line:
            line = re.sub(pattern, '[6]', line, count=1)
            # 如果存在 '(('，删除首个 (数字,数字) 时间戳
            time_pattern = r'\(\d+,\d+\)'
            time_match = re.search(time_pattern, line)
            if time_match:
                line = line[:time_match.start()] + line[time_match.end():]
        else:
            line = re.sub(pattern, '[0]', line, count=1)

    # 将 '((' 替换为 '('，并将 ')( ' 替换为 '('
    line = line.replace('((', '(').replace(')(', '(')

    # 删除多余的孤立括号
    line = re.sub(r'\(\s*\)', '', line)  # 移除空括号
    
    # 确保首尾没有多余的单独括号
    while line.startswith('(') and line.count('(') > line.count(')'):
        line = line[1:]
    while line.endswith(')') and line.count(')') > line.count('('):
        line = line[:-1]

    return line.strip()

def process_lyrics(input_text):
    lines = input_text.strip().split('\n')
    processed_lines = [process_line_fixed(line) for line in lines]
    result = '\n'.join(processed_lines)

    # 检查并修正行中是否存在 “](”，若存在则改为“]”
    result = result.replace('](', ']')

    # 检查并修正行中是否存在两个空格，若存在则改为一个空格
    result = re.sub(r'  +', ' ', result)

    return result

def main():
    # 从环境变量中获取 GitHub 相关信息
    token = os.getenv('GITHUB_TOKEN')
    issue_number = int(os.getenv('ISSUE_NUMBER'))
    repository_name = os.getenv('GITHUB_REPOSITORY')

    g = Github(token)
    repo = g.get_repo(repository_name)
    issue = repo.get_issue(number=issue_number)

    # 获取 Issue 内容
    input_text = issue.body or ""

    # 处理歌词
    processed_text = process_lyrics(input_text)

    # 添加评论
    issue.create_comment(f"Processed Lyrics:\n\n```\n{processed_text}\n```")

if __name__ == "__main__":
    main()
