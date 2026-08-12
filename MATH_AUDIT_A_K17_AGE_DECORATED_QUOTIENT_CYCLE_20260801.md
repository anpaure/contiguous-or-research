# Audit of the `k=17` Catalan-orbit age-decorated cycle reduction

Date: 2026-08-01  
Lane: A / connected age word and literal quotient lift  
Status: **conditional reduction verified, with one required voltage-twist clarification and one residence-scope clarification**

This note audits

* `MATH_REDUCTION_K17_CATALAN_ORBIT_AGE_DECORATED_RAINBOW_CYCLE_20260801.md`, SHA-256
  `cdebb8b6ef75461e65f04ed5d8a79d210cc30876ecc1392119555d6ddbc6f646`; and
* `scratch/k17_age_type_euler_word_20260801.tsv`, SHA-256
  `e55bea5534c80560755dbc34a1f40e5cb9e67bca23e82d72caf902d2a1fd39f8`.

No construction of the still-missing decorated quotient cycle is claimed.

## 1. Exact audit of the connected type word

The TSV has exactly `1430` data rows.  Its type multiplicities, in the
displayed type order, are

\[
 (139,297,8,20,20,140,127,237,442).
\]

Every row has coordinate sum `9` and last coordinate `c_3=1`.  Every
declared transition `c\to c'` satisfies

\[
 c'_{i+1}\le c_i\qquad(0\le i<3).
\]

The `next_type_id` on each row is the type on the following row, including
the last-to-first cyclic link.  The sixteen nonzero arc multiplicities are

\[
\begin{array}{c|r@{\qquad}c|r}
0\to8&139&1\to6&127\\
1\to8&170&2\to8&8\\
3\to7&20&4\to3&20\\
5\to5&139&5\to8&1\\
6\to2&8&6\to7&119\\
7\to0&139&7\to7&98\\
8\to1&297&8\to4&20\\
8\to5&1&8\to8&124.
\end{array}
\]

Their row and column sums are the type multiplicities above.  The support
is strongly connected: type `8` reaches every branch, every branch returns
to `8`, and the two arcs `8\to5` and `5\to8` attach the former loop bank.
Thus this particular TSV is indeed one Euler circuit, not merely a balanced
circulation.

The numbers of available suffix ranks `1,...,8`, counted once per type
occurrence and rank, are exactly

\[
                    (436,8,40,140,364,728,1144,1430).
\]

This independently reproduces the certificate table.  In particular, the
word closes the former type-support problem but supplies no owner, colour,
or partition data by itself.

## 2. The changing-owner lemma is exact

Let

\[
T=C_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d,
\qquad T'=T-\{\alpha\}+\{\beta\},
\qquad C_d=\{\alpha\}.
\]

For survivor sets `S_i\subseteq C_i` of sizes `c'_{i+1}`, put

\[
C'_{i+1}=S_i,
\qquad
C'_0=\{\beta\}\cup\bigcup_{i<d}(C_i-S_i).             \tag{2.1}
\]

The sets in (2.1) are disjoint and their union is `T'`.  Moreover

