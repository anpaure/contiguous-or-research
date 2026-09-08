# K16 zero-port staircases and the nonlocal `0xc279` gap commutator

Date: 2026-07-30

## 0. Verdict

Two independently authenticated length-12,873 structures expose the same
missing operation: a provider must be transplanted nonlocally and its donor
debt must be closed by a second exchange.  This note proves exact
construction and obstruction theorems for both structures.

1. The projected old-coordinate trace

   ```text
   scratch/k16_repeatfree_projected_D0_20260730/best_projected.word
   ```

   covers every nonempty 15-bit target at least twice.  Zeroing its best
   position leaves the nested load-one pair

   \[
                 \texttt{0x4879}\subset\texttt{0x6879}.
   \]

   Their unique surviving occurrences form one nested packet.  Moving any
   nonempty helper block whose union is contained in `0x4879` immediately
   after that packet creates a second occurrence of both targets.  There are
   exactly 520 remote one-cell candidates with the required projected halo
   containment.  They are not yet safe relocations: the exact projected gate
   is a three-seam cut-capacity inequality, and literal K16 completion also
   requires opposite physical (z)-phases.

2. A centered three-cell zero diamond

   \[
        (x,y,z)\longmapsto(x\vee y,\varnothing,y\vee z)
   \]

   is forced if the middle output is required to be zero and both adjacent
   pair unions are fixed.  Its complete occurrence drift has a closed
   OR-polynomial formula and touches at most (4(k+1)+2) target labels.  On
   the authenticated trace it repairs the *other* minimum-port pair at
   position 1 but creates exactly three new debts.  Erasing the two naturally
   exposed contaminant bits repairs those three and creates ten others.  That
   particular erasure is not a completion; a nonlocal or multicell
   compensator is required.

3. In the ghost-free waste-three middle schedule, the four forced upper
   holes share the unique rank-eight core

   \[
                         C=\texttt{0xc279}.
   \]

   Moving the existing (C)-owner from its donor gap into the recipient gap
   realizes all four at once and changes the arbitrary-width upper-hole set
   exactly from four recipient flags to six donor flags.  No other single
   rank-eight bridge can preserve both donor q1 flags.

4. A second exact 2-opt commutator restores all six donor flags.  It leaves
   only

   \[
                 \texttt{0x6379}\subset\texttt{0xe379}
   \]

   and the canonical two-window literalization fails at exactly two new cut
   endpoints, missing bits `0x0008` and `0x0010`.  The natural next 2-opt
   makes the middle turns exact and realizes both missing upper flags, but
   exports two new nested cut staircases

   \[
       \texttt{0x437b}\subset\texttt{0x537b},\qquad
       \texttt{0x7279}\subset\texttt{0x7a79}.
   \]

   Thus the operation is an exact debt circulation, not a closure.  Any
   successful continuation must place its cuts in duplicate upper reserve
   or absorb both exported staircases in the same physical atlas.

Neither construction is yet a universal K16 word.  The projected helper
still needs a safe three-cut relocation and a physical (z)-phase.  The
upper commutator still needs another nonlocal rethread/collar and a lower
compiler.  The
global bracket remains

\[
                         12873\leq\nu(16)\leq12874.
\]

## 1. Authenticated inputs and scope corrections

Exactly two of the six authenticated K15 batch parents, seeds 1 and 5, are
rank-seven repeat-free after the depth-two erosion: their 6,436 depth-two
cells consist of all 6,435 rank-seven masks once and one rank-six junk cell.
The other four batch parents are not repeat-free.  Seed 5 is the retained
`K15_REPEATFREE_SEED`.

The projected length-12,873 trace is

\[
 A\;|\;\pi(B[3:]),
\]

where (A) is `scratch/k15.endpoint_normalized.word`, (B) is repeat-free
seed 5, and

\[
 \pi=(5,9,10,7,8,4,0,2,12,13,14,3,6,11,1).
\]

Here “projected double cover” means multiplicity **at least** two, not
exactly two.  It is only the old-coordinate projection of an even lift.  A
physical phase assignment must still give the required marked and unmarked
occurrences.

