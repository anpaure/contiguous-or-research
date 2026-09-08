# Neutral recency moves and explicit small-target pulses

2026-09-08. Pure-proof record by `exact_b_induction`, with the two-step
fixed-boundary pulse proposed by root during the analysis. No computation.
This is a construction lemma and an exact palette interface, not a claim
that the current 17-dimensional word has been completed.

## 1. General neutral successor normal form

Let the old recency blocks be B1,...,Bt and Cj their cumulative unions,
C0=empty. Suppose Cm has rank below s, C_(m+1) has rank s, and exactly
m nonempty old prefixes have rank below s. Append a nonempty X and require
a NEW rank-s prefix and unchanged potential b_s=m.

These conditions are equivalent to:

1. |X union Cm|=s;
2. Bj\X is nonempty for every 1<=j<=m;
3. X union Cm is not in the already recorded rank-s target family.

Indeed, the new prefixes are the distinct X union Cj. A fresh rank-s
prefix must arise from an old below-s prefix, since a rank-s old prefix
can only reproduce itself. If it first reaches rank s at j<m, fewer
than m low prefixes remain. Neutrality therefore forces j=m and all
earlier candidates to remain distinct. The displayed conditions give
exactly this behavior, proving the converse as well.

Equivalently X=Z union V, where Z is outside Cm, |Z|=s-|Cm|, V is
contained in Cm, and V does not contain any complete old block Bj,
1<=j<=m. In particular |X|<=s-m.

If additionally |Cm|=s-1 and both ranks s-1 and s are fresh with both
potentials neutral, then X has exactly one external element z, and

    X={z} union (Bm\{p}) union V,
    p in Bm, V subset C_(m-1), Bj\V nonempty for j<m.

The two new middle targets are Cm+z and (Cm\{p})+z. Their global
freshness is an explicit remaining condition, not implied by rank alone.

## 2. Stable three/four-window specialization

Suppose the literal last one-, two-, three-, and four-letter unions are

    C, C+u, C+u+v, C+u+v+w,

where |C|=s-3>=1 and u,v,w are distinct outside C. These are the first
four recency prefixes. Write B=C+u, A=C+u+v, T=C+u+v+w.

A move preserving both middle potentials and introducing fresh ranks
s-1 and s has exactly the form

    X={x} union U,   x outside T, U a proper subset of C,

subject to B+x and A+x being globally unused. The exclusion x outside T
includes the old-owner obstruction: x=w would reproduce T. Including u
or v is forbidden by the singleton old-block conditions. Including all
of C collapses a low recency prefix and is not neutral.

The new middle targets depend only on x, not on U. Thus a specified
small target S with S\C={x}, x outside T, and |S|<=s-3 can be inserted
directly whenever those two middle colors are unused.

## 3. An actual two-step host with fixed end state

Choose distinct x,y outside T, choose d in C, and let U be any subset
of C\{d}. Append

    X_U=U+{x},             Y=(C\{d})+{y}.                 (3.1)

The four newly supplied middle colors, independently of U and d, are

    rank s-1: B+x, C+x+y;
    rank s:   A+x, B+x+y.                               (3.2)

They are distinct within each rank and differ from the initial A,T.
Every new triple and four-window has its prescribed rank, and both
potentials remain unchanged. After the two moves the ENTIRE recency
state, not only its first prefixes, is independent of U. Its beginning is

    (C\{d}+y | {x} | {d} | {u} | {v} | {w} | ...),

where x,y are removed from their old tail blocks. This follows directly
by subtracting Y from the intermediate blocks U+x and C\U: their
residues are respectively {x} and {d}.

There is also literal host preservation. The two adjacent pair ORs
touching the variable X_U are

    C union X_U=C+x,
    X_U union Y=(C\{d})+x+y.

Both are independent of U. Every interval of length at least two that
contains X_U contains at least one of these adjacent pairs. Therefore
all interval ORs of length at least two remain exactly unchanged as U
varies; only the one-letter target X_U may change. Any fixed continuation
after Y has the same property and starts in the same actual recency state.

## 4. Several middle partners without globally unused coordinates

Let Z be the complement of the CURRENT owner T, g=|Z|. Coordinates in Z
may have appeared anywhere earlier in the word. Let Z_good be the x in Z
for which both B+x and A+x are absent from the current target inventories.
Let E_bad be the unordered pairs {x,y} in binom(Z,2) for which at least
one of C+x+y and B+x+y is already recorded at its corresponding rank.

For a prescribed x in Z_good, the exact number of possible y for (3.1)
is g-1-deg_Ebad(x). Every such choice works for ALL U subset C\{d}.
The total number of ordered fresh port pairs is at least

    |Z_good|(g-1)-2|E_bad|.

These are constructive finite palette criteria: each passing pair gives
the literal two-letter insertion and fixed-state host above. They make no
assumption that any coordinate is globally new. Conversely, an arbitrary
old target inventory can exhaust all candidates, so no unconditional
freshness guarantee from the current state alone is possible.

## 5. A six-step pulse for a target inside the current large block

Let S be any nonempty subset of C and choose x in S. Put B0=C\{x}.
Take four distinct a,b,c,d outside the current T and append

    B0+a, B0+b, B0+c, B0+d, S, B0+a.                    (5.1)

Every appended letter is nonempty. The six rank-(s-1) triple targets are

    C+u+a,
    C+a+b,
    B0+a+b+c,
    B0+b+c+d,
    C+c+d,
    C+a+d.

The six rank-s four-window targets are

    C+u+v+a,
    C+u+a+b,
    C+a+b+c,
    B0+a+b+c+d,
    C+b+c+d,
    C+a+c+d.

All six targets within each rank are distinct, and none equals the
corresponding initial middle target. The formulas are independent of
the choice of S containing x, because B0 union S=C. They follow by
literal three- and four-window unions, so old targets remain covered.

The final recency state begins

    (B0+a | {x} | {d} | {c} | {b} | ...),

again independently of S. Thus the pulse restores the stable block-size
pattern while realizing S as an actual letter. Global middle freshness
requires the twelve displayed targets to avoid the previous inventories;
this is a fully explicit finite test for each ordered four-tuple.

The delay is necessary in the elementary eviction route: inserting x
immediately after it leaves the current rank-(s-1) core reproduces the
preceding rank-s owner. The fourth preparatory letter in (5.1) avoids
that immediate repetition; the final letter restores the large first block.

For a quantitative sufficient freshness criterion, choose the ordered
distinct a,b,c,d uniformly from Z. For any one displayed target whose
outside support uses j of these positions, each specified j-subset of Z
has probability 1/binom(g,j). If M_i old targets occur in that displayed
baseline family, its failure probability is M_i/binom(g,j_i). Thus
sum_i M_i/binom(g,j_i)<1 guarantees a fresh pulse, with at least the
complementary fraction of all ordered four-tuples passing. This is only
a sufficient counting criterion; the explicit target list is exact.

## 6. Relation to the verified native291 prefix

The native291 certificate gives N-D8=N-D9=3, with final b8=2,b9=3.
An extension to length24313 covering every rank-eight and rank-nine set
must introduce a fresh target at both ranks at EVERY appended position:
N-D_s never decreases and its final value would still be three.

The neutral lemmas above therefore give actual extension moves, provided
their named middle targets pass the finite historical-palette test. They
do not establish that such tests continue to pass until the full cube is
covered. Root and frontier are separately auditing actual native291
extensions. No such computational result is asserted in this note.
