# The rainbow pair--triple obstruction

## Status

This note proves a purely combinatorial obstruction to a globally rainbow
intersection triangle.  It uses neither factorability, upper shadows, pinning,
nor SAT.  In particular, it refutes Gate R2 of the canonical `k=11`,
`sigma=369` maximal-shadow/reservoir branch before the twelve reservoir cells
are assigned.

It does **not** refute the bare mixed `02|03` witness schedule, a construction
that permits collisions among consecutive intersections, or the unrestricted
length-`465` problem.

## 1. General theorem

Let

\[
 C_1,C_2,\ldots,C_M\in\binom{[k]}r
\]

be distinct, and put

\[
 P_i=C_i\cap C_{i+1}\quad(1\le i<M),
 \qquad
 T_i=C_i\cap C_{i+1}\cap C_{i+2}
      =P_i\cap P_{i+1}\quad(1\le i<M-1).
\]

Assume that every `P_i` and `T_i` is nonempty and that all these masks are
pairwise distinct, including across the two depths.  Write

\[
 H=\binom{k}{r-1},\qquad G=\binom{k}{r-2},
\]

and let `h` be the number of rank-`r-1` masks absent from the pair row
`{P_i}`.

### Theorem 1

One necessarily has

\[
 \boxed{
 h\ge
 \left\lceil\frac{2H-M-G}{2}\right\rceil .}
 \tag{1.1}
\]

If a larger globally distinct nested-core family contains all the `P_i` and
`T_i` and misses only `q` masks of the whole punctured lower ideal, then
`q\ge h`, so the same lower bound holds for `q`.

### Proof

Because `C_i` and `C_{i+1}` are distinct `r`-sets, every `P_i` has rank at
most `r-1`.  Every `T_i` is contained in `P_i` but is distinct from it, so
every `T_i` has rank at most `r-2`.  The same observation shows that no still
deeper globally distinct nested core can have rank `r-1`.  Consequently, every
rank-`r-1` value attained by the nested-core family occurs in the pair row.

Exactly `H-h` pair cores have rank `r-1`.  Hence the number `ell` of lower-rank
pair cores is

\[
 \ell=(M-1)-(H-h)=M-1-H+h.                 \tag{1.2}
\]

A low pair `P_j` can spoil only the two triples `T_{j-1}` and `T_j` (with the
obvious endpoint truncation).  At least

\[
 (M-2)-2\ell=2H-M-2h                         \tag{1.3}
\]

triple cores therefore have both flanking pairs of rank `r-1`.

For such an index `i`, the distinct sets `P_i` and `P_{i+1}` are two
`(r-1)`-subsets of the common `r`-set `C_{i+1}`.  They omit different elements
of `C_{i+1}`, so

\[
 |T_i|=|P_i\cap P_{i+1}|=r-2.                \tag{1.4}
\]

The `T_i` are pairwise distinct, while there are only `G` masks of rank
`r-2`.  Thus

\[
 2H-M-2h\le G,
\]

which is equivalent to (1.1).  If the full core family misses `q` lower
masks, then in particular it misses at most `q` masks of rank `r-1`; as noted
above those masks can occur only in the pair row, so `h\le q`.  This proves
the final assertion.  QED

The estimate remains valid when the lower bound in (1.3) is negative; it is
then merely vacuous.  Boundary pairs can only reduce the number of spoiled
triples, so there is no endpoint correction missing from the proof.

## 2. Odd and even middle layers

### Odd dimension

Let `k=2m+1`, `r=m+1`, and

\[
 M=\binom{2m+1}{m+1}=\binom{2m+1}m.
\]

Then `H=M` and

\[
 G=\binom{2m+1}{m-1}=\frac{m}{m+2}M.
\]

Theorem 1 becomes

\[
 \boxed{q\ge h\ge\left\lceil\frac{M}{m+2}\right\rceil.}
 \tag{2.1}
\]

### Even dimension

Let `k=2m`, `r=m`, and `M=\binom{2m}m`.  For `m\ge2`,