The all-position zero census has minimum projected deficiency two at exactly
positions 0 and 1.  The exact zero-plus-one-substitution audit closes only
those two minimum ports; it does not close larger-deficiency zero ports or a
block rethread.

The second source is ghost-free only in the first-delivery sense: it has no
same-target occurrences at different right deadlines.  It still has the
three same-right flats `0x4e71`, `0xcc63`, and `0xce61`.

## 2. Exact OR-polynomial block calculus

Let \(\mathbb Z[\mathcal B_k]\) be the free abelian group on Boolean masks,
with the OR-convolution product

\[
                         [S]*[T]=[S\cup T].
\]

For a finite block (X=(x_1,\ldots,x_m)), define:

* (u(X)=[x_1\vee\cdots\vee x_m]);
* (P(X)), the sum of the ORs of its positive-length prefixes, with
  multiplicity (the OR value is allowed to be empty);
* (Q(X)), the sum of the ORs of its positive-length suffixes, with
  multiplicity (again allowing the empty OR value);
* (C(X)), the sum of the OR masks of all nonempty contiguous intervals of
  (X), with multiplicity.

### Theorem 2.1 (concatenation identities)

For any two blocks (X,Y),

\[
\begin{aligned}
 P(XY)&=P(X)+u(X)*P(Y),\\
 Q(XY)&=Q(Y)+Q(X)*u(Y),\\
 C(XY)&=C(X)+C(Y)+Q(X)*P(Y).
\end{aligned}
\tag{2.1}
\]

Consequently, for blocks (B_1,\ldots,B_m) in an order \(\sigma\),

\[
\begin{aligned}
C(B_{\sigma(1)}\cdots B_{\sigma(m)})
=&\sum_i C(B_i)\\
&+\sum_{i<j}Q(B_{\sigma(i)})
  *\!\!\prod_{i<h<j}u(B_{\sigma(h)})
  *P(B_{\sigma(j)}).
\end{aligned}
\tag{2.2}
\]

#### Proof

Every prefix of (XY) either lies in (X), or consists of all of (X)
followed by a prefix of (Y).  The suffix identity is symmetric.  Every
interval of (XY) is internal to one block or is a suffix of (X) followed
by a prefix of (Y).  This proves (2.1).  Iteration classifies every
cross-block interval by its first and last blocks, proving (2.2).

Every prefix- or suffix-OR chain has at most (k+1) distinct masks.  Thus
comparing two orders of five fixed blocks changes at most

\[
             2\binom52(k+1)^2=5120\qquad(k=15)
\tag{2.3}
\]

distinct target labels.  This bound is independent of the total word
length.  It is the finite cut kernel behind the helper relocation below.

## 3. Projected reserve conservation

For a possibly-zero projected word (W) of length (L), let

\[
 \mu_W(S)=\#\{[a,b]:\bigvee_{i=a}^b W_i=S\}.
\]

Define the deficiency and excess relative to multiplicity two by

\[
 D_2(W)=\sum_{S\ne\varnothing}(2-\mu_W(S))^+,
 \qquad
 E_2(W)=\sum_{S\ne\varnothing}(\mu_W(S)-2)^+.
\tag{3.1}
\]

If the zero runs have lengths \(\ell_1,\ell_2,\ldots\), put

\[
                        Z(W)=\sum_j\binom{\ell_j+1}{2}.
\]

### Theorem 3.1 (exact reserve identity)

\[
 \boxed{
 E_2(W)-D_2(W)
 =\binom{L+1}{2}-Z(W)-2(2^{15}-1).}
\tag{3.2}
\]

#### Proof

Exactly (Z(W)) intervals have empty OR.  Hence

\[
 \sum_{S\ne\varnothing}\mu_W(S)=\binom{L+1}{2}-Z(W).
\]

Sum the identity

\[
 \mu_W(S)-2=(\mu_W(S)-2)^+-(2-\mu_W(S))^+
\]

over the (2^{15}-1) nonempty masks.

For the authenticated projected (D_2=0) trace, replacing one cell by an
isolated zero at fixed length and leaving the minimum raw deficiency
(D_2=2) gives

