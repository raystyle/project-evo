# 模板:可直接拷改的参数化空壳

> 形态取自家族仓实测实践(git 历史在档),参数化去私有名;占位符一律尖括号形。标准三段式:**本地编译**(主开发机交叉加实机矩阵)到 **GitHub 产物发布**(gh release 直发)到 **CI/CD Action 自动播种 R2**。

## 一、本地编译与发布(命令面,主开发机)

```bash
set -euo pipefail
TAG="v<版本>"; VER="<版本>"
# 1 版本一致性闸:tag 对载体 manifest(不一致即止)
<载体版本读取命令,如 grep -m1 '^version = ' Cargo.toml>
# 2 测试闸先行
<测试命令,如 cargo test --locked>
# 3 本地交叉编译(linux 本职加 win-gnu 交叉;mac 形在 mac 实机跑同款命令)
<构建命令,见第二节各型片段>
# 4 打包:单顶层目录 = 二进制加 README 加 LICENSE;win 形 zip 他形 tar.gz,逐包边车
for triple in <目标列表>; do
  d="<tool>-${TAG}-${triple}"; mkdir -p "dist/$d"
  cp "<产物路径 ${triple}>" "dist/$d/"; cp README.md LICENSE* "dist/$d/"
  if [ "<win 形判定 ${triple}>" = yes ]; then (cd dist && zip -q -r "$d.zip" "$d" && sha256sum "$d.zip" > "$d.zip.sha256")
  else (cd dist && tar czf "$d.tar.gz" "$d" && sha256sum "$d.tar.gz" > "$d.tar.gz.sha256"); fi
done
# 5 解包冒烟:每包解出跑 --version 对 VER(交叉件在目标实机跑)
<解包冒烟命令>
# 6 GitHub 产物发布:gh 直发钉 latest,禁 draft(dist 全量上,npm 形 *.tgz、py 形 wheel 与 sdist 同链)
gh release create "$TAG" dist/* --latest \
  --title "<tool> $TAG" --notes "<正式版说明,含发现通道一句>"
```

dev 滚动版(随仓裁):`gh release upload dev <资产> --clobber` 挂 prerelease(首次 `gh release create dev --prerelease --target main`)。

## 二、各型本地编译片段

rust 形(本地交叉,三目标实证形):

```bash
# linux 本职
cargo build --release --locked --target x86_64-unknown-linux-gnu
# win-gnu 交叉(ubuntu/debian 装 mingw-w64;CRT 静态零 DLL)
rustup target add x86_64-pc-windows-gnu
cargo build --release --locked --target x86_64-pc-windows-gnu
# mac arm64:在 mac 实机跑 cargo build --release --locked --target aarch64-apple-darwin
# 扩岗(aarch64-linux 交叉、musl 纯静态)随仓裁
```

go 形(本地交叉六目标):

```bash
BIN=<bin>; mkdir -p dist
for t in linux/amd64 linux/arm64 darwin/amd64 darwin/arm64 windows/amd64 windows/arm64; do
  os="${t%/*}"; arch="${t#*/}"; ext=""; [ "$os" = windows ] && ext=".exe"
  CGO_ENABLED=0 GOOS="$os" GOARCH="$arch" go build -trimpath -ldflags="-s -w" \
    -o "dist/${BIN}-${os}-${arch}${ext}" ${MAIN_PATH:-.}
done
```

npm 形:

```bash
[ -f package-lock.json ] && npm ci || npm install
npm test --if-present && npm run build --if-present
mkdir -p dist && npm pack --pack-destination dist
```

py 形:

```bash
python -m pip install --upgrade pip build && python -m build
mkdir -p dist && cp <wheel 与 sdist> dist/
```

native 形(autotools/C++,自含静态):

```bash
# 自含构建,树内依赖闭包;静态断言正向两连(缺即红),跨宿主闸必配:
<configure 与 make 自含形>
file <bin> | tee file.out | grep -q "statically linked" || { echo "非静态(file)"; exit 1; }
ldd <bin> > ldd.out 2>&1 || true
grep -q "not a dynamic executable" ldd.out || { echo "非静态(ldd)"; exit 1; }
docker run --rm -v "$PWD/dist:/x" <异版本宿主镜像> /x/<bin> --version
```

