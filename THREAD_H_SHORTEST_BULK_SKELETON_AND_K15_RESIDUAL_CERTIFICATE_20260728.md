# Gaussian interval depth is necessary for a full-ideal bulk skeleton

## Exact controller-word criterion and the frozen `k=15` residual certificate

Date: 2026-07-28

Status: unconditional controller-word equivalence, exact interval-capacity
theorem, and an imported audited finite obstruction for the frozen Hall-29
carrier.  The required rethreaded bulk skeleton is not constructed.

## 0. Outcome

A uniform non-singleton compiler for the complete lower ideal cannot be a
length-two theorem.  For any word attaining the Pascal lower-bound length
`P=W+d`, every lower target must use an interval of length at most `d`, and
the number of intervals of length at most `ell` is

\[
 N_\ell(P)=\ell P-\binom{\ell}{2}.
\]

If `sigma=dW+binom(d+1,2)-Lambda` is the arithmetic slack, the smallest
interval cap not already excluded by counting is exactly

\[
 \ell_{\rm cnt}=
 \begin{cases}
 d-1,&\sigma\ge W+1,\\
 d,&\sigma<W+1.
 \end{cases}
\]

Thus the first full-lower-ideal bulk theorem not excluded by raw cell
capacity has interval depth `d-1` or `d`, hence `Theta(sqrt(k))` on odd
dimensions.  At `k=15`,
`d=3`, `sigma=2928<W+1`, and length at most two has only `12875`
cells for `16383` lower targets.  Length three is arithmetically mandatory.
More sharply, every selected lower-target witness system uses at least
`3508` length-three cells.

The frozen Hall-29 carrier gives a sharper finite obstruction.  Degree-one
peeling selects 1,489 noncolliding target--cell pairs; after those pairs are
reserved, the conditional residual graph has 35 targets and only six cells.
Every one of those cells has length three, and each has exactly two nested
candidate targets.  Hence:

* no residual target can be installed on an *unreserved* singleton or
  length-two cell while the selected pairs and carrier are fixed;
* a fixed controller word can realize at most six of the 35 residual
  targets; and
* any repair preserving the peeled architecture must unlock at least 29
  further distinct physical cell addresses.

Choosing controller pairs cannot unlock them: the residual graph is the
exact maximal candidate graph after those reservations.  More strongly,
before peeling there is a 1,524-target shore with only 1,495 candidate
cells.  Thus this carrier is a literal counterexample to any postprocessing
theorem purporting to complete it without changing its candidate graph.  A
positive theorem must make new exact cell addresses eligible, for example
by rethreading the carrier chronology, and then construct the common
controller word.  It is not enough to solve another matching problem on the
old cells.

## 1. Exact bulk-plus-terminal controller-word theorem

Let `P` be a linearly ordered source-position set.  A physical cell `c` has
an interval `I_c subseteq P`; let `C_ell` be the available, unreserved cells
of length at most `ell`.  At each position `p`, let `E_p` be the fixed
maximal envelope.  Let
`F` be the fixed owner labels with their active intervals, let `P_0` be the
fixed protected pairs `(L,J_L)`, and let `R` be a family of pairwise distinct
residual subset targets.

A **bulk-terminal controller word of cap `ell`** consists of:

1. one eligible cell `c_S in C_ell` for every `S in R`;
2. nonempty traces `Q_p subseteq E_p`;
3. at most two active controller labels `Gamma_p` at each position; and
4. the partition

   \[
    R_{\rm term}=\{S:|I_{c_S}|=1\},
    \qquad R_{\rm bulk}=R\setminus R_{\rm term},
   \]

such that:

\[
 Q_p=E_p\cap\bigcap_{L\in\Gamma_p}L,
 \tag{1.1}
\]

every controller in `Gamma_p` is active at `p`, every other fixed or
residual owner active at `p` contains `Q_p`, and

\[
 \bigcup_{p\in J_L}Q_p=L
 \qquad((L,J_L)\in P_0),
 \tag{1.2}
\]

\[
 \bigcup_{p\in I_{c_S}}Q_p=S
 \qquad(S\in R).
 \tag{1.3}
\]

Eligibility includes every fixed-carrier envelope, mandatory-coordinate,
and deadline condition.  In particular, if a residual target is used as a
controller at `p`, then `p in I_(c_S)`.

