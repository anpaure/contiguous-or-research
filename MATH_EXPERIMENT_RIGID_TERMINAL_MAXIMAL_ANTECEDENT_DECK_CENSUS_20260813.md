# H100 census of the full rigid-terminal maximal-candidate deck

**Date:** 2026-08-13  
**Method:** exact standard/complement-GK factor generation, literal full
rotation rigid-`C6` switch, directed component replay, maximal depth-`d`
intersection word, and exhaustive cyclic source-interval OR census.  All
substantive enumeration ran on `h100`, not on the local Mac.  
**Status:** exact finite data and a general rank obstruction.  The touched
rigid braid/residual sector is componentwise resident and has a perfectly
rank-stratified maximal source deck through width `d`.  It never supplies
any target below rank `R-d`.  The full terminal factor is already
nonresident for `m>=5`, and its maximal-candidate deck develops a
rotation-invariant bottom-row hole.  No claim extrapolating the finite
bottom-row counts to all `m` is made.

## 1. Exact reconstruction

Put

\[
                         n=2m+1,qquad R=m+1.
\]

For every rank-`m` set `L`, the standard/complement-GK factor has directed
successor

\[
                         L\longmapsto p^{-2}(L).
\]

For the rigid packet use

\[
 K=\{1,\ldots,m-2\},\qquad
 (a_0,a_1,a_2)=(m-1,m,m+1),qquad c=0,
\]

\[
 P_i=K+a_i+a_{i+1},qquad Q_i=K+a_i+c.
\]

At every phase `t`, replace the three directed arcs

\[
                         P_i(t)\to Q_i(t)
\]

by

\[
                         P_i(t)\to Q_{i+1}(t).
\]

The script verifies that every old arc is present, every new head is used
once, and complementation gives a directed rank-`R` owner factor.

For a directed owner cycle `T`, its maximal candidate word is

\[
                         P_j=\bigcap_{a=0}^{d}T_{j-a}.          \tag{1.1}
\]

The program records whether `D^dP=T`, then enumerates every cyclic interval
of `P` of widths `1,...,d` and its exact OR value.

## 2. First global finding: the full factor is not resident

For `m=4`, `d=2`, the full factor happens to satisfy `D^dP=T`.  Starting
at `m=5`, unchanged PBBS components contain short runs, and `(1.1)` is not
an antecedent of the full terminal factor.  Exact mismatch counts were:

\[
\begin{array}{c|rrrrrrrr}
m&4&5&6&7&8&9&10&11\\ \hline
d&2&3&3&3&3&3&3&4\\
\#\{j:(D^dP)_j\ne T_j\}
 &0&99&156&225&306&399&504&77694.
\end{array}                                                   \tag{2.1}
\]

Thus “the maximal antecedent of the full rigid terminal factor” is not a
literal object beyond the smallest case.  The source-deck census for the
full factor must be read as a **maximal-candidate** census.  This recovers
computationally the proof-level warning that the rigid move makes only its
touched braid/residual sector resident; it does not repair every ambient
PBBS component.

## 3. The touched sector has exact width/rank stratification

The touched terminal sector consists of one braid cycle and
`gcd(2m+1,3)` residual cycles.  Its total owner count is

\[
 2(2m+1)+(2m+1)(2m-4)
 =(2m+1)(2m-2).                                      \tag{3.1}
\]

The H100 replay through `m=100` verified `D^dP=T` on every touched cycle.
More sharply, for every tested `m` and every width `1<=w<=d`, **all**
`(2m+1)(2m-2)` source intervals have rank

\[
                         |\operatorname {OR}(I)|=R-d+w-1.      \tag{3.2}
\]

There were no other ranks.  Representative rows are:

\[
\begin{array}{c|c|c|c}
m&d&\text{sector size}&\text{ranks at widths }1,\ldots,d\\ \hline
5&3&88&3,4,5\\
11&4&460&8,9,10,11\\
20&5&1558&16,17,18,19,20\\
50&7&9898&44,45,46,47,48,49,50\\
100&9&39798&92,93,94,95,96,97,98,99,100.
\end{array}                                                   \tag{3.3}
\]

