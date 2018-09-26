---
layout: post
categories: Programmer
tags: Programmer
title: "Logger for debug"
description: poerfull logger in debug
---

今天下午在调试代码的时候发现，出了问题用原来的logger，根本没办法排查具体是什么问题，出现在哪里？
所以开始反省什么是真正又用的logger信息，logger.debug里面应该dump什么类型的message。

1. 程序入口处，记录传入参数，用于检查输入是否符合预期
2. 运行时间较长的过程，添加process bar，用于检查发生中断的位置，也可以用于查看单步的大概时间
3. 如果最终返回结果只包含部分生成结果，则需要记录完整的生成结果。比如生成一个matrix，最终只需要其中某一列，应该记录matrix和列标。
4. 记录返回值

