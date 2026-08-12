# Minimum repetitions in the triangular bounding-box word

## 1. Scope and outcome

Put

\[
 \mathcal T_R=\{P_0=(0,0)\}\cup
 \{E_{s,y}=(s,y):1\le s\le R,\ 0\le y<s\},
 \qquad P_s=E_{s,0}.
\]

A word in this note uses only letters from `T_R` and is required to contain
every letter at least once.  It is universal when, for every

\[
             0\le u<r\le R,\qquad 0\le x<r,
\]

some contiguous interval has bounding box

\[
                         [u,r]\times[0,x].             \tag{1.1}
\]

Let

\[
 \rho(R)=\min\{|W|-|\mathcal T_R|:W\text{ is such a universal word}\},
 \qquad |\mathcal T_R|=1+{R(R+1)\over2}.              \tag{1.2}
\]

The minimum is not determined for general `R`.  The main unconditional
advance is the linear lower bound

\[
 \boxed{
 \rho(R)\ge
 \left\lceil{\lfloor R/2\rfloor-2\over2}\right\rceil
 ={R\over4}-O(1).
 }                                                       \tag{1.3}
\]

For `R>=3` this is to be combined with the independent exact-once
obstruction `rho(R)>=1`.  Consequently, a construction with `O(R)` repeated
letters would have the best possible *order* of additive overhead.

The explicit fan word in `TRIANGULAR_PEAK_SHARING.md` gives

\[
 \rho(R)\le {R(R+1)\over2}-1.                          \tag{1.4}
\]

Thus the presently proved repetition gap is linear versus quadratic.  No
claim that either scale is the truth is made here.

This note also records two structural facts useful for the surviving
noncanonical construction route:

1. `T_R` is naturally the edge set of a complete graph, with one extra
   loop; and
2. a near-once word necessarily uses some witnesses of length
   `(2/3+o(1))R`.  Hence a construction cannot be reduced to making a
   constant-size provider triple locally consecutive.

The linear lower bound and the portal-grid normal form were independently
obtained in `NONCANONICAL_TRIANGULAR_BRAID.md`.  The complete-graph and
long-witness statements below are complementary refinements.

## 2. Complete-graph reformulation

Identify the cell `E_(s,y)` with the undirected edge `{y,s}` of
`K_(R+1)` on vertices `0,...,R`; identify `P_0` with a loop at vertex zero.
Thus

\[
              \mathcal T_R\setminus\{P_0\}=E(K_{R+1}). \tag{2.1}
\]

For an ordinary edge `e={a,b}`, `a<b`, write

\[
                         \ell(e)=a,\qquad h(e)=b,       \tag{2.2}
\]

and give the loop `P_0` both values zero.  Then (1.1) says exactly that an
interval of the edge word satisfies

\[
 \min h=u,\quad\max h=r,\quad\min\ell=0,\quad\max\ell=x. \tag{2.3}
\]

Equivalently, all its edges lie in the Ferrers rectangle

\[
 \mathcal R(u,r,x)=
 \{e:u\le h(e)\le r,\ 0\le\ell(e)\le x\},             \tag{2.4}
\]

and the interval touches all four sides of that rectangle.

This reformulation is exact, not merely an analogy.  It exposes why the
triangle has `1+binom(R+1,2)` cells and suggests using edge decompositions,
trails, and rotation systems.  However, Theorem 3 below shows that a bare
Euler-tour idea based only on constant-length local edge patterns is too
weak.

### Lemma 1 (an explicit noncanonical three-provider support)

If `u>=2` and `x>=1`, the three cells

\[
                         E_{u,1},\qquad P_r,\qquad E_{r,x} \tag{2.5}
\]

have bounding box `[u,r]x[0,x]`.  For `u=1`, replace `E_(u,1)` by `P_1`;
for `u=0`, use `P_0`.

#### Proof

The first coordinates in (2.5) are `u,r,r`, so their minimum and maximum
are `u,r`.  Their second coordinates are `1,0,x`, so their minimum and
maximum are `0,x`.  The two boundary cases are immediate.  QED.

Thus the peak supplying height zero may be tied to the *upper* row `r`,
while the minimum row is supplied by a low nonpeak arm.  This is precisely
the three-provider escape excluded by the canonical `P_u,E_(r,x)` theorem.
The hard part is not provider existence: it is placing these providers, and
the necessary clean fillers, in one shared word.

For one fixed `r`, the literal grid word

