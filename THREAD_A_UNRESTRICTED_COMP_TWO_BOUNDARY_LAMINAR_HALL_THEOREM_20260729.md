# Unrestricted depth compiler: exact interval atlas and the two-boundary laminar Hall theorem

Date: 2026-07-29

Status: theorem note.  The compiler statements below are unconditional.  The
last section states exactly which of their hypotheses are supplied by PBBS and
which are not.  In particular, no all-odd existence theorem is asserted.

## 0. Verdict and theorem hierarchy

The strongest scalar statement is false: the data consisting only of
PBBS-style flag nesting together with

\[
 \sum_{s\le q}|H_s|\le 2q
\]

does not imply the unrestricted compiler.  Even two disjoint, nested-label
pins which are separately chronology-compatible can jointly erase a required
coordinate from one middle window; Proposition 2.3 gives the exact local
obstruction.

There are instead three rigorously distinct statements.

1. For a fixed chronology, Theorem 2.1 is an exact characterization of the
   unrestricted `COMP_d(T)` after one witness interval per lower target is
   chosen.
2. Upper completeness of that same `T` plus `COMP_d(T)` is the minimal
   necessary-and-sufficient fixed-chronology lemma for a universal antecedent
   with `D^dA=T`; this is Corollary 2.2.
3. PBBS flags, a two-cycle opening, a robust core, or the restriction
   `DA=DP` are wrappers which may certify the minimal lemma.  None of them is
   part of its statement, and the last restriction is not necessary.

The positive Hall theorem below fixes one robust core first.  It then reduces
the boundary part to explicit laminar/two-prefix cuts and proves integrality.
At `q=1`, capacity two is intrinsic to every unrestricted compiler.  At
larger depth, `2q` is only the capacity of the declared literal boundary
bank, not a restriction on arbitrary multi-letter witnesses.

## 1. Set-up

Let

\[
 k=2m+1,\qquad r=m+1,\qquad W={k\choose r},
\]

and let `d=d(k)` be the least integer such that

\[
 dW+{d+1\choose2}\ge \sum_{s=1}^{r-1}{k\choose s}.
\]

For odd `k`, the sum on the right is `2^(k-1)-1`, and

\[
 d(k)=\sqrt{\pi k/8}+O(1).
\]

Fix a linear Johnson path

\[
 T=(T_0,\ldots,T_{W-1}),\qquad |T_i|=r,
\]

For every finite set word `X`, write

\[
 (D^tX)_i=\bigcup_{j=0}^{t}X_{i+j}.                    \tag{1.0}
\]

Put `N=W+d`, `J={0,...,N-1}`.  Its maximal erosion envelope is

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(p,W-1)}T_i
 \qquad(p\in J).                                      \tag{1.1}
\]

Assume throughout that `T` is linearly `d`-resident: every maximal
coordinate-presence run not truncated by a global endpoint has at least
`d+1` states.  Then

\[
 D^dP=T,
 \qquad
 |P_p|=r-\delta(p),
 \qquad
 \delta(p)=\min\{d,p,N-1-p\}.                         \tag{1.2}
\]

Indeed, within at most `d` Johnson transitions no coordinate can be deleted
twice, or be inserted and then deleted: either event would create an
internal positive run of at most `d` states.  Consecutive intersections
therefore lose one fresh coordinate per transition, giving the rank formula.
Every coordinate of `T_i` has, inside its positive run, an erosion window
contributing to positions `i,...,i+d`; conversely each such erosion window
is contained in `T_i`.  This proves `D^dP=T` coordinatewise.

For `1<=q<=d`, define the left, right, and two-sided boundary banks

\[
 L_q=\{0,\ldots,q-1\},\qquad
 R_q=\{N-q,\ldots,N-1\},\qquad
 B_q=L_q\mathbin{\dot\cup}R_q.                         \tag{1.3}
\]

Thus `|L_q|=|R_q|=q` and `|B_q|=2q`; in particular `B_1` consists of
the two outer source positions, not all `2d` high-boundary positions.

## 2. Exact unrestricted interval-atlas criterion