\[
 E_2(W_{\rm raw})=E_2(W_{\rm original})+1.
\]

A completed isolated-zero double cover would instead have

\[
 E_2(W_{\rm final})=E_2(W_{\rm original})-1.
\]

Thus completion must consume two excess units relative to the raw-zero
state: the unit created by zeroing and one inherited reserve unit.  Merely
shuttling two deficits without consuming multiplicity reserve cannot close.

## 4. Nested-staircase helper relocation

### Lemma 4.1 (nested-staircase halo)

Suppose a packet has the form

\[
                P=W_s|W_{s-1}|\cdots|W_1|K
\]

and its suffix-OR staircase is

\[
 T_0=\bigvee K,\qquad
 T_i=\bigvee(W_i|\cdots|W_1|K),\quad1\leq i\leq s.
\tag{4.1}
\]

If a nonempty helper block (H) satisfies

\[
                         \bigvee H\subseteq T_0
\tag{4.2}
\]

and is moved immediately after (K), then every (T_i) acquires a new
distinct occurrence:

\[
 K|H,\quad W_1|K|H,\quad\ldots,\quad
 W_s|\cdots|W_1|K|H.
\tag{4.3}
\]

#### Proof

Appending (H) changes none of the ORs in (4.1), by (4.2).  Every interval
in (4.3) is strictly longer than its retained predecessor, so the
occurrences are distinct.

For the best zero port (p=0),

\[
 T_0=\texttt{0x4879}\subset
 T_1=\texttt{0x6879}.
\]

Their unique surviving occurrences are

\[
 K=[10096,10098],\qquad W_1|K=[10095,10098].
\tag{4.4}
\]

The raw-zero trace contains exactly 523 nonzero cells contained in (T_0).
Three lie in (K), leaving exactly 520 remote one-cell helper candidates.

### Theorem 4.2 (exact three-cut criterion)

Suppose a helper lies to the left and factor the raw-zero word as

\[
                       A|H|B|P|D.
\]

Move it after (P):

\[
                       A|B|P|H|D.
\tag{4.5}
\]

Let (I(S)) count occurrences of (S) internal to the five retained
blocks, and let (X_{\rm old}(S),X_{\rm new}(S)) count cross-block
occurrences in the two orders.  Then

\[
 \mu_{\rm new}(S)
 =I(S)+X_{\rm new}(S)
 =\mu_{\rm raw}(S)+X_{\rm new}(S)-X_{\rm old}(S).
\tag{4.6}
\]

Hence (4.5) preserves projected double coverage if and only if

\[
 \boxed{
 X_{\rm new}(S)-X_{\rm old}(S)
 \geq 2-\mu_{\rm raw}(S)
 \quad\text{for every }S\ne\varnothing.}
\tag{4.7}
\]

The halo lemma guarantees (4.7) for the two deficient rows.  A strong
sufficient cut-protection condition is

\[
 I(S)\geq2\quad
 (S\notin\{\texttt{0x4879},\texttt{0x6879}\}),
\tag{4.8}
\]

with the two packet occurrences in (4.4) retained.  The right-hand helper
case is symmetric.

For a helper (h), let \(\mathcal F_S\) be the set of candidates that
violate (4.7) at row (S).  A concrete sufficient existence certificate is

\[
                         \sum_S|\mathcal F_S|<520.
\tag{4.9}
\]

The 5,120-label kernel (2.3) makes each candidate check finite.  Inequality
(4.9), or a structural PBBS bound implying it, is the one open zero-port
lemma **in the projected layer**.  The previous zero-plus-one-substitution
no-go does not test (4.5), which changes three seams and both prefix/suffix
contexts.

There is a deterministic alternative to the union bound.  For a helper
(H), let

\[
 \lambda_H(S)=\#\{R:R\text{ is a positive-length suffix of }P,
                 \ \bigvee R\vee\bigvee H=S\}.
\tag{4.10}
\]

### Lemma 4.3 (laminar suffix reserve)

For the rethread (4.5),