### Theorem 1.1 (exact bulk-terminal criterion)

A trace-two residual extension using cells of length at most `ell` exists if
and only if a bulk-terminal controller word of cap `ell` exists.

For a fixed word `(Q_p)`, the cells selected for distinct residual targets
are automatically distinct.  Moreover `M_p=Q_p` is one common private
reserve on all positions, and every terminal target satisfies

\[
 Q_p=S\qquad\text{at its singleton position }p.
 \tag{1.4}
\]

Thus, once targetwise existence of an available eligible realizing cell is
verified, no cross-target Hall competition remains after the word is fixed.

#### Proof

Given a trace-two extension, take `Q_p` to be its actual meet and choose at
most two active owners generating that meet.  The fixed and residual
equalities give (1.2)--(1.3), and controller activity gives the footprint
condition.  This constructs the word.

Conversely, every active owner contains `Q_p`, while the active controllers
in (1.1) have intersection with `E_p` exactly `Q_p`.  Hence the meet of all
active owners is `Q_p`, is nonempty, and has owner dimension at most two.
Equations (1.2)--(1.3) give every protected and residual equality.

If two distinct targets selected the same cell, (1.3) would make both equal
to the unique union of `Q_p` on that interval, a contradiction.  Hence cell
injectivity is automatic; this is the right-degree-one collapse.  Finally
`M_p=Q_p` is nonempty and satisfies every protected union by (1.2) and every
residual union by (1.3), while a singleton instance of (1.3) is exactly
(1.4).  \(\square\)

The theorem is an equivalence, not an existence result.  Its value is that
it specifies the shortest possible new object: one interval-union word with
bounded controller dimension and a terminal singleton reserve.  There is no
separate residual Hall theorem after it is built.

The following normal form separates the genuinely non-singleton choice from
the terminal absorber.

### Theorem 1.2 (exact exposed-bulk/terminal-reserve normal form)

Partition `R=R_bulk disjoint-union R_term`.  Choose distinct available,
base-eligible cells

\[
 \psi(S),\quad 2\le |I_{\psi(S)}|\le\ell
 \qquad(S\in R_{\rm bulk}),
\]

and distinct available singleton cells `phi(T)={p(T)}` for
`T in R_term`, disjoint from the bulk cells.  Define the exposed bulk core

\[
 B_p=E_p
 \cap\bigcap_{F:p\in I_F}F
 \cap\bigcap_{S\in R_{\rm bulk}:
                    p\in I_{\psi(S)}}S.
 \tag{1.5}
\]

Let `kappa_bulk(p)` be the least number of active fixed or bulk labels whose
meet with `E_p` equals `B_p`, and put

\[
 H_{\rm bulk}=\{p:\kappa_{\rm bulk}(p)>2\}.
\]

Then these choices extend to a trace-two residual word if and only if there
are nonempty reserves `M_p subseteq B_p` satisfying all five conditions:

1. for every fixed protected pair,

   \[
    \bigcup_{p\in J_L}M_p=L;
    \tag{1.6}
   \]

2. for every bulk target,

   \[
    \bigcup_{p\in I_{\psi(S)}}M_p=S;
    \tag{1.7}
   \]

3. every terminal target obeys

   \[
    M_{p(T)}\subseteq T\subseteq B_{p(T)};
    \tag{1.8}
   \]

4. every exposed hot position is terminal-used:

   \[
    H_{\rm bulk}\subseteq\{p(T):T\in R_{\rm term}\};
    \tag{1.9}
   \]

5. final protected containment holds: if `p in J_L`, then
   `B_p subseteq L` when `p` is not terminal-used, whereas the matched
   terminal target `T subseteq L` when `p=p(T)`.

The final controller word is forced by these data:

\[
 Q_p=
 \begin{cases}
 T,&p=p(T),\\
 B_p,&p\notin\{p(T):T\in R_{\rm term}\}.
 \end{cases}
 \tag{1.10}
\]

#### Proof

For necessity, start from an extension using the prescribed cells, so its
singleton-assigned targets are exactly the prescribed `R_term`.  Remove
those singleton owners when forming (1.5).  At a terminal position the
actual meet is `B_p cap T`, but
the singleton target equality says it is `T`; hence `T subseteq B_p`.  At
every other position the actual meet is `B_p`.  Set `M_p=Q_p`.  Fixed and
bulk equalities give (1.6)--(1.7), terminal containment gives (1.8), and
trace two away from terminal positions gives (1.9).  A final entry on a
protected window lies in its protected label, which is exactly Condition 5.

