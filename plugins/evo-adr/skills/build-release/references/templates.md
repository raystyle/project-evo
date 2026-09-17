# 模板:可直接拷改的参数化空壳

> 家规形态的参数化空壳,占位符一律尖括号形;拷进目标仓按型号拼装。仓名零出现。

## 一、通用 workflow 骨架

```yaml
name: pack-release-r2
on:
  push:
    branches: [main]
    tags: ["v*"]
  pull_request:
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: pack-${{ github.ref }}
  cancel-in-progress: true

jobs:
  detect:
    runs-on: ubuntu-latest
    outputs:
      has_go: ${{ steps.f.outputs.has_go }}
      has_rust: ${{ steps.f.outputs.has_rust }}
      has_npm: ${{ steps.f.outputs.has_npm }}
      has_py: ${{ steps.f.outputs.has_py }}
    steps:
      - uses: actions/checkout@v4
      - id: f
        shell: bash
        run: |
          set -euo pipefail
          for k in go:go.mod rust:Cargo.toml npm:package.json py:pyproject.toml; do
            var="${k%%:*}"; f="${k#*:}"
            echo "has_${var}=$([ -f "$f" ] && echo true || echo false)" >> "$GITHUB_OUTPUT"
          done

  build:
    needs: detect
    if: needs.detect.outputs.has_<型> == 'true'
    runs-on: <按型>
    steps:
      - uses: actions/checkout@v4
      # 按型拼第二节片段;测试闸必须在打包前
      - run: <测试命令>
      - run: <构建与打包到 out/>
      - run: cd out && sha256sum ./* > SHA256SUMS && for f in ./*; do sha256sum "$f" > "$f.sha256"; done
      - uses: actions/upload-artifact@v4
        with:
          name: <型>-assets
          path: out/
          if-no-files-found: error

  publish:
    needs: [detect, build]
    if: |
      always() &&
      github.event_name != 'pull_request' &&
      needs.build.result == 'success'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with: { path: collected }
      - run: mkdir -p release-files && find collected -type f ! -name '*.zip' -exec cp -t release-files {} +
      - name: gh release 直发(仅 tag)
        if: startsWith(github.ref, 'refs/tags/')
        run: gh release create "$GITHUB_REF_NAME" release-files/* --latest --title "<tool> $GITHUB_REF_NAME"
        env: { GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}" }
      - name: rclone 双段播种(仅 tag)
        if: startsWith(github.ref, 'refs/tags/')
        env:
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          R2_ENDPOINT: ${{ secrets.R2_ENDPOINT }}
          R2_BUCKET: ${{ secrets.R2_BUCKET }}
        run: |
          set -euo pipefail
          <拼第三节镜像步模板:版本段加 stable 滚动段>
      - name: 零上传红灯
        if: startsWith(github.ref, 'refs/tags/')
        env:
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          R2_ENDPOINT: ${{ secrets.R2_ENDPOINT }}
          R2_BUCKET: ${{ secrets.R2_BUCKET }}
        run: |
          set -euo pipefail
          n=$(rclone lsf :s3:$R2_BUCKET/<tool>/${GITHUB_REF_NAME#v}/ --s3-endpoint $R2_ENDPOINT \
            --s3-access-key-id $R2_ACCESS_KEY_ID --s3-secret-access-key $R2_SECRET_ACCESS_KEY \
            --s3-no-check-bucket | wc -l)
          [ "$n" -gt 0 ] || { echo "::error::镜像版本段零对象"; exit 1; }
          echo "mirror objects: $n"
  # dispatch 补推口:publish 挂 workflow_dispatch 加 needs 链 always(),已含上方 if 形
```

## 二、各型构建片段

go 形:

```bash
BIN=<bin>; mkdir -p out
for t in linux/amd64 linux/arm64 darwin/amd64 darwin/arm64 windows/amd64 windows/arm64; do
  os="${t%/*}"; arch="${t#*/}"; ext=""; [ "$os" = windows ] && ext=".exe"
  CGO_ENABLED=0 GOOS="$os" GOARCH="$arch" go build -trimpath -ldflags="-s -w" \
    -o "out/${BIN}-${os}-${arch}${ext}" ${MAIN_PATH:-.}
done
```

rust 形(matrix.target 五目标):

```bash
cargo test --release --locked --target ${{ matrix.target }}
cargo build --release --locked --target ${{ matrix.target }}
cp "target/${{ matrix.target }}/release/${BIN}${EXT}" "out/${BIN}-${{ matrix.target }}${EXT}"
```

npm 形:

```bash
[ -f package-lock.json ] && npm ci || npm install
npm test --if-present && npm run build --if-present
mkdir -p out && npm pack --pack-destination out
```

py 形:

```bash
python -m pip install --upgrade pip build
python -m build && mkdir -p out && cp dist/* out/
```

native 形(自含静态):

```bash
# 容器内自含构建,树内依赖闭包;跨宿主闸必配:
<configure 与 make 自含形>
ldd out/<bin> 2>/dev/null 1>&2; [ $? -ne 0 ] || file out/<bin> | grep -q 'dynamically linked' && { echo "::error::非静态"; exit 1; }
docker run --rm -v "$PWD/out:/x" <异版本宿主镜像> /x/<bin> --version
```

manifest 形(纯文档/插件仓):无 build job;publish 换为清单一致性测试与市场快照刷新,不推镜像。

## 三、rclone 镜像步模板

```bash
set -euo pipefail
VER="${GITHUB_REF_NAME#v}"
COMMON=(--s3-endpoint "$R2_ENDPOINT" --s3-access-key-id "$R2_ACCESS_KEY_ID" \
  --s3-secret-access-key "$R2_SECRET_ACCESS_KEY" --s3-no-check-bucket)
# 版本段:immutable 长缓存头
rclone copy release-files/ ":s3:$R2_BUCKET/<tool>/$VER/" "${COMMON[@]}" \
  --header-upload "Cache-Control: public, max-age=31536000, immutable"
# stable 滚动段:短缓存加滚代清旧
rclone sync release-files/ ":s3:$R2_BUCKET/<tool>/stable/" "${COMMON[@]}" \
  --header-upload "Cache-Control: public, max-age=60" --delete-excluded
```

## 四、自升级契约核对清单

- [ ] self update 双通道:自家 stable 段优先,GitHub release 404 自动回落
- [ ] digest 判新:升级器与发布器同 digest 判据,逐件对 `.sha256` 边车锚校验
- [ ] dev 加 stable 双通道是否开放:随仓裁,写进仓内 AGENTS
- [ ] 元数据回写:升级后回写安装管理器的工具级状态,或管理器以实值探活判,无旧版残留
- [ ] 验收判据:同工具 self update 与管理器 update 同报已最新;各端终态同 digest
- [ ] 无自升级面(fork/静态资产):归安装管理方单通道,版本 pin 滚即升,终态同 digest