\[
                         \mu_{\rm new}(S)\geq I(S)+\lambda_H(S).
\tag{4.11}
\]

Consequently it is projected-D0 whenever the right side is at least two for
every nonempty (S).  In particular, suppose every vulnerable row

\[
                         \mathcal V=\{S\ne\varnothing:I(S)<2\}
\]

is the OR of a suffix (R_S) of (P), and

\[
                         \bigvee H\subseteq\bigcap_{S\in\mathcal V}S.
\tag{4.12}
\]

Then the retained interval (R_S) and the new interval (R_S|H) are two
distinct occurrences of (S), so the rethread is projected-D0.

#### Proof

The internal occurrences and the new suffix-plus-helper occurrences are
disjoint families, proving (4.11).  Under (4.12), each vulnerable row has
one member in each family.  Nonvulnerable rows already have two internal
members.

Projected multiplicity is not literal even-dimensional completion.  Write a
physical mask as \((S,e)\), where (e) records the marked coordinate (z).
All block identities above hold in the phase-labelled OR semilattice

\[
                    (S,e)*(T,f)=(S\vee T,e\vee f).
\]

### Corollary 4.4 (literal phased halo)

If every packet suffix (R_i) has physical OR \((T_i,0)\) and the moved helper
has physical OR \((h,1)\) with (h\subseteq T_0), then (R_i) and (R_i|H)
literally witness (T_i) and (T_i\cup\{z\}), respectively.  If every other
vulnerable physical row has two protected internal witnesses of the required
phases, and the projected-zero cell is lifted as the singleton \(\{z\}\),
the rethread gives a literal zero port and phase split on the whole declared
atlas.

The corresponding five-block physical support bound is

\[
                         2\binom52(16+1)^2=5780.
\tag{4.13}
\]

If a retained packet suffix already carries (z), OR-monotonicity prevents
the halo from creating its unmarked mate.  Thus the phase condition in the
corollary is essential, and none of the 520 projected candidates is yet
certified as a physical helper.

## 5. The centered zero diamond

Put \(\widehat Q(A)=[\varnothing]+Q(A)\) and
\(\widehat P(B)=[\varnothing]+P(B)\).

### Theorem 5.1 (exact zero-diamond drift)

For

\[
 A|x|y|z|B
 \longmapsto
 A|(x\vee y)|\varnothing|(y\vee z)|B,
\tag{5.1}
\]

the occurrence-polynomial drift is

\[
\boxed{
 \Delta C=
 \widehat Q(A)*([x\vee y]-[x])
 +([y\vee z]-[z])*\widehat P(B)
 +[\varnothing]-[y].}
\tag{5.2}
\]

At most (4(k+1)+2) distinct target labels occur in (5.2).

#### Proof

Every interval containing at least two of the three displayed cells keeps
the same OR.  The changed intervals are precisely the left suffixes ending
at (x), the right prefixes beginning at (z), and the singleton (y).
These are the three summands in (5.2).  Each exterior OR chain has at most
(k+1) distinct masks.

At the other minimum port (p=1) of the authenticated trace,

\[
 (\texttt{0x4879},\texttt{0x2039},\texttt{0x2869})
 \longmapsto
 (\texttt{0x6879},\varnothing,\texttt{0x2879}).
\tag{5.3}
\]

This restores `0x2879` and `0x287d`, but leaves exactly

\[
 \texttt{0x4879},\qquad
 \texttt{0x286d}\subset\texttt{0x2c6d}
\tag{5.4}
\]

at load one.  Their unique surviving packets are respectively

```text
[10096,10098], [12294,12296], [12294,12297].
```

Removing contaminant `0x2000` from cell `0x2808` at position 10095 and
`0x0010` from `0x201c` at position 12293 clones all three packets.  Exact
replay then leaves ten new load-one targets.  The boundary bits must be
handled by an additional nonlocal or multicell compensation; these two
natural erasures are not a completion.  Transporting already-clean helper
blocks is one candidate, not a proved necessity.

## 6. The four-hole common-core fork

Let

\[
 C=\texttt{0xc279},\quad
 A=\texttt{0xca71},\quad
 B=\texttt{0xc639}.
\]

