# 利用規約解析APIサーバー

## API
- post /analysis/url
	- send
		- string: target url
	- response
		- { msgs: string }

- post /analysis/text
	- send
		- string: term text
	- response
		- { msgs: string }