Conversely, install the chosen bulk and terminal owners.  At `p(T)`, (1.8)
gives the actual meet `B_p cap T=T`; elsewhere it is `B_p`.  Thus it is the
word (1.10) and is nonempty.  A terminal meet is generated by its one
singleton owner.  Off the terminal image, (1.9) gives
`kappa_bulk(p)<=2`.  Condition 5 gives the upper containment of every fixed
protected union, while `M_p subseteq Q_p` and (1.6) give the reverse
containment.  On a bulk interval, activity gives `Q_p subseteq S`, while
(1.7) supplies the reverse union containment.  Terminal equality is
`Q_(p(T))=T`.  Hence all protected and target equalities hold with owner
dimension at most two.  \(\square\)

Condition 5 is intentionally asymmetric.  Requiring `B_p subseteq L` also
at a terminal-used position would be sufficient but not necessary: the
singleton owner may remove `B_p setminus L`.  Once the bulk choice is fixed,
Theorem 1.2 leaves precisely one common-reserve, hot-saturating terminal
singleton problem; after targetwise realizing cells are verified and the
resulting word is fixed, right-degree one eliminates every cross-target Hall
question.  Here `(M_p)` is one common lower reserve for all protected and
bulk windows; the final reserve is `(Q_p)`.  At a terminal position one only
needs `M_(p(T)) subseteq T`, not equality.

There is also an exact coordinate form of the terminal obstruction.  For a
required pair `(K,I_K)` (either a protected pair or one of the chosen bulk
pairs) and `x in K`, put

\[
 P^b_{K,x}=\{p\in I_K:x\in B_p\},
 \qquad
 D_x=\{p(T):x\notin T\}.
 \tag{1.11}
\]

### Corollary 1.3 (private-hit falsifier)

Fix the bulk cells and a terminal injection satisfying
`T subseteq B_(p(T))`, the hot-position condition (1.9), and the containment
part of Condition 5.  Then the forced word (1.10) satisfies every protected
and bulk union equality if and only if

\[
 P^b_{K,x}\not\subseteq D_x
 \qquad\text{for every required }(K,I_K)\text{ and every }x\in K.
 \tag{1.12}
\]

Thus a single pair `(K,x)` for which (1.12) fails is a finite certificate
that the proposed bulk-plus-terminal word has destroyed a necessary private
hit.

#### Proof

Before the terminal owners are installed, the positions of `I_K` carrying
`x` are exactly `P^b_(K,x)`.  A terminal owner removes `x` from that exposed
bulk support exactly at the positions in `P^b_(K,x) cap D_x`; it cannot
introduce `x`, because `T subseteq B_(p(T))`.
Hence `x` occurs in the final union on `I_K` exactly when
`P^b_(K,x) setminus D_x` is nonempty.  Condition (1.12) therefore says that
every coordinate of `K` survives.  The assumed containment prevents any
coordinate outside `K`, so the final union is exactly `K`.  This argument is
reversible.  \(\square\)

Corollary 1.3 tests a terminal injection *after* it is proposed.  The
stronger constructive interface sought below is to choose one reserve
`(M_p)` already satisfying (1.6)--(1.7), and then find an injection that
contains that same reserve at every terminal position.

That interface is exactly the earlier private-reserve matching theorem,
with one additional compulsory-position cut.  Fix the bulk cells and a
nonempty reserve `(M_p)`, with `M_p subseteq B_p`, satisfying
(1.6)--(1.7), and let `U` be the available singleton positions.  Join a
terminal target `T` to `p in U` only when its singleton cell is
base-eligible for `T` (including every envelope, mandatory-coordinate, and
deadline condition), when

\[
 M_p\subseteq T\subseteq B_p
 \tag{1.13}
\]

and, for every protected pair `(L,J_L)` with `p in J_L`, also `T subseteq
L`.  Let `H subseteq U` consist of positions at which either
`kappa_bulk(p)>2` or `B_p` violates one of the protected containments active
there.  Assume every position outside `U` is already trace-two and satisfies
all its protected containments.

### Proposition 1.4 (exact terminal matching after a common reserve)