The four forced upper holes obey

\[
\begin{aligned}
A\vee C&=\texttt{0xca79},\\
C\vee B&=\texttt{0xc679},\\
\texttt{0xea61}\vee A\vee C&=\texttt{0xea79},\\
\texttt{0xeb60}\vee\texttt{0xea61}\vee A\vee C
 &=\texttt{0xeb79}.
\end{aligned}
\tag{6.1}
\]

Their intersection is exactly (C), of rank eight.  Moreover `0xc679`
and `0xca79` are incomparable.  Therefore a single rank-eight common
provider must equal (C), and one-sided cumulative extensions cannot realize
the family: a one-core realization needs a two-sided fork or a second
(C)-occurrence.

The physical block

\[
 (\texttt{0x8010},\texttt{0x4001},\texttt{0x8269})
\tag{6.2}
\]

at positions 11727--11729 has OR (C).  Moving it immediately before the
tail cell `0xc608` realizes all four targets literally.  A complete replay
finds 30 remaining holes, including six middle holes.  Thus (6.2) is an exact
provider transplant, not a universal physical braid.

## 7. Target-order gap transport

The middle-target order isolates the essential exchange from the lower
compiler.  At the donor and recipient sockets put

\[
 P-C-Q=(\texttt{0xc371},\texttt{0xc279},\texttt{0xe269}),
\]

\[
 A-B=(\texttt{0xca71},\texttt{0xc639}).
\]

The intersections (P\cap Q) and (A\cap B) have rank six, while each of
(P\cap C,C\cap Q,A\cap C,C\cap B) has rank seven.  Moving (C) between
(A,B) performs the degree-neutral three-edge exchange

\[
             \{PC,CQ,AB\}\longmapsto\{PQ,AC,CB\},
\tag{7.1}
\]

transporting the displayed distance-two gap from the recipient to the donor.
The rank-eight target multiset, including the three flats, is unchanged.

Before the move, (C) is the unique common owner of two donor staircases:

\[
 \texttt{0xc379},\ \texttt{0xc37b},\ \texttt{0xd37b}
\tag{7.2}
\]

on the left and

\[
 \texttt{0xe279},\ \texttt{0xf279},\ \texttt{0xfa79}
\tag{7.3}
\]

on the right.  Their unique arbitrary-width target-order occurrences are

```text
0xc379 [11726,11727]    0xe279 [11727,11728]
0xc37b [11725,11727]    0xf279 [11727,11729]
0xd37b [11724,11727]    0xfa79 [11727,11730].
```

Exact replay proves that (7.1) changes the upper-hole set from the four
targets in (6.1) to precisely the six targets in (7.2)--(7.3).

### Lemma 7.1 (one-bridge obstruction)

If a rank-eight set (D) between (P,Q) preserves both donor q1 colours,

\[
 P\vee D=\texttt{0xc379},\qquad
 D\vee Q=\texttt{0xe279},
\tag{7.4}
\]

then (D=C).

#### Proof

Equations (7.4) imply

\[
 D\subseteq\texttt{0xc379}\cap\texttt{0xe279}=C.
\]

Both (D) and (C) have rank eight, so equality follows.  Since the
ghost-free target schedule has only one (C)-owner, a different single
bridge cannot preserve both donor colours.  A second bridge or a closed
alternating circulation is necessary.

### Theorem 7.2 (exact two-window realization after gap transport)

Let (T'_0,\ldots,T'_{12872}) be the commutated target order.  Define

\[
 q_0=T'_0,\qquad q_i=T'_{i-1}\cap T'_i\quad(i\geq1).
\tag{7.5}
\]

Then

\[
 q_i\vee q_{i+1}=T'_i\quad(0\leq i<12872),
\qquad q_{12872}=T'_{12872}.
\tag{7.6}
\]

The cell-rank histogram is

```text
rank 6: 3,   rank 7: 12866,   rank 8: 4.
```

Thus the new middle schedule is literally feasible with the same length;
deadline feasibility is not the obstruction.  The explicit (q)-word is
not universal: it has 14,897 holes, including the lower rank-seven holes
`0x4879` and `0xc269`.  A lower compiler remains essential.

