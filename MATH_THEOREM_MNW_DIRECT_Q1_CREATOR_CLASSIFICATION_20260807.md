# The residual `1101011011` hole has no support-safe direct hex creator

**Date:** 2026-08-07  
**Method:** complete touching-step and inverse-pair exhaustion; no
computation or search  
**Status:** unconditional for one incidence hex in the current direct
positive route.  Two literal creators exist, and both move the hole to a
canonical unit provider.

Put

\[
                         Q_1=1101011011.             \tag{1.1}
\]

Its canonical inverse list is only `(6,7)`, at `1101000011`; that
occurrence is removed by the H1 repair C8.

For a centre `Q_1-\{p,q\}`, exactly one desired addition is currently
selected only for

\[
 \{1,9\},\{2,7\},\{4,6\},\{4,7\},
 \{4,10\},\{6,9\},\{7,9\}.                         \tag{1.2}
\]

Testing the five possible core labels in each row leaves exactly two
alternating faces:

\[
\begin{array}{c|c|c}
\text{desired pair}&\text{centre pair}&\text{core label}\\ \hline
\{4,7\}&\{5,7\}&9,\\
\{6,9\}&\{6,8\}&4.
\end{array}                                         \tag{1.3}
\]

The first face has core `1100010001`, active labels `9,5,4`, and current

\[
 [Q_1]+[1100110111]-[1100111011]-[1101010111].      \tag{1.4}
\]

The negative target `1101010111` has the unique inverse pair `(8,9)`,
which this face removes.

The second face has core `1100001001`, active labels `4,8,9`, and current

\[
 [Q_1]+[1101101101]-[1101011101]-[1101101011].      \tag{1.5}
\]

The last two negative targets have the unique inverse pairs `(6,8)` and
`(4,5)`, respectively, and those are exactly the occurrences removed.

Consequently neither face is support safe.  Every other one-selected
centre fails one auxiliary phase, and all remaining centres have zero or
two desired selected additions (or only an endpoint incidence).  Hence a
single direct hex cannot close `Q_1`; it can only relay its unit debt.

This theorem does not exclude a correlated multi-face annulus packet in
which the new unit targets are recreated elsewhere.