\[
 H=\frac{m}{m+1}M,
 \qquad
 G=\frac{m(m-1)}{(m+1)(m+2)}M.
\]

Theorem 1 gives

\[
 \boxed{
 q\ge h\ge
 \left\lceil
   \frac{M(m-1)}{(m+1)(m+2)}
 \right\rceil.}
 \tag{2.2}
\]

The tiny cases not covered by the displayed `r-2` layer can be checked
directly.

In either parity the required deficit is

\[
 \Omega(M/k)=\Omega(2^k/k^{3/2}).             \tag{2.3}
\]

Therefore a maximal-shadow construction which insists that **all** adjacent
pair and triple cores are nonzero and globally pairwise distinct cannot leave
only a polynomial-size boundary reservoir.  It must sacrifice exponentially
many lower masks to that reservoir, or relax the global rainbow requirement.
This conclusion applies only to that specified architecture; it is not a
lower bound on `nu(k)` itself.

## 3. The canonical `k=11`, `sigma=369` branch

Here

\[
 k=11,\quad r=6,\quad M=H=462,\quad G=330.
\]

The canonical branch requires the following `1011` nontrivial cores to be
nonzero and globally pairwise distinct:

* all `461` adjacent pair intersections;
* all `460` adjacent triple intersections;
* `90` four-fold intersections.

They are all members of the `1023`-element punctured lower ideal, so their
complement has only

\[
 q=1023-1011=12                              \tag{3.1}
\]

masks.  But (2.1) requires

\[
 q\ge h\ge\left\lceil\frac{462}{7}\right\rceil=66.
 \tag{3.2}
\]

This is already a contradiction.  Equivalently, `h\le12` would leave at
least `450` rank-five pair cores and at most `11` low pairs.  At least

\[
 460-2\cdot11=438                              \tag{3.3}
\]

distinct triples would then have rank four, although only
`\binom{11}{4}=330` rank-four masks exist.

Thus no row can pass Gate R2 in
`K11_BOUNDARY_RESERVOIR_SEARCH_DESIGN.md`.  The contradiction does not need
the mixed run condition R1, upper-shadow gate R3, the reservoir bijection, or
the pin-survival test.

## 4. Stronger contradiction after reservoir order is imposed

For completeness, the proposed twelve-cell order argument is also correct.
The reservoir containment poset has exactly three maximal cells:

\[
 [1,2],\qquad[370,372],\qquad[463,465].       \tag{4.1}
\]

If two reservoir intervals are properly nested, their distinct OR labels are
strictly nested.  Since all reservoir labels have rank at most five, a
rank-five label can occur only at a maximal reservoir cell.  Hence at most
three rank-five masks are missing from the core family.

It follows that at least `459` of the `461` pairs have rank five.  The at most
two low pairs touch at most four triples, so at least

\[
 460-4=456>330                                \tag{4.2}
\]

pairwise-distinct triples have rank four.  This strengthens the numerical
contradiction, but is logically unnecessary: Section 3 already refutes the
rainbow-core gate before any reservoir labeling exists.

## 5. A stronger maximal-factor loss bound allowing collisions

The preceding contradiction assumes a globally rainbow core triangle.  For
the canonical `k=11` maximal factor one can retain arbitrary collisions and
still prove a much stronger loss than the previously known four-mask
boundary collapse.

Consider the `1023` physical cells consisting of the `1011` pair, triple,
and quadruple cores and the twelve reservoir cells.  Let

\[
 q=1023-
 \#\{\text{distinct nonempty masks of ranks }1,\ldots,5
       \text{ attained by those cells}\}.       \tag{5.1}
\]

Thus `q` counts every loss caused by a zero or rank-six value and every loss
caused by collisions.  Let

* `ell` be the number of the `461` pair positions whose value has rank at
  most four (zero included); and
* `delta_5` be the number of repeated rank-five pair occurrences, namely

  \[
  \delta_5=(461-\ell)
   -\#\{\text{distinct rank-five pair values}\}. \tag{5.2}
  \]

### Theorem 2

Every factorable maximal factor on the canonical `k=11`, `sigma=369`
schedule satisfies

