# 项目介绍和使用说明书

## 项目名称
**Convert QRC lyrics to Lyricify Syllable.**

## 项目简介
Convert QRC lyrics to Lyricify Syllable. 是一个工具，用于从 GitHub Issue 中获取歌词内容，自动修正和格式化文本中的括号、时间戳以及其他潜在问题，然后将处理后的结果以评论的形式附加到该 Issue 中。该工具通过 Python 实现，依赖于 GitHub API 和正则表达式技术，能够高效、智能地完成歌词内容的清理工作。

# [点击这里使用本工具](https://github.com/HKLHaoBin/Convert-QRC-lyrics-to-Lyricify-Syllable/issues/new/choose)
---

## 功能特点
1. **文本修正**：
   - 替换 `[xxxx,yyyy]` 格式为 `[0]` 或 `[6]`。
   - 删除包含时间戳的 `(数字,数字)`。
   - 修正括号格式，如将 `((` 替换为 `(`，删除空括号 `()`。
   - 修正行中多余的空格和无意义的字符。
   - 确保每行括号数量匹配。

2. **GitHub 集成**：
   - 从指定 GitHub Issue 中提取内容。
   - 将修正后的结果以评论形式提交到相应的 Issue 中。

---

## 使用说明

脚本会自动从指定的 GitHub Issue 中读取内容，处理后将结果作为评论添加到 Issue 中。

---

## 示例
假设 Issue 内容为：
```
[1234,5678](( (word1)(word2)
```

脚本处理后会生成以下结果并作为评论提交：
```
Processed Lyrics:
[0](word1(word2)
```

## 注意事项
 输入文本格式应与工具的处理逻辑相匹配，以确保修正效果最佳。

## 许可证
此项目使用 MIT 许可证。
