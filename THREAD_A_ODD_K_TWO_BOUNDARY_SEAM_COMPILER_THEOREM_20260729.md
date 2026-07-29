# Two-boundary seam/compiler theorem for odd dimensions

Date: 2026-07-29

Status: unconditional reduction theorem, with an independently verified
`k=15` instance.  The theorem does not assert that its seam and compiler
hypotheses hold for every odd dimension.

## 0. Result and scope

The exact `k=15` word reveals a dimension-independent mechanism.  A
two-component middle-layer factor may be opened and joined by a seam which
recycles neither deleted lower-`q=1` colour.  The two deleted colours are
locally admissible at the two outer letters of the maximal erosion and can be
installed there when the common omission compiler is feasible.  This removes
the old requirement that the seam itself repair one cut colour.

The endpoint installation is only one part of the proof.  For a general odd
dimension one must still prove all three of the following for the same
oriented seam:

1. linear depth-`d` residence and exact middle ownership;
2. arbitrary-width upper coverage after the two cyclic components are cut;
3. feasibility of one integral lower compiler with its adjacent omission
   equations.

The theorem below proves that these hypotheses are sufficient for
`nu(k)=B(k)`, gives an exact 0--1 characterization of the declared compiler,
and proves that the two lower-`q=1` cut colours have no intrinsic endpoint
obstruction.

## 1. Parameters and derivative notation

Let

\[
 k=2m+1,\qquad r=m+1,\qquad W={k\choose r},
\]

and put

\[
 \Lambda=\sum_{s=1}^{r-1}{k\choose s}.
\]

Let `d=d(k)` be the least nonnegative integer for which

\[
 \Lambda\le dW+{d+1\choose2},
 \qquad B(k)=W+d.                                      \tag{1.1}
\]

For a finite set word `X=(X_0,...,X_(L-1))`, define

\[
 (D^tX)_i=\bigcup_{j=0}^{t}X_{i+j}
 \qquad(0\le i<L-t).                                  \tag{1.2}
\]

Write `supp(X)` for the set of distinct values occurring in `X`.  The
monotone-deadline theorem gives unconditionally

\[
                         \nu(k)\ge B(k).                \tag{1.3}
\]

Throughout the construction theorem assume

\[
                         1\le d<r,
 \qquad h=r-d\ge1.                                     \tag{1.4}
\]

The condition `h>=1` guarantees that maximal unassigned source letters are
nonempty.  Odd dimensions with `d=0` are outside this seam formulation and
must be handled separately.

## 2. Linear residence and maximal erosion

Let

\[
 T=(T_0,\ldots,T_{W-1})                                \tag{2.1}
\]

be a linear ordering of all rank-`r` subsets of `[k]`, with consecutive
terms adjacent in `J(k,r)`.  Thus

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.                 \tag{2.2}
\]

Call `T` strongly `d`-resident if every maximal interval of state indices on
which a coordinate is present, unless truncated by a global endpoint, has at
least `d+1` states.  Define its
maximal depth-`d` erosion `P=(P_0,...,P_(W+d-1))` by

\[
 P_j=\bigcap_{i=\max(0,j-d)}^{\min(W-1,j)}T_i.          \tag{2.3}
\]

### Lemma 2.1 (erosion identity and exact boundary profile)

If `T` is strongly `d`-resident, then

\[
                         D^dP=T,                        \tag{2.4}
\]

and

\[
 |P_j|=r-\min\{d,j,W+d-1-j\}.                          \tag{2.5}
\]

Consequently the rank profile of `P` is

\[
 r,r-1,\ldots,h+1,
 \underbrace{h,\ldots,h}_{W-d\text{ entries}},
 h+1,\ldots,r-1,r.                                     \tag{2.6}
\]

There are exactly `2d` cells of rank greater than `h`, but only two
outermost cells of rank `r`.

#### Proof

In any block of at most `d` transitions, the deleted coordinates are
distinct and no later deleted coordinate was inserted earlier in the same
block.  Otherwise a coordinate would be reinserted and deleted again within
at most `d` transitions, producing a positive run of length at most `d`.
Hence an intersection across `q+1` consecutive carrier states, `q<=d`,
loses exactly `q` distinct elements of its first state.  The number of
transitions in (2.3) is

\[
 \min\{d,j,W+d-1-j\},
\]

which proves (2.5) and (2.6).

Every \(P_j\) appearing in \((D^dP)_i\) is contained in \(T_i\), so
\((D^dP)_i\subseteq T_i\).  Conversely, fix \(x\in T_i\).  The positive run of
\(x\) containing \(i\) either meets a global endpoint or contains at least
`d+1` states.  It therefore contains a (possibly endpoint-truncated)
intersection interval from (2.3) which contains `i`.  For its right endpoint
\(j\in[i,i+d]\), one has \(x\in P_j\).  Hence \(x\in(D^dP)_i\), proving (2.4).
\(\square\)

