# Strict-alternation obstruction in the Goddyn--Gvozdjak construction

This note concerns the particular product construction of Goddyn and Gvozdjak,
*Binary Gray Codes with Long Bit Runs*, EJC 10 (2003), R27, Lemma 3 and its
displayed circuit on pp. 4--5 (recurrence: Corollary 8, p. 6)
([DOI](https://doi.org/10.37236/1720), [journal PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v10i1r27/pdf/)),
not arbitrary long-run Gray codes.

Let their Lemma 3 be applied to $Q_a\square Q_c=Q_d$, where
$d=a+c$. Its displayed Hamilton circuit alternates an edge of $Q_a$
and an edge of $Q_c$ at every step. Thus its cyclic transition sequence
$t_0,\ldots,t_{2^d-1}$ alternates labels from the disjoint coordinate
classes $A,C$, of sizes $a,c$.

Let $r=\operatorname{mrl}(t)$, and regard $t$ as a cyclic singleton OR
word. Fix $1\le \ell<r$. Any interval whose union has cardinality
$\ell$ has exactly $\ell$ positions: an interval of length at least
$r$ contains $r$ consecutive pairwise-distinct transition labels, while
an interval of length below $r$ has no repeated label. Consequently **all**
rank-$\ell$ interval unions of this word, including unintended witnesses,
obey the alternation constraint.

Writing $\ell=2s$, every such target $S$ satisfies

\[
 |S\cap A|=|S\cap C|=s,
\]

so the rank-$\ell$ support has size at most

\[
 N_{a,c}(2s)=\binom as\binom cs. \tag{1}
\]

Writing $\ell=2s+1$, it instead satisfies one of the two possible balances,
and hence

\[
 N_{a,c}(2s+1)
 \le \binom a{s+1}\binom cs+\binom as\binom c{s+1}. \tag{2}
\]

Equivalently, after division by $\binom d\ell$, (1)--(2) are one or two
point probabilities for a hypergeometric random variable

\[
 X=|S\cap A|,\qquad S\sim\binom{[d]}\ell.
\]

In the split used in the proof of their Theorem 1,
$a,c=d/2+O(\log d)$. For $\ell=d/2+O(1)$, Stirling's formula (or the
standard maximal-atom estimate for this central hypergeometric law) gives

\[
 \frac{N_{a,c}(\ell)}{\binom d\ell}=O(d^{-1/2}). \tag{3}
\]

The theorem's target bound $r\ge\lfloor d-2.001\log_2d\rfloor$ has
$d/2<r$ for all sufficiently large $d$. Whenever that bound is realized
by a direct Lemma-3 product step, its strictly-alternating transition word
realizes only an
$O(d^{-1/2})$ fraction of the middle-rank OR targets; it misses
$1-O(d^{-1/2})$.

This does not contradict the long-run theorem. That theorem controls local
label repetition (and therefore cleanliness/geodesicity), not global diversity
of transition sets. It also is not a lower bound for every long-run Gray code.
In particular, the proof of Theorem 1 sometimes passes from dimension
$a+c$ to $a+c+1$ using monotonicity, so (1)--(3) are asserted only for
the literal strictly-alternating product cycles supplied by Lemma 3 and
Corollary 8. Any use of this route for coefficient one must vary or destroy
the top-level alternation, for example through many correlated coordinate
splits; cleanliness alone is insufficient.