## 8. The second 2-opt commutator

In the order after (7.1), cut the edges

\[
 (\texttt{0x4379},\texttt{0x6279}),\qquad
 (\texttt{0xc371},\texttt{0xe269})
\tag{8.1}
\]

and reverse the intervening segment.  The new edges are

\[
 (\texttt{0x4379},\texttt{0xc371}),\qquad
 (\texttt{0x6279},\texttt{0xe269}),
\tag{8.2}
\]

whose unions are `0xc379` and `0xe279`.  Exact arbitrary-width upper replay
then leaves only

\[
          \texttt{0x6379},\qquad
          \texttt{0xe379}=\texttt{0x6379}\cup\{\texttt{0x8000}\}.
\tag{8.3}
\]

These are precisely the two unions removed at the cuts in (8.1).  The
canonical pair-intersection cells (7.5) fail (7.6) at exactly two positions:

```text
target 0x4379: covered 0x4371, missing bit 0x0008;
target 0x6279: covered 0x6269, missing bit 0x0010.
```

Thus the four-hole upper obstruction has become a two-cut-union debt plus a
two-bit endpoint collar.

### Theorem 8.1 (the natural middle-perfect closure exports two staircases)

In this twice-commutated order, make the non-inverse 2-opt cut

\[
 (\texttt{0x4373},\texttt{0x4379}),\qquad
 (\texttt{0x7269},\texttt{0x6279})
\tag{8.4}
\]

and reverse the intervening block.  The terminal four-state chain becomes

\[
 \texttt{0xc371}-\texttt{0x4379}-
 \texttt{0x6279}-\texttt{0xe269}.
\tag{8.5}
\]

Its three edge unions are

\[
             \texttt{0xc379},\quad
             \texttt{0x6379},\quad
             \texttt{0xe279},
\]

and the first three states have union `0xe379`.  Hence (8.5) restores both
targets in (8.3).  It also repairs both middle turn equations: the common
intersection of `0x4379` and `0x6279` supplies the missing bits `0x0008`
and `0x0010`.  Exact replay has no two-window middle failure.

Nevertheless the new target order has exactly four arbitrary-width upper
holes,

\[
 \boxed{
 \texttt{0x437b}\subset\texttt{0x537b},\qquad
 \texttt{0x7279}\subset\texttt{0x7a79}.}
\tag{8.6}
\]

#### Proof

Before (8.4), the four rows in (8.6) have the unique occurrences

```text
0x437b [5287,5288]     0x537b [5286,5288]
0x7279 [11725,11726]   0x7a79 [11724,11726].
```

They are exactly the two length-one and length-two exterior staircases at
the cut edges.  The new left seam has union `0x737b`, containing
`0x2000` outside the left staircase, while the new right seam has union
`0x6379`, containing `0x0100` outside the right staircase.  Thus no interval
crossing a new seam can reproduce a row in (8.6).  Reversal preserves the OR
of intervals wholly internal to the moved block, and the listed old
occurrences were unique.  All four rows are therefore absent.  Deterministic
arbitrary-width replay proves that there are no further upper holes and
verifies the middle equations stated above.

More generally, a 2-opt that cuts two globally unique nested exterior
staircases and whose new seam unions each contain a contaminant outside the
corresponding larger row necessarily exports both staircases.  Theorem 8.1
is a scoped obstruction to this exact natural closure, not to every possible
third commutator.  It shows why duplicate outside witnesses in the cut halo
are a genuine capacity requirement.

### Corollary 8.2 (sharp direct-join 2-opt obstruction)

Among single segment reversals that repair both endpoint bits by directly
joining `0x4379` to `0x6279` while retaining one linear path, the minimum
upper defect is four.

#### Proof

There are only two path-preserving 2-opt pairings.  Cutting the two incoming
edges is Theorem 8.1 and has exactly four holes.  Cutting the two outgoing
edges is the inverse of the first 2-opt; it restores the six donor-staircase
holes (7.2)--(7.3).  Either mixed-side pairing closes one side into a cycle
instead of one path.  Thus the two legal direct-join reversals have defects
four and six.  This does not exclude a reversal using a different opposing
provider pair or a higher-order braid.