Here `COMP_d(T)` denotes the unrestricted interface: a nonzero source word
`A=(A_p)_(p in J)` with `D^dA=T` in which every nonempty target of rank
below `r` is the union of a source interval.  No condition on `DA` is
imposed.  Every such word automatically satisfies `A_p subseteq P_p`.

For each nonempty lower target `S`, `|S|<r`, choose a nonempty source
interval `I_S` of length at most `d`.  For a coordinate `x`, put

\[
 Q_x=\{p:x\in P_p\}\setminus
      \bigcup_{\substack{S:\ |S|<r\\x\notin S}} I_S.   \tag{2.1}
\]

The intervals `I_S` are only prospective witnesses; no source word has yet
been chosen.

### Theorem 2.1 (exact atlas form of unrestricted `COMP_d(T)`)

`COMP_d(T)` is feasible if and only if intervals `I_S` can be chosen so
that

\[
 Q_x\cap[i,i+d]\ne\varnothing
 \quad(0\le i<W,\ x\in T_i),                            \tag{2.2}
\]

\[
 Q_x\cap I_S\ne\varnothing
 \quad(|S|<r,\ x\in S),                                \tag{2.3}
\]

and

\[
 \{x:p\in Q_x\}\ne\varnothing\quad(p\in J).           \tag{2.4}
\]

When these conditions hold, the coordinatewise maximal integral word

\[
 A_p=\{x:p\in Q_x\}                                    \tag{2.5}
\]

is a feasible compiler.

#### Proof

Suppose first that `A` is feasible.  Choose one witnessing interval `I_S`
for every lower target.  Since `D^dA=T`, every source letter is contained in
all middle windows using it, hence `A_p subseteq P_p`.  If `x notin S`, the
equality `union_(p in I_S) A_p=S` deletes `x` from all of `I_S`; consequently
the support of `x` in `A` is contained in `Q_x`.  The positive part of the
middle-window equalities gives (2.2), the positive part of each target
equality gives (2.3), and nonzero source letters give (2.4).

Conversely, (2.1) makes every letter in (2.5) a subset of `P_p`.  Therefore
no coordinate outside `T_i` can occur in `[i,i+d]`, while (2.2) supplies
every coordinate in `T_i`; hence `D^dA=T`.  For a lower target `S`, (2.1)
deletes every coordinate outside `S` throughout `I_S`, and (2.3) supplies
every coordinate of `S`, so the union on `I_S` is exactly `S`.  Condition
(2.4) makes the word nonzero.  These are precisely the constraints of
`COMP_d(T)`.  QED.

The theorem is an exact integral characterization.  It also explains why
there is no exact ordinary-Hall theorem for unrestricted `COMP_d(T)` before
the witness intervals are fixed: choosing `I_S` changes, simultaneously for
all coordinates, the allowed sets `Q_x` in (2.1).

Call `T` **upper-complete** if every target `U` of rank greater than `r` is
the union of a consecutive interval of `T`.

### Corollary 2.2 (minimal fixed-chronology equivalence)

Assume that `T` lists every rank-`r` target exactly once.  There is a
nonzero universal word `A` of length `W+d` with `D^dA=T` if and only if
`T` is upper-complete and the intervals in Theorem 2.1 can be chosen to
satisfy (2.2)--(2.4).  When `d=d(k)`, this proves

\[
                         \nu(k)=W+d=B(k).               \tag{2.6}
\]

#### Proof

If `T` is upper-complete, Theorem 2.1 supplies every lower target and the
equation `D^dA=T` supplies the middle layer.  If
`U=T_i union ... union T_j`, then

\[
 U=A_i\cup A_{i+1}\cup\cdots\cup A_{j+d},             \tag{2.7}
\]

so every upper target also occurs.

Conversely, Theorem 2.1 applied to the actual lower witnesses gives
(2.2)--(2.4).  If an upper target is witnessed by `A_a,...,A_b`, its interval
has at least `d+1` letters, since a shorter interval is contained in one
rank-`r` middle window.  Every source position in `[a,b]` belongs to a full
`(d+1)`-window contained in `[a,b]`; therefore