For the theorem one may replace strong residence by the conclusions
(2.4)--(2.6).  They are a convenient checkable erosion package, not a
minimal hypothesis: Theorem 4.1 itself uses only `D^dP=T` and nonemptiness of
the unassigned default cells.

### Lemma 2.2 (linear intersection tower)

Under the hypotheses of Lemma 2.1, for `0<=t<=d` and
`0<=i<W+d-t`,

\[
 (D^tP)_i=
 \bigcap_{a=\max(0,i+t-d)}^{\min(W-1,i)}T_a.             \tag{2.7}
\]

In particular every rank-`(r-1)` value in a positive row below `T` is the
intersection colour of two consecutive terms of `T`.

#### Proof

The inclusion from left to right follows directly from (2.3): every
intersection defining a summand \(P_{i+j}\), `0<=j<=t`, contains the common
index interval on the right of (2.7).  Conversely, fix a coordinate present
throughout that common interval.  Its containing positive run either meets a
global endpoint or has length at least `d+1`.  Among the `t+1` erosion
windows defining \(P_i,\ldots,P_{i+t}\), one is contained in this run, so the
coordinate occurs in the left side.  This proves (2.7).  A value in (2.7)
has rank `r-1` only when its intersection interval has exactly two terms,
which proves the last assertion.  \(\square\)

## 3. The exact maximal-default compiler

Define the residual lower family

\[
 \mathcal R(P)=
 \left\{S\subseteq[k]:1\le |S|<r,\quad
 S\notin\bigcup_{t=1}^{d-1}\operatorname{supp}(D^tP)
 \right\}.                                               \tag{3.1}
\]

These are exactly the lower targets not already supplied by the fixed
positive derivative rows if one imposes `DA=DP`.

Let `J={0,...,W+d-1}`.  A maximal-default compiler assignment is an
injection

\[
                         \phi:\mathcal R(P)\longrightarrow J             \tag{3.2}
\]

such that

\[
                         S\subseteq P_{\phi(S)}                          \tag{3.3}
\]

for every residual target.  It defines

\[
 A_p=
 \begin{cases}
 S,&\phi(S)=p,\\
 P_p,&p\notin\phi(\mathcal R(P)).
 \end{cases}                                             \tag{3.4}
\]

### Theorem 3.1 (exact compiler criterion)

The assignment (3.2)--(3.4) satisfies `A<=P` and `DA=DP` if and only if

\[
 A_p\cup A_{p+1}=P_p\cup P_{p+1}
 \qquad(0\le p<W+d-1).                                  \tag{3.5}
\]

Equivalently, introduce binary variables `y_(S,p)` only when
\(S\subseteq P_p\), and impose

\[
 \sum_p y_{S,p}=1,
 \qquad
 \sum_S y_{S,p}\le1.                                   \tag{3.6}
\]

For a coordinate `x`, define

\[
 \epsilon_{p,x}=
 \mathbf1_{x\notin P_p}
 +\mathbf1_{x\in P_p}
   \sum_{\substack{S\in\mathcal R(P)\\x\notin S}}y_{S,p}.             \tag{3.7}
\]

Then (3.5) is equivalent to the adjacent omission inequalities

\[
 \epsilon_{p,x}+\epsilon_{p+1,x}\le1
 \quad
 \left(x\in P_p\cup P_{p+1}\right).                    \tag{3.8}
\]

Thus (3.6)--(3.8) are an exact integral characterization of this compiler,
not a marginal Hall relaxation.

#### Proof

Containment (3.3) gives `A<=P`.  Equation (3.5) is the coordinatewise
definition of `DA=DP`.  If \(x\) belongs to \(P_p\cup P_{p+1}\), then
\(\epsilon_{p,x}\) records exactly whether the actual letter \(A_p\) omits
\(x\):
an unassigned position uses `P_p`, while an assigned position uses its
unique target.  The union in (3.5) loses `x` precisely when both adjacent
letters omit it.  This is excluded exactly by (3.8).  The assignment and
capacity equations are exactly (3.6).  \(\square\)

Containment Hall is necessary but not sufficient; (3.8) is the chronology
coupling which Hall alone discards.

## 4. Universal-word theorem

Call the linear middle chronology `T` upper-complete if

\[
 \forall U\subseteq[k],\ |U|>r,\quad
 U=\bigcup_{i=a}^{b}T_i
 \quad\text{for some }0\le a\le b<W.                    \tag{4.1}
\]

### Theorem 4.1 (linear seam/compiler sufficiency)

Let `k,r,W,d,h,T,P` satisfy (1.1)--(2.6).  Suppose:

1. `T` is a permutation of the rank-`r` layer and is upper-complete in the
   arbitrary-width sense (4.1);
