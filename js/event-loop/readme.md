# 进程线程
1. 进程：CPU在运行指令和保存上下文所需要的时间（系统在执行打开指令，到加载微信上下文环境，直到彻底关闭微信之前的这段时间，都是一个进程）
2. 线程：是进程中的一个更小的单位，指的是执行一段指令所需的时间（打开微信聊天界面就需要一个渲染线程，获取最新消息还需要网络线程）

浏览器新开一个页面就是一个进程，这个进程中有很多线程互相配合最后展示页面给用户。涉及到的线程有：
1. http线程
2. js 引擎线程
3. 渲染线程

线程之间通常都可以同时工作，只有js引擎线程和渲染线程是互斥的。同时会发生冲突

# 异步
- v8在执行js代码时，默认只开启一个线程（js是单线程的），所以考虑到执行效率v8会先执行同步代码，遇到异步代码（会耗时的代码）会将异步代码存放到任务队列等到js引擎的任务空闲再执行异步代码。

# Event-Loop
- js代码中有同步和异步之分，异步还被分为宏任务和微任务

微任务：promise.then  ,process.nextTick,MutationObserver
宏任务：setTimeout,setInterval,ajax,I/O,UI rendering(页面渲染)

- 执行顺序
1. 先执行同步代码（第一个宏任务里的），这个过程遇到异步存入异步队列
2. 同步执行完毕后执行微任务队列的任务
3. 微任务队列执行完毕后有需要的情况下渲染页面（有html）
4. 渲染完毕后执行宏任务队列的任务（下一个宏任务，开启了下一个时间循环）

# await
1. 会将后续的代码挤入微任务队列
2. 浏览器将await的执行时间提前了（await后面的代码要当同步来看）