\[
 \bigcup_{p=a}^{b}A_p
   =\bigcup_{i=a}^{b-d}T_i.                             \tag{2.8}
\]

Thus `T` is upper-complete.  Finally the monotone-deadline lower bound and
the constructed length `W+d` give (2.6).  QED.

### Proposition 2.3 (nested pins do not imply common chronology)

For every `d>=2` and `r>=2d+1` there is a strongly `d`-resident Johnson
path segment and two pins whose target labels are nested, whose source
intervals are disjoint, and which are each individually feasible, but which
are infeasible together.

Choose an `r`-set `U`, distinct

\[
 a_1,\ldots,a_d,b,c_1,\ldots,c_d\in U,
\]

and fresh coordinates `alpha_1,...,alpha_d,beta_1,...,beta_d`.  Put

\[
 T_j=(U\setminus\{a_1,\ldots,a_j\})
       \cup\{\alpha_1,\ldots,\alpha_j\}
       \quad(0\le j\le d),                             \tag{2.9}
\]

and continue for `1<=s<=d` by deleting `c_s` and inserting `beta_s`.
Every positive run meets an endpoint or has at least `d+1` states, so this
segment is strongly resident.  Its left erosion satisfies

\[
 P_p=U\setminus\{a_1,\ldots,a_p\}\quad(0\le p\le d). \tag{2.10}
\]

Consider

\[
 (\{0\},S),\qquad([1,d],R),
 \qquad S=U\setminus\{b\},\quad
 R=U\setminus\{a_1,b\}.                               \tag{2.11}
\]

The first pin is individually feasible: it removes `b` only at position
zero, while `P_1` still supplies `b` to the first central window.  The
second is individually feasible: its only new negative deletion is `b` on
`[1,d]`; position zero supplies `b` to `T_0`, and the right erosion position
`i+d` supplies it to every later displayed window `T_i`.  Its positive
coordinates are already all available in `P_1`, and `r>=2d+1` keeps every
letter nonempty.  Equivalently, each pin separately passes (2.2)--(2.4).

Together the two negative intervals delete `b` from every position of
`[0,d]`, contradicting `b in T_0`.  Yet `R subset S`, the two source
intervals are disjoint (hence laminar), and the scalar q1/q2 loads are
`1<=2` and `2<=4`.  Thus neither label laminarity nor scalar boundary Hall
can replace the common central-hit test.  This is a local obstruction; a
PBBS-specific theorem could avoid it only by proving an additional global
property.

## 3. PBBS flags give exact fixed frames

Suppose `1<=q<=d` and an actual linear flag survives in `T`:

\[
 S=\bigcap_{t=0}^{q}T_{i+t}.                            \tag{3.1}
\]

Define its source frame

\[
 I(i,q)=[i+q,i+d].                                      \tag{3.2}
\]

### Lemma 3.1 (flag-to-frame identity)

For every surviving flag (3.1),

\[
 \bigcup_{p\in I(i,q)}P_p=S.                            \tag{3.3}
\]

At a fixed start `i`, the frames and labels form parallel nested chains:

\[
 I(i,q+1)\subset I(i,q),\qquad
 \bigcap_{t=0}^{q+1}T_{i+t}\subset
 \bigcap_{t=0}^{q}T_{i+t}.                              \tag{3.4}
\]

#### Proof

The linear intersection-tower identity gives

\[
 D^{d-q}P_{i+q}=\bigcap_{t=0}^{q}T_{i+t}.
\]

The left side is the union of `P_(i+q),...,P_(i+d)`, proving (3.3).
Both inclusions in (3.4) are immediate.  QED.

Thus a selected surviving PBBS flag is stronger than a marginal statement
that its value occurs: it supplies a concrete, chronology-correct interval
pin.  Cyclic support alone does not say that one such frame survives a
chosen opening.

## 4. A robust-core Hall theorem for unrestricted `COMP_d(T)`

Let `F` be a family of lower targets.  For each `S in F`, fix an interval
`I_S` of length at most `d` satisfying

\[
 \bigcup_{p\in I_S}P_p=S.                               \tag{4.1}
\]