The fixed bulk skeleton and reserve extend through the prescribed terminal
family if and only if the compatibility graph (1.13) has a matching which
saturates every terminal target and uses every position of `H`.
Equivalently, writing `N(X)` for the neighbourhood of a target family `X`,
one needs exactly

\[
 |N(X)|\ge |X|,
 \qquad
 |N(X)\cap H|\ge |X|+|H|-|R_{\rm term}|
 \tag{1.14}
\]

for every `X subseteq R_term` (together with the evident
`|H|<=|R_term|<=|U|`).

#### Proof

A compatible matched target makes the final entry at `p` equal to `T` and
still contains `M_p`; an unmatched position keeps `B_p` and also contains
`M_p`.  Therefore the one reserve continues to certify every equality
(1.6)--(1.7).  The definition of `H` says exactly which positions cannot be
left unmatched.  This proves the first equivalence by Theorem 1.2.

For the cut form, add `|U|-|R_term|` dummy left vertices, each adjacent to
every vertex of `U setminus H` and to no vertex of `H`.  A perfect matching
of the augmented balanced graph is exactly a target-saturating matching
using all of `H`.  Hall shores with no dummy give the first inequality in
(1.14); shores containing all dummies give the second, and smaller dummy
shores are weaker.  If `|U|=|R_term|`, there are no dummies, but the second
inequality follows from the first because
`|N(X) setminus H|<=|U setminus H|=|R_term|-|H|`.  \(\square\)

For completeness, the weighted normalized-matching certificate now has a
precise role.  Partition `R_term` by rank, put

\[
 n_{p,t}=|\{T\in R_{\rm term}:|T|=t,\ T\sim p\}|,
\]

and suppose nonnegative numbers `lambda_(p,t)` vanish when `n_(p,t)=0` and
satisfy

\[
 \sum_t\lambda_{p,t}\le1,
 \qquad
 \sum_{p:T\sim p}\frac{\lambda_{p,|T|}}{n_{p,|T|}}\ge1
 \quad(T\in R_{\rm term}).
 \tag{1.15}
\]

Giving an eligible edge `(T,p)` weight
`lambda_(p,|T|)/n_(p,|T|)` gives every target total weight at least one and
every position total weight at most one.  Trim incident weights at any
target whose total exceeds one; position loads only decrease.  Bipartite
integrality then produces an integral matching.  Thus (1.15) completes the
terminal round when `H` is empty.  When `H` is nonempty, (1.15) alone does
not in general certify compulsory-`H` coverage: the second cut in (1.14),
or the analogous fractional certificate on the dummy-augmented graph, is
additionally necessary.  This is the exact boundary of the
normalized-matching method.

## 2. Exact interval-depth capacity

Return to the Pascal package notation

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W=\binom{k}{r},
 \qquad \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},
\]

and let `d` be least with

\[
 \Lambda\le dW+\binom{d+1}{2}.
 \tag{2.1}
\]

The Pascal lower-bound target length is

\[
 P=W+d.
\]

### Lemma 2.1 (general short-band theorem)

Let a word of length `P=W+d` cover all `W` distinct rank-`r` targets.  Then
every interval of length `d+1` contains a selected rank-`r` witness.
Consequently every interval whose union has rank below `r` has length at
most `d`.

#### Proof

Choose one witnessing interval for each rank-`r` target.  Their left
endpoints are pairwise distinct: two intervals with the same left endpoint
are nested, so their unions are nested; equal rank would force equal targets.
The same argument makes their right endpoints pairwise distinct.

Fix an interval `I` of length `d+1` and suppose it contains none of the `W`
selected witnesses.  Assign to each witness its left endpoint when that
endpoint lies strictly before `I`; otherwise assign its right endpoint,
which must lie strictly after `I`.  Pairwise endpoint distinctness makes
this assignment injective.  But the number of endpoint positions strictly
outside `I` is

\[
 P-(d+1)=W-1,
\]

too small for `W` witnesses.  This contradiction proves the first claim.
Every interval of length at least `d+1` contains a length-`d+1` subinterval,
whose union contains a rank-`r` witness; it therefore cannot have lower
rank.  \(\square\)

### Lemma 2.2 (cell count)

A word of length `P` has exactly

\[
 N_\ell(P)=\sum_{j=1}^{\ell}(P-j+1)
 =\ell P-\binom{\ell}{2}
 \tag{2.2}
\]