2. the exact maximal-default compiler (3.6)--(3.8) is feasible.

Then its word `A` has length `W+d=B(k)`, covers every nonempty subset of
`[k]`, and therefore

\[
                         \boxed{\nu(k)=B(k)}.             \tag{4.2}
\]

#### Proof

Theorem 3.1 gives `DA=DP`, so

\[
 D^tA=D^tP\quad(t\ge1),
 \qquad D^dA=D^dP=T.                                    \tag{4.3}
\]

Every lower target of rank below `r` either occurs in one of the fixed rows
`D^tP`, `1<=t<d`, or belongs to `R(P)` and is installed literally in `A`.
Thus all lower targets occur.  Equation (4.3) supplies every middle target.

If \(U\) is an upper target and (4.1) gives
\(U=T_a\cup\cdots\cup T_b\), then (4.3) gives

\[
 U=A_a\cup A_{a+1}\cup\cdots\cup A_{b+d},               \tag{4.4}
\]

a literal contiguous interval of `A`.  Hence every upper target occurs.
All letters are nonempty: assigned targets are nonempty and unassigned
letters have rank at least `h>=1`.  The word is universal and has length
`W+d`; (1.3) proves optimality.  \(\square\)

Within the declared subclass `A<=P`, `DA=DP`, and maximal values at every
position not used by a residual target, the compiler criterion is necessary
and sufficient.  It is only sufficient among arbitrary optimal words,
because a general compiler need not freeze `DA`.

## 5. The two-boundary lemma

Let `F` be a two-cycle 2-factor of `J(k,r)` on all `W` middle vertices.  Give
an edge `XY` its lower-`q=1` colour

\[
                         \chi(XY)=X\cap Y.                \tag{5.1}
\]

Assume the colour support is the complete rank-`(r-1)` layer.  Since the
factor has exactly `W` edges and

\[
 {k\choose r-1}={k\choose r}=W,                          \tag{5.2}
\]

every colour occurs exactly once.

Cut one edge in each component and orient the resulting paths `Q_0,Q_1`.
Let the deleted colours be `c_0,c_1`, and join the tail of `Q_0` to the head
of `Q_1` by a Johnson seam of colour `s`.  Put `T=Q_0Q_1`.

### Lemma 5.1 (exact q1 loss and endpoint absorption)

The missing lower-`q=1` colours of `T` are exactly

\[
                         \{c_0,c_1\}\setminus\{s\}.      \tag{5.3}
\]

Every missing `c_i` is locally admissible at the outer erosion cell belonging
to its own component when the adjacent erosion cell is left maximal.  More
precisely, if the left global endpoint belongs to the cut of component zero,
then

\[
 P_0=T_0,\qquad P_1=T_0\cap T_1,                         \tag{5.4}
\]

and the partial assignment

\[
                         A_0=c_0,\qquad A_1=P_1          \tag{5.5}
\]

satisfies

\[
                         A_0\cup A_1=P_0\cup P_1.        \tag{5.6}
\]

The symmetric statement holds at the right endpoint.  Hence a seam may
recycle neither deleted colour: both losses have compatible, distinct outer
boundary positions.

#### Proof

The internal transition colours of `T` are the complete old deck with
`c_0,c_1` deleted and `s` inserted.  This proves (5.3).

At the left endpoint, `c_0` is an `(r-1)`-facet of `T_0`.  The retained first
transition has colour \(P_1=T_0\cap T_1\).  It is a different facet,
because the old q1 deck was squarefree and the retained edge is not the cut
edge.  Two distinct `(r-1)`-facets of an `r`-set have union equal to the
whole `r`-set.  Thus \(c_0\cup P_1=T_0=P_0\cup P_1\), proving (5.6).
The right endpoint is identical after reversal.  \(\square\)

Lemma 5.1 proves local compatibility with maximal adjacent cells.  It does
not permit one to ignore (3.8) if the full compiler also changes those
adjacent cells.  The two endpoint pins must be included in the same integral
compiler instance.

## 6. Two-cycle theorem

### Theorem 6.1 (two-boundary seam/compiler theorem)

Let `k=2m+1` and let `d=d(k)<r`.  Suppose there exists a two-cycle factor
`F` on the rank-`r` layer with complete q1 colour deck.  Suppose one can
choose and orient one cut in each cycle and one connecting Johnson seam so
that the resulting path `T` has all of the following properties.

1. **Erosion/residence.**  `T` satisfies (2.4)--(2.6); it is enough that it
   be strongly `d`-resident.
2. **Upper chronology.**  Every upper target satisfies (4.1).  Equivalently,
   relative to the two opened paths, it has either a surviving interval
   witness inside one path or a witness which is the union of a suffix of
   `Q_0` and a prefix of `Q_1`.