\[
 \boxed{q\ge42.}                                \tag{5.3}
\]

### Proof

First consider rank five.  The pair row supplies exactly

\[
 461-\ell-\delta_5                           \tag{5.4}
\]

distinct rank-five values.  A deeper core supplies no new rank-five value:
if it has rank five, containment in a pair core forces equality with that
pair value.

The twelve maximal-factor reservoir cells supply at most three additional
distinct rank-five values.  This assertion requires the maximal-factor
collapse, not merely the fact that the reservoir poset has three maximal
elements: a nonmaximal reservoir interval could otherwise have rank five
below a rank-six container.  In the maximal factor, Proposition 3.4 of
`SINGLE_SWITCH_MAXIMAL_SHADOW_THEOREM.md` gives three monotone zones.  The
left triangle has values `A_1^max=C_1` and `A_2^max=C_1\cap C_2`, so at most
one of its distinct values has rank five.  The switch-column suffix values
form one inclusion chain, and the collapsed terminal values form another;
each chain has at most one distinct value of any fixed rank.  Hence the
reservoir contributes at most three distinct rank-five masks.

There are `462` rank-five masks in total.  Therefore

\[
 q\ge \ell+\delta_5-2.                         \tag{5.5}
\]

Now consider the `460` triple positions.  Low pairs spoil at most `2\ell`
of them.  Among the remaining adjacent high-pair positions, equality of the
two rank-five labels can occur at most `delta_5` times: for every label, a
run of `s` equal occurrences uses `s-1` of the repeat occurrences counted by
`delta_5`, and separated repetitions only make this bound looser.  Hence at
least

\[
 g=460-2\ell-\delta_5                         \tag{5.6}
\]

triples are flanked by distinct rank-five facets and consequently have rank
four.  There are only `330` rank-four masks, so these cells incur at least

\[
 \max(0,g-330)=
 \max(0,130-2\ell-\delta_5)                   \tag{5.7}
\]

duplicate occurrences.  These losses occur in triple cells and have rank
four, while the `delta_5` losses occur in pair cells and have rank five, so
they add.  Comparing the number of physical cells with the number of
distinct valid lower values gives

\[
 q\ge
 \delta_5+
 \max(0,130-2\ell-\delta_5).                  \tag{5.8}
\]

It remains only to minimize the maximum of (5.5) and (5.8) over nonnegative
integers `ell,delta_5`.  When `2ell+delta_5<130`, decreasing `delta_5` can
only help, and the two bounds with `delta_5=0` balance at

\[
 \ell-2=130-2\ell,
 \qquad \ell=44,
\]

where both equal `42`.  The neighboring integers give larger maxima.  When
`2ell+delta_5>=130`, (5.8) is `delta_5`, while (5.5) and the constraint give
a minimum of at least `63`.  Thus the global minimum is `42`, proving
(5.3).  QED

The theorem concerns the coordinatewise maximal factor.  A sparse repaired
factor can change reservoir values and shrink physical core ORs, so (5.3)
does not by itself rule out all repaired factors on the same witness
schedule.

### Theorem 3 (collision-tolerant maximal-factor bound in general)

Consider a factorable single-switch schedule at rank-count equality, with a
permutation of `M=binom(k,r)` rank-`r` central sets and delay `d>=3`.  After
the `sigma` shortened central cells are removed, Proposition 3.2 of
`SINGLE_SWITCH_MAXIMAL_SHADOW_THEOREM.md` leaves exactly

\[
 L=\sum_{s=1}^{r-1}\binom ks
\]

candidate lower cells: all feasible nontrivial meet cores and the boundary
reservoir.  Let

\[
 q=L-
 \#\{\text{distinct nonempty lower masks attained by these }L
       \text{ maximal-factor cells}\}.          \tag{5.9}
\]

Put `H=binom(k,r-1)` and `G=binom(k,r-2)`.  Then

\[
 \boxed{
 q\ge
 \max\left(0,
 \left\lceil\frac{2H-M-G-6}{3}\right\rceil
 \right).}                                     \tag{5.10}
\]