manifest 形(纯文档/插件仓):无编译无播种;发布形 = 清单三处一致与市场快照刷新。

## 三、CI/CD Action 自动播种 workflow

> 发布事件触发,从 Release 下载资产 rclone 推段;编译不在 CI,CI 只播种(附测试岗随仓裁)。

```yaml
name: r2-seed
on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      tag:
        description: '补推的 v* tag(从 Release 拉资产重灌)'
        default: ''
        type: string

permissions:
  contents: read

jobs:
  seed:
    # 选装 dev 段(prerelease 滚动)时须同步放宽本 if 收 prerelease 事件
    if: ${{ !github.event.release.prerelease || inputs.tag != '' }}
    runs-on: ubuntu-latest
    env:
      # env-remote 配置形:命名 remote r2:,四键走 Secrets,NO_CHECK_BUCKET 必带(受限 token 无建桶权)
      RCLONE_CONFIG_R2_TYPE: s3
      RCLONE_CONFIG_R2_PROVIDER: Cloudflare
      RCLONE_CONFIG_R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
      RCLONE_CONFIG_R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
      RCLONE_CONFIG_R2_ENDPOINT: ${{ secrets.R2_ENDPOINT }}
      RCLONE_CONFIG_R2_NO_CHECK_BUCKET: "true"
      R2_BUCKET: ${{ secrets.R2_BUCKET }}
    steps:
      - name: 取资产
        env: { GH_TOKEN: "${{ github.token }}" }
        run: |
          TAG="${{ github.event.release.tag_name || inputs.tag }}"
          echo "TAG=$TAG" >> "$GITHUB_ENV"; echo "VER=${TAG#v}" >> "$GITHUB_ENV"
          gh release download "$TAG" --repo "$GITHUB_REPOSITORY" -D dist --clobber
      - run: command -v rclone || (curl -fsSL https://rclone.org/install.sh | sudo bash)
      - name: 灌段(版本段 immutable 加 stable 滚动)
        run: |
          set -euo pipefail
          INC=(--include "*.zip" --include "*.tar.gz" --include "*.tgz" --include "*.whl" --include "*.sha256")
          rclone copy dist/ "r2:${R2_BUCKET}/<tool>/${VER}/" "${INC[@]}" \
            --header-upload "Cache-Control: public, max-age=31536000, immutable" \
            --checksum -v --stats-one-line
          rclone sync dist/ "r2:${R2_BUCKET}/<tool>/stable/" "${INC[@]}" \
            --header-upload "Cache-Control: public, max-age=60" --delete-excluded
      - name: 零上传红灯(版本段与 stable 段分别清点报数,任一零即红;确无资产仓型用显式豁免开关)
        run: |
          set -euo pipefail
          nv=$(rclone lsf "r2:${R2_BUCKET}/<tool>/${VER}/" | wc -l)
          ns=$(rclone lsf "r2:${R2_BUCKET}/<tool>/stable/" | wc -l)
          [ "$nv" -gt 0 ] || { echo "::error::镜像版本段零对象"; exit 1; }
          [ "$ns" -gt 0 ] || { echo "::error::stable 段零对象(漏滚)"; exit 1; }
          echo "mirror objects: ver=$nv stable=$ns"
      - name: 对账回显
        run: rclone lsl "r2:${R2_BUCKET}/<tool>/${VER}/"
  # dev prerelease 滚动段(随仓裁):release.prerelease 形灌 <tool>/dev/ 段(sync delete-excluded)
  # CI 测试岗随仓裁(docs 门禁、投影门禁、测试矩阵),编译面不在 CI
```

## 四、自升级契约核对清单

- [ ] self update 双通道:自家镜像 stable 段优先,GitHub release 404 自动回落
- [ ] digest 判新:升级器与发布器同 digest 判据,逐件对 `.sha256` 边车锚校验
- [ ] dev 加 stable 双通道是否开放:随仓裁,写进仓内 AGENTS
- [ ] 元数据回写:升级后回写安装管理器的工具级状态,或管理器以实值探活判,无旧版残留
- [ ] 验收判据:同工具 self update 与管理器 update 同报已最新;各端终态同 digest
- [ ] 无自升级面(fork/静态资产):归安装管理方单通道,版本 pin 滚即升,终态同 digest