## 9. Witness-complete provider circulation

The common-(Q) theorem must be stated on physical cell indices, not merely
as an abstract count of target-order occurrences.  Let (E_p) be the allowed
nonempty envelope at cell position (p), and let

\[
             \mathcal A=\{(I_\alpha,T_\alpha)\}
\]

be a selected family of **physical** contiguous intervals and their required
OR targets.  Put

\[
 Q_p=E_p\cap\bigcap_{\alpha:p\in I_\alpha}T_\alpha,
\tag{9.1}
\]

where an unused intersection is the full ground set.  Fixed cells are
encoded by singleton equality rows.

### Theorem 9.1 (exact common-envelope realization)

There exist nonempty cells (x_p\subseteq E_p) satisfying

\[
                       \bigvee_{p\in I_\alpha}x_p=T_\alpha
                       \quad(\alpha\in\mathcal A)
\tag{9.2}
\]

if and only if

\[
 Q_p\ne\varnothing\quad\text{for every }p,
 \qquad
 \bigvee_{p\in I_\alpha}Q_p=T_\alpha
                       \quad(\alpha\in\mathcal A).
\tag{9.3}
\]

When (9.3) holds, the maximal assignment (x_p=Q_p) is a solution.

#### Proof

Any solution has (x_p\subseteq Q_p), so its row equality forces the second
condition in (9.3), and nonempty cells force the first.  Conversely, the
maximal assignment is nonempty and (9.3) gives every row equality.

The atlas must be witness-complete for the conclusion sought.  Counting an
“unaffected” witness outside (\mathcal A) is not enough: maximalizing cells
can destroy an undeclared interval.  One must either include that physical
interval in (\mathcal A), or freeze all of its cells by their envelopes.

### Lemma 9.2 (linear target-order lifting)

Suppose physical cells (x_0,\ldots,x_{n-1}) and middle targets
(T_0,\ldots,T_{n-1}) obey

\[
 T_i=x_i\vee x_{i+1}\quad(0\leq i<n-1),
 \qquad T_{n-1}=x_{n-1}.
\tag{9.4}
\]

Then every nonwrapping target-order interval lifts literally:

\[
 \bigvee_{i=a}^b T_i=
 \begin{cases}
  \bigvee_{p=a}^{b+1}x_p,&b<n-1,\\
  \bigvee_{p=a}^{n-1}x_p,&b=n-1.
 \end{cases}
\tag{9.5}
\]

#### Proof

Expand (9.4); every interior cell is repeated under OR and idempotence
removes the repetitions.  The terminal formula uses the boundary singleton.

Thus an upper-complete **linear** target order plus exact middle turns gives
literal middle and all-upper coverage.  It gives no lower coverage.  Cyclic
occurrences wrapping the eventual opening do not count unless a boundary
cell is duplicated explicitly.

### Corollary 9.3 (conditional closed braid)

A rethreaded K16 target order yields a universal physical word if all of the
following hold:

1. it retains every middle owner and has a selected nonwrapping occurrence
   of every strict-upper target;
2. the physical atlas contains every middle row in (9.4), the terminal row,
   and one selected lower/compiler interval for every lower target;
3. the allowed envelopes and this complete atlas satisfy (9.3).

Indeed Theorem 9.1 realizes all middle and lower rows, and Lemma 9.2 lifts
the selected target-order occurrences to all upper rows.

For the order after the first 2-opt, the common-envelope test cannot repair
the two missing endpoint bits without changing the target incidences.  The
middle rows force

\[
 x_i\subseteq T_{i-1}\cap T_i,\qquad
 x_{i+1}\subseteq T_i\cap T_{i+1},
\]

so necessarily

\[
                         T_i\subseteq T_{i-1}\cup T_{i+1}.
\tag{9.6}
\]