The frames supplied by Lemma 3.1 are the intended application.  Let

\[
 \mathcal R={S:1\le |S|<r\}\setminus F               \tag{4.2}
\]

be the residual target family.

A **robust flag core** is a sequence `C=(C_p)_(p in J)` such that

\[
 C_p\subseteq P_p,                                      \tag{4.3}
\]

\[
 \bigcup_{p=i}^{i+d}C_p=T_i\quad(0\le i<W),             \tag{4.4}
\]

and

\[
 \bigcup_{p\in I_S}C_p=S\quad(S\in F).                 \tag{4.5}
\]

The core letters may be empty.  For a residual target define its literal
eligibility set

\[
 N_C(S)=\{p\in J:C_p\subseteq S\subseteq P_p\}.         \tag{4.6}
\]

Call a completion **`C`-dominating and literal on \(\mathcal R\)** when
`C_p subseteq A_p subseteq P_p` for every position and every target in
\(\mathcal R\) occurs as a source letter at a position distinct from the positions
chosen for the other residual targets.

### Theorem 4.1 (unrestricted sandwich-Hall compiler)

Fix `F`, its frames, and a robust core `C`.  There is a `C`-dominating
compiler in which every residual target is installed as a distinct literal
source letter if and only if

\[
 \left|\bigcup_{S\in X}N_C(S)\right|\ge |X|
 \qquad(X\subseteq\mathcal R).                          \tag{4.7}
\]

In particular, (4.7) is a sufficient condition for unrestricted
`COMP_d(T)`.  It is not the one-core condition `DA=DP`.

#### Proof

By Hall's theorem, (4.7) gives an injection

\[
 \phi:\mathcal R\longrightarrow J,qquad
 \phi(S)\in N_C(S).
\]

Set

\[
 A_p=\begin{cases}
 S,&p=\phi(S),\\
 P_p,&p\notin\phi(\mathcal R).
 \end{cases}                                           \tag{4.8}
\]

Then `C_p subseteq A_p subseteq P_p` at every position.  Sandwiching (4.4)
between the corresponding unions of `C`, `A`, and `P` gives `D^dA=T`.
The same argument with (4.5) and (4.1) preserves every fixed flag frame.
Every residual target occurs literally.  All source letters are nonempty:
matched letters are nonempty targets and unmatched `P_p` have rank at least
`r-d>=1`.  Hence `A` is feasible for `COMP_d(T)`.

Conversely, in any `C`-dominating literal completion, choose one literal
occurrence of each distinct residual target.  The chosen positions are
distinct, and `C_p subseteq S subseteq P_p` at such a position.  They form a
matching in (4.6), so Hall is necessary.  QED.

This theorem proves integrality twice, rather than assuming marginal
balance.  First, a core can be given coordinatewise by integral hitting
sets.  For each coordinate `x`, the requirements in (4.4)--(4.5) are line
intervals that must be hit inside `{p:x in P_p}`.  In the induced order on
the allowed positions their incidence matrix has consecutive ones and is
totally unimodular; linear optimization has an integral optimum, and the
unweighted minimum-cardinality hitting set can also be found greedily.
Second, after that *same* core is fixed, (4.7) gives an
integral target-to-position matching.  Separate fractional cores and
separate marginal target balances do not imply the existence of one common
pair `(C,phi)`.

## 5. Boundary forcing and the exact `2q` scope

For `1<=q<=d`, call a residual rank-`(r-q)` target `S` **boundary forced**
when

\[
 S\notin\operatorname{supp}(P).                         \tag{5.1}
\]

### Lemma 5.1 (literal boundary forcing)

If `S` is boundary forced of rank `r-q`, then

\[
 N_C(S)\subseteq B_q.                                   \tag{5.2}
\]

Consequently, Hall implies

\[
 \left|\bigcup_{s=1}^{q}\mathcal H_s\right|\le2q       \tag{5.3}
\]

for every family `H_s` of boundary-forced residual targets of rank `r-s`.

#### Proof

