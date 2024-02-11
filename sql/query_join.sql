-- Inner join between authors and books
SELECT authors.first, authors.last, books.title, books.year_published
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;
