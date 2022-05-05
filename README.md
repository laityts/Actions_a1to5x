# Actions A1TO5X
 
**如何使用a1to5x转换a1包成5x可用的刷机包**

* 登录你的github,fork这个项目到你的github

## 说明
### 1. 创建token
转到你的`repo settings > Developer settings > Personal access tokens > Generate new token` 
- `note`: 填写RELEASE
- `Expiration`: 改为No expiration
- `Select scopes`: 全部勾选
- `Generate token`: 点击创建token
- `token`: 复制得到的token令牌

### 2. 添加secrets
转到你的`repo settings > secrets > new repository secret` 
- `Name`: 填写RELEASE
- `Value`: 填写刚刚复制的token

### 3. Running workflow
- 转到你的 repo `Actions`
- 选择 `a1to5x` 工作流程(workflow)
- 打开 `Run workflow`
- 输入 ROM文件名 在 `ROM NAME` (可选)
- 输入 ROM链接地址 在 `ROM LINK` 
- 点击`Run workflow` 按钮运行工作流程
