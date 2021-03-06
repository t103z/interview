# -*- encoding: utf-8 -*-

"""
JSON converted from swagger.yaml.
"""

swagger_schema = {
    "swagger": "2.0",
    "info": {
        "description": "在线面试平台API文档",
        "version": "0.0.1",
        "title": "Interview Platform API Documents"
    },
    "host": "localhost:3030",
    "basePath": "/v1",
    "tags": [
        {
            "name": "user",
            "description": "平台用户相关API"
        },
        {
            "name": "candidate",
            "description": "候选人相关API"
        },
        {
            "name": "room",
            "description": "面试房间相关API"
        },
        {
            "name": "report",
            "description": "面试报告相关API"
        },
        {
            "name": "chat",
            "description": "聊天数据相关API"
        },
        {
            "name": "problem",
            "description": "面试题相关API"
        }
    ],
    "schemes": [
        "https"
    ],
    "paths": {
        "/room": {
            "get": {
                "tags": [
                    "room"
                ],
                "summary": "获取所有面试房间",
                "parameters": [
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "符合条件的面试房间列表",
                        "schema": {
                            "$ref": "#/definitions/RoomList"
                        }
                    },
                    "400": {
                        "description": "读取错误",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "post": {
                "tags": [
                    "room"
                ],
                "summary": "添加面试房间",
                "parameters": [
                    {
                        "name": "room",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/RoomPost"
                        }
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "创建房间成功，返回房间信息",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    },
                    "400": {
                        "description": "创建房间失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/room/{room_id}/logo": {
            "put": {
                "tags": [
                    "room"
                ],
                "summary": "上传面试房间logo",
                "consumes": [
                    "image/*"
                ],
                "parameters": [
                    {
                        "name": "room_id",
                        "in": "path",
                        "description": "面试房间id",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "image",
                        "in": "body",
                        "description": "logo图片",
                        "required": True,
                        "type": "file"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "更改logo成功，返回房间信息",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    },
                    "400": {
                        "description": "更改logo失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/room/{room_id}": {
            "get": {
                "tags": [
                    "room"
                ],
                "summary": "获取面试房间信息",
                "parameters": [
                    {
                        "name": "room_id",
                        "in": "path",
                        "description": "面试房间id",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "面试房间信息",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "房间不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "put": {
                "summary": "更改房间信息",
                "description": "更改房间信息",
                "tags": [
                    "room"
                ],
                "parameters": [
                    {
                        "name": "room_id",
                        "in": "path",
                        "description": "面试房间id\n",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "room",
                        "in": "body",
                        "description": "面试房间信息\n",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/RoomPost"
                        }
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "房间信息更改成功,返回更改后的信息",
                        "schema": {
                            "$ref": "#/definitions/Room"
                        }
                    },
                    "400": {
                        "description": "房间信息更改失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "房间不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "delete": {
                "summary": "删除房间",
                "tags": [
                    "room"
                ],
                "parameters": [
                    {
                        "name": "room_id",
                        "in": "path",
                        "description": "面试房间id\n",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "删除房间成功"
                    },
                    "400": {
                        "description": "删除房间失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "房间不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/candidate": {
            "get": {
                "summary": "读取全部候选人列表",
                "description": "读取全部候选人列表\n",
                "tags": [
                    "candidate"
                ],
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "offset",
                        "in": "query",
                        "description": "从第几个候选人开始读\n",
                        "default": 0,
                        "minimum": 0,
                        "type": "integer",
                        "format": "integer"
                    },
                    {
                        "name": "limit",
                        "in": "query",
                        "description": "读取数量\n",
                        "default": 10,
                        "maximum": 100,
                        "type": "integer",
                        "format": "integer"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "responses": {
                    "200": {
                        "description": "候选人列表",
                        "schema": {
                            "$ref": "#/definitions/CandidateList"
                        }
                    },
                    "400": {
                        "description": "候选人列表获取失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "post": {
                "summary": "添加候选人",
                "tags": [
                    "candidate"
                ],
                "parameters": [
                    {
                        "name": "candidate",
                        "in": "body",
                        "description": "添加的候选人信息\n",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/PostCandidate"
                        }
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "添加候选人成功,返回候选人信息",
                        "schema": {
                            "$ref": "#/definitions/Candidate"
                        }
                    },
                    "400": {
                        "description": "添加候选人失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/candidate/{candidate_id}": {
            "get": {
                "tags": [
                    "candidate"
                ],
                "summary": "查询候选人信息",
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "候选人 id\n",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "候选人信息",
                        "schema": {
                            "$ref": "#/definitions/Candidate"
                        }
                    },
                    "400": {
                        "description": "候选人信息获取失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "候选人不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "candidate"
                ],
                "summary": "更改候选人信息",
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "候选人 id\n",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "candidate",
                        "in": "body",
                        "description": "更改后的候选人信息\n",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/Candidate"
                        }
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "候选人信息更改成功,返回更改后的信息",
                        "schema": {
                            "$ref": "#/definitions/Candidate"
                        }
                    },
                    "400": {
                        "description": "候选人信息更改失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "候选人不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "candidate"
                ],
                "summary": "删除候选人",
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "候选人 id\n",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "候选人删除成功"
                    },
                    "400": {
                        "description": "候选人删除失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "候选人不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/candidate/room/{room_id}": {
            "get": {
                "tags": [
                    "candidate"
                ],
                "summary": "获取属于某个房间的候选人列表",
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "room_id",
                        "in": "path",
                        "type": "string",
                        "description": "房间id",
                        "required": True
                    },
                    {
                        "name": "offset",
                        "in": "query",
                        "description": "从第几个候选人开始读\n",
                        "default": 0,
                        "minimum": 0,
                        "type": "integer",
                        "format": "integer"
                    },
                    {
                        "name": "limit",
                        "in": "query",
                        "description": "读取数量\n",
                        "default": 10,
                        "maximum": 100,
                        "type": "integer",
                        "format": "integer"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "responses": {
                    "200": {
                        "description": "候选人列表",
                        "schema": {
                            "$ref": "#/definitions/CandidateList"
                        }
                    },
                    "400": {
                        "description": "候选人列表获取失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/candidate/{candidate_id}/status": {
            "put": {
                "tags": [
                    "candidate"
                ],
                "summary": "改变候选人面试状态",
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "候选人 id\n",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "status",
                        "in": "query",
                        "type": "string",
                        "description": "候选人新的面试状态\n",
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "面试状态更改成功",
                        "schema": {
                            "$ref": "#/definitions/Candidate"
                        }
                    },
                    "400": {
                        "description": "候选人删除失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "候选人不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/user/register": {
            "post": {
                "tags": [
                    "user"
                ],
                "summary": "创建账户",
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Created user object",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/User"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "创建用户成功",
                        "schema": {
                            "$ref": "#/definitions/User"
                        }
                    },
                    "400": {
                        "description": "注册失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "401": {
                        "description": "存在同名用户",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/user/login": {
            "get": {
                "tags": [
                    "user"
                ],
                "summary": "用户登陆",
                "description": "",
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "username",
                        "in": "query",
                        "description": "用户名",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "password",
                        "in": "query",
                        "description": "密码",
                        "required": True,
                        "type": "string",
                        "format": "password"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "登陆成功",
                        "schema": {
                            "$ref": "#/definitions/LoginInfo"
                        },
                        "headers": {
                            "X-Rate-Limit": {
                                "type": "integer",
                                "format": "integer",
                                "description": "calls per \
                                    hour allowed by the user"
                            },
                            "X-Expires-After": {
                                "type": "string",
                                "format": "date-time",
                                "description": "date in UTC when token expires"
                            }
                        }
                    },
                    "400": {
                        "description": "无效用户名或密码",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/user/logout": {
            "get": {
                "tags": [
                    "user"
                ],
                "summary": "HR log out",
                "description": "",
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "responses": {
                    "200": {
                        "description": "退出成功"
                    },
                    "403": {
                        "description": "用户未登陆",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/user/{username}": {
            "get": {
                "tags": [
                    "user"
                ],
                "summary": "获取用户信息",
                "description": "只有HR和面试官用户可以进行本操作",
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "username",
                        "in": "path",
                        "description": "用户名",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "读取信息成功",
                        "schema": {
                            "$ref": "#/definitions/User"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "用户不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "user"
                ],
                "summary": "更改用户信息",
                "description": "只有HR和面试官用户可以进行本操作",
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "username",
                        "in": "path",
                        "description": "用户名",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "body",
                        "in": "body",
                        "description": "更改后的信息",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/User"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "更改信息成功，返回更改后的信息",
                        "schema": {
                            "$ref": "#/definitions/User"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "用户不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "user"
                ],
                "summary": "删除用户",
                "description": "只有HR和面试官用户可以进行本操作",
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "username",
                        "in": "path",
                        "description": "用户名",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "删除成功"
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "用户名不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/report/{candidate_id}": {
            "get": {
                "tags": [
                    "report"
                ],
                "summary": "获取面试者面试报告",
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "面试者id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "面试报告获取成功",
                        "schema": {
                            "$ref": "#/definitions/Report"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试者id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "report"
                ],
                "summary": "更改面试者面试报告",
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "面试者id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "body",
                        "in": "body",
                        "description": "新的报告文本",
                        "type": "string",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/ReportIn"
                        }
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "面试报告更改成功",
                        "schema": {
                            "$ref": "#/definitions/Report"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试者id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "report"
                ],
                "summary": "删除面试者面试报告",
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "面试者id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "required": True,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "删除成功"
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试者id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/chat/{candidate_id}": {
            "get": {
                "summary": "获取面试者聊天记录",
                "description": "获取面试者聊天记录，按时间逆序排列\n",
                "tags": [
                    "chat"
                ],
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "面试者id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "offset",
                        "in": "query",
                        "description": "偏移\n",
                        "default": 0,
                        "minimum": 0,
                        "type": "integer",
                        "format": "integer"
                    },
                    {
                        "name": "limit",
                        "in": "query",
                        "description": "读取数量\n",
                        "default": 10,
                        "maximum": 20,
                        "type": "integer",
                        "format": "integer"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "responses": {
                    "200": {
                        "description": "面试记录列表",
                        "schema": {
                            "$ref": "#/definitions/ChatList"
                        }
                    },
                    "400": {
                        "description": "面试记录获取失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试者id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "post": {
                "summary": "添加聊天记录",
                "tags": [
                    "chat"
                ],
                "parameters": [
                    {
                        "name": "candidate_id",
                        "in": "path",
                        "description": "面试者id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "chat",
                        "in": "body",
                        "description": "聊天记录",
                        "schema": {
                            "$ref": "#/definitions/Chat"
                        },
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "聊天记录添加成功"
                    },
                    "400": {
                        "description": "聊天记录添加失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试者id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/problem/room/{room_id}": {
            "get": {
                "summary": "获取房间内面试题目",
                "tags": [
                    "problem"
                ],
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "room_id",
                        "in": "path",
                        "description": "房间id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "offset",
                        "in": "query",
                        "description": "偏移\n",
                        "default": 0,
                        "minimum": 0,
                        "type": "integer",
                        "format": "integer"
                    },
                    {
                        "name": "limit",
                        "in": "query",
                        "description": "读取数量\n",
                        "default": 10,
                        "maximum": 20,
                        "type": "integer"
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "responses": {
                    "200": {
                        "description": "面试题列表",
                        "schema": {
                            "$ref": "#/definitions/ProblemList"
                        }
                    },
                    "400": {
                        "description": "面试题获取失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "房间id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "post": {
                "summary": "添加面试题",
                "tags": [
                    "problem"
                ],
                "parameters": [
                    {
                        "name": "room_id",
                        "in": "path",
                        "description": "房间id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "problem",
                        "in": "body",
                        "description": "添加的题目",
                        "schema": {
                            "$ref": "#/definitions/Problem"
                        },
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "面试题添加成功"
                    },
                    "400": {
                        "description": "面试题添加失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "房间id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/problem/{problem_id}": {
            "get": {
                "summary": "获取面试题目",
                "description": "由面试题id获取面试题目",
                "tags": [
                    "problem"
                ],
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "name": "problem_id",
                        "in": "path",
                        "description": "面试题id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "responses": {
                    "200": {
                        "description": "面试题获取成功",
                        "schema": {
                            "$ref": "#/definitions/Problem"
                        }
                    },
                    "400": {
                        "description": "面试题获取失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试题id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "put": {
                "summary": "更改面试题",
                "tags": [
                    "problem"
                ],
                "parameters": [
                    {
                        "name": "problem_id",
                        "in": "path",
                        "description": "面试题id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "problem",
                        "in": "body",
                        "description": "更改后的题目",
                        "schema": {
                            "$ref": "#/definitions/Problem"
                        },
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "面试题更改成功,返回更改后的面试题",
                        "schema": {
                            "$ref": "#/definitions/Problem"
                        }
                    },
                    "400": {
                        "description": "面试题更改失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试题id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "delete": {
                "summary": "删除面试题",
                "tags": [
                    "problem"
                ],
                "parameters": [
                    {
                        "name": "problem_id",
                        "in": "path",
                        "description": "面试题id",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "token",
                        "in": "query",
                        "type": "string",
                        "required": True
                    }
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "删除面试题成功"
                    },
                    "400": {
                        "description": "面试题删除失败",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "403": {
                        "description": "用户无访问权限",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    },
                    "404": {
                        "description": "面试题id不存在",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "_Error": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "error"
            ],
            "properties": {
                "error": {
                    "type": "string"
                }
            }
        },
        "Error": {
            "type": "object",
            "additionalProperties": False,
            "allOf": [
                {
                    "$ref": "#/definitions/_Error"
                }
            ],
            "example": {
                "error": "错误信息"
            }
        },
        "User": {
            "type": "object",
            "required": [
                "username",
                "email",
                "type"
            ],
            "additionalProperties": False,
            "properties": {
                "username": {
                    "type": "string"
                },
                "type": {
                    "enum": ["hr", "interviewer", "candidate"]
                },
                "email": {
                    "type": "string"
                },
                "password": {
                    "type": "string"
                },
                "organization": {
                    "type": "string"
                },
                "contact": {
                    "type": "string"
                }
            },
            "example": {
                "username": "Tom",
                "type": "hr",
                "email": "example@example.com",
                "password": "12345",
                "organization": "Example Company",
                "contact": "Example Contact"
            }
        },
        "LoginInfo": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "user": {
                    "$ref": "#/definitions/User"
                },
                "token": {
                    "type": "string",
                    "example": "123456"
                }
            }
        },
        "Room": {
            "type": "object",
            "required": [
                "id",
                "name",
                "interviewer",
                "candidates",
                "problems"
            ],
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "面试房间ID",
                    "example": "1001"
                },
                "name": {
                    "description": "面试房间名称",
                    "type": "string",
                    "example": "计蒜课秋招（前端）"
                },
                "logo": {
                    "description": "面试房间企业logo Url",
                    "type": "string",
                    "example": "http://example.com/examplepage"
                },
                "interviewer": {
                    "description": "面试官，若不存在则置空",
                    "type": "string"
                },
                "candidates": {
                    "description": "候选人ID列表",
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "example": [
                        "100",
                        "101",
                        "102"
                    ]
                },
                "problems": {
                    "description": "面试题ID列表",
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "example": [
                        "200",
                        "201"
                    ]
                }
            }
        },
        "RoomPost": {
            "type": "object",
            "required": [
                "name",
                "interviewer"
            ],
            "additionalProperties": False,
            "properties": {
                "name": {
                    "description": "面试房间名称",
                    "type": "string",
                    "example": "计蒜课秋招（前端）"
                },
                "interviewer": {
                    "description": "面试官，若不存在则置空",
                    "type": "string"
                },
                "candidates": {
                    "description": "候选人ID列表",
                    "type": "array",
                    "items": {
                        "type": "integer"
                    },
                    "example": [
                        "100",
                        "101",
                        "102"
                    ]
                }
            }
        },
        "RoomList": {
            "type": "object",
            "required": [
                "offset",
                "limit",
                "count",
                "rooms"
            ],
            "additionalProperties": False,
            "properties": {
                "offset": {
                    "type": "integer",
                    "format": "integer",
                    "description": "面试房间列表的读取偏移",
                    "example": "0"
                },
                "limit": {
                    "type": "integer",
                    "format": "integer",
                    "description": "面试房间列表的读取个数，最大为100",
                    "minimum": "0",
                    "maximum": "100",
                    "example": "20"
                },
                "count": {
                    "description": "总面试房间数",
                    "type": "integer",
                    "format": "integer",
                    "example": "1"
                },
                "rooms": {
                    "description": "面试房间列表",
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Room"
                    }
                }
            }
        },
        "PostCandidate": {
            "type": "object",
            "required": [
                "name",
                "email",
                "status"
            ],
            "additionalProperties": False,
            "properties": {
                "name": {
                    "description": "候选人姓名",
                    "type": "string",
                    "example": "Mike"
                },
                "email": {
                    "description": "候选人邮箱",
                    "type": "string",
                    "example": "example@example.com"
                },
                "phone": {
                    "description": "候选人手机号",
                    "type": "string",
                    "example": "1300000000"
                },
                "status": {
                    "description": "候选人状态",
                    "default": "未面试",
                    "type": "string"
                },
                "roomId": {
                    "description": "候选人被分配的唯一的面试房间 id",
                    "type": "integer",
                    "example": "1001"
                }
            }
        },
        "Candidate": {
            "type": "object",
            "required": [
                "id",
                "name",
                "email",
                "status"
            ],
            "additionalProperties": False,
            "properties": {
                "id": {
                    "description": "候选人id",
                    "type": "integer",
                    "example": "3001"
                },
                "name": {
                    "description": "候选人姓名",
                    "type": "string",
                    "example": "Mike"
                },
                "email": {
                    "description": "候选人邮箱",
                    "type": "string",
                    "example": "example@example.com"
                },
                "phone": {
                    "description": "候选人手机号",
                    "type": "string",
                    "example": "1300000000"
                },
                "status": {
                    "description": "候选人状态",
                    "default": "未面试",
                    "type": "string"
                },
                "roomId": {
                    "description": "候选人被分配的唯一的面试房间 id",
                    "type": "integer",
                    "example": "1001"
                },
                "record": {
                    "description": "面试记录文件",
                    "type": "object",
                    "properties": {
                        "video": {
                            "description": "视频记录",
                            "type": "integer"
                        },
                        "board": {
                            "description": "白板",
                            "type": "integer"
                        },
                        "chat": {
                            "description": "聊天文件",
                            "type": "integer"
                        },
                        "code": {
                            "description": "代码",
                            "type": "integer"
                        },
                        "report": {
                            "description": "报告",
                            "type": "integer"
                        }
                    }
                }
            }
        },
        "CandidateList": {
            "type": "object",
            "required": [
                "count",
                "offset",
                "limit",
                "candidates"
            ],
            "additionalProperties": False,
            "properties": {
                "offset": {
                    "type": "integer",
                    "format": "integer",
                    "description": "候选人列表的读取偏移"
                },
                "limit": {
                    "type": "integer",
                    "format": "integer",
                    "description": "候选人列表读取个数，上限100",
                    "minimum": 0,
                    "maximum": 100
                },
                "count": {
                    "type": "integer",
                    "format": "integer",
                    "description": "候选人总人数"
                },
                "candidates": {
                    "description": "候选人列表",
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Candidate"
                    }
                }
            }
        },
        "Report": {
            "type": "object",
            "required": [
                "id",
                "candidateId",
                "text"
            ],
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "报告id",
                    "example": "7001"
                },
                "candidateId": {
                    "type": "string",
                    "description": "报告所属面试者id",
                    "example": "101"
                },
                "text": {
                    "type": "string",
                    "description": "报告文本"
                }
            }
        },
        "ReportIn": {
            "type": "object",
            "required": [
                "id",
                "candidateId",
                "text"
            ],
            "additionalProperties": False,
            "properties": {
                "candidateId": {
                    "type": "string",
                    "description": "报告所属面试者id",
                    "example": "101"
                },
                "text": {
                    "type": "string",
                    "description": "报告文本"
                }
            }
        },
        "Chat": {
            "type": "object",
            "required": [
                "candidateId",
                "time",
                "text",
                "sender"
            ],
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "integer",
                    "example": "10001"
                },
                "candidateId": {
                    "type": "string",
                    "description": "聊天所属面试者id",
                    "example": "101"
                },
                "time": {
                    "type": "string",
                    "format": "date-time",
                    "description": "聊天项时间,按RFC3339规范",
                    "example": "2016-01-20T13:30:00Z"
                },
                "text": {
                    "type": "string",
                    "description": "聊天文本"
                },
                "sender": {
                    "type": "boolean",
                    "description": "消息发送方,false代表面试官,true代表面试者",
                    "default": True
                }
            }
        },
        "ChatList": {
            "type": "object",
            "required": [
                "offset",
                "limit",
                "chats"
            ],
            "additionalProperties": False,
            "properties": {
                "offset": {
                    "type": "integer",
                    "format": "integer",
                    "description": "读取偏移"
                },
                "limit": {
                    "type": "integer",
                    "format": "integer",
                    "description": "读取个数",
                    "minimum": 0,
                    "maximum": 20
                },
                "chats": {
                    "description": "聊天记录列表",
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Chat"
                    }
                }
            }
        },
        "ProblemContent": {
            "type": "object",
            "required": [
                "title",
                "description"
            ],
            "additionalProperties": False,
            "properties": {
                "title": {
                    "type": "string",
                    "description": "题目标题",
                    "example": "题目1"
                },
                "description": {
                    "type": "string",
                    "description": "题目描述",
                    "example": "这是一个面试题样例"
                },
                "option": {
                    "type": "array",
                    "description": "选择题选项",
                    "items": {
                        "type": "object",
                        "required": [
                            "content",
                            "correct"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "content": {
                                "type": "string"
                            },
                            "correct": {
                                "type": bool
                            }
                        }
                    }
                },
                "sampleInput": {
                    "type": "string",
                    "description": "编程题样例输入",
                    "example": "1 2"
                },
                "sampleOutput": {
                    "type": "string",
                    "description": "编程题样例输出",
                    "example": "-1"
                }
            }
        },
        "Problem": {
            "type": "object",
            "required": [
                "id",
                "roomId",
                "type",
                "content"
            ],
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "题目id",
                    "example": "3901"
                },
                "roomId": {
                    "type": "integer",
                    "description": "题目所属房间id",
                    "example": "1001"
                },
                "type": {
                    "type": "string",
                    "description": "题目类型(choice, blank, answer, code)",
                    "example": "choice"
                },
                "content": {
                    "description": "题目内容",
                    "schema": {
                        "$ref": "#/definitions/ProblemContent"
                    }
                }
            }
        },
        "ProblemList": {
            "type": "object",
            "required": [
                "offset",
                "limit",
                "problems"
            ],
            "additionalProperties": False,
            "properties": {
                "offset": {
                    "type": "integer",
                    "format": "integer",
                    "description": "读取偏移"
                },
                "limit": {
                    "type": "integer",
                    "format": "integer",
                    "description": "读取个数",
                    "minimum": 0,
                    "maximum": 20
                },
                "problems": {
                    "description": "面试题列表",
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Problem"
                    }
                }
            }
        }
    }
}
