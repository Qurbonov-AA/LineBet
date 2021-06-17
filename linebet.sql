-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Июн 17 2021 г., 10:11
-- Версия сервера: 5.5.62
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `linebet`
--

-- --------------------------------------------------------

--
-- Структура таблицы `imgs`
--

CREATE TABLE `imgs` (
  `id` int(11) NOT NULL,
  `file_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `imgs`
--

INSERT INTO `imgs` (`id`, `file_id`, `user_id`, `status`) VALUES
(1, 'AgACAgIAAxkBAAIBpGCPwQ2eWSup3FylCiIe2DMIXTA7AAIBsTEbxlRxSE65zXOQFQdANJQapC4AAwEAAwIAA20AAyqRAAIfBA', '1062838548', 'front'),
(2, 'AgACAgIAAxkBAAIBpmCPwROnQoKoYk319MHos4N_zoAwAAIBsTEbxlRxSE65zXOQFQdANJQapC4AAwEAAwIAA20AAyqRAAIfBA', '1062838548', 'backend'),
(6, 'AgACAgIAAxkBAAIBuGCPz4wZ_U1H_D3EQZltGJ7mcG0pAAIzsjEbO0t4SDungGTKsENqcMmKoi4AAwEAAwIAA3kAA1bOAQABHwQ', '387713426', 'front'),
(7, 'AgACAgIAAxkBAAIBumCPz5DF39sQaElSxaQVfY4CqFDfAAJMsjEbO0t4SF0hcFq6xSO_-OlWoi4AAwEAAwIAA20AA3DWAQABHwQ', '387713426', 'backend');

-- --------------------------------------------------------

--
-- Структура таблицы `kurs`
--

CREATE TABLE `kurs` (
  `id` int(11) NOT NULL,
  `1xbet_uz` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `1xbet_ru` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `1xbet_us` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `linebet_uz` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `linebet_ru` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `linebet_us` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `melbet_uz` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `melbet_ru` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `melbet_us` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `qiwi` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `in_out` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `kurs`
--

INSERT INTO `kurs` (`id`, `1xbet_uz`, `1xbet_ru`, `1xbet_us`, `linebet_uz`, `linebet_ru`, `linebet_us`, `melbet_uz`, `melbet_ru`, `melbet_us`, `qiwi`, `in_out`) VALUES
(1, '4%', ' 145 UZS', '10400 UZS', '4%', '135 UZS', '10400 UZS', '4%', '135 UZS', '10400 UZS', '148 UZS', 0),
(2, '0%', '135 UZS', '10400 UZS', '0%', '135 UZS', '10400 UZS', '0%', '135 UZS', '10400 UZS', ' 140 UZS', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `outpays`
--

CREATE TABLE `outpays` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_card` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dates` date NOT NULL,
  `types` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'new'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `outpays`
--

INSERT INTO `outpays` (`id`, `user_id`, `user_card`, `dates`, `types`, `status`) VALUES
(1, 387713426, ' 0', '2021-06-16', 'push_1xuzb', 'new'),
(2, 387713426, ' 0', '2021-06-16', 'push_lineuzb', 'new'),
(3, 387713426, ' 0', '2021-06-16', 'push_melbetuzb', 'new'),
(4, 387713426, ' 0', '2021-06-16', 'push_1xuzb', 'new'),
(5, 554547536, '8600140435703799', '2021-06-16', 'push_lineuzb', 'new');

-- --------------------------------------------------------

--
-- Структура таблицы `pays`
--

CREATE TABLE `pays` (
  `id` int(11) NOT NULL,
  `client_card` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_id` int(11) NOT NULL,
  `price` int(7) NOT NULL,
  `dates` varchar(25) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'new',
  `name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `pays`
--

INSERT INTO `pays` (`id`, `client_card`, `client_id`, `price`, `dates`, `status`, `name`) VALUES
(2, '8600310491574232', 387713426, 50000, '2021-05-06 15:21:00', 'old', 'LineBet UZS'),
(3, '8600310491574232', 387713426, 150000, '2021-05-19 09:31:15', 'old', 'LineBet UZS'),
(4, '8600310491574232', 387713426, 75000, '2021-05-19 10:00:36', 'old', 'MelBet UZS'),
(5, '8600310491574232', 387713426, 125000, '2021-05-19 10:00:48', 'old', '1XBET UZS'),
(6, '8600310491574232', 387713426, 750000, '2021-05-31 11:37:28', 'old', '1XBET UZS'),
(7, '8600310491574232', 387713426, 15000, '2021-05-31 12:20:02', 'old', 'MelBet UZS'),
(8, '8600310491574232', 387713426, 5000, '2021-05-31 12:37:27', 'old', '1XBET UZS'),
(9, '8600310491574232', 387713426, 5000, '2021-05-31 12:42:47', 'old', '1XBET UZS'),
(11, '8600140435703799', 554547536, 222660099, '2021-06-10 14:25:41', 'new', 'MelBet UZS'),
(12, '8600140435703799', 554547536, 1, '2021-06-10 14:26:12', 'new', 'MelBet UZS'),
(13, '8600140435703799', 554547536, 100000, '2021-06-10 14:26:53', 'new', '1XBET UZS'),
(14, '8600140435703799', 554547536, 1, '2021-06-10 14:31:31', 'new', '1XBET UZS'),
(15, '8600140435703799', 554547536, 10000, '2021-06-10 14:32:27', 'new', '1XBET UZS'),
(18, '8600310491574232', 387713426, 5000, '2021-06-10 14:49:50', 'new', '1XBET UZS'),
(19, '8600140435703799', 554547536, 50000, '2021-06-10 14:50:45', 'new', '1XBET UZS'),
(21, '8600140435703799', 554547536, 50000, '2021-06-14 22:10:16', 'new', '1XBET UZS'),
(22, '8600140435703799', 554547536, 30000, '2021-06-15 13:06:59', 'new', '1XBET UZS'),
(23, '8600140435703799', 554547536, 50000, '2021-06-16 13:20:39', 'new', '1XBET UZS'),
(31, '8600140435703799', 554547536, 34500, '2021-06-16 19:20:23', 'new', '1XBET UZS'),
(32, '8600140435703799', 554547536, 32003, '2021-06-16 19:23:26', 'new', '1XBET UZS'),
(33, '8600140435703799', 554547536, 50000, '2021-06-16 20:01:44', 'new', '1XBET UZS');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `uzcard` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0',
  `linebet_uz` int(11) NOT NULL,
  `promokod` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `1xbet_uz` int(11) NOT NULL,
  `link` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `melbet_uz` int(11) NOT NULL,
  `admin` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'user',
  `number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `chat_id`, `uzcard`, `linebet_uz`, `promokod`, `1xbet_uz`, `link`, `melbet_uz`, `admin`, `number`) VALUES