If `p notin B_q`, (1.2) gives `|P_p|<=r-q`.  The strict case makes
`S subseteq P_p` impossible.  In the equality case, containment and equal
rank force `S=P_p`, contrary to (5.1).  Thus (5.2) holds.  Since
`B_1 subset ... subset B_q` and `|B_q|=2q`, applying Hall to the union of
the first `q` defect classes proves (5.3).  QED.

The qualification "literal" is essential.  Here is an odd-dimensional
counterexample to deriving `2q` from the unrestricted antecedent equations.
Take `k=7`, relabel the ground set as `{0,...,6}`, put `r=4` and `d=q=2`,
and let

\[
 (v_0,\ldots,v_{17})=
 (1,2,3,4,1,2,5,3,1,6,2,4,5,1,6,4,3,5).               \tag{5.4}
\]

Put

\[
 T_i=\{0,v_i,v_{i+1},v_{i+2}\}\quad(0\le i<16),        \tag{5.5}
\]

and

\[
 A_p=\begin{cases}
 \{0,v_p\},&p\equiv0\pmod3,\\
 \{v_p\},&p\not\equiv0\pmod3.
\end{cases}                                           \tag{5.6}
\]

Here the local path length is `L=16` and the source length is `L+d=18`;
the erosion and antecedent identities are the same as above with `L` in
place of the full-layer length `W`.

Every repetition in (5.4) is separated by at least four positions, so every
four consecutive entries are distinct.  Its consecutive unordered triples
are, in order,

```text
123 234 134 124 125 235 135 136
126 246 245 145 156 146 346 345,
```

and are pairwise distinct.  Hence (5.5) is a simple Johnson path.
Occurrences of any nonzero coordinate in the `v`-word are separated by at
least four positions, so every internal positive run in `T` has exactly
three or more states; `T` is 2-resident.  Every three consecutive source
positions contain exactly one position congruent to zero modulo three, so

\[
 D^2A=T.                                                \tag{5.7}
\]

Every erosion letter contains coordinate `0`.  Nevertheless the six
two-letter intervals beginning at positions `1,4,7,10,13,16` realize the
six distinct rank-two targets

\[
 \{2,3\},\{1,2\},\{1,3\},\{2,4\},\{1,6\},\{3,5\}.      \tag{5.8}
\]

None belongs to `supp(P)`, and six is greater than `2q=4`.  This path is a
local antecedent counterexample, not a complete middle-layer permutation;
its role is to prove that residence plus `D^dA=T` does not impose the deeper
`2q` inequality.  Thus the deeper `2q` bounds are a sufficient
literal-boundary architecture and a necessary condition inside that
architecture, not a theorem of the unrestricted compiler interface.

The `q=1` statement is different and genuinely unrestricted.

### Lemma 5.2 (unrestricted two-channel theorem at `q=1`)

Let `A` be any antecedent with `D^dA=T`.  If a rank-`(r-1)` target `S` is
not an internal transition colour `T_i intersection T_(i+1)`, then every
witness interval for `S` starts at source position `0` or ends at source
position `N-1`.  At most one distinct such target can be witnessed on each
side.  Hence the number of missing q1 colours is at most two in every
unrestricted compiler.

#### Proof

Let `[a,b]`, of length at most `d`, witness `S`.  The middle windows
containing it have indices

\[
 K(a,b)=[\max(0,b-d),\min(a,W-1)]\cap\mathbb Z.          \tag{5.9}
\]

For every `i in K(a,b)`, `S subseteq T_i`.  If `K(a,b)` contains two
indices, it contains consecutive indices `i,i+1`; then

\[
 S\subseteq T_i\cap T_{i+1},
\]

and both sides have rank `r-1`, so `S=T_i intersection T_(i+1)`, contrary
to the hypothesis.  Thus `K(a,b)` is a singleton.  Since `b-a+1<=d`, the
only singleton cases in (5.9) are `a=0` and `b=N-1`.

All unions of intervals starting at `0` are nested as their right endpoint
moves.  Two distinct sets of the same rank cannot be nested.  Thus at most
one distinct missing q1 target uses the left side; reversal gives the same
statement on the right.  QED.