#### Proof

Let `ell` count pair cells below rank `r-1`, and let `delta` count repeated
rank-`r-1` pair occurrences.  Suppose the reservoir contributes at most `b`
distinct rank-`r-1` masks.  Deeper meet cores add no new mask of that rank,
because each is contained in a pair core and equality is the only way to
retain rank `r-1`.  The missing top-lower-rank masks therefore give

\[
 q\ge H-M+1+\ell+\delta-b.                    \tag{5.11}
\]

As in Theorem 2, at least `M-2-2ell-delta` triples are flanked by distinct
rank-`r-1` facets and hence have rank `r-2`.  Duplicate pair occurrences and
the excess of these triple cells over the `G` available rank-`r-2` masks are
disjoint cell losses.  Consequently

\[
 q\ge\delta+
 \max(0,M-2-2\ell-\delta-G)
 \ge M-2-2\ell-G.                              \tag{5.12}
\]

Dropping the nonnegative `delta` from (5.11), multiplying that inequality by
two, and adding (5.12) eliminates `ell`:

\[
 3q\ge2H-M-G-2b.                              \tag{5.13}
\]

For the single-switch maximal factor, `b<=3`.  The left reservoir triangle
collapses to one inclusion chain of values beginning at the rank-`r` set
`C_1`; the switch column is a second chain; and the terminal triangle
collapses to a third chain.  Each chain contains at most one distinct
rank-`r-1` value.  Substituting `b=3` in (5.13), taking integrality and the
trivial bound `q>=0`, proves (5.10).  QED

For the two middle-layer parities this becomes

\[
\begin{array}{ll}
k=2m+1,\ r=m+1:
 &\displaystyle
 q\ge\max\left(0,
   \left\lceil\frac{2M}{3(m+2)}-2\right\rceil\right),\\[3mm]
k=2m,\ r=m:
 &\displaystyle
 q\ge\max\left(0,
   \left\lceil
    \frac{2M(m-1)}{3(m+1)(m+2)}-2
   \right\rceil\right).
\end{array}                                    \tag{5.14}
\]

Thus a single-switch maximal factor misses

\[
 \Omega(M/k)=\Omega(2^k/k^{3/2})              \tag{5.15}
\]

lower masks even when arbitrary zero cores, repetitions, and cross-depth
collisions are allowed.  This is stronger than the earlier quadratic
boundary loss `(d-1)^2`.

Moreover, the standard boundary support `Omega` consists of three zones of
total size `O(d)`.  Only `O(d^2)` intervals of length at most `d` meet those
zones.  A central-preserving edit supported there can therefore change only
`O(d^2)` candidate lower-cell values.  In the middle-rank regime
`d=Theta(sqrt(k))`, this is polynomial, whereas (5.15) is exponential.
Consequently boundary-only repair of the maximal factor is asymptotically
impossible even without a rainbow-core assumption.

### Corollary 4 (every successful repair has large physical support)

Let `A^max` be the maximal factor of any prescribed central schedule at
length `M+d`, and suppose it misses `q` lower masks.  Every other factor `A`
realizing the same central intervals satisfies, coordinatewise,

\[
 A_j\subseteq A_j^{\max}\qquad(1\le j\le M+d). \tag{5.16}
\]

If `A` covers the entire lower ideal, then its physical modification support

\[
 \operatorname{supp}(A,A^{\max})
   =\{j:A_j\ne A_j^{\max}\}
\]

obeys

\[
 \boxed{
 |\operatorname{supp}(A,A^{\max})|
 \ge
 \left\lceil\frac{q}{\binom{d+1}{2}}\right\rceil
 =\left\lceil\frac{2q}{d(d+1)}\right\rceil.}   \tag{5.17}
\]

To prove this, choose in `A` one witness for each of the `q` lower masks
missing from `A^max`.  The rank-count interval lemma forces every such
witness to have length at most `d`: any interval of length at least `d+1`
contains a selected rank-`r` central witness and therefore has rank at least
`r`.  The chosen physical intervals are distinct because their OR-values are
different.  Each one's OR must change between `A^max` and `A`, or else its
target would not have been missing from `A^max`.

