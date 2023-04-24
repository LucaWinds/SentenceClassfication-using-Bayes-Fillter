# SentenceClassfication-using-Bayes-Fillter
SentenceCategoryClassfication using Bayes Fillter | easy example


#**Bayes' Theorem |**
A theorem related to conditional probability, established by Thomas Bayes. <br>

`P(B|A) = P(A|B)P(B)/P(A)`<br>

P(A): probability of A occurring <br>
P(B): probability of B occurring <br>
P(A|B): conditional probability of A occurring given that B has occurred <br>
P(B|A): conditional probability of B occurring given that A has occurred <br>

※ Conditional Probability <br>
`P(B|A) = P(B∩A)/P(A)` <br>
The probability of event B given that event A has occurred. <br>

#**Naive Bayes Classifier |** <br>
A classification algorithm that uses Bayes' Theorem to classify text into appropriate categories by examining the frequency of word occurrences in the text. <br>

A represents a set of words in the text and P(B) represents the probability of being classified into each category. <br>
P(A|B) is expressed by separating the input words into P(a1|B)P(a2|B)P(a3|B)...P(aN|B) as follows: <br>
If A is a set of each word aN, then P(A|B) can be expressed as follows. <br>
` P(A|B) = P(a1|B)P(a2|B)P(a3|B)...P(aN|B) ` <br>
Each probability of P(aN|B) is the probability of appearing in a category, and can be conveniently calculated by dividing the number of occurrences of the word in the category by the total number of words in the category.
