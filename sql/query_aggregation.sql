-- SQL file to use aggregation functions

SELECT
    COUNT(year_published),
    AVG(year_published),
    MIN(year_published),
    MAX(year_published)
    FROM books;
