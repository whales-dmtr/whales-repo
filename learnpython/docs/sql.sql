/* Базы данных */

/* База данных - это программа, с помощью которой можно структурированно хранить большие объемы данных. */
/* Реляционные бд - это базы данных в которых присутствуют relation, тоесть связи. */
/* Для создания и взаимодействия с базами данных используется СУБД - система управления базами данных. */
/* SQL - это язык запросов к базе данных, эти запросы передает СУБД. */
/* PostgreSQL и MySQL - это СУБД, которые отвечают за передачу запросов к базе данных. */

/* CREATE ... - создает сущность в sql */

CREATE DATABASE mysuperdb  /* создает базу данных */

CREATE TABLE users (  /* создает таблицу */
    id INT PRIMARY KEY,  /* здесь перчисляем все колонки таблицы */
    username VARCHAR(32) NOT NULL, /* название тип(макс_колво_символов) доп характеристики */
    email VARCHAR(64) NOT NULL 
    /* NOT NULL говорит о том, что в колонке не может быть пустого значения */
    /* PRIMARY KEY говорит о том, что эта колонка это уникальный идентификатор */
)

/* INSERT - вставляет что-то */

INSERT INTO table_name(id, username, email) /* для вставки в таблицу используем INTO, также помими имени таблицы указываем столбцы, в которые будем вставлять */
VALUES (1, 'Dima', 'dmtroley@gmail.com') /* перечисляем что хотим вставить в таком же порядке, как и выше */

UPDATE users SET  /* обновление данных в таблице users */
username = 'Vasiliy'  /* после SET пишем что будем изменять */
WHERE id = 3  /* после WHERE указываем условие, оно нужно чтоб изменить конкретную запись, а не все значения конкретной колонки */

DELETE FROM users /* удаление из таблицы users */
WHERE id = 2 OR id = 3 /* условие: где айди 2 или где айди 3 */

SELECT email FROM users  /* выводит информацию из таблицы*/
/* SELECT колонки, которые хотим видеть FROM из какой таблицы */
WHERE id = 2 /* условие: где айти 2 */
/* AND дополнительное условие, должно быть также выполненно */
/* OR дополнительное условие, может быть не выполненно */
/* после SELECT можно указать * чтоб вывести все колонки */

CREATE spendings ( /* это таблица с тратами юзеров */
	id INT PRIMARY KEY,
	price INT NOT NULL,
	date TIMESTAMP DEFAULT now(),  
	user_id INT NOT NULL, /* эта колонка это ссылки на юзеров */

	CONSTRAINT users_id_fk FOREIGN KEY (user_id) REFERENCES users(id)
    /* ключевое слово CONSTRAINT нужно для добавления ограничений, после него указываем название ограничения */
    /* FOREIGN KEY говорит о том что колонка user_id это ссылки на поле id из таблицы users*/
);

/* для вывода нескольких таблиц используется JOIN */
/* с помощью JOIN мы можем объединять колонки из разных таблиц, если они связаны внешними ключами */

SELECT * FROM spendings /* тут пишем таблицу к которой будем присоединять другую */
JOIN users ON users.id = spendings.user_id  /* здесь сначала после JOIN пишем таблицу которую будем присоединять, а потом пишем условие */
/* важно понимать, что в этом запросе используются две таблицы и поэтому если указываем колонку нужно указывать из какой таблицы */

SELECT spendings.pric, users.username FROM spendings
JOIN users ON users.id = spendings.user_id 
/* теперь выведенно будет только затраты и имена пользователей */
/* также можно объединять и больше двух таблиц */
SELECT users.username, spendings.price, marks.mark FROM users
JOIN spendings ON users.id = spendings.user_id
JOIN marks ON users.id = marks.user_id

/* такой вид джоинов называется INNER JOIN и их особенность в том, что они не выведут поля у которых условие не соответствует */
/* но если вам нужно вывести и поля к которым пары не нашлось, можно использовать OUTER JOIN */
/* при использовании аутер джоина также нужно указать LEFT или RIGHT */
/* LEFT говорит о том что будут выводится колонки, которые не нашли пару, таблицы К КОТОРОЙ ПРИСОЕДИНЯЕМ */
/* RIGHT говорит о том что будут выводится колонки, которые не нашли пару, таблицы КОТОРУЮ ПРИСОЕДИНЯЕМ */

SELECT users.username, spendings.price FROM users
LEFT OUTER JOIN spendings ON users.id = spendings.user_id

/* Агрегатные функции */

SELECT SUM(price) FROM spendings /* выведет сумму всей колонки price */
SELECT MIN(price) FROM spendings /* выведет минимальное число в колонке price */
SELECT MAX(price) FROM spendings /* выведет максимальное число в колонке price */
/* их нельзя использовать с WHERE */

/* GROUP BY определяет колонку по которой будет групироваться использование агрегатной функции */
/* если не указать груп бай то агрегатная функция будет применятся сразу ко всей колонке */
/* также важно понимать, что если вы выводите чтото помимо результата агрегатных функций(дополнительные колонки) то тогда нужно групировать и добавляемую колонку */

SELECT SUM(price) FROM spendings
GROUP BY user_id

/* также можно объеденить действие джоинов и агрегатных функций */
/* джоины всегда писать перед груп бай */

SELECT SUM(spendings.price), users.username FROM spendings
JOIN users ON spendings.user_id = users.id
GROUP BY users.username

/* HAVING можно использовать груп бай и это пародия на WHERE только с хэвинг можно использовать агрегатные функции*/
SELECT SUM(price) FROM spendings
GROUP BY user_id
HAVING SUM(price) > 1000

ALTER TABLE cars /* эта конструкция используется для изменения струкутры таблицы(типы и названия колонок, ограничения и тд) */
ALTER COLUMN color TYPE VARCHAR(30); /* с помощью TYPE можно изменить тип */

ALTER TABLE marks /* также можно добавить ограничение */
ADD CONSTRAINT mark_check CHECK (mark BETWEEN 0 AND 13) /* здесь мы проверяем чтоб оценка было между 0 и 13 */

ALTER TABLE spendings
ADD COLUMN category BIGINT

SELECT SUM(price) FROM spendings
GROUP BY user_id
HAVING SUM(price) > 1000
ORDER BY SUM(price) DESC /* мы можем сортировать результаты, после ORDER BY пишем поле, по которому сортируем */
/* по дефолту сортировать будет по возрастанию, но если указать DESC тогда по убыванию*/

/* выводит топ 3 самых дорогих покупок */
SELECT price FROM spendings
ORDER BY price DESC
LIMIT 3  /* лимит по результатам */

SELECT name
FROM passenger
WHERE name LIKE '%man' /* можно написать часть текста и если она будет в поле условие будет принято*/
/* нужно использовать % для уточнение где этот паттерн может быть */
/* '%patern' в конце */
/* 'patern%' в начале */
/* '%patern%' где угодно */

SELECT COUNT(*) as count  /* выводит количество полей определенного столбца*/
FROM trip
WHERE plane = 'TU-134'

SELECT company.name as name FROM company
JOIN trip ON trip.company = company.id
WHERE trip.plane = 'Boeing' 
GROUP BY company.id  /* с помощью груп бай айди можно также удалять дубликаты */

ALTER TABLE pass_in_trip
RENAME plane TO place /* переименновать колонку */

SELECT town_to,
to_char(time_in - time_out, 'HH:MM:SS') /* to_char преобразовывает время в нужный формат */
AS flight_time
FROM trip
WHERE town_from = 'Paris'; 
