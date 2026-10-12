# 网关诊断面:overcast API 网关

> overcast 部分实测定稿中:models 与推理面已实测(2026-10-12,见回填位),无鉴权 health 探针仍未知名,回填位保留;别家网关路径仅作参照,不写在 overcast 名下。判据来源:研究档 cfg-02(2026-10-12,官方文档加三网关源码对照)加 hst 手册面加总台实战实证(2026-10-12);`hst diagnose` 是活性层活权威(打真网关烧最小 token,与 doctor 的零网络体检分家)。

## 现状两形

- **settings 钉组形**:env 钉 `ANTHROPIC_BASE_URL` + 凭证(`ANTHROPIC_AUTH_TOKEN` 走 Bearer 或 `ANTHROPIC_API_KEY` 走 x-api-key 或 apiKeyHelper)加三档 `ANTHROPIC_DEFAULT_OPUS/SONNET/HAIKU_MODEL`(另有第四档 FABLE 与 `ANTHROPIC_MODEL`)
- **环境注入形**:settings 零 ANTHROPIC_*,接入走会话环境

> 部署面 [实证: 2026-10-12]:钉组形已部署 lan-mac(发起端)、win 面、local-wsl 面(总台镜像到 wsl);环境注入形仍为其余接入的合法形态

## 官方拼接规范

- base 是**源站,不含 `/v1`、无尾斜杠**:Claude Code 自己接 `/v1/messages`(推理)、`/v1/messages/count_tokens`、`GET /v1/models?limit=1000`(发现,缺省超时 3 秒,重定向当失败);base 以 `/v1` 结尾会拼出 `/v1/v1/messages`(config-lint error)
- 头种:Bearer 用 `ANTHROPIC_AUTH_TOKEN`,x-api-key 用 `ANTHROPIC_API_KEY`,apiKeyHelper 两头都送;`anthropic-beta` 与 `anthropic-version` 须原样转发
- 只设 base 不设网关凭证 = 订阅穿网关模式(文档形态,advisory)
- **模型名 `[1m]` 后缀剥离** [用户口径加实证: 2026-10-12]:Claude Code 客户端发网关前剥离模型名 `[1m]` 后缀(1M 上下文标记),网关 models 列表只有剥离形;raw curl 带 `[1m]` 直打回 400 unknown provider **不代表配置错**(实证:zp-cc-glm53[1m] 直打 400,剥离形 zp-cc-glm53 打 200);手测验证一律用剥离形
- 官方验证请求(回包 `{"id":"msg_` 开头即通;401 换头种再试):

```bash
curl -sS -w '\n%{http_code}\n' -X POST "$ANTHROPIC_BASE_URL/v1/messages" \
  -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
  -H "anthropic-version: 2023-06-01" -H "content-type: application/json" \
  -d '{"model": "<模型id>", "max_tokens": 1, "messages": [{"role": "user", "content": "."}]}'
```

## 诊断三层

层序固定:配置对齐(零网络)到连通性(可达与鉴权,正文控制在 max_tokens 1 或一次 models)到活性(最小真实补全,烧 token);上层已判定的不放到下层再烧一次。`hst doctor` 不入三层(findings 全是宿主面,判例 2026-10-12 实测);`hst diagnose agents`(配置指向、别名在册核对、key 活性)横跨配置对齐与活性两层,活跑 schema 待证,允许活跑时指向错误为 error。

### 配置对齐层

| 判据 | 档 |
| --- | --- |
| 意图走网关而 BASE_URL 缺失或为空 | error |
| base 以 `/v1` 结尾(config-lint 已查) | error |
| base 仅有尾斜杠 | advisory |
| 只设 base 无任一凭证(订阅穿网关) | advisory |
| 三档 pin 与 ANTHROPIC_MODEL 全空且未对照过 models | advisory;网关名与缺省不一致仍不钉 | error |
| 项目 `.claude/settings.json` env 含凭证变量(error,`${VAR}` 引用形放行;config-lint 已查)或 CUSTOM_HEADERS 带 Authorization 与 x-api-key(人工判据,config-lint 未实现) | error;用户面同形 | advisory |

### 连通性层

