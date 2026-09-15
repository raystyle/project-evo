# project-evo 命令行为验证用例集（（1） 工具/命令行为评估）

> project-evo 是文档即代码体系插件(核心 skill 为 dev-evo)；机检形态为 skill 内 `scripts/check.py`（PEP 723 零依赖，`uv run check.py <项目>` 直跑，退出码 0/1/2），本文件是其等价 PowerShell 用例集，验证一个项目是否遵守 project-evo 骨架。
> 用例均参数化 `$ProjectRoot`（默认指向本仓库自身，也能指向任意目标项目复用）。
> 每条可直接复制复验。

---

## 一、骨架结构验证

```powershell
# 前置:设定目标项目根(须为采用 project-evo 骨架的项目)
$ProjectRoot = "D:\目标项目"
Set-Location $ProjectRoot

# [PE-01] AGENTS 五节合同齐备(Commands/Must/Must not/Read first 四硬节 + 环境软节)
"## Commands","## Must not","## Read first","## 环境" | Where-Object { -not (Select-String -Path AGENTS.md -Pattern ([regex]::Escape($_)) -Quiet) }
# 预期: 空结果(注: "## Must" 用 Must not 反查,另单独跑下行)
Select-String -Path AGENTS.md -Pattern "^## Must$" -Quiet
# 预期: True

# [PE-02] docs/adr 目录与 README 索引在位
(Test-Path "docs\adr") -and (Test-Path "docs\adr\README.md")
# 预期: True

# [PE-03] docs/requirements 目录与 README 索引在位
(Test-Path "docs\requirements") -and (Test-Path "docs\requirements\README.md")
# 预期: True

# [PE-04] CLAUDE.md 一行桥接(存在才查)
if (Test-Path CLAUDE.md) { (Get-Content CLAUDE.md | Where-Object { $_.Trim() }).Count }
# 预期: 1(仅 @AGENTS.md)
```

## 二、ADR/REQ 状态机与索引验证

```powershell
# [PE-05] 文件名规范(docs 下无空格/括号/冒号;README 豁免)
Get-ChildItem docs -Recurse -File -Filter *.md | Where-Object { $_.Name -match '[()\s:]' -and $_.Name -ne "README.md" } | Select-Object Name
# 预期: 空结果

# [PE-06] ADR 命名与状态机(ADR-NNNN 前缀;status 合法;superseded_by 可达)
$adrs = Get-ChildItem docs\adr -File -Filter *.md | Where-Object { $_.Name -ne "README.md" -and $_.Name -notlike "0000-template*" }
$ids = $adrs | ForEach-Object { (Select-String -Path $_.FullName -Pattern '^id: (.+)$').Matches.Groups[1].Value.Trim() }
$adrs | ForEach-Object {
    $head = (Get-Content $_.FullName -Raw) -split "`n---", 3 | Select-Object -First 1
    if ($_.BaseName -notmatch '^ADR-\d{4}') { "$($_.Name): 命名非 ADR-NNNN" }
    $status = ([regex]::Match($head, 'status:\s*(\S+)')).Groups[1].Value
    if ($status -notin @("proposed","accepted","superseded")) { "$($_.Name): status 非法 $status" }
    if ($status -eq "superseded") {
        $sup = ([regex]::Match($head, 'superseded_by:\s*(\S+)')).Groups[1].Value
        if ($sup -in @("","null") -or $ids -notcontains $sup) { "$($_.Name): superseded_by 悬空 $sup" }
    }
}
# 预期: 空结果(adr 目录为空则本组跳过)

# [PE-07] REQ 命名与状态机(implemented 须带 trace)
$reqs = Get-ChildItem docs\requirements -File -Filter *.md | Where-Object { $_.Name -ne "README.md" -and $_.Name -notlike "0000-template*" }
$reqs | ForEach-Object {
    $head = (Get-Content $_.FullName -Raw) -split "`n---", 3 | Select-Object -First 1
    if ($_.BaseName -notmatch '^REQ-\d{3}') { "$($_.Name): 命名非 REQ-NNN" }
    $status = ([regex]::Match($head, 'status:\s*(\S+)')).Groups[1].Value
    if ($status -notin @("draft","implemented","rejected")) { "$($_.Name): status 非法 $status" }
    if ($status -eq "implemented") {
        $trace = ([regex]::Match($head, 'trace:\s*(\S+)')).Groups[1].Value
        if ($trace -in @("","null")) { "$($_.Name): implemented 缺 trace" }
    }
}
# 预期: 空结果(requirements 目录为空则本组跳过)

# [PE-08] ADR/REQ 索引一致(每个文件 id 登记进各自 README)
$adrIdx = Get-Content docs\adr\README.md -Raw; $reqIdx = Get-Content docs\requirements\README.md -Raw
$adrs | Where-Object { -not $adrIdx.Contains(((Select-String -Path $_.FullName -Pattern '^id: (.+)$').Matches.Groups[1].Value.Trim())) } | Select-Object Name
$reqs | Where-Object { -not $reqIdx.Contains(((Select-String -Path $_.FullName -Pattern '^id: (.+)$').Matches.Groups[1].Value.Trim())) } | Select-Object Name
# 预期: 空结果
```

## 三、内容规范验证

```powershell
# [PE-09] 六态标记在研究文档中出现(有此类文档时)
rg -l "\[实证:|\[推断:|\[经验:|\[假设:" docs\research
# 预期: 非空(research 至少一篇带标记;目录空则跳过)
# 注记: 中转态是否带验证路径、收尾是否处置悬空条目,属语义判断,机检不做,收尾手检(见 base-writing-standards.md 六态红线)

# [PE-10] 标题禁括号(正文 markdown 标题行)
rg -n "^#+ .*[()]" docs AGENTS.md README.md
# 预期: 空结果(围栏代码块内 # 注释不算)

# [PE-11] 四类禁字(emoji/破折号/箭头/智能引号;豁免区感知)
rg -n "[\x{2600}-\x{27BF}\x{1F000}-\x{1FAFF}\x{2705}\x{26A0}\x{2014}\x{2013}\x{2190}-\x{21FF}\x{201C}\x{201D}]" AGENTS.md README.md CHANGELOG.md docs -g "*.md"
# 预期: 空结果(规则唯一权威是 scripts/mdrules.py,此处粗检)

# [PE-12] AGENTS 与 docs 各 README 提到的本仓文件真实存在(反引号路径粗检)
$idxFiles = @("AGENTS.md") + (Get-ChildItem docs -Directory | ForEach-Object { Join-Path $_.FullName "README.md" } | Where-Object { Test-Path $_ })
$misses = $idxFiles | ForEach-Object { Select-String -Path $_ -Pattern '`([\w\-\\/\.]+\.(?:md|py|rs|toml|ts))`' -AllMatches } | ForEach-Object { $_.Matches } | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique | Where-Object { -not (Test-Path $_) }
$misses
# 预期: 空结果(有扫描脚本则优先用脚本)
```

---

## 复验前提

- **pwsh 7 跨平台**（Windows/Linux/macOS 均可装）；rg（ripgrep）在 PATH。本用例集以 pwsh 书写，三平台同跑；纯 bash 环境按语义转写（`Test-Path`到`test -f`，数组遍历到`for`，rg 用法不变）
- 用例对「最小集」项目：PE-06/PE-07/PE-09 在对应目录为空时跳过不算失败
- 目标项目若裁剪（如 research/guides 缓建）：相应检查豁免，须在项目 AGENTS 注明裁剪决定
- 平台差异（路径分隔符、大小写敏感文件系统）以目标项目 AGENTS 环境节声明的路径写法为准（见 env-platform.md 三节）