contiguous cells of lengths `1,...,ell`.

In particular,

\[
 N_d(W+d)=dW+\binom{d+1}{2}.
 \tag{2.3}
\]

#### Proof

There are `P-j+1` intervals of length `j`; summing proves (2.2).  Substitute
`P=W+d` and simplify to get (2.3).  \(\square\)

Define the arithmetic slack

\[
 \sigma=dW+\binom{d+1}{2}-\Lambda.
 \tag{2.4}
\]

For `d>=1`, minimality of `d` gives the exact range

\[
 0\le \sigma\le W+d-1.
 \tag{2.5}
\]

For `d=0` the same range is immediate.

### Theorem 2.3 (exact raw-cell threshold)

Assume `d>=2`.  Let `ell_cnt` be the least `ell` for which the number of
physical cells of length at most `ell` is at least the number `Lambda` of
distinct lower targets.  Then

\[
 \boxed{
 \ell_{\rm cnt}=
 \begin{cases}
 d-1,&\sigma\ge W+1,\\
 d,&\sigma<W+1.
 \end{cases}}
 \tag{2.6}
\]

Consequently every bulk-terminal theorem whose selected bulk and terminal
occurrences are responsible for the complete `Lambda`-target lower ideal in
a length-`P` package must permit interval length at least `ell_cnt`.  This is
necessary only; the count does not construct a controller word.  For a
proper residual family after fixed cells have been reserved, the analogous
threshold must instead be computed from its unreserved eligible cells.

#### Proof

By (2.2)--(2.4),

\[
 N_{d-1}(W+d)=N_d(W+d)-(W+1)
 =\Lambda+\sigma-(W+1).
 \tag{2.7}
\]

Thus length `d-1` has enough cells exactly when `sigma>=W+1`.

It remains to exclude `d-2`.  Minimality of `d` in (2.1) gives

\[
 \Lambda>(d-1)W+\binom d2.
 \tag{2.8}
\]

A direct calculation from (2.2) gives

\[
 \left((d-1)W+\binom d2\right)-N_{d-2}(W+d)
 =W+3-d>0.
 \tag{2.9}
\]

Indeed `d<=r-1`, since `(r-1)W>=Lambda`, and `W>=r`, so the last quantity
is positive.  Equations (2.8)--(2.9) show
`N_(d-2)(W+d)<Lambda`.  Together with (2.3) and (2.7), this proves (2.6).
\(\square\)

The slack range (2.5) follows from the same minimality inequality (2.8):
subtracting it from the left side of (2.4) gives `sigma<W+d`, and `sigma`
is an integer.

### Theorem 2.4 (mandatory row census)

Choose one witnessing cell for every one of the `Lambda` distinct lower
targets, and let `n_j` be the number chosen from the row of physical
intervals of length `j`.  Then, for every `1<=j<=d`,

\[
 n_j\ge \bigl(P-j+1-\sigma\bigr)_+.
 \tag{2.10}
\]

In particular, any bulk-terminal decomposition of the entire lower ideal
has at least `P-sigma` terminal singleton targets.

#### Proof

Lemma 2.1 puts every chosen lower witness among the `N_d(P)` short cells.
Distinct targets require distinct cells, so exactly

\[
 N_d(P)-\Lambda=\sigma
\]

short cells are not selected.  The length-`j` row contains `P-j+1` cells;
at most all `sigma` unselected cells can lie in that row.  This proves
(2.10).  For `j=1`, every selected cell is a singleton target occurrence,
which proves the final assertion.  \(\square\)

For odd `k`, the exact identity `Lambda=2^(k-1)-1` and the central-binomial
estimate give

\[
 d=\sqrt{\frac{\pi k}{8}}+O(1).
\]

Indeed `Lambda/W=sqrt(pi k/8)+O(k^(-1/2))`, and the definition of `d` gives
the exact sandwich

\[
 \frac{\Lambda}{W}-\frac{\binom{d+1}{2}}{W}
 \le d\le\left\lceil\frac{\Lambda}{W}\right\rceil.
\]

The upper bound makes `d=O(sqrt(k))`, so the quadratic correction divided by
`W` is exponentially small.  Hence `d=Lambda/W+O(1)`.  The shortest
arithmetically possible bulk theorem has Gaussian interval depth.  Any
fixed length cap, including length two, is eventually impossible.