At `0x4379`, bit `0x0008` is in neither neighbor; at `0x6279`, bit
`0x0010` is in neither neighbor.  A further target-order rethread is forced.
The natural rethread of Theorem 8.1 fixes (9.6), but loses the four upper
rows (8.6), and by Lemma 9.2 no alternative cell assignment on that fixed
order can restore them.

Accordingly, a concrete sufficient continuation is a further open-path
circulation which:

* changes both opposing-bit incidences so (9.6) holds everywhere;
* retains outside nonwrapping witnesses for every deleted upper halo, or
  creates replacements (including both nested staircases in (8.6)); and
* passes the witness-complete common-envelope test with one interval for
  every lower target.

This is a conditional sufficient template, not a proof of existence or
minimality.  It precisely separates the remaining upper-reserve problem
from the simultaneous lower compiler.

## 10. Audit artifacts

Authenticated inputs:

* `scratch/k15_batch_parents_20260730.audit.json`, SHA-256
  `8c005e42d6185e691a27772b1b70d8950becf85a191535bda13185476570717f`;
* `scratch/k16_repeatfree_projected_D0_20260730/best_projected.word`,
  SHA-256
  `b394211dc3483cd0596a63fc66a960db7593d49078e90062935b6cc3cf99d448`;
* `scratch/k16_repeatfree_projected_D0_20260730/zeroports.tsv`, SHA-256
  `cfad9793861990c876b559c846e620f6b48b43e837558522314aafee13fb96a6`;
* `scratch/k16_repeatfree_projected_D0_zeroport_one_sub_20260730.audit.json`,
  SHA-256
  `f922ccd695101fa54f805923634f2e43125c044cdda30be72d79f6747e11d034`;
* `scratch/k16_ghostfree_p12827_schedule_20260730.audit.json`, SHA-256
  `cefa500933ddcc67c1ee553265164127598d39217d433ca59638e3c1762a14ee`;
* `scratch/k16_ghostfree_schedule_forced_upper_nogo_20260730.audit.json`,
  SHA-256
  `ad51e658059be6af7d3b4b7b9a34488b843fbe7bcfd7f6cf08b50b0e47aadb9b`.

New lightweight audits:

* `scratch/audit_k16_repeatfree_D0_zero_diamond_20260730.py` and
  `scratch/k16_repeatfree_D0_zero_diamond_20260730.audit.json`, with file
  SHAs `ec599189b3e8b3e723dc28f3200f447d9e7074cd1256464913dd226bd056009c`
  and `c643c45a8b370d6b9852e9ecc48f4672c30c50168923b06c5cc24cfdf91024ec`;
* `scratch/audit_k16_ghostfree_fourhole_core_relocation_20260730.py` and
  `scratch/k16_ghostfree_fourhole_core_relocation_20260730.audit.json`, with
  file SHAs `b0bd875944f297c9c24a94dd047a65afb34b99b1fb2a3e7ecfaddccb1045d05f`
  and `eec44b5bb8fd1b36b6acbe7554753fbf09514932b92d98fe8b4e933c31dece03`;
* `scratch/audit_k16_ghostfree_c279_gap_commutator_20260730.py` and
  `scratch/k16_ghostfree_c279_gap_commutator_20260730.audit.json`, with file
  SHAs `8b5a5e19f03c6fcb28fdc1058072f2d196952ad39908d21c8bdf6385dc7e3c45`
  and `c4a64757573ba4372026c2bd8a23e91be9171523fce1228ec0773bbd73030b91`.

The first new audit verifies the reserve numbers, the 520 helper count, the
zero-diamond drift, and the failed contaminant erasure.  The second verifies
literal recovery of the four upper masks and the 30-hole collateral.  The
third independently replays the target-order relocation, the six unique
donor staircases, the exact two-window realization, the 2-opt compression to
two upper holes, and the two remaining endpoint bits.  Its v2 extension also
verifies the unique two-cut staircases, the middle-perfect direct-join
closure, and its exact four-hole export (8.6).  The three JSON payload hashes
are self-consistent after serialization.

No SAT, exhaustive neighborhood search, web access, or remote computation
was used for this note.  The new scripts perform only deterministic replay of
the theorem-forced moves.
