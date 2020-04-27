-- https://medium.com/google-cloud/a-journey-into-bigquery-fuzzy-matching-2-of-1-more-soundex-and-levenshtein-distance-e64b25ea4ec7
CREATE OR REPLACE FUNCTION
  dq.dq_fm_LevenshteinDistance(in_a string,
    in_b string)
  RETURNS INT64
  LANGUAGE js AS 
"""/*
 * Data Quality Function - Fuzzy Matching
 * dq_fm_LevenshteinDistance
 * Based off of https://gist.github.com/andrei-m/982927
 * input: Two strings to compare the edit distance of.
 * returns: Integer of the edit distance.
 */
var a = in_a.toLowerCase();
var b = in_b.toLowerCase();
  
if(a.length == 0) return b.length; 
if(b.length == 0) return a.length;
var matrix = [];
// increment along the first column of each row
var i;
for(i = 0; i <= b.length; i++){
  matrix[i] = [i];
}
// increment each column in the first row
var j;
for(j = 0; j <= a.length; j++){
  matrix[0][j] = j;
}
// Fill in the rest of the matrix
for(i = 1; i <= b.length; i++){
  for(j = 1; j <= a.length; j++){
    if(b.charAt(i-1) == a.charAt(j-1)){
      matrix[i][j] = matrix[i-1][j-1];
    } else {
      matrix[i][j] = 
        Math.min(matrix[i-1][j-1] + 1, // substitution
        Math.min(matrix[i][j-1] + 1, // insertion
        matrix[i-1][j] + 1)); // deletion
    }
  }
}
return matrix[b.length][a.length];
"""

WITH
  data AS (
  SELECT
    'Whiskey' a,
    'whisky' b
  UNION ALL
  SELECT
    'drinjs' a,
    'Drinks' b
  UNION ALL
  SELECT
    'Chandler Bing' a,
    'Miss Chanandler Bong' b)
SELECT
  a,
  b,
  `dq.dq_fm_LevenshteinDistance`(a, b) as ldistance
FROM
  data



-- 
-- 혹은 외부 PERSISTANT UDF
-- 아쉽게도 한글은 지원하지 않음... 
fhoffa.x.levenshtein('Whiskey', 'whisky')

