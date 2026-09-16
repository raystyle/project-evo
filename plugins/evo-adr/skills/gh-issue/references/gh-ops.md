# gh 命令细则

> 仓解析、去重判定、发单预检、坑表与复验。命令均 2026-09-16 本仓实跑或以实证单走通。

## 一、目标仓解析序

- 解析序:cwd 的 git 仓(`git rev-parse --show-toplevel`)到 `git remote get-url origin`(无 origin 取 `git remote` 列出的首个)到 `gh repo view --json nameWithOwner,viewerPermission` 核对
- URL 两形态:HTTPS `https://github.com/<owner>/<repo>.git` 与 SSH `git@github.com:<owner>/<repo>.git`,都剥 `.git` 尾取 owner/repo;非 github.com 域即止,回执未能发
- fork 默认发 upstream(报错多在上游代码引入);确疑在 fork 自有提交引入时问用户裁定
- **禁硬编码工具名到仓映射表**:新工具、改名、搬仓都会漂移;git remote 自取加显式 `--repo` 覆盖一切场景 [实证: 本仓实测 remote 返 HTTPS 形态,gh repo view 返 nameWithOwner 与 ADMIN]
- 不在 git 仓内跑的命令报错(裸 CLI):问用户上游仓,或从工具自身输出找仓线索(`--version` 页脚、帮助文案),仍无即止回执

## 二、去重双通道与判定矩阵

- 双通道:`gh search issues "<词>" --repo <owner>/<repo> --state open`(全局索引,覆盖广但有延迟)加 `gh issue list --repo <owner>/<repo> --state all --search "<词>"`(仓内实时);发单前复跑一次仓内通道兜底索引延迟
- 搜索词纪律:报错首行错误码、异常名、工具子命令,两三个词;太宽(单用工具名)误判相关,太窄漏检
- 判定矩阵:

| 通道结果 | 判定 | 动作 |
| --- | --- | --- |
| open 且实质同(同命令同症状) | 重复 | 不发,回执附既有链接 |
| closed 且当前版本仍复现 | 旧单已关 | 发,正文相关单段附旧单链接 |
| 命中但症状不同 | 相关非重复 | 发,正文并列相关单 |
| 双通道空 | 新缺陷 | 发 |

- 「实质同」以命令与错误码为准,不以标题措辞为准

## 三、发单:label 与权限预检

- 权限:`gh repo view --json viewerPermission` 取值 ADMIN、MAINTAIN、WRITE、TRIAGE、READ;WRITE 及以上才发,不足则回执未能发并建议(提给有权限处,或走 fork 加 PR)
- label:`gh label list --repo <owner>/<repo> --json name` 预检,命中 `bug` 才 `--label bug`;未命中去 label 发。他人仓不建 label;自有仓可先 `gh label create bug --repo <owner>/<repo>` 再带
- 命令形态:`gh issue create --repo <owner>/<repo> --title "<工具名> <版本>:<症状一句话>" --body-file <正文文件>`,label 预检命中加 `--label bug`;stdout 返 issue URL
- label 不存在仍硬带:HTTP 422 整单 exit 1,一条没发出去 [实证: 2026-09-16 本仓实跑失败路径] ,预检即为此
- body 落临时文件,发完删

## 四、坑表

| 坑 | 症状 | 处理 |
| --- | --- | --- |
| label 不存在 | create 整单 exit 1(HTTP 422) | 发前 label list 预检;未命中去 label 重发 |
| private 或权限不足 | search 或 create 401/403 | gh auth status 核认证;viewerPermission 预检,不足即止回执 |
| 超长报错淹没正文 | stderr 数百行带 ANSI 色码 | 剥色码,截断保首尾各 20 行标中段(见 issue-body 截断纪律) |
| 索引延迟漏判 | search 空但仓内实有 | 双通道;发前复跑仓内 issue list 加 search |
| 交互挂起 | 无头环境缺 --title 或 --body 弹编辑器 | 两标志必显式 |
| remote URL 形态差 | SSH 或 HTTPS 解析失败 | 两形态规则剥 .git 尾;仍失败问用户要 --repo |

## 五、复验命令

```bash
gh --version
gh auth status
gh repo view <owner>/<repo> --json nameWithOwner,viewerPermission
```
