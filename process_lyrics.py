import re

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

# 示例输入文本
input_text = """
"""

# 将输入文本按行分割
lines = input_text.strip().split('\n')

# 使用修正逻辑处理每一行
processed_lines_fixed = [process_line_fixed(line) for line in lines]

# 将处理后的行合并为单个字符串
result_fixed = '\n'.join(processed_lines_fixed)

# 检查并修正行中是否存在 “](”，若存在则改为“]”
result_fixed = result_fixed.replace('](', ']')

# 检查并修正行中是否存在两个空格，若存在则改为一个空格
result_fixed = re.sub(r'  +', ' ', result_fixed)

print(result_fixed)