### Corollary 2.5 (`k=15` requires length three)

For `k=15`,

\[
 r=8,\quad W=6435,\quad \Lambda=16383,\quad d=3,
\]

\[
 N_2(W+d)=2\cdot6438-1=12875<16383,
\]

while

\[
 N_3(W+d)=19311,
 \qquad \sigma=19311-16383=2928<6436=W+1.
\]

Thus no length-6,438 `k=15` compiler, regardless of carrier, can cover the
lower ideal using only singleton and length-two cells.  Length three is
mandatory.
Moreover Theorem 2.4 gives the simultaneous row bounds

\[
 n_1\ge3510,\qquad n_2\ge3509,\qquad n_3\ge3508.
 \tag{2.11}
\]

Thus a full bulk-terminal decomposition at `k=15` must leave at least 3,510
distinct singleton targets in its terminal round.  This full-package census
must not be reapplied to the already peeled 35-target Hall-29 residual.
\(\square\)

## 3. Frozen Hall-29 residual certificate

The following finite data are imported from the audited proof artifact

`scratch/k15_h29_one_owner_cia_audit.json`,

for carrier hash

`5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c`.

The degree-one peeling theorem selects 1,489 noncolliding target--cell owner
pairs, which the conditional peeled architecture reserves.  The remaining
target set is

\[
\begin{split}
R_{29}=\{&89,311,449,960,1103,1920,2420,2575,2676,2932,4213,\\
&4877,4909,5801,6308,7504,8217,8218,9524,9588,10868,\\
&13616,13620,16422,17683,17738,18272,18970,19568,20516,\\
&21641,21779,24610,27760,29776\}.
\end{split}
 \tag{3.1}
\]

It has 35 targets, with rank histogram

\[
 9\text{ of rank }4,\quad1\text{ of rank }5,\quad
 17\text{ of rank }6,\quad8\text{ of rank }7.
\]

Its exact residual adjacency is the following complete table; targets not
listed in the right column are isolated.  The start is zero-based in the
source word.

\[
\begin{array}{c|c|c|c}
\text{cell}&\text{start}&\text{length}&\text{candidate targets}\\ \hline
15899&3024&3&2420,2932\\
16597&3722&3&4877,4909\\
18079&5204&3&17683,21779\\
18088&5213&3&2676,10868\\
18090&5215&3&9524,9588\\
18985&6110&3&19568,27760
\end{array}
 \tag{3.2}
\]

Before peeling, the corresponding Dulmage--Mendelsohn shore has 1,524
targets and only 1,495 candidate cells.  Thus its Hall deficiency is already
29.  Peeling preserves matching feasibility and exposes exactly the same
deficiency as the 35-versus-6 kernel (3.2).

### Theorem 3.1 (reserved Hall-29 kernel obstruction)

Keep the Hall-29 carrier and reserve its 1,489 peeled owner pairs.
Then:

1. no target in `R_29` has an eligible *unreserved* singleton or length-two
   cell;
2. every bulk-terminal controller word has at most six realized residual
   targets; and
3. completing the residual family requires at least 29 additional distinct
   eligible cell addresses outside the six in (3.2).

#### Proof

The depth column of the audited artifact is two for every cell in (3.2), so
each interval has length three.  The table is the complete residual
adjacency after the reserved pairs are removed, proving the first assertion.

For a fixed controller word, one physical cell has the one value

\[
 \bigcup_{p\in I_c}Q_p.
\]

It can therefore realize at most one of its two displayed candidates.  This
is exactly the right-degree-one theorem.  Six cells realize at most six
distinct residual targets.  Since `|R_29|=35`, at least 29 further distinct
eligible cells are necessary.  The fixed graph has none, proving the final
claim.  \(\square\)

### Theorem 3.2 (unconditional fixed-candidate-graph cut)

Even if the 1,489 reservations are released, the unchanged Hall-29
candidate graph admits no injective target--cell assignment on the audited
shore.  Any repair of that same 1,524-target shore must make at least 29
cell addresses outside its old 1,495-cell neighbourhood newly eligible.

#### Proof

The full shore has 1,524 targets and neighbourhood size 1,495, so Hall's
inequality fails by 29.  Releasing the peeled reservations merely returns
this full graph.  If fewer than 29 cells outside its old neighbourhood
become eligible, the repaired neighbourhood still has size below 1,524.
\(\square\)

