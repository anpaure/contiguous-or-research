# Pair-cell clocks have universal labelled target portals above a subexponential low bank

**Date:** 2026-08-13  
**Status:** unconditional local portal theorem and exact fractional orbit reduction.  For
odd `k=2R-1`, every strict-lower target of rank at least
`ceil(3 log_2(R-1))+1` occurs in some labelled good pair cell, either as a
programmable source letter or as a consecutive-intersection fan cell.  The omitted
target bank has size `exp(O((log R)^2))=W^{o(1)}`.  This is a local/orbit statement:
it does not choose all portals inside one owner factor, pass the simultaneous interval
cap, absorb the bad owner cells, or fuse the resulting components.

## 1. Setup

Put

\[
 k=2R-1,\qquad p=R-1,\qquad
 q\ge2,\qquad h=\lceil3\log _2p\rceil,\qquad M=q+h,       \tag{1.1}
\]

and assume `M<=p`.  A labelled pair cell means the construction of
`MATH_THEOREM_PAIR_CELL_LONG_RUN_Q_WINDOW_CLOCK_EXPLICIT_LEAVE_AND_EXACT_SPLICE_CAP_20260813.md`:
one sentinel `z`, a perfect matching of the other `2p` coordinates, an occupancy
sector, and a long-run Hamilton Gray cycle on the cell's singleton pairs.  A cell of
dimension `m>=M` is called good.

For a good cell with owner trace `(T_i)`, let

\[
 P_t=\bigcap_{u=0}^{q-1}T_{t-u},\qquad
 C=\bigcap_iT_i,\qquad B_t=P_t-C.                         \tag{1.2}
\]

Then `|C|=R-m` and `|B_t|=m-q+1`.  By redistributing the
permanent coordinates of `C` on cyclic hitting schedules, a singleton source cell at
`t` realizes exactly the interval of Boolean values

\[
                  B_t\subseteq S\subseteq B_t\cup C.     \tag{1.3}
\]

## 2. Universal programmable-letter portals

### Theorem 2.1

Let `S subseteq [k]` have rank `s` with

\[
                         h+1\le s\le R-q.                 \tag{2.1}
\]

There is a labelled good pair cell of dimension

\[
                         m=s+q-1                          \tag{2.2}
\]

and a source address `t` for which

\[
                         B_t=S.                           \tag{2.3}
\]

Consequently `S` is a literal singleton source cell after choosing every permanent
core schedule to avoid `t`.  This choice may also be made on the
immediate-lower-preserving face when `q>=3`.

#### Proof

The range (2.1) gives `M<=m<=p`.  Choose a sentinel `z` outside `S`.
Start with any long-run Hamilton Gray cycle on `Q_m` and mark an address
`t`.  Its preceding `q-1` transition directions are distinct.  Coordinate
permutations transport the Gray cycle, so relabel those directions and the
other `m-q+1` directions as follows.

* Use `s=m-q+1` untouched singleton pairs.  Put one distinct element of `S` on the
  side selected throughout the marked `q`-owner window, and give it a distinct mate
  outside `S`.
* Use `q-1` further singleton pairs for the marked transition directions, with both
  members outside `S`.

The required outside coordinates, including the sentinel, number

\[
                  s+2(q-1)+1.                             \tag{2.4}
\]

Because `m=s+q-1`, all `m` pairs have now been declared singleton.  After
their endpoints and the sentinel are chosen, exactly

\[
 2p+1-s-\bigl(s+2(q-1)+1\bigr)=2(p-m)                    \tag{2.5}
\]

coordinates remain.  Pair them arbitrarily.  Put

\[
 \epsilon\equiv R-m\pmod2,
 \qquad a={R-\epsilon-m\over2},
 \qquad b=p-m-a.                                         \tag{2.6}
\]

The parity definition makes `a` integral.  Since `m<=p`, it also gives
`0<=a<=p-m`, so `b>=0`.  Declare `a` of the remaining pairs double and
the other `b` empty, and put the sentinel in the owner precisely when
`epsilon=1`.  All permanent coordinates are outside `S`.

Across the marked `q` owners, every transitioned singleton pair contributes nothing
to the intersection, while the untouched selected sides contribute exactly `S`.
Thus `B_t=S`.  Theorem 2.2 and Corollary 2.3 of the distributed-permanent-core theorem
give the two final assertions.  \(\square\)

