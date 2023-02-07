# Удалённые рабочие столы

## Определение

*Удалённый рабочий стол (Remote Desktop)* — это термин, которым обозначается режим управления, когда один компьютер получает права администратора по отношению к другому (удалённому). Связь между устройствами происходит в реальном времени посредством сети Интернет или локальной сети.

Уровень доступа в режиме удалённого администрирования определяется конкретными задачами и может быть изменен по необходимости. Например:

+ В одном случае подключение к рабочей сессии дает возможность полного контроля и взаимодействия с удаленным компьютером, при котором допускается запуск на нем приложений и манипуляции с файлами
+ В другом - удалённый доступ к рабочему столу позволяет лишь вести наблюдения за процессами, без вмешательства в работу его системы.

*Удалённое администрирование* — предустановленная функция практически в каждой известной сегодня операционной системе, одновременно с этим, существует довольно большое количество программ, которые делают данный процесс более удобным, добавляя в стандартные версии новые функции.

Существуют несколько видов удалённого администрирования:
+ Компьютер-сеть - позволяет контролировать работу локальной сети офиса или интернет-кафе
+ Терминал–компьютер - упрощает связь пользователя с системой, например, платежные терминалы банков
+ Компьютер–компьютер - чаще всего применяемый в быту, однако легко решающий и серьезные управленческие задачи
+ Сеть–сеть - отличный инструмент при необходимости взаимодействия между удаленными корпоративными сетями

## SSH

SSH (Secure SHell - защищенная оболочка) - сетевой протокол прикладного уровня, предназначеный для безопасного удаленного доступа к UNIX-системам. Данный протокол эффективен тем, что шифрует всю передаваемую информацию по сети. По умолчанию, используется 22-й порт. В основном он нужен для удаленного управления данными пользователя на сервере, запуска служебных команд, работы в консольном режиме с базами данных.

### Преимущества

Использование SSH подключения имеет ряд преимуществ:

+ Безопасная работа на удалённом сервере с использованием командной оболочки
+ Использование разных алгоритмов шифрования (симметричного, асимметричного и хеширования)
+ Возможность безопасного использования любого сетевого протокола, что позволяет передавать по защищенному каналу файлы любого размера

Главным преимуществом SSH является использование шифрования для защиты передачи данных между хостом и клиентом. Хост — это удаленный сервер к которому ты хочешь получить доступ, тогда как клиент — это компьютер с которого ты пытаешься получить доступ к хосту. 

### Недостатки

Использование SSH подключения имеет свой недостаток:

+ Протокол SSH не имеет средств защиты от действий злоумышленника, получившего root-доступ. Одной из мер предосторожности является ограничение использования режима root без острой необходимости

## RDP

RDP подключение позволяет управлять компьютером удалённо. RDP считается так называемым "прикладным протоколом", который основан на TCP. После того, как устанавливается соединение на транспортном уровне, начинается инициализация сессии этого протокола. В рамках такой сессии и происходит передача данных.

После того, как фаза инициализации будет завершена, сервер начинает передавать на компьютер (где установлен RDP-клиент) графический вывод. Затем сервер ожидает, когда к нему поступят входные данные от устройств ввода-вывода (мышь и клавиатура). Если говорить простым языком, то принцип работы RPD выглядит следующим образом: пользователь при помощи мыши и клавиатуры управляет компьютером удалённо.

Сегодня эта технология используется повсеместно. Она нужна, в первую очередь, для того, чтобы управлять компьютерными системами. Также многие наработки этой технологии используются и в робототехнике. Даже простейшая радиоуправляемая игрушка основана на схожем принципе. Человеку, в руках которого находится пульт управления, нужно использовать его, чтобы управлять движением радиоуправляемой игрушки.

Обычно для графического вывода используется копия дисплея, которая может передаваться в качестве изображения. Передача вывода происходит при помощи примитивов.

### Для чего используется RDP

Сегодня протокол RDP может применяться в нескольких случаях:

+ В целях администрирования
+ В целях получения доступа к любому серверу приложений

Этот вид соединения применяется любыми операционными системами, которые выпускала компания Microsoft. Обычно все серверные версии ОС от Microsoft могут поддерживать сразу несколько удалённых подключений, а также один локальный вход в систему.

Если же речь идёт о клиентской версии Windows, то она может поддерживать исключительно один вход. Он может быть как удалённым, так и локальным. Для получения разрешения удалённых подключений нужно включить удалённый доступ к рабочему столу. Это можно сделать прямо в свойствах рабочей станции.

Важно отметить, этот удалённый доступ возможен далеко не всегда. Удалённый доступ функционирует исключительно в версии Windows, которая предназначена для сервера. Ещё одно преимущество в данном случае заключается в том, общее число удалённых подключений не ограничено. С другой стороны, потребуется настройка сервера лицензий, а также его активация. Этот сервер можно установить на любой отдельно взятый сетевой узел, а также - на сервер терминалов.

Некоторые пользователи не понимают, что удалённый доступ к любому серверу может быть обеспечен только в случае установки все необходимых лицензий на сервер лицензий.

### Как защитить RDP

Настройка безопасности RDP - это один из ключевых вопросов. Именно правильная настройка протокола влияет на то, насколько будет безопасно передавать данные. Это особенно актуально для государственных компьютерных систем, а также различных частных коммерческих компаний, которые хотят иметь надёжную защиту от конкурентов. Сертификат RDP предусматривает использование любого доступного подхода для обеспечения безопасности. Для RDP можно использовать либо встроенную подсистему безопасности, либо же внешнюю подсистему безопасности.

В случае если пользователь выберет встроенную подсист ему, все функции по обеспечению безопасности будут реализованы средствами, которые изначально имеются в RDP. Речь идёт о процессах шифрования и аутентификации.

Если же будет выбрана внешняя подсистема безопасности, то пользователю придётся полагаться на надёжность таких внешних модулей, как CredSSP и TLS. Преимущества этого способа обеспечения безопасности заключаются в крайне надёжной аутентификации и эффективном шифровании.

Именно качественное шифрование позволяет защитить свою систему от взлома злоумышленников. Сегодня существует масса вредоносных программ и алгоритмов, которые нужны для взлома. Более того, взлом может совершить не только квалифицированный специалист, но и рядовой пользователь, который приобрёл специальное вредоносное программное обеспечение.

Многих пользователей интересует вопрос о том, какой порт использует RDP (RDP сервер). Стандартный порт - это порт под номером 3389/TCP.