\[
 |C'_0|
 =1+\sum_{i<d}(c_i-c'_{i+1})
 =1+(r-c_d)-(r-c'_0)=c'_0,                            \tag{2.2}
\]

where the last equality uses `c_d=1`.  Appending the source letter `C'_0`
refreshes exactly the nonsurvivors and `\beta`; the survivors acquire age
one more; and `\alpha` disappears.  Hence Lemma 2.1 is a literal
last-occurrence update, not merely a type-count identity.

Iterating the lemma gives nonempty source letters because every certified
type has `c_0>0`.  If `P_i=(C^i_0,\ldots,C^i_3)` is the partition after
the `i`th append and `A_i=C^i_0`, induction gives

\[
                 T_i=A_{i-3}\cup A_{i-2}\cup A_{i-1}\cup A_i. \tag{2.3}
\]

It also proves that every **positive** coordinate run in the owner word has
length at least four.  It does not, by itself, give a lower bound on zero
runs.  Thus Section 3's word “residence” is correct if residence means the
positive-run condition used for the depth-three source lift; if signed
residence is intended, that sentence must be qualified.  The proof of
Theorem 5.1 uses the literal source construction (2.3), so no zero-run
hypothesis is needed there.

## 3. Required voltage-twisted formulation of item 4

There is one important point that should be made explicit in the definition
of the quotient object.

Let `\rho` generate `Z_17`.  Choose canonical representatives `T_i` of the
successive quotient owner orbits.  If the selected quotient edge at step
`i` has voltage `v_i`, its canonical physical realization is

\[
                         T_i\longrightarrow \rho^{v_i}T_{i+1}. \tag{3.1}
\]

A representative partition `P_i` of `T_i` is compatible with the next
representative partition `P_{i+1}` precisely when Lemma 2.1 holds between

\[
                         P_i\quad\hbox{and}\quad \rho^{v_i}P_{i+1}, \tag{3.2}
\]

not necessarily between `P_i` and `P_{i+1}`.  The last edge must satisfy
the same condition with `P_0`:

\[
                         P_{N-1}\longrightarrow\rho^{v_{N-1}}P_0. \tag{3.3}
\]

Equations (3.2)--(3.3) are the exact twisted cyclic-closure condition hidden
in the phrase “on every selected edge.”  With them included, after one
quotient lap the state is `\rho^V P_0`, where

\[
                              V=\sum_i v_i\pmod {17}. \tag{3.4}
\]

After seventeen laps it is exactly `P_0`.  If `V\ne0`, then `V` generates
`Z_17`, so the lift is one `17N=24310`-owner cycle.  This proves the voltage
claim in Theorem 5.1.  Without (3.2)--(3.3), a list of unshifted
representative partitions does not by itself define a periodic physical
source word.

For a fixed quotient owner cycle, fixed voltages, and the supplied type
word, this also gives an exact finite criterion.  Let `\mathcal P_i` be the
partitions of `T_i` of the prescribed type whose oldest singleton is the
coordinate deleted by (3.1), and let

\[
 \mathcal R_i\subseteq\mathcal P_i\times\mathcal P_{i+1}
\]

be the relation defined by (3.2).  A literal age decoration exists if and
only if the cyclic relational product

\[
             \mathcal R_0\mathcal R_1\cdots\mathcal R_{N-1} \tag{3.5}
\]

has a diagonal entry.  This is the smallest exact remaining chronology
gate before suffix colours and upper witnesses are imposed.

The gate is nonvacuous.  If `\alpha_i` is the coordinate deleted at step
`i`, then the transition forces the next physical deletion to lie in the
current age-two class:

\[
                       \rho^{v_i}\alpha_{i+1}\in C^i_2. \tag{3.6}
\]

Indeed the next oldest class is the singleton survivor
`S_2\subseteq C^i_2`.  In particular, an edge which inserts a coordinate
and the next edge deletes it has an empty relation, although its pair of
age **types** may satisfy every numerical transition inequality.  The TSV
therefore solves only the type Euler row, not (3.5).

For the current word, `1144` positions have `c_2=1`.  At each such position
(3.6) determines `C^i_2` completely.  The remaining `286` positions have
`c_2=2`.  This quantifies the rigidity of the literal lift.

## 4. Suffix coverage and linearization

For an age partition, the union of the newest `j` source letters is

\[
                         C_0\cup\cdots\cup C_{j-1}.   \tag{4.1}
\]

All nine certified types have positive entries, so their three proper
suffix ranks are strictly increasing.  At rank `s=2,...,8`, the number of
available quotient slots equals the number `\binom{17}{s}/17` of target
orbits.  Therefore item 5 is sufficient provided it is read literally as:

> among **all** available suffix slots of rank `s`, the determined target
> orbits are pairwise distinct.

Under that reading, the slots form a bijection with the target orbits, and
equivariant lift covers every physical rank-`s` target exactly once.  A
single rank-one slot similarly rotates through all seventeen singletons.

At rank eight, (4.1) is

\[
 C_0\cup C_1\cup C_2=T-C_3=T\cap T',                \tag{4.2}
\]

so the rank-eight suffix and the lower Johnson-edge colour are literally
the same set.  This part of the reduction is exact.

Let the resulting physical source period be
`A_0,\ldots,A_{W-1}`, where `W=24310`.  The linear word

\[
 A_0,A_1,\ldots,A_{W-1},A_0,A_1,A_2                \tag{4.3}
\]

has length `W+3=24313`.  It contains every cyclic source interval of width
at most four, and hence retains all singleton and proper-suffix witnesses
and all `W` owner windows.

For any nonwrapping source interval of length at least four,

\[
 \bigcup_{j=a}^{b}A_j
 =\bigcup_{j=a}^{b-3}(A_j\cup A_{j+1}\cup A_{j+2}\cup A_{j+3}), \tag{4.4}
\]

so it is the union of a consecutive nonwrapping owner interval.  Conversely
the union of consecutive owners is the corresponding source interval with
three endpoint letters added.  Thus item 8 is a valid sufficient condition:
if, after choosing the opening, noncrossing owner intervals cover every
rank `10,...,17` target, (4.3) contains literal interval witnesses for all
of them.  The condition is deliberately stronger than necessary, since
some cut-crossing cyclic intervals also survive using the three repeated
letters, but that causes no gap.

## 5. Verdict

After interpreting item 4 by the twisted equations (3.2)--(3.3), the
implication

\[
  \text{certificate-decorated quotient cycle}\quad\Longrightarrow\quad
  \nu(17)=24313
\]

is correct.  The authenticated TSV exactly supplies the connected cyclic
type word and its tight suffix-capacity counts.  It supplies none of the
following: a quotient Johnson cycle, the twisted partition loop (3.5),
actual suffix-orbit distinctness, nonzero voltage, or an upper-safe opening.

The minimal correction to the canonical reduction is expository but
load-bearing: state the voltage shift in item 4 and on the final edge.  The
minimal unresolved physical gate is the nonempty twisted cyclic product
(3.5), already constrained by the forced-next-deletion law (3.6).  Suffix
rainbows and upper safety remain additional simultaneous rows, not
consequences of the age word.