### Theorem 2.2 (top programmable-letter rank)

Every target `S` of rank

\[
                         s=R-q+1                          \tag{2.7}
\]

also has a programmable singleton-letter portal in a good cell.

#### Proof

Choose `z in S`, take `m=p`, and use the sector in which the sentinel is present.
Then `C={z}` and `|B_t|=p-q+1=s-1`.  Put the elements of `S-{z}` on the selected
sides of the untouched singleton pairs and use the remaining `q-1` pairs for the
marked transition directions.  There are no double or empty pairs in this
`m=p` sector.  The complement of `S` supplies exactly all required
mates and transition labels.  Hence `B_t=S-{z}` and `S=B_t union C`; emit `z` at
the marked address.  \(\square\)

## 3. Universal top-fan portals

### Theorem 3.1

Let

\[
                         R-q+2\le s\le R-1               \tag{3.1}
\]

and put `r=R-s`, so `1<=r<=q-2`.  Every rank-`s` target `S`
is the intersection of `r+1` consecutive owners in a labelled dimension-`p` good
pair cell.  It is therefore a literal source interval of width `q-r` in that cell's
maximal antecedent.

#### Proof

Choose `z in S`, take all `p` pairs singleton, and use the sector in which `z` is
present.  Choose `r` consecutive distinct transition directions at an address of the
long-run Gray cycle.  Put the `p-r=s-1` elements of `S-{z}` on the selected sides of
the untouched pairs.  The complement of `S` has size `p+r`; it supplies their `p-r`
mates and both sides of the `r` transition pairs, exactly exhausting the complement.
The intersection of the resulting `r+1` owners is `S`.  The literal source identity

\[
 \bigcap_{j=0}^{r}T_{i+j}
   =\bigcup_{u=r}^{q-1}P_{i+u}                            \tag{3.2}
\]

is Theorem 3.1 of the pair-cell clock theorem.  \(\square\)

Combining Theorems 2.1, 2.2, and 3.1 gives a labelled good-cell portal for every
strict-lower target of rank at least `h+1`.

## 4. The remaining target bank is subexponential

Let

\[
                         \mathcal L_{\rm low}
   =\{S subseteq[k]:1\le |S|\le h\}.                      \tag{4.1}
\]

### Corollary 4.1

\[
 |\mathcal L_{\rm low}|
   =\sum_{s=1}^{h}\binom{2p+1}{s}
   \le h\left({e(2p+1)\over h}\right)^h
   =\exp\!\bigl(O((\log p)^2)\bigr)=W^{o(1)}.            \tag{4.2}
\]

Thus the failure of the good-cell threshold removes only a subexponential bank of
**target values**, although the bad owner leave remains exponentially large in
absolute size.

#### Proof

For `h<=k/2`, the binomial coefficients increase through rank `h`, and the standard
bound `binom(k,h)<= (ek/h)^h` gives (4.2).  Since
`log W=Theta(p)` while `h=Theta(log p)`, the last equality follows.  \(\square\)

## 5. Exact orbit-fractional consequence

Fix one pointed portal from Theorem 2.1, 2.2, or 3.1 at each admissible rank `s`, and
take its full `Sym([k])` orbit.  The symmetric group is transitive on rank-`s` targets,
so every such target lies in the same positive number `D_s` of pointed portals.
Giving every pointed portal weight `1/D_s` is therefore an exact fractional one-cover
of the entire rank-`s` row.

This observation is deliberately only fractional.  A permutation changes the whole
pair partition and owner factor.  It does **not** imply that one can select portals
for different targets inside one common factor, nor that multiple marked intervals in
one cell satisfy the coordinatewise cyclic hit/avoid cap.

## 6. Remaining integral gate

The local support problem is now confined to the following exact integral synthesis.

1. Choose one or a bounded family of pair partitions whose good cells cover every
   owner, or absorb the low-dimensional owner cells by cross-cell trades.
2. Match every target of rank at least `h+1` to a pointed portal in the chosen cells,
   with each physical source interval used at most once.
3. For every permanent coordinate, make the chosen positive/negative marked intervals
   admit one cyclic hitting schedule.
4. Realize the `W^{o(1)}` low target bank inside a protected part of the same `W+O(1)`
   source addresses, and fuse the resident components.

The theorem closes labelled portal existence and shows that the exceptional
**target** bank is tiny on the exponential scale.  It does not turn that asymptotic
smallness into additive word length.