| 判据 | 档 |
| --- | --- |
| TCP/TLS 失败、拒连、证书错(证书对照 connect 页 `NODE_EXTRA_CA_CERTS`) | error |
| 进程探针非 200(探针位见下表,无鉴权) | error |
| 期望 JSON 的路径回 text/html 且 200(one-api 控制台回退形) | error |
| 官方验证 POST 回 401(换头种再判)或 one-api 形 403 令牌无权该模型 | error |
| `/v1/v1/messages` 形 404(配置层漏网时) | error |
| 发现超时或被重定向(慢网关设 `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS`) | advisory(选择器回退缓存) |
| `/fast` 网络错而推理正常(该检查直打 api.anthropic.com) | advisory,不当网关宕机 |

### 活性层

| 判据 | 档 |
| --- | --- |
| 钉住的模型 id 不在网关权威 models 列表,或补全回不存在(**先剥 `[1m]` 后缀再比对**,带后缀形不在列表不是漂移) | error |
| LiteLLM `GET /health`(Bearer 真请求)unhealthy_endpoints 出现某模型而 liveliness 仍 200 | 该模型 error,进程算过 |
| `hst diagnose cache`(缺省测 `/v1/models` 全量别名,探测错误退 1) | 退出码 1 即 error |
| 列表多出客户端不用的 id;目录短暂缺条目而补全仍成功 | advisory |

## 端点惯例对照

overcast 定稿前的参照:

| 网关 | 进程探针(无鉴权) | models | 推理 | 鉴权 |
| --- | --- | --- | --- | --- |
| LiteLLM | `GET /health/liveliness`(200 `I'm alive!`);`GET /health/readiness`(db connected) | `GET /v1/models` | `POST /v1/messages`(另有 `/anthropic` 透传) | Bearer(`GET /health` 本身要鉴权且打真请求,归活性层) |
| new-api | `GET /api/status` | `GET /v1/models` | `POST /v1/messages` | Bearer |
| one-api | `GET /api/status` | `GET /v1/models` | 无 `/v1/messages`(relay 表只有 chat/completions) | Authorization,令牌可带 `-渠道id` 后缀钉渠道 |

## agent 侧四类错形

1. 键组不齐:base 配了凭证缺或头种不对(401)
2. token 失效:401 或 one-api 形 403(令牌无权该模型)
3. 模型映射漂移:发现列表与钉住别名不一致(剥 `[1m]` 后比对,见拼接规范节);新模型名未路由回 404;内建 id 须在网关 model_list 有同名
4. base 尾斜杠与路径拼接:`/v1` 双拼、SDK 侧二次拼后缀(LiteLLM SDK 未关 `LITELLM_ANTHROPIC_DISABLE_URL_SUFFIX` 时)、one-api 非 `/v1` 非 `/api` 路径回 HTML 200

## 修法

- base 修成源站形(无 `/v1` 无尾斜杠);头种与网关说明对齐
- 401/403:先轮换 token 再清史,禁扩豁免消红
- 漂移:对照 `GET /v1/models` 对齐三档 pin;部分后台子调用无视覆盖,覆盖名与内建 id 要同时路由

## 回填位

- [x] overcast models 端点 [实证: 2026-10-12]:`GET /v1/models?limit=1000`,Bearer,200 JSON 六模型
- [x] overcast 推理端点 [实证: 2026-10-12]:`POST /v1/messages`(anthropic 形,Bearer;别名 zp-cc-glm53 路由,回包 model=glm-5.3)
- [ ] overcast 无鉴权 health 探针(未知名,实装后填)
- [ ] hst diagnose 与 overcast 的配套参数
- [ ] 四端网关配置对齐基线(钉组形标准键组)

## 命名族注记

- `zp-cc-*` = Claude Code 专用别名族 [用户口径: 2026-10-12]
- `zp-cx-*` 族归属待证:models 列表 owned_by 标 glm 与 xai,勿写死 [待证]

权威:llm-gateway-connect 与 llm-gateway-protocol 与 llm-gateway-rollout 与 model-config(code.claude.com/docs);LiteLLM docs/proxy/health 与 client_setup/claude_code;new-api 与 one-api 仓 router 源码。