3. **Common lower compiler.**  The residual family (3.1), including the one
   or two q1 colours in (5.3), admits one integral assignment satisfying
   (3.6)--(3.8), with each missing cut colour pinned to its own outer
   endpoint.

Then `nu(k)=B(k)`.

#### Proof

Under item 1, Lemma 2.2 shows that every rank-`(r-1)` value in the fixed
positive rows is an internal transition colour of `T`.  Hence the missing
colours (5.3) really belong to the residual family (3.1).  Lemma 5.1 proves
that their proposed endpoint pins have no local obstruction, even when the
seam recycles neither cut colour.  Item 3 imposes the remaining global
omission constraints.  Items 1--3 are exactly the hypotheses of Theorem 4.1.
Apply that theorem and then the monotone-deadline lower bound.  \(\square\)

The source factor may be cyclically complete at every lower and upper depth;
this is a powerful way to obtain candidates for items 2--3, but it is not by
itself a substitute for them.  Opening destroys witnesses, and collective
cyclic completeness does not imply linear completeness.

## 7. Exact `k=15` instantiation

For `k=15`,

\[
 r=8,\qquad W=6435,\qquad d=3,\qquad h=5.                \tag{7.1}
\]

The independently audited source factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.best.json
```

has SHA-256

```text
0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555.
```

It has two physical cycles of lengths `6390` and `45`, minimum run four,
and collective cyclic lower/upper completeness at every depth.  The winning
opening is

```text
state order       44 -> 12863
component order   0,1
cuts              22,41
orientations      0,1
```

Its Johnson seam recycles neither deleted colour.  The two q1 residuals are

```text
18553, 18033,
```

and the final word places them at its first and last positions.  There is no
rank-six residual.  Here

\[
 |\mathcal R(P)|=
 \sum_{j=1}^{5}{15\choose j}+2=4943+2=4945.             \tag{7.2}
\]

The exact compiler assigns all 4,945 targets, satisfies every omission row,
and emits

```text
answers/k15.word
```

of length `6438`, with SHA-256

```text
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b.
```

Two independent literal verifiers give

```text
covered nonempty masks   32767/32767
D^3 length               6435
D^3 distinct rank-8      6435
word length              6438
status                   VERIFIED_OPTIMAL.
```

Thus Theorem 6.1 specializes to the unconditional equality

\[
                         \boxed{\nu(15)=6438}.            \tag{7.3}
\]

## 8. Exactly what PBBS supplies and what remains for general odd `k`

The audited PBBS machinery supplies the following structural ingredients.

1. A middle-layer 2-factor with exact middle ownership.
2. A complete canonical lower and upper cyclic flag tower: every target has
   a cyclic witness, with explicit bounded multiplicity.
3. In the complement-projected upper-shore/fixed-matching factor used for
   the `k=15` construction, an exact q1 rainbow deck.  This is an additional
   factor property, not a property of the raw PBBS `m`-set `f^2` factor,
   whose q1 loads need not be one.
4. A concrete component decomposition and literal cyclic chronology on
   which cuts, seams, residence, and witness loss can be evaluated.

PBBS does **not** presently supply, uniformly in `k`, the three hypotheses
which Theorem 6.1 needs after cutting:

1. a reduction to exactly two components (or a multi-boundary analogue);
2. an oriented Johnson seam whose final path is `d(k)`-resident and retains
   every arbitrary-width upper target;
3. an integral solution of the common residual compiler (3.6)--(3.8).

A sufficient all-odd existence schema is therefore:

> For every odd `k`, some PBBS-supported or PBBS-modified two-cycle factor
> admits one oriented seam satisfying Theorem 6.1(1)--(3).

That statement, together with the theorem proved here, implies
`nu(k)=B(k)` for every odd `k`.  It remains unproved.  Separate rankwise Hall
assignments, cyclic all-depth support, or endpoint containment alone are all
strictly weaker.

## 9. Adversarial audit

1. The two source cycles are collectively all-depth complete; neither cycle
   is asserted to be complete by itself.
2. A cyclic witness which crosses a deleted edge is lost.  Fixed-window
   survival does not imply arbitrary-width upper survival.
3. The erosion has `2d` high boundary cells, not two.  “Two-boundary” refers
   specifically to the two outer rank-`r` cells which absorb the cut q1
   facets.
4. Lemma 5.1 proves local endpoint compatibility only.  Other compiler pins
   can create adjacent omission conflicts, which is why (3.8) remains.
5. Ordinary containment Hall does not imply (3.8), and a fractional
   assignment does not produce a word.
6. The condition `DA=DP` is a sufficient grading restriction, not a
   necessary property of every optimal word.
7. If `h=0`, unmatched maximal letters can be empty; hypothesis (1.4) cannot
   be silently dropped.
8. The `k=15` conclusion rests on the retained word and independent literal
   verification, not on solver status or the factor audit alone.