(1, 387713426, ' 0', 0, 'iFnwvLAAHc', 1234567, 'https://t.me/LinrBet_Bot?start=iFnwvLAAHc', 1254789, '0', '+998973226755'),
(5, 1386463075, '0', 0, '0', 0, '0', 0, '0', '0'),
(6, 554547536, '8600140435703799', 0, '0', 222660099, '0', 222660099, 'admin', '0'),
(7, 1062838548, '0', 0, '0', 0, '0', 0, '0', '0'),
(9, 1713680678, '0', 0, 'KjzomZJm1o', 0, 'https://t.me/LinrBet_Bot?start=KjzomZJm1o', 0, '0', '0'),
(10, 784266795, '0', 0, 'e5RxjURXbDc', 0, '', 0, 'user', '0'),
(11, 710257299, '', 0, 'u6nJ57yb8u8', 0, '', 0, 'user', '0'),
(12, 1885419321, '0', 0, 'oNLDbg0ke4Q', 0, '', 0, 'user', '0');

-- --------------------------------------------------------

--
-- Структура таблицы `users_promo`
--

CREATE TABLE `users_promo` (
  `id` int(11) NOT NULL,
  `user_id` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_id` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dates` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `users_promo`
--

INSERT INTO `users_promo` (`id`, `user_id`, `client_id`, `dates`) VALUES
(2, '1713680678', '387713426', '2021-05-17'),
(3, 'None', '710257299', '2021-06-11'),
(4, 'None', '710257299', '2021-06-11');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `imgs`
--
ALTER TABLE `imgs`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `kurs`
--
ALTER TABLE `kurs`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `outpays`
--
ALTER TABLE `outpays`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `pays`
--
ALTER TABLE `pays`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users_promo`
--
ALTER TABLE `users_promo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `imgs`
--
ALTER TABLE `imgs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `kurs`
--
ALTER TABLE `kurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `outpays`
--
ALTER TABLE `outpays`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `pays`
--
ALTER TABLE `pays`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT для таблицы `users_promo`
--
ALTER TABLE `users_promo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