This proves why q1 capacity is exactly two, independently of one-core or
literal assumptions.  It does not extend to `q>=2`, as the preceding local
example shows.

## 6. The two-boundary laminar Hall condition

Let `H=H_1 dotcup ... dotcup H_d` be boundary-forced high targets, where
`|S|=r-q` for `S in H_q`.  Reserve `B_d` for these targets and reserve
`J\setminus B_d` for the remaining residual family `R_bulk`.

For `S in H_q`, choose integers

\[
 0\le\ell_L(S),\ell_R(S)\le q                           \tag{6.1}
\]

such that the following literal eligibilities have been checked:

\[
 \{0,\ldots,\ell_L(S)-1\}\cup
 \{N-\ell_R(S),\ldots,N-1\}\subseteq N_C(S).            \tag{6.2}
\]

Empty prefixes are allowed.  These are certified neighborhoods; any extra
edges of `N_C(S)` may be ignored.

### Lemma 6.0 (laminar-neighborhood Hall reduction)

Let `D` be a finite target family and let `E(S)` be nonempty subsets of a
unit-capacity position set.  If the distinct sets `E(S)` form a laminar
family, then a matching saturating `D` exists if and only if

\[
 \#\{S\in D:E(S)\subseteq L\}\le |L|                 \tag{6.3a}
\]

for every `L` among the distinct neighborhoods.

#### Proof

Necessity is Hall.  For arbitrary `X subseteq D`, take the
inclusion-maximal neighborhoods among `{E(S):S in X}`.  Laminarity makes
them pairwise disjoint.  Partition `X` under these maximal sets and apply
(6.3a) to each one.  Summing gives
`|X|<=|union_(S in X)E(S)|`, so Hall gives an integral matching.  QED.

Thus, if the actual PBBS/core lists `N_C(S)` (or certified sublists of them)
are laminar, Hall reduces to one load inequality per laminar node.  Nesting
of the *target labels* does not imply neighborhood laminarity; the lists
must be computed after the common core is fixed.

The union of a left prefix and a right prefix need not itself form a
laminar family.  Its special two-chain structure nevertheless has an exact
quadratic-size Hall description.

### Theorem 6.1 (two-prefix Hall theorem)

The certified boundary graph has a matching saturating `H` if and only if

\[
 \boxed{
 \#\{S\in H:\ell_L(S)\le a,\ \ell_R(S)\le b\}\le a+b
 }
 \qquad(0\le a,b\le d).                                \tag{6.3}
\]

If, in addition,

\[
 \left|\bigcup_{S\in X}
       \bigl(N_C(S)\cap(J\setminus B_d)\bigr)\right|
 \ge |X|\qquad(X\subseteq\mathcal R_{\rm bulk}),       \tag{6.4}
\]

then `COMP_d(T)` is feasible.

For a compact bulk certificate, it is enough to exhibit nonempty sublists

\[
 E(S)\subseteq N_C(S)\cap(J\setminus B_d)
 \qquad(S\in\mathcal R_{\rm bulk})                    \tag{6.4a}
\]

whose distinct values are laminar and satisfy (6.3a).  Lemma 6.0 then
implies (6.4) on this certified subgraph.  Every membership in (6.4a) is the
literal PBBS/core bit test `C_p subseteq S subseteq P_p`; no marginal or
fractional inference is used.

#### Proof

Write `L_a={0,...,a-1}` and `R_b={N-b,...,N-1}`.  In the certified graph,
the neighborhood of `S` is exactly

\[
 E(S)=L_{\ell_L(S)}\cup R_{\ell_R(S)}.
\]

Necessity of (6.3) follows because every target counted on its left has all
its certified neighbors in the `a+b` positions `L_a union R_b`.

For sufficiency, take a nonempty `X subseteq H` and put

\[
 a=\max_{S\in X}\ell_L(S),\qquad
 b=\max_{S\in X}\ell_R(S).
\]

Then `X` is contained in the family counted in (6.3), whereas

\[
 \bigcup_{S\in X}E(S)=L_a\cup R_b.
\]

