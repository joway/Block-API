CodeVS Auth API
===

## API

### Basic Auth /auth

- login
- register
- activate
- change password
- forget password

### User Profile

- update profile
- list profile

### Social Auth : /social

- / : 当前用户下的所有社交帐户及其信息
- /binging : 登陆状态下传code绑定社交化帐号
- /login : 前端跳转到认证页得到code，使用code登陆帐户。
	- 后台根据code解析用户信息, 判断是否绑定了帐号:
		- 若绑定了, 则直接登陆换取jwt token并返回
		- 若未绑定, 重定向到注册/登陆界面, 用户注册/登陆后再调用绑定API进行绑定(前端需要一直保存着之前的code)
- /redirect: 查询对应provider 的跳转认证url 。(前端也可以直接写死跳转, 不需要调用该API)


PS: 以上API为Restful API 提供，如果是在Django原生的模板下时, 可以使用如下三个API，可以直接从callback上获取code，不需要前端发送过来。



### Oauth

- authorize
- access_token
- refresh_token
- user

PS : django-oauth-toolkit 暂时不支持jwt方式

提供两种 grant_type 形式的认证:
- authorization_code
- jwt_bearer

相关论文: https://tools.ietf.org/html/draft-ietf-oauth-jwt-bearer-12

## Social Auth 流程:

#### 第三方帐户未绑定状态下使用 Social Auth 登陆:

- 跳转到 .../auth/callback/xxx/?code=xxx&&state=xxx 下, 等待用户选择是否绑定一个帐号或注册一个新帐号
- 若绑定帐号则跳转到 .../auth/social/bind , 并输入帐号密码以绑定帐号
- 若注册新帐号, 则 .../auth/social/register, 注册新帐号并绑定之前的social auth 帐号