A fixed physical position belongs to at most `ell` intervals of length
`ell`, and hence to at most

\[
 \sum_{\ell=1}^d\ell=\binom{d+1}{2}           \tag{5.18}
\]

short intervals in total.  Every changed interval meets the modification
support.  A union bound therefore permits at most
`|supp(A,A^max)| binom(d+1,2)` changed short intervals, proving (5.17).

Combining Theorem 3 with `d^2=Theta(k)` in the middle-rank regime shows that
every universal factor realizing such a central schedule differs from its
maximal factor in at least

\[
 \Omega(M/k^2)=\Omega(2^k/k^{5/2})            \tag{5.19}
\]

physical positions.  This is a support-size statement; it does not by itself
prove that those positions are uniformly distributed through the word.

For `k=11`, Theorem 2 gives `q>=42` and `d=3`, so every successful factor on
the q369 central schedule must differ from its maximal factor in at least

\[
 \left\lceil42/6\right\rceil=7               \tag{5.20}
\]

positions.

### Corollary 5 (boundary-only repair is impossible)

Let

\[
\Omega=\{1,2,370,371,372,463,464,465\}.       \tag{5.21}
\]

Any edit of the maximal factor supported only on `Omega`, while retaining
the prescribed rank-six central row, still misses at least nineteen lower
masks.

Indeed, direct enumeration of the physical cores shows that exactly eleven
nontrivial core intervals meet `Omega`: one at the left boundary, seven at
the switch, and three at the terminal boundary.  They are precisely the
eleven intervals listed in (5.12) of
`K11_BOUNDARY_RESERVOIR_SEARCH_DESIGN.md`.  All twelve reservoir cells also
meet `Omega`.  Every other one of the `1023` candidate lower-cell OR-values
is unchanged by an `Omega`-supported edit.  The other `369` short cells are
the selected central triples; preserving the central row keeps their values
at rank six, so they cannot cover a lower target.

Changing one physical interval value can introduce at most one new distinct
lower mask.  Theorem 2 starts with at least `42` missing masks, and at most
`11+12=23` relevant interval values can change.  Hence at least

\[
 42-23=19                                      \tag{5.22}
\]

lower masks remain absent.  By the rank-count interval lemma, no mask below
rank six can be recovered by an interval of length four or more.  Therefore
the boundary-only/local-reservoir repair program cannot produce a universal
word.  A viable factor on this schedule would have to change positions
outside `Omega` (affecting at least nineteen additional lower-cell values),
or else abandon the prescribed central row or schedule.

This corollary does not bound the number of outside *physical positions*
that must change, because one position may lie in several short intervals.

## 6. Exact scope for the ledger

What is proved:

1. the general pair--triple deficit bound (1.1);
2. its odd and even middle-layer forms (2.1)--(2.2);
3. impossibility of the canonical `k=11` globally rainbow `1011`-core branch;
4. impossibility of polynomial-size reservoirs for the analogous all-pair,
   all-triple globally rainbow architecture in growing dimension;
5. the collision-tolerant lower bound `q>=42` for the canonical maximal
   factor;
6. impossibility of every central-preserving repair supported only on the
   eight-position boundary zone `Omega`;
7. the general collision-tolerant maximal-factor loss
   `Omega(M/k)` for every middle-rank single-switch schedule with `d>=3`,
   and hence asymptotic impossibility of polynomial-size boundary repair;
8. the physical support lower bound
   `|supp(A,Amax)|>=ceil(2q/(d(d+1)))`, which becomes `Omega(M/k^2)` in
   the middle-rank regime and gives at least seven changed positions at
   `k=11`.

What is not proved:

1. impossibility of the `02|03` monotone witness schedule itself;
2. impossibility after allowing repeated, zero, or deliberately omitted
   pair/triple cores;
3. impossibility of a mixed-delay braid using a different short-cell
   allocation;
4. `nu(11)>465`, or any new unrestricted lower bound.
