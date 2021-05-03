-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 03 2021 г., 07:07
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
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `uzcard/humo` int(20) NOT NULL,
  `linebet_uz` int(11) NOT NULL,
  `linebet_ru` int(11) NOT NULL,
  `1xbet_uz` int(11) NOT NULL,
  `1xbet_ru` int(11) NOT NULL,
  `melbet_uz` int(11) NOT NULL,
  `melbet_ru` int(11) NOT NULL,
  `qiwi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `chat_id`, `uzcard/humo`, `linebet_uz`, `linebet_ru`, `1xbet_uz`, `1xbet_ru`, `melbet_uz`, `melbet_ru`, `qiwi`) VALUES
(1, 387713426, 0, 0, 0, 0, 0, 0, 0, 0),
(5, 1386463075, 0, 0, 0, 0, 0, 0, 0, 0),
(6, 554547536, 0, 0, 0, 0, 0, 0, 0, 0);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `kurs`
--
ALTER TABLE `kurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