\[
 \begin{split}
 &E_{r,r-1},E_{r,r-2},\ldots,E_{r,1},P_r,\\
 &E_{r-1,1},E_{r-2,1},\ldots,E_{2,1},P_1,P_0           \tag{2.6}
 \end{split}
\]

covers all targets with that upper row `r` and positive height: start at
`E_(r,x)` and stop at the row-`u` provider.  Its failure as a global
construction is equally precise: the column-one spine in the second line
is recopied for every `r`.  Sharing those spines across different `r` is
the remaining superposition problem.

## 3. A near-once word must use long witnesses

There are

\[
 T_R=\sum_{r=1}^R r^2={R(R+1)(2R+1)\over6}            \tag{3.1}
\]

distinct target rectangles.  One physical interval has only one bounding
box, so witnesses selected for distinct targets are distinct intervals.

### Theorem 2 (short-window counting obstruction)

Let a universal word have length `n`, and let `Lambda` be the largest,
over all targets, of the length of a shortest witness.  Then

\[
 T_R\le \Lambda n-{\Lambda(\Lambda-1)\over2}.          \tag{3.2}
\]

In particular,

\[
 \Lambda\ge
 \left\lceil
 {2n+1-\sqrt{(2n+1)^2-8T_R}\over2}
 \right\rceil.                                        \tag{3.3}
\]

If `n=|T_R|+O(R)`, then

\[
                         \Lambda\ge(2/3+o(1))R.        \tag{3.4}
\]

#### Proof

The number of physical intervals of lengths at most `Lambda` is

\[
 \sum_{j=1}^{\Lambda}(n-j+1)
 =\Lambda n-{\Lambda(\Lambda-1)\over2}.               \tag{3.5}
\]

Choose one shortest witness for each target.  They are pairwise distinct,
because the bounding box of one fixed interval is unique.  This proves
(3.2).  Solving the resulting quadratic inequality gives (3.3).

For `n=(1/2+o(1))R^2`, divide (3.1) by `n`; the smaller root in (3.3) is
`T_R/n+O(T_R^2/n^3)=(2/3+o(1))R`.  QED.

The three cells in Lemma 1 are therefore only a support certificate.  No
near-once construction can represent all targets by uniformly bounded
clean intervals around those supports.  It must arrange long intervals so
that the same nested extrema simultaneously encode many targets.

## 4. Linear repetition is necessary

Call a letter a **peak** when its second coordinate is zero and a nonpeak
otherwise.  Let a word have `p` peak occurrences, split into `b` maximal
contiguous peak runs.  Let `q=|W|-|T_R|`, and let `q_p` be the number of
peak occurrences beyond the compulsory `R+1`; then `q_p<=q` and

\[
                         p=R+1+q_p.                    \tag{4.1}
\]

### Lemma 3 (peak runs versus the zero-height layer)

\[
                         p-b\ge R,
 \qquad\text{and hence}\qquad q_p\ge b-1.             \tag{4.2}
\]

#### Proof

For every `i=0,...,R-1`, a witness for

\[
                         [i,i+1]\times\{0\}           \tag{4.3}
\]

contains only `P_i,P_(i+1)` and contains both.  It therefore contains a
physical adjacency `P_i|P_(i+1)` or its reverse.  Different `i` require
different physical adjacencies.  The number of peak--peak adjacencies in
`b` peak runs containing `p` positions is exactly `p-b`, proving (4.2).
QED.

### Lemma 4 (top adjacent targets need many portals)

The word has at least `ceil((R-1)/2)` physical peak--nonpeak adjacencies.

#### Proof

For `i=1,...,R-1`, consider the target

\[
                         [i,i+1]\times[0,i].           \tag{4.4}
\]

Its witness contains a peak and the height-`i` cell `E_(i+1,i)`, hence it
crosses some physical peak--nonpeak adjacency.

If one fixed adjacency is used by (4.4), the first coordinates of both of
its letters belong to `{i,i+1}`.  A fixed pair of first coordinates is
contained in at most two such consecutive two-element sets.  Hence one
physical portal can be charged by at most two values of `i`.  There are
`R-1` values, proving the claim.  QED.

### Theorem 5 (linear excess theorem)

Every universal spanning word over `T_R` satisfies

\[
 \boxed{
 q\ge
 \left\lceil{\lfloor R/2\rfloor-2\over2}\right\rceil.
 }                                                       \tag{4.5}
\]

#### Proof

Each of the `b` peak runs has at most two boundary portals, so Lemma 4 gives

\[
 b\ge\left\lceil{R-1\over4}\right\rceil.              \tag{4.6}
\]

Lemma 3 now gives

