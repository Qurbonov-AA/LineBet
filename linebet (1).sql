-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 07 2021 г., 10:00
-- Версия сервера: 5.5.62
-- Версия PHP: 7.3.26

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
(2, '8600310491574232', 387713426, 50000, '2021-05-06 15:21:00', 'new', 'LineBet UZS');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `uzcard` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0',
  `linebet_uz` int(11) NOT NULL,
  `linebet_ru` int(11) NOT NULL,
  `1xbet_uz` int(11) NOT NULL,
  `1xbet_ru` int(11) NOT NULL,
  `melbet_uz` int(11) NOT NULL,
  `melbet_ru` int(11) NOT NULL,
  `humo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `chat_id`, `uzcard`, `linebet_uz`, `linebet_ru`, `1xbet_uz`, `1xbet_ru`, `melbet_uz`, `melbet_ru`, `humo`) VALUES
(1, 387713426, '8600310491574232', 12345678, 0, 87456987, 0, 987456140, 0, 0),
(5, 1386463075, '0', 0, 0, 0, 0, 0, 0, 0),
(6, 554547536, '0', 0, 0, 0, 0, 0, 0, 0),
(7, 1062838548, '0', 0, 0, 0, 0, 0, 0, 0);

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
-- AUTO_INCREMENT для таблицы `pays`
--
ALTER TABLE `pays`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