Equation `(3.2)` is exactly what the maximal-antecedent row identity
predicts for a simple `d`-resident Johnson trace: one maximal letter has
rank `R-d`, and each added source position introduces one new coordinate.
The finite replay is therefore an independent end-to-end audit of the
closed braid/residual formulas and their orientation.

## 4. Sharp deep-row conclusion

Every maximal source letter on a componentwise `d`-resident simple
rank-`R` Johnson cycle has rank `R-d`.  Hence every nonempty source
interval has rank at least `R-d`.  In particular

\[
 \boxed{
 \text{the maximal touched-sector antecedent contains no target of rank}
 <R-d.}                                                       \tag{4.1}
\]

The H100 sector replay found zero such occurrences in every case through
`m=100`.  This is not merely an observed pattern: `(4.1)` follows
immediately from monotonicity of OR and the constant letter rank `R-d`.

Thus the census gives a decisive negative answer to the hoped-for surprise
at depths `q>d`: the maximal rigid-sector antecedent cannot accidentally
cover even one deep target.  Every deep target requires a nonmaximal
antecedent obtained by deleting coordinates, or a separate remote payload
atlas.  No orbit multiplicity inside the maximal word changes this rank
barrier.

## 5. Unexpected finite full-factor bottom-row hole

Although the full maximal candidate word is not an antecedent, its
top-rank OR deck is still informative diagnostically.  For `m=5,...,10`,
the ranks `R-d,...,R-2` were complete, but rank `R-1=m` had respectively

\[
                         77,117,165,221,285,357                 \tag{5.1}
\]

missing values.  These numbers are exactly

\[
                         (m-1)(2m+1).                           \tag{5.2}
\]

The missing family is invariant under ground rotation.  It contains one
entire canonical PBBS component of length

\[
                         3(2m+1)                                \tag{5.3}
\]

for every `m=5,...,10`.  At `m=11`, where the deadline increases to four,
the pattern changes sharply: ranks `R-d` and `R-d+1` remain complete, but
the next two ranks have `6693` and `67436` holes, and many whole canonical
components lie inside the bottom-row missing family.

These finite data show that neither reversing every terminal cycle nor
taking the union of both orientations repairs the hole: the directed,
reversed, and either-orientation value sets were identical in every tested
row.  They suggest a simple orbit classification of the bottom defect, but
`(5.2)` is recorded only as a verified `d=3`, `m=5,...,10` pattern, not a
proved all-parameter formula.

## 6. Reproducible artifacts

The exact enumerator is

* `scratch/audit_rigid_terminal_maximal_antecedent_deck_20260813.py`.

Its SHA-256 is

`1eba3647c2a5cc443b0dd266eefab90e6867d9a8c18b851b8177e7607b4895ff`.

The exhaustive full-factor output for `m=4,...,11` is

* `scratch/h100_results/rigid_terminal_maximal_deck_m4_m11_20260813.json`,

SHA-256

`71408faa7ad6ccbe3f1b2aa19797fa511e5128366e9d78f71d071cfc8641f00e`.

The lightweight closed-form touched-sector replay through `m=100` is

* `scratch/h100_results/rigid_sector_maximal_deck_m4_m100_20260813.json`,

SHA-256

`b1217943a632dde5a3b53961b103620ded8ae5eaa11fd24b07e94ec3590244c5`.

The local machine performed only syntax checks, hashing, and inspection of
returned data.  Factor generation and exhaustive deck enumeration ran on
`h100`.

## 7. Consequence

The rigid-terminal route now has a clean empirical/theoretical split:

1. the touched braid/residual components are genuinely resident and their
   maximal deck is exactly the top-`d` rank ladder;
2. the untouched ambient factor remains nonresident;
3. maximal source letters make every deep target impossible by rank; and
4. even the diagnostic maximal candidate deck has a structured
   rotation-invariant bottom-row hole.

Therefore the next deep-compiler theorem cannot be an unnoticed support
property of the maximal rigid antecedent.  It must be a controlled
nonmaximal thinning/remote-atlas theorem coinstantiated with resident
completion.

