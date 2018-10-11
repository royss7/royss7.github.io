---
layout: post
categories: Programming
tags: Programming
title: "Logger for debug"
description: poerfull logger in debug
---

今天下午在调试代码的时候发现，出了问题用原来的logger，根本没办法排查具体是什么问题，出现在哪里？
所以开始反省什么是真正又用的logger信息，logger.debug里面应该dump什么类型的message。

1. 程序入口处，记录传入参数，用于检查输入是否符合预期
2. 运行时间较长的过程，添加process bar，用于检查发生中断的位置，也可以用于查看单步的大概时间
3. 如果最终返回结果只包含部分生成结果，则需要记录完整的生成结果。比如生成一个matrix，最终只需要其中某一列，应该记录matrix和列标。
4. 记录返回值

_update on Seq 28st, 2018_

Learn how to effective logging:
- [Effective logging](http://www.kdgregory.com/index.php?page=java.logging)
  - Try logging guards if huge object, e.g if (logger.isDebugEnabled) logSomething; //the object is too large, use guard to skip it when not debug,
  - Effective logging is a delicate balance between logging enough data to identify problems, while not being buried by details (or filling your disk drive). The reasons for error and fatal error logging are pretty straightforward: the former should be used when the program has hit an unexpected state, the latter when it's about to shut down. In either case, you should log as much information as you can, in the hope that a post-mortem analysis can find and fix the condition(s) that led to the error.
  - Programs are made interesting by their “if” statements; everything else is just moving bits from one place to another. Not surprisingly, this is also where most bugs occur, so it's a great place to insert logging statements. You should log the variables used by the condition, not the condition's branches. If there's a problem you'll want to know why a particular branch was taken: the cause, not the effect.这一条之前有见过，条件判断时应该记录条件值。
  - Do not log in short loops `while (paramItx.hasMoreElements()){logger.debug("parameter \"" + paramName + "\" = " + request.getParameter(paramName)); // it's not need}`
  - Don't log exception messages, pass the exception object to the logger, `logger.debug("in method foo()", new Exception("stack trace"));`

- [10 Tips for proper application logging](https://www.javacodegeeks.com/2011/01/10-tips-proper-application-logging.html)
  - blogger thaught Slf4j is better than log4j(actually said **In my opinion, SLF4J is the best logging API available, mostly because of a great pattern substitution support:**), `SLF4J log.debug("Found {} records matching filter: '{}'", records, filter);` vs `log4j log.debug("Found " + records + " records matching filter: '" + filter + "'");` This is not only longer and less readable, but also inefficient because of extensive use of string concatenation. SLF4J adds a nice {} substitution feature. Also, because string concatenation is avoided and toString() is not called if the logging statement is filtered, _there is no need for isDebugEnabled() anymore_. BTW, have you noticed single quotes around filter string parameter?
  - Logging frameworks have two major benefits over System.out., i.e. categories and levels.
  - Instead, a log file should be readable, clean and descriptive. Don’t use magic numbers, log values, numbers, ids and include their context. Show the data being processed and show its meaning. Show what the program is actually doing. Good logs can serve as a great documentation of the application code itself.
  - You should **never** include file name, class name and line number, although it’s very tempting.
  - First of all, _avoid logging exceptions, let your framework or container (whatever it is) do it for you._ There is one, ekhem, exception to this rule: if you throw exceptions from some remote service (RMI, EJB remote session bean, etc.), that is capable of serializing exceptions, make sure all of them are available to the client (are part of the API). Otherwise the client will receive NoClassDefFoundError: SomeFancyException instead of the “true” error. Don’t include exception message(it will make confused), as it will be printed automatically after the log statement, preceding stack trace.
  - 