The scope of Theorem 3.2 is every owner/controller assignment on this fixed
carrier whose occurrences obey the audited necessary local eligibility
predicate.  It does not rule out a rethreaded carrier or another physical
model that changes that predicate and hence the candidate graph.

### Corollary 3.3 (what must change at `k=15`)

No choice of controller pairs or private reserve on the frozen Hall-29 word
can repair its deficiency while leaving the candidate graph unchanged.  A
successful nearby construction must change that graph, for example by
rethreading the middle carrier.  Releasing or replacing only the peeled
owner reservations is not an escape.  If the 1,489 pairs are preserved, at
least 29 additional unreserved exact cells beyond (3.2) are needed; even if
they are released, at least 29 cells outside the old full-shore
neighbourhood must become eligible.  The one-defect near-cell atlas is only
a sufficient-only list of possible future carrier edits and is not itself a
completion theorem.

#### Proof

The exact candidate predicate is necessary for every owner assignment on
this fixed carrier: it encodes the maximal envelope, mandatory middle
private hits, and per-position nonemptiness.  Table (3.2) exhausts the
unreserved residual predicate, while Theorem 3.2 handles the full graph.
Therefore changing only controller selection or reservations cannot evade
the two cuts.  The remaining statements follow from Theorems 3.1--3.2.
\(\square\)

## 4. The shortest surviving replacement theorem

The preceding results isolate the next statement without a hidden Hall
quantifier.

### Open Lemma 4.1 (Gaussian-depth bulk controller word)

For every `k`, construct a Pascal carrier, select one occurrence of each of
the complete `Lambda` lower targets, and partition those selected
occurrences into a non-singleton bulk and a singleton terminal round.  The
resulting bulk-terminal controller word has cap

\[
 \ell\in\{d-1,d\},\qquad \ell\ge\ell_{\rm cnt},
\]

such that:

1. all natural flag pins and labelled spills remain protected;
2. the interval unions on lengths `2,...,ell` realize the non-singleton bulk
   part of the lower ideal;
3. the traces `Q_p` are generated by at most two active owner labels and
   every controller footprint lies in its selected occurrence; and
4. the exposed bulk cores admit one nonempty lower reserve `(M_p)` satisfying
   (1.6)--(1.7), and the remaining singleton targets admit the
   hot-saturating compatibility matching of Proposition 1.4.  The final
   word contains this reserve everywhere; at a terminal position
   `M_p subseteq Q_p=T`, rather than necessarily `M_p=Q_p`.

At `k=15`, a repair retaining the 1,489 peeled reservations needs at least
35 unreserved residual addresses, hence at least 29 beyond (3.2).  Any
repair of the same 1,524-target shore, even after releasing the
reservations, must make at least 29 addresses outside the old 1,495-cell
full-shore neighbourhood newly eligible.

Open Lemma 4.1 is not proved.  Theorem 2.3 shows that its Gaussian interval
depth is arithmetically minimal among full-ideal length-`P` packages, and
Theorems 3.1--3.2 show that it cannot be a postprocessing theorem for the
unchanged Hall-29 candidate graph.  It requires a carrier and controller
word designed together.

## 5. Proved/conditional boundary

Unconditional conclusions are:

1. Theorem 1.1 is an exact word-level equivalence and includes the
   right-degree-one collapse and common terminal reserve.
2. The raw-cell counting threshold for a complete lower-ideal witness
   system is `d-1` or `d`, decided by the exact arithmetic slack.  Conditional
   on a length-`P` universal word, its actual full-system cap lies between
   `ell_cnt` and `d`; arithmetic alone does not construct cap `d-1` in the
   high-slack case.  This scale is `Theta(sqrt(k))` on odd dimensions.
3. Every length-6,438 `k=15` compiler must use length-three lower cells.
4. The audited frozen Hall-29 graph rules out completion of this carrier by
   any postprocessing that leaves its candidate graph unchanged.  It forces
   29 additional distinct unreserved eligible addresses beyond the six if
   the peeled pairs are retained, and 29 newly eligible addresses outside
   the old full-shore neighbourhood even if they are released.

No rethreaded carrier, Gaussian-depth controller word, Hall-zero `k=15`
compiler, or proof of `nu(k)=B(k)` is claimed.