\[
 q\ge q_p\ge b-1
 \ge\left\lceil{R-1\over4}\right\rceil-1.             \tag{4.7}
\]

The final expression equals (4.5); equivalently one may use the direct
peak-incidence proof in `NONCANONICAL_TRIANGULAR_BRAID.md`.  QED.

This theorem allows arbitrary noncanonical witnesses and repeated
nonpeaks.  Its scope restriction is only that the word is over `T_R` and
contains every cell.  If arbitrary entries outside the triangular alphabet
are admitted, `rho(R)` is no longer the appropriate excess parameter and a
different statement is needed.

## 5. Exact and certified small information

The exact initial values proved without heuristic nonexistence claims are

\[
                         \rho(1)=0,\qquad\rho(2)=0,
                         \qquad\rho(3)=1,\qquad\rho(4)=2. \tag{5.1}
\]

For `R=2`, one permutation is

```text
(2,1) (2,0) (1,0) (0,0)
```

For `R=3`, the exact-once obstruction gives the lower bound one, and the
following length-eight word attains it:

```text
(1,0) (2,1) (0,0) (1,0) (2,0) (3,0) (3,1) (3,2)
```

For `R=4`, the proof-producing NFA/SAT encoding in
`TRIANGULAR_NFA_SAT.md` proves that length 12 is impossible, and an
independently checked length-13 word exists.  The UNSAT result has a verified
DRAT certificate, so this is an exact value rather than a failed-search
inference.

The currently certified upper witnesses give

\[
                         1\le\rho(5)\le4,
 \qquad                    1\le\rho(6)\le5,
 \qquad                    1\le\rho(7)\le9.            \tag{5.2}
\]

The length-20 word is recorded in `NONCANONICAL_TRIANGULAR_BRAID.md`.
The length-27 `R=6` word is
recorded in `scratch/triangular_r6_plus5.txt` and independently passes
the generic interval, alphabet, and spanning checks.  The length-38 `R=7`
word is recorded in `scratch/triangular_r7_plus9.txt`; its interval audit and
completion-core decomposition are in `R7_CERTIFICATE_STRUCTURE.md`.
Failed heuristic
searches are not lower bounds.  In particular:

* an `R=5` search with two repeats remained two targets short;
* one long `R=5` search with three repeats remained only the target
  `(u,r,x)=(2,3,2)` short.

These observations are useful for choosing absorbers, but none proves
`rho(5)=4`, `rho(6)=5`, or `rho(7)=9`.

The first three successful excesses `1,2,4` equal

\[
                         \left\lfloor{(R-1)^2\over4}\right\rfloor, \tag{5.3}
\]

the size of the strict-interior depth-`R-1` antichain derived in the
companion note.  The `R=6` certificate has only five repeats whereas
(5.3) equals six, so (5.3) is now disproved both as an all-`R` exact
formula and as a universal lower bound.  The antichain still explains the
small values but cannot be injected one-for-one into repeated positions.

## 6. The precise surviving alternatives

The current theorem ledger leaves two qualitatively different possibilities.

### Linear-overhead portal braid

There may exist a word of length

\[
                         |\mathcal T_R|+O(R).           \tag{6.1}
\]

Theorem 5 says this would be optimal in additive order.  Proposition 4 of
`NONCANONICAL_TRIANGULAR_BRAID.md` reduces it to superposing `O(R)` joins of
two nested chains (portal grids).  Lemma 1 above shows a uniform provider
choice; Theorem 2 says the superposition must deliberately create long
clean intervals rather than isolated three-letter gadgets.

A useful constructive target is therefore:

> Order the complete-graph edges and `P_0`, with `O(R)` repeated edges, so
> that `O(R)` peak--nonpeak portals have left/right extrema chains whose
> join grids cover every Ferrers rectangle (2.4).

The edge formulation suggests rotation systems or a global Euler/Hierholzer
splicing argument, but ordinary Eulericity alone is insufficient.

### Quadratic strict-interior obstruction

It is also possible that the strict-interior antichain forces
`Omega(R^2)` repetitions by a mechanism stronger than endpoint charging.
To prove this, one needs a congestion theorem showing that one excess
occurrence cannot repair many members of that antichain.  Present portal
grids can contain `Theta(R)` equal-depth targets, so the ordinary antichain
argument gives only a linear obstruction.

The exact next mathematical discriminator is consequently one of:

1. construct a global `O(R)`-portal edge braid satisfying (6.1); or
2. prove a portal-congestion inequality of quadratic total cost.

Small-case optimization alone does not distinguish these alternatives.
