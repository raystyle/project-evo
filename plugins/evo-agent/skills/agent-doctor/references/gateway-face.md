# 网关诊断面:overcast API 网关

> 候实装框架:overcast 网关配置在即(现状配置端 = lan-mac 工作台),本页先立诊断三层与判据位,端点路径与鉴权形态待 overcast 实装后回填定稿(沿 s5 候首版实测标注先例)。hst 的 `diagnose` 子命令是活性权威:打真网关烧最小 token,与 doctor 的零网络体检分家。

## 现状两形

两形都合法:

- **settings 钉组形**(lan-mac 工作台现形):用户 settings.json 的 env 钉 `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN` + `ANTHROPIC_DEFAULT_HAIKU/SONNET/OPUS_MODEL` 模型映射
- **环境注入形**(wsl 总台现形):settings 零 ANTHROPIC_*,接入走会话环境(vault env 注入)

诊断面覆盖两形:钉组形查配置内一致性,注入形查环境变量到位。

## 诊断三层

1. **配置对齐层**(agent-doctor config-lint 已查):
   - 钉组形键组配对:BASE_URL 配了而 AUTH_TOKEN 缺、模型映射键组不齐 -> advisory(网关键组不齐)
   - token 明文落用户面 -> advisory(提示迁 apiKeyHelper 或 vault env);落项目面 -> error
2. **连通性层**(手跑):
   ```bash
   curl -sS -o /dev/null -w '%{http_code} %{time_total}s\n' "$ANTHROPIC_BASE_URL/health"   # 端点候实装定稿
   ```
   - 判读:超时 = 网关不在或路由错;401/403 = token 失效或权限;5xx = 网关侧
3. **活性层**(hst 活权威):
   ```bash
   hst diagnose    # 打真网关烧最小 token;与 doctor 零网络体检分家
   ```

## 修法

- 键组不齐:补齐缺键或整组迁注入形,不留半组
- 401/403:轮换 token(先轮换再清史,禁扩豁免消红)再更新注入源
- 模型映射漂移:对照网关侧模型清单对齐三档映射

## 回填位

overcast 实装后定稿:

- [ ] health 端点路径与鉴权头形态
- [ ] 模型清单拉取命令
- [ ] hst diagnose 与 overcast 的配套参数(若有)
- [ ] 四端网关配置对齐基线(base_url 与 token 与模型映射的端内标准形)