Thus `|X|<=a+b=|N(X)|`; Hall gives an integral boundary matching.  Equation
(6.4) gives an integral bulk matching.  Their right shores are disjoint, so
their union is a matching of every residual target into `N_C(S)`.  Apply
Theorem 4.1.  QED.

The one-dimensional capacity statements are strict shadows of (6.3).  Since
every member of `H_1 union ... union H_q` has both prefix lengths at most
`q`, setting `(a,b)=(q,q)` gives

\[
 \sum_{s=1}^{q}|H_s|\le2q.                              \tag{6.5}
\]

At `q=1`, (6.3) gives not only `|H_1|<=2`, but also capacity one on each
individual side.  This is the exact distinction:

\[
 \text{q1: one left channel + one right channel};
 \qquad
 \text{depth q: q nested slots on each side}.           \tag{6.6}
\]

Scalar (6.5) is not sufficient.  Two q1 targets with certified types
`(ell_L,ell_R)=(1,0)` satisfy the total count `2<=2` but violate (6.3) at
`(a,b)=(1,0)`.  Concretely, with `T_0={1,2,3}`, retained facet
`P_1={2,3}`, and endpoint core `C_0={1}`, both facets `{1,2}` and `{1,3}`
are individually left-end legal, but the one left channel cannot host both.
This is the minimal obstruction to replacing full Hall by marginal balance.

## 7. How PBBS flags certify the prefix lengths

Consider the left global cut.  Suppose a cyclic depth-q flag occurrence
crossing that cut has the form

\[
 S=\bigcap_{t=-a}^{b}V_t,
 \qquad a\ge1,\ b\ge0,\ a+b=q,                          \tag{7.1}
\]

where `V_0,...,V_b` become `T_0,...,T_b` after opening.  Then

\[
 S\subseteq P_p=\bigcap_{t=0}^{p}T_t
 \qquad(0\le p\le b).                                  \tag{7.2}
\]

Therefore this one physical PBBS flag certifies

\[
 \ell_L(S)\ge b+1                                      \tag{7.3}
\]

as soon as the finitely checkable core inclusions

\[
 C_p\subseteq S\qquad(0\le p\le b)                    \tag{7.4}
\]

hold.  The right statement is obtained by reversal.  Since `a>=1`, one has
`b+1<=q`, exactly matching the bank in (6.1).  Flags sharing a cut give
nested prefixes; the resulting two-chain Hall test (6.3) has only
`(d+1)^2` inequalities.

For `q=1`, a deleted factor edge has `a=1,b=0`.  If the factor is q1-rainbow,
the deleted facet and the retained facet at that endpoint are distinct.
The unique coordinate omitted by the retained facet belongs to the deleted
facet.  For the central equations alone one may therefore take the endpoint
core to be that one coordinate and obtain a certified endpoint edge.  Extra
fixed flag frames can constrain the same core, so their compatibility still
has to be checked in item 4 below.  Subject to that common-core check, a
deleted colour on the leftmost component gets the left channel, and the
deleted colour on the rightmost component gets the right channel.  A seam
need not recycle either colour.

## 8. Dimension-uniform two-boundary compiler theorem

### Theorem 8.1 (PBBS-flag/two-boundary sufficient theorem)

Let `k=2m+1`, `1<=d(k)<r`, and suppose a q1-exact factor is opened into a
linear rank-r path `T` using at most two global boundary cuts and at most one
seam.  Suppose all of the following hold for one common opening.

1. **Residence:** `T` is linearly `d`-resident, so (1.2) holds.
2. **Upper safety:** every target of rank greater than `r` is the union of an
   arbitrary-width interval of `T`.
3. **Surviving flag atlas:** a family `F` of lower targets has concrete
   surviving flag frames satisfying (4.1).  In particular, Lemma 3.1 may be
   used for all selected depths `q<=d`.
4. **One integral robust core:** the same selected frames admit a core `C`
   satisfying (4.3)--(4.5), including any prescribed endpoint-core
   restrictions needed by the unrecycled q1 colours.
5. **Boundary two-prefix Hall:** every high residual target assigned to the
   boundary has PBBS-certified prefix lengths satisfying (6.1)--(6.3).
6. **Bulk Hall:** all other residual targets satisfy (6.4); equivalently for
   this sufficient theorem, they may be given PBBS/core-checkable laminar
   sublists satisfying (6.3a) as in (6.4a).

Then there is a nonzero word `A` of length `W+d` with `D^dA=T` which covers
every lower target.  It also covers every middle and upper target, and hence

\[
 \nu(k)=W+d=B(k).                                      \tag{8.1}
\]

#### Proof

Items 3--6 and Theorems 4.1 and 6.1 give an integral feasible solution of
`COMP_d(T)`.  Its `d`th derivative supplies every middle target.  If an upper
target is `T_i union ... union T_j`, then it is

\[
 A_i\cup A_{i+1}\cup\cdots\cup A_{j+d},
\]

so item 2 supplies all upper targets.  The word has length `W+d`; the
monotone-deadline lower bound gives equality.  QED.

The strongest nonreserved version replaces items 5--6 by the single full
Hall condition (4.7) on all residual targets.  The reserved version is
useful because the PBBS cut flags make its boundary graph two-prefix and
therefore reduce its exponentially stated Hall family to the explicit
`O(d^2)` inequalities (6.3).

## 9. Exactly what PBBS supplies, and what remains

The audited PBBS flag theorem supplies:

1. for every depth and every target value, at least one cyclic physical flag
   occurrence (with the proved multiplicity bound);
2. nested flag towers at a common occurrence, which become the nested fixed
   frames of Lemma 3.1 when they survive a linear opening;
3. crossing-cut flags which, after an orientation is fixed, certify the
   boundary-prefix containments (7.2); and
4. through the stated complement/bipartite lift, the q1-exact source deck.
   This last statement is not a claim that the raw PBBS m-set `f^2` factor
   itself is the required q1-exact rank-r factor.

PBBS does not presently supply uniformly in `m`:

1. a flag-preserving reduction to at most two components together with
   linear `d(k)`-residence;
2. an arbitrary-width upper-safe opening;
3. a simultaneous choice of surviving flag occurrences whose *same* robust
   integral core is compatible with all residual targets;
4. the two-prefix Hall inequalities (6.3) for every boundary hole; or
5. the bulk Hall condition (6.4).

In particular, cyclic all-depth support is not a compiler.  It supplies the
candidate intervals used in the theorem, but not their cut-survival,
simultaneous core, or integral target matching.  The exact k=15 certificate
verifies the unrestricted atlas criterion and the nonreserved global-Hall
form of Theorem 4.1 for one opening.  Its retained matching uses some inner
boundary positions for deep targets, so no claim is made here that it obeys
the optional `B_d` reservation of Theorem 6.1.  In either form, the finite
certificate does not prove dimension-uniform existence.

## 10. Logical boundary

The conclusions can be summarized sharply.

* Theorem 2.1 is necessary and sufficient for unrestricted `COMP_d(T)`.
* Corollary 2.2 is the minimal fixed-chronology theorem: upper completeness
  plus unrestricted `COMP_d(T)` is equivalent to a universal antecedent with
  `D^dA=T`.  PBBS, two-cycle topology, and `DA=DP` are only wrappers.
* Theorem 4.1 is necessary and sufficient in the fixed-frame,
  robust-core, literal-residual subclass, and is sufficient without any
  `DA=DP` assumption.
* Lemma 6.0 reduces Hall to one node inequality when the actual fixed-core
  target neighborhoods are laminar; PBBS label nesting alone does not meet
  that hypothesis.
* Theorem 6.1 is the exact Hall theorem for the PBBS-certified two-prefix
  boundary graph.  It proves integral allocation.
* q1 capacity two is necessary for every unrestricted compiler.
* cumulative depth-q capacity `2q` is exact for the declared literal
  boundary banks.  For `q>=2` it is not implied by the antecedent equations:
  unrestricted multi-letter witnesses can exceed it.  No deeper `2q`
  necessity theorem for full `COMP_d(T)` is asserted.
* PBBS flags make all objects in the hypotheses finite and explicit; proving
  that one opening satisfies them in every odd dimension remains the open
  theorem.
