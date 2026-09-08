# Complete-reversal reset rail: sharp opening collateral, exact Ferrers payment,
# and the one-oriented quotient host gate

**Date:** 2026-08-01  
**Lane:** AD, direct literal fusion / exterior chronology  
**Status:** exact synthesis of the authenticated complete-reversal packet,
the frozen sharp linearization-collateral theorem, and the unconditional q1
host, now formulated modulo the frozen global-reversal induction gauge.
Same-edge reversal is exact internally, but every bare source cut loses at
least \(d(2d-1)\) cyclic OR values.  For \(d\ge2\), even the forward
\(d\)-cell restitution tail leaves at least \(d(d-1)/2\) such values
unsupported.  Whole-copy reflection transports one completed oriented word
and all of its certificates exactly; it does not create the missing
witnesses.  The frozen \(d\)-overlap/Ferrers theorem now supplies those
witnesses locally using \(O(d)\) protected owner positions and, once those
slots are embedded in the unavoidable global source budget, zero added
source letters.  This note keeps the **global embedding** of the packet and
twin bank into one oriented upper-surjective carrier, one-oriented residual
compilation, and regeneration explicitly open.  No fixed-address
cross-phase compiler intersection is required.

## 0. Input and verdict

Use the packet in

```text
MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md
SHA-256 f2a1c1bedcd58ce74c9c1b983affb2995a07d4fe73017e74e939dc6c5e0f8ac0
```

with its stated safe hypotheses

\[
                         r\ge 2d+2,
 \qquad                  k-r\ge 2d+1.                       \tag{0.1}
\]

It gives a simple rank-\(r\) Johnson cycle

\[
                         Z=(Z_0,\ldots,Z_{M-1}),
 \qquad                  M=4d+2,                              \tag{0.2}
\]

whose opposite phase is the complete reversal, whose immediate lower and
upper palettes are simple, whose positive runs have length at least
\(d+1\), and whose maximal cyclic depth-\(d\) antecedent is nonempty.

We also use the frozen sharp cut theorem

```text
MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md
SHA-256 4dd51e428d3d94dfc881a154567bed417451e66617a9427d8e4e18d60d2752f1
```

and the unconditional phase-common q1 host theorem

```text
MATH_THEOREM_RESET_OPEN_PATH_PHASE_COMMON_Q1_HOST_20260801.md
```

Finally, orientation is quotiented by the frozen theorem

```text
MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md
SHA-256 a93aae5224bf520be31ed180f22ec2855ae36268d85e2aba32603f2b9678e022
```

The local cut payment is the frozen theorem

```text
MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md
```

The exact direct-fusion verdict is the following.

1. Opening the same undirected edge in the two orientations gives two
   literal reverse Hamilton paths on the packet roots.  Their surviving
   linear owner/source inventories agree phasewise.
2. This agreement is not completeness.  Every bare cut loses at least
   \(d(2d-1)\) internally unique source-OR values, with an exact rank
   histogram.  For \(d\ge2\), the forward \(d\)-cell restitution tail
   still loses at least \(d(d-1)/2\) of them.
3. At the owner-sequence level, the natural cut has \(\Theta(d)\) genuine
   prefix/suffix union states.  At the literal source level, the quadratic
   cut theorem is the decisive unconditional no-go.
4. If the two exterior pieces and the packet arise from one concrete
   source word and are exchanged and reversed together, the whole composite
   is a literal reversal.  Every deck and run already present transports
   exactly, but missing cyclic packet targets remain missing.
5. Full packet support survives exactly when every value lost at the cut
   has a nonwrapping ambient witness outside the surviving packet-internal
   cells.  Under whole-copy reflection this condition need be checked in
   only one phase.
6. The coefficient-one \(d\)-overlap has an exact leave of two upper
   Ferrers triangles, totalling \(d(d+1)\) targets.  Explicit \(2d\)- and
   \(3d\)-owner Johnson banks cover all of them with simple disjoint q1
   resources.  This is a local \(O(d)\)-owner payment which costs no letters
   beyond the global owner/source budget after slot embedding; it is not yet
   a global host embedding.
7. Complete reversal of the closed packet, or of the already joined
   composite, changes no undirected support and therefore has component
   change zero.  Planting/opening the packet can join components; its phase
   reversal cannot do so by itself.
8. In an existential reversal-closed induction, one complete oriented
   source/witness/compiler certificate suffices; its reverse is obtained
   functorially.  A fixed-address matching in the intersection of the two
   phase graphs is unnecessary.  With \(c>1\) independently orientable
   components, however, global reversal removes at most one binary choice;
   when component labels are fixed, \(c-1\) relative phase bits remain.

Thus cyclic residence and phasewise internal transport are closed, and the
linear support debt has an exact local twin-bank payment.  The remaining
state is a protected packet-plus-bank embedding/joining state with exterior
witnesses and one terminal compiler, not another search for a favourable
packet cut.

## 1. Same-edge opening and literal source

Open the undirected edge \(Z_{M-1}Z_0\).  The two owner paths are

\[
 P^+=(Z_0,Z_1,\ldots,Z_{M-1}),\qquad
 P^-=(Z_{M-1},Z_{M-2},\ldots,Z_0)=\operatorname{rev}P^+.
                                                               \tag{1.1}
\]

This convention is load-bearing.  Basing both directed cycles at \(Z_0\)
would open two different undirected edges.

### Theorem 1.1 (exact linear packet)

The two paths in (1.1):

* use the same \(M\) distinct roots;
* use the same \(M-1\) distinct lower colours and the same \(M-1\)
  distinct upper colours, namely all packet edge colours except those of
  the cut edge;
* have identical multisets of internal contiguous unions at every width;
  and
* have identical internal coordinate-run inventories, with their two
  endpoint states exchanged.

#### Proof

The two lists contain the same roots in reverse order.  Their internal
edges are the same undirected cycle edges except for the common deleted
edge, so their lower and upper palettes agree occurrence by occurrence.
Reversal maps an interval \([a,b]\) to
\([M-1-b,M-1-a]\) and preserves its family of root sets.  It therefore
preserves the union and every coordinate trace.  \(\square\)

Let

\[
 A_j^+=\bigcap_{t=j-d}^{j}Z_t                              \tag{1.2}
\]

be the cyclic maximal antecedent, with indices modulo \(M\).  The frozen
packet theorem proves

\[
 D^dA^+=Z^+,
 \qquad A_i^-=A_{d-i}^+.                                  \tag{1.3}
\]

### Theorem 1.2 (exact linear antecedent and restitution charge)

The literal word

\[
 \widetilde A^+
  =(A_0^+,\ldots,A_{M-1}^+,A_0^+,\ldots,A_{d-1}^+)          \tag{1.4}
\]

has length

\[
                              M+d=5d+2                      \tag{1.5}
\]

and satisfies

\[
                              D^d\widetilde A^+=P^+.        \tag{1.6}
\]

Its literal reversal generates \(P^-\).  At derivative depth
\(0\le q<d\), linearization has exactly \(d-q\) wrap-restoration cells
which are absent from the cyclic row inventory.  Across all proper lower
derivative depths their total occurrence charge is

\[
                    \sum_{q=0}^{d-1}(d-q)
                    ={d(d+1)\over2}.                       \tag{1.7}
\]

#### Proof

Every one of the \(M\) consecutive length-\(d+1\) windows of (1.4) is
the corresponding cyclic window of \(A^+\), proving (1.6).  Reversal
commutes with a fixed-length sliding union after reversing the window
index, proving the opposite phase.  At depth \(q\), a linear word of
length \(M+d\) has \(M+d-q\) cells, while the cyclic row has \(M\)
occurrences.  Their difference is \(d-q\); summing gives (1.7).
\(\square\)

The last \(d\) source positions in (1.4) are not free.  They must be
overlapped with an ambient source chain or charged to the boundary
compiler.  Cyclic literalness alone does not erase them.

### Theorem 1.3 (exact forced loss after a cyclic restitution tail)

Fix a cut of the cyclic source word \(A\), write the resulting order as
\(A_0,\ldots,A_{M-1}\), and append its first \(\ell\) cells, where
\(0\le\ell\le2d-1\).  Among the short cyclic values supplied by intervals
of widths \(2,\ldots,2d\), the number still absent from the extended linear
word is exactly

\[
 \sum_{w=2}^{2d}\max\{0,w-1-\ell\}
      =\binom{2d-\ell}{2}.                                \tag{1.8}
\]

These values are pairwise distinct and have no cyclic witnesses of another
width.  In particular:

* the bare cut \(\ell=0\) loses \(d(2d-1)\) such values;
* the forward owner-exact restitution tail \(\ell=d\) in (1.4) still
  loses at least

  \[
                         \binom d2={d(d-1)\over2}          \tag{1.9}
  \]

  distinct values; at rank \(r+u\) it loses exactly \(u\) members of this
  forced family, for \(1\le u\le d-1\); and
* a one-sided copy of consecutive cyclic source cells cannot restore the
  entire forced short family unless \(\ell\ge2d-1\).

The word with \(\ell=d\) has exactly \(M\) depth-\(d\) owner windows.
Taking \(\ell=2d-1\) instead creates \(d-1\) additional owner-window occurrences,
so the latter is not an owner-neutral local repair.  Formula (1.8) is only
the exact short-family ledger; additional long-interval losses may remain.

#### Proof

A width-\(w\) cyclic interval crossing the cut consists of a nonempty
pre-cut suffix followed by \(b\) after-cut cells, where
\(1\le b\le w-1\).  The appended tail reproduces it exactly iff
\(b\le\ell\).  Hence precisely
\(\max\{0,w-1-\ell\}\) crossing intervals of width \(w\) remain absent.
The short-interval injectivity theorem in the frozen collateral note says
that all these OR-values are distinct and have no witness of another width.
Every interval of the extended word of length at most \(M\) projects to a
cyclic interval; an interval longer than \(M\) contains the full cyclic
support and cannot equal one of these short values.  Thus no new alternate
witness was omitted from the count.  Summing gives (1.8).  With
\(\ell=d\), put \(w=d+1+u\); the
source-cell rank is \(r-d\), so the lost value has rank \(r+u\), and its
multiplicity is \(u\).  Finally a length-\(M+\ell\) source word has
\(M+\ell-d\) depth-\(d\) windows, proving the owner-occurrence statement.
\(\square\)

Thus the occurrence restitution charge (1.7) and the target-support debt
(1.8) are different ledgers.  The former makes every desired packet owner
literal; it does not make the opened packet's cyclic OR deck complete.

The later Ferrers construction uses the oppositely placed coefficient-one
overlap
\[
 (A_{M-d},\ldots,A_{M-1},A_0,\ldots,A_{M-1}),             \tag{1.10}
\]
not a lucky bare cut.  It also has exactly \(M\) depth-\(d\) owner windows.
Its remaining support debt is classified completely and paid by protected
ambient owners in Theorem 4.6 below.  This does not contradict Theorem 1.3:
the cut collateral remains real, but it is deliberately duplicated inside
the coefficient-one owner budget.

## 2. The natural-cut source transporter

Use the notation of the frozen packet.  The reset has permanent core
\(K\), private cyclic coordinates
\(X_0,\ldots,X_{2d+1}\), seam coordinate
\(\delta=X_d\), and return exchanges
\(x_1,\ldots,x_d\in K\).  Put

\[
 H_i=X_i\quad(0\le i<d),
 \qquad K_0=K\setminus\{x_1,\ldots,x_d\}.                  \tag{2.1}
\]

At the natural cut \(Q_{d-1}E\), the first \(d+1\) cyclic erosion cells
have the exact form

\[
 A_t=K_0\cup\{\delta\}
       \cup\{x_1,\ldots,x_t\}
       \cup\{H_t,\ldots,H_{d-1}\},
 \qquad0\le t\le d.                                      \tag{2.2}
\]

### Proposition 2.1 (literal boundary/source transporter)

Every set in (2.2) has rank \(r-d\), and

\[
 A_t-A_{t+1}=\{H_t\},\qquad
 A_{t+1}-A_t=\{x_{t+1}\}
 \quad(0\le t<d).                                         \tag{2.3}
\]

Thus these \(d+1\) source states form a literal Johnson chain which
transports \((H_0,\ldots,H_{d-1})\) to
\((x_1,\ldots,x_d)\).  The appended restitution tail in (1.4) uses only
\(A_0,\ldots,A_{d-1}\); \(A_d\) is the other endpoint of the displayed
source chain.  This source transporter must not be identified with the
outgoing short *residence* bank of Theorem 3.1, which contains
\(x_1,\ldots,x_{d-1},\delta\).  It is a useful \(d\)-cell source socket,
not a constant-size one.

#### Proof

The rank calculation is

\[
 |K_0|+1+t+(d-t)=r-d.
\]

The set difference in (2.3) is immediate from (2.2).  \(\square\)

## 3. Exact residence state after opening

The closed cycle is already depth-\(d\) resident.  Opening an edge can
only split a cyclic run into endpoint-clipped pieces; hence the isolated
paths in (1.1) are resident under the clipped-path convention.  Global
concatenation removes that clipping and must be checked.

### Theorem 3.1 (natural-cut age banks)

For the plus path at the natural cut, the only positive prefix runs shorter
than \(d+1\) are

\[
 H_i=X_i\quad(0\le i<d),
 \qquad \operatorname{preAge}(H_i)=i+1.                    \tag{3.1}
\]

The only positive suffix runs shorter than \(d+1\) are

\[
 x_j\quad(1\le j<d),qquad
 \operatorname{sufAge}(x_j)=d-j,                           \tag{3.2}
\]

together with

\[
 \operatorname{sufAge}(\delta)=d.                         \tag{3.3}
\]

All other endpoint-positive runs have length at least \(d+1\).  The
reverse phase swaps prefix and suffix banks.  In particular there are
exactly \(d\) short coordinate obligations on each side.

#### Proof

The cyclic run census from the frozen theorem gives length \(3d+1\) for
the seam-intersection coordinates and selected core coordinates, and
length \(2d+1\) for \(\delta\).  Reading their positions relative to the
cut gives the split lengths in (3.1)--(3.3).  Every other cyclic run either
misses the cut or leaves a boundary piece of length at least \(d+1\).
Reversal exchanges the two ends.  \(\square\)

For a join between a left exterior word \(X\) and the packet, the exact
coordinatewise test has four cases.  If the adjacent endpoint bits are
\((1,1)\), the exterior suffix age plus packet prefix age must be at least
\(d+1\).  For \((0,1)\), the packet prefix run is bracketed at the join
and must itself have length at least \(d+1\).  For \((1,0)\), the exterior
suffix run is bracketed and must itself have length at least \(d+1\).
The case \((0,0)\) creates no positive run.  The right join has the
symmetric four cases.  Theorem 3.1 identifies every packet coordinate for
which the packet-side part of this test is nonautomatic.

## 4. Exact exterior accumulated-union current of the owner sequence

This section concerns contiguous unions in the rank-\(r\) **owner
sequence**.  It is not the literal source-word current of the antecedent
\(\widetilde A\); the latter has different prefix/suffix states and is
subject to Theorem 1.3.

The current is a gate only for a **relative** switch which reverses the
packet while holding an ordered exterior fixed.  In the
reversal-quotient route the entire exterior is reversed too, and Theorem
5.2 transports the completed word without requiring \(\Delta_w=0\).
Formula (4.2) remains necessary for named one-sided sockets and for
independent component phases not removed by the one global gauge bit.

Let \(X\) and \(Y\) be unchanged exterior owner words.  For \(j\ge1\), let
\(L_j\) be the union of the last \(j\) letters of \(X\), and let \(R_j\)
be the union of the first \(j\) letters of \(Y\).  For \(1\le t\le M\),
put

\[
 p_t=\bigcup_{i=0}^{t-1}Z_i,
 \qquad
 s_t=\bigcup_{i=M-t}^{M-1}Z_i.                            \tag{4.1}
\]

Write \([C]\) for one unit of multiset mass at mask \(C\).

### Theorem 4.1 (complete owner-level crossing-current formula)

At fixed width \(w\), replacing \(P^+\) by \(P^-\) in the unchanged
context \(X\,\square\,Y\) has signed crossing contribution

\[
 \boxed{
 \Delta_w=
 \sum_{\substack{1\le t<M\\w-t\ge1}}
 \left(
 [L_{w-t}\cup s_t]-[L_{w-t}\cup p_t]
 +[R_{w-t}\cup p_t]-[R_{w-t}\cup s_t]
 \right),}                                                \tag{4.2}
\]

where a term is retained only when the corresponding exterior suffix or
prefix exists.  Internal intervals and intervals spanning the whole packet
cancel separately.

Consequently (4.2) is a necessary-and-sufficient multiset criterion for
owner-level exterior upper-deck transparency.  A clean sufficient condition is the
pointwise mirror equation

\[
                              L_j=R_j                       \tag{4.3}
\]

for every relevant \(j\); then the two boundary currents cancel term by
term.  Matching only the endpoint owner is insufficient.

#### Proof

An interval crossing only the left boundary contains a suffix of \(X\)
and the first \(t\) packet roots.  Reversal replaces \(p_t\) by \(s_t\).
At the right boundary it replaces \(s_t\) by \(p_t\), giving the opposite
pair.  An internal interval is carried to its reversal, while an interval
meeting both exteriors contains all packet roots and hence the common total
union.  These exhaust all intervals.  \(\square\)

### Theorem 4.2 (the natural cut has a linear boundary ladder)

At the natural cut,

\[
                         p_t\ne s_t
 \quad\hbox{for }1\le t\le3d+1,                            \tag{4.4}
\]

whereas

\[
                         p_t=s_t=\bigcup_i Z_i
 \quad\hbox{for }3d+2\le t\le M.                          \tag{4.5}
\]

Thus the packet has \(\Theta(d)\) genuine owner-level exterior states.  In
the unrestricted mask-word model, if one fresh singleton letter
\(\{\eta\}\), with
\(\eta\notin\bigcup_iZ_i\), is put immediately to the left and there is
no right context, the width-\((t+1)\) deck loses
\(\{\eta\}\cup p_t\) and gains
\(\{\eta\}\cup s_t\) for each of the exactly \(3d+1\) values of \(t\)
in (4.4).  No other interval of that width contains \(\eta\).

Hence no context-independent bounded-ticket theorem follows in arbitrary
mask context from cyclic transparency.  This singleton witness is not, by
itself, a legal rank-\(r\) Johnson exterior or a certified depth-\(d\) source
chronology.  Theorem 1.3 is the unconditional literal-source no-go.

#### Proof

Starting at \(E=T_0\), the prefix first acquires the \(d+1\) reset
coordinates outside \(E\), then, after the reset plateau, acquires
\(y_1,\ldots,y_d\).  Starting from the opposite end, the suffix first
acquires \(y_{d-1},\ldots,y_1\), then \(\alpha\) and \(x_d\), and later
the remaining reset coordinates.  More explicitly, with ranks measured
above \(r\),

\[
 |p_t|-r=
 \begin{cases}
 t-1,&1\le t\le d+2,\\
 d+1,&d+2\le t\le2d+2,\\
 t-d-1,&2d+2\le t\le3d+2,\\
 2d+1,&3d+2\le t\le M,
 \end{cases}                                               \tag{4.6}
\]

and

\[
 |s_t|-r=
 \begin{cases}
 t-1,&1\le t\le d+2,\\
 d+1,&d+2\le t\le2d+1,\\
 t-d,&2d+1\le t\le3d+1,\\
 2d+1,&3d+1\le t\le M.
 \end{cases}                                               \tag{4.7}
\]

For \(t\le2d+1\), \(s_t\) contains a fresh \(y\)-coordinate while
\(p_t\) contains none, so equality is impossible.  For
\(2d+2\le t\le3d+1\), (4.6)--(4.7) give different ranks.  Both have the
complete packet support from \(t=3d+2\) onward.  This proves
(4.4)--(4.5), and the private-\(\eta\) conclusion follows because only the
left crossing interval contains \(\eta\).  \(\square\)

The private-tag example is conditional on the availability of a coordinate
outside the packet support.  The support has size \(r+2d+1\), so the
literal marker is available under \(k-r\ge2d+2\) (or after passing to a
one-coordinate extension), not under the tight equality
\(k-r=2d+1\).  It is an owner/mask-deck counterexample to an *arbitrary
unchanged exterior* theorem.  It does not rule out a legal prepared mirror
exterior, a protected duplicate witness, or a phase-dependent whole-copy
exchange.

### Theorem 4.3 (exact ambient-duplication criterion)

Let \(B_c\) be any chosen linear realization of the cyclic source packet at
cut \(c\): it may be the bare \(M\)-cell linearization or the forward
\(M+d\)-cell realization (1.4).  For each mask \(T\), put

\[
 \mu_c(T)=
 \left[
   \operatorname{mult}_{\operatorname{Deck}_{\rm cyc}(A)}(T)
   -\operatorname{mult}_{\operatorname{Deck}_{\rm int}(B_c)}(T)
 \right]_+,                                               \tag{4.8}
\]

where `int` counts intervals wholly inside the designated packet block.
Embed that block into one literal word

\[
                             W^+=X\,B_c\,Y.               \tag{4.9}
\]

Let \(N_+(T)\) count nonwrapping intervals of \(W^+\) which are not wholly
inside the packet block and have union \(T\).  Then the complete cyclic
packet deck is contained in the deck of \(W^+\), with multiplicity, iff

\[
                             N_+(T)\ge\mu_c(T)
                 \qquad\hbox{for every }T.                \tag{4.10}
\]

If

\[
                             W^- = \operatorname{rev}(W^+),\tag{4.11}
\]

then (4.10) need be checked only for \(W^+\): reversal transports every
ambient witness and every packet-internal witness bijectively.  For mere
set coverage, replace multiplicities in (4.8)--(4.10) by indicators.

#### Proof

The intervals of \(W^+\) partition into those wholly inside the designated
packet block and all remaining intervals.  Coordinatewise multiset
subtraction gives (4.10).  Reversal is a bijection on nonwrapping intervals
and preserves their unions, proving (4.11). \(\square\)

For the bare cut, the forced short family alone has
\(d(2d-1)\) distinct members, each with deficit one.  Therefore any
protected disjoint ambient bank must supply at least that many distinct
interval occurrences.  If all of them must lie inside one consecutive
\(n\)-letter bank, then

\[
 {n(n+1)\over2}\ge d(2d-1),
 \qquad\hbox{hence}\qquad n\ge2d-1.                       \tag{4.12}
\]

For the forward \(d\)-cell restitution word, its still-forced family in
(1.9) similarly requires at least \(d-1\) positions in any single
standalone consecutive bank, by interval-counting.  These are capacity
lower bounds, not constructions: arbitrary intervals of a bank need not
have the required masks, and occurrence-labelled cap use still requires its
own Hall audit in the chosen orientation.  A fixed-address cap common to
both phases is needed only for a local relative-phase switch, not for
global reflection.

### Proposition 4.4 (two antipodal cuts cover the forced short family)

At the abstract deck level, two copies of the cyclic source word cut at
antipodal boundaries \(c\) and \(c+(2d+1)\) cover every cyclic interval of
width at most \(2d\) internally in at least one copy.  Thus two
linearizations are necessary and sufficient to cover the complete forced
short family by cut duplication.

#### Proof

One linearization misses the nonempty family in Theorem 1.3.  A cyclic
interval of width at most \(2d\) contains at most \(2d-1\) internal
boundaries, so it cannot cross two boundaries at cyclic distance \(2d+1\).
It therefore survives in at least one of the antipodal linearizations.
\(\square\)

Proposition 4.4 is not yet a physical coefficient-one lift.  Two literal
copies repeat the packet owners and palettes.  It identifies the exact
deck-level duplication architecture which an owner-disjoint quotient weave
or an already-present ambient witness bank would have to realize.

### Theorem 4.5 (direct screened socket and its flat-length obstruction)

Let the cyclic source cut lie between adjacent cells \(A_{c-1},A_c\), and
put

\[
                              B=A_{c-1}\cup A_c.           \tag{4.13}
\]

Insert a source connector \(G=(G_1,\ldots,G_g)\) of nonempty letters
between these cells.  If

\[
                              G_i\subseteq B
                    \qquad(1\le i\le g),                 \tag{4.14}
\]

then every cyclic interval crossing this cut has its OR-value restored:
replace its old suffix--prefix witness by the same suffix, all of \(G\),
and the same prefix.  The OR is unchanged.  Its new witness is \(g\) cells
longer, so this is an ungraded target-coverage statement, not equality of
the width-graded deck unless \(g=0\).

Conversely, restoring the unique cyclic width-two target \(B\) by this
direct boundary-spanning witness forces (4.14).  For \(d\ge2\), if the
surrounding source is required to have every depth-\(d\) owner of rank
\(r\), then necessarily

\[
                              g\le d-2.                    \tag{4.15}
\]

#### Proof

Every old crossing interval contains both endpoint cells, hence contains
\(B\).  Adding letters satisfying (4.14) changes none of its unions.  For
the converse, the direct witness for the width-two target contains
\(A_{c-1},G_1,\ldots,G_g,A_c\); equality with \(B\) forces every inserted
letter to lie in \(B\).

The adjacent source cells have rank \(r-d\) and differ by one exchange, so

\[
                              |B|=r-d+1<r.                 \tag{4.16}
\]

If \(g\ge d-1\), the \(g+2\) consecutive cells
\(A_{c-1},G_1,\ldots,G_g,A_c\) contain a length-\(d+1\) window wholly in
\(B\).  Its union has rank at most \(r-d+1<r\), contradicting flat
rank-\(r\) depth-\(d\) legality. \(\square\)

Condition (4.15) is necessary, not sufficient: for a shorter connector all
crossing owner windows, Johnson adjacencies, palettes, and residence still
require literal checking.  In particular, the arbitrary long residual path
given by the unconditional q1 host is not automatically a screened source
socket.  It must instead provide ambient duplicates, use a nonflat actuator,
or participate in a larger reflected word.  Theorem 4.6 takes the first
route: its Ferrers banks are ambient witnesses, not a direct connector
through the cut.

### Theorem 4.6 (exact Ferrers twin-bank discharge)

Use the sharp source normal form with a permanent set \(H\) of size
\(h\ge4\), so

\[
 r=h+2d+1,\qquad
 \Omega=H\mathbin{\dot\cup}X\mathbin{\dot\cup}C
 \mathbin{\dot\cup}U\mathbin{\dot\cup}Y
 \mathbin{\dot\cup}\{\alpha,\delta\}.                     \tag{4.17}
\]

For the coefficient-one overlap (1.10), all \(M=4d+2\) packet owners occur
exactly once, every target of rank at most \(r\) survives, and the complete
remaining set leave is the disjoint union

\[
 {\cal F}_X=
 \{B_X\cup X[1,i]\cup X[j+2,d]:0\le i\le j<d\},           \tag{4.18}
\]

\[
 {\cal F}_U=
 \{\Omega\setminus U[i+1,j+1]:0\le i\le j<d\},            \tag{4.19}
\]

where

\[
 B_X=H\cup C\cup Y\cup\{\alpha,\delta\}.                  \tag{4.20}
\]

Each family has \(\binom{d+1}{2}\) targets.  At rank \(r+t\),
\({\cal F}_X\) has \(t\) targets; at rank \(r+d+t\),
\({\cal F}_U\) has \(t\) targets, for \(1\le t\le d\).  Thus the exact
leave has size

\[
                              d(d+1).                     \tag{4.21}
\]

There are explicit Johnson paths \({\cal P}_X,{\cal P}_U\) on \(2d\) and
\(3d\) rank-\(r\) owners respectively such that their interval unions cover
\({\cal F}_X\) and \({\cal F}_U\).  Four markers in \(H\) make:

* all \(5d\) bank owners distinct and disjoint from all packet owners;
* all \(5d-2\) lower-q1 bank colours distinct; and
* all \(5d-2\) upper-q1 bank colours distinct, with no collision against
  the surviving opened-packet upper palette.

Every non-boundary positive run in either bank already has length at least
\(d+1\).  The four exact boundary profiles are:

* \({\cal P}_X\)-left: \(\eta_2\) debt \(1\), and \(x_s\) debt \(s+1\)
  for \(1\le s<d\);
* \({\cal P}_X\)-right: \(\eta_1\) debt \(1\), and \(x_s\) debt
  \(d+2-s\) for \(2\le s\le d\);
* \({\cal P}_U\)-left: \(\eta_3\) debt \(1\), and \(u_j\) debt \(j+1\)
  for \(1\le j<d\);
* \({\cal P}_U\)-right: \(\eta_4\) debt \(1\), and \(u_j\) debt
  \(d+2-j\) for \(2\le j\le d\).

Thus two one-sided Ferrers collars of at most \(d\) roots suffice only in
the endpoint-bank layout where \({\cal P}_X\)-left and
\({\cal P}_U\)-right are the two globally clipped ends (or receive certified
exterior continuation); the two inward-facing ends are collared.  Conditional
on explicit simple/disjoint collars and \(d\) private filler labels, this
layout uses at most \(7d\) bank owners.  If both banks must be internal or
cyclic with no exterior continuation, four collars are required, giving at
most \(9d\) bank owners.  Once embedded consecutively in one resident owner
chronology, maximal erosion turns every bank owner interval into a literal
source-interval witness.

The raw packet plus bank ledger is

\[
 \begin{array}{c|c}
 \text{owners}&9d+2\\
 \text{distinct lower adjacencies}&9d-1\\
 \text{distinct upper adjacencies}&9d-1.
 \end{array}                                               \tag{4.22}
\]

Among the bank upper colours, exactly one equals the packet's omitted upper
edge colour; every bank upper colour lies outside the surviving packet
upper palette.  Hence the full packet upper-q1 set is restored.  The
omitted packet lower adjacency is not
restored as an adjacency by this statement; its target value survives in
the source deck and its factor occurrence belongs to the residual q1
completion.

At the owner/lower-q1 level, specialize to the middle-levels setting
\(r=m\) in \(ML_m\).  The opened packet plus the two collared banks has at
most \(11d-1\) protected Johnson edges in the endpoint-bank/two-collar
layout, hence at most \(22d-2\) protected incidence edges of maximum degree
two; its protected vertex ledger has at most \(11d+2\) owners and at most
\(11d-1\) lower colours.
Conditional on the explicit collar/endpoint layout, the
fixed-protected-subgraph extension theorem therefore gives a spanning q1
two-factor whenever

\[
                              m\ge22d.                     \tag{4.23}
\]

With four collars and both banks internal, the corresponding upper bounds
are \(13d-1\) Johnson edges and \(26d-2\) incidences, giving the sufficient
threshold \(m\ge26d\).  The raw bank is invariant under complete reversal.  In the
quotient formulation it is enough to embed and compile one orientation;
the reverse certificate is automatic.

#### Proof

The owner statement is Theorem 2.1 of the frozen \(d\)-overlap theorem.
Its four-block interval classification gives (4.18)--(4.21) and proves
there is no lower or middle leave.  Its explicit \(X\)-gap path and
\(U\)-gap path give the two interval banks.  Their four-marker signatures
prove owner and q1 disjointness.  The internal run census and the nested
one-sided boundary profiles give the displayed collar alternatives.
Counting the protected incidences gives (4.23) and its four-collar analogue;
the protected-factor theorem supplies the conditional q1 extensions.
Reversal preserves the two complete gap families and transports every
witness. \(\square\)

Theorem 4.6 is the promised local realization of the **indicator/set**
version of criterion (4.10).  It pays the quadratic target count with only
\(O(d)\) reserved owner positions and
no positions beyond the unavoidable global \(W+d\) source budget after
slot embedding.  Those owners must still be selected inside the
ambient coefficient-one carrier and the bank paths must occur in a literal
resident chronology before their interval witnesses exist.  Mere
owner/lower-q1 factor containment is insufficient.  The theorem does not
join the three paths, preserve arbitrary exterior witnesses, give global
upper surjectivity, or construct a terminal compiler.

## 5. Topology and the exact whole-copy positive theorem

The closed packet and its reversal have identical undirected support.

### Proposition 5.1 (no intrinsic fusion)

Complete reversal changes the packet component count by zero.  More
generally, reversal of any already selected simple cycle changes neither
its weak component nor its length.  Therefore the complete-reversal packet
has no intrinsic graphic-rank or Hall gain.

Opening one edge turns the packet into a path.  Planting that path between
two already exposed paths can join them, but this gain comes from the two
new exterior joins, not from phase reversal.

### Theorem 5.2 (whole-copy guarded fusion)

Let \(X\) and \(Y\) be two directed Johnson paths, and let \(P=P^+\) be
the opened reset--return packet.  Assume:

1. the owner sets of \(X,P,Y\) are pairwise disjoint;
2. two new Johnson join edges make \(C^+=X\,P\,Y\) one simple path;
3. all immediate lower and upper colours in \(C^+\) are distinct; and
4. there is one concrete literal source word \(B^+\) such that
   \(D^dB^+=C^+\), with the required flat ranks and strict join residence.

Then

\[
 C^+=X\,P\,Y,
 \qquad
 C^-=\operatorname{rev}(Y)\,\operatorname{rev}(P)\,
                  \operatorname{rev}(X)
       =\operatorname{rev}(C^+).                            \tag{5.1}
\]

These are simple owner-path phases on the same owner set and with the same
immediate palettes.  Moreover

\[
                              B^-=\operatorname{rev}(B^+)  \tag{5.1b}
\]

is a literal source for \(C^-\).  The two source words and every derivative
row have identical interval-OR decks and coordinate-run inventories.  If a
common undirected closing edge is legal, the owner closures are opposite
orientations of one simple cycle.

The three paths are three components before the joins and one afterward,
so prospective planting has component change \(-2\), or \(-1\) if only the
two exterior components are charged and the prepared packet is regarded as
the connector.  Between \(C^+\) and \(C^-\), however, the component change
is zero.

In particular, two disjoint q-gon paths can be connected without repeating
an owner when they satisfy hypotheses 1--4 and are exchanged and reversed
as whole copies.  Holding the two q-gon exteriors fixed while reversing
only \(P\) is not covered and is obstructed by (4.2) and the boundary-age
banks in Theorem 3.1.  Whole-copy reversal also does not restore any cyclic
packet target absent from \(B^+\); when \(B^+\) contains the designated
linear packet block \(B_c\), exact completeness is criterion (4.10).

#### Proof

The two joins make \(X,P,Y\) one simple path.  Reversing the complete list
reverses every edge, including the joins, without changing any root, lower
colour, or upper colour.  Sliding union commutes with reversal, so
\(D^dB^-=\operatorname{rev}(D^dB^+)=C^-\).  Reversal bijects all intervals
and all coordinate runs.  The component count is immediate.  \(\square\)

This theorem is a conditional literal composition theorem, not a global
host-existence theorem.  In particular, root/palette disjointness and the
one concrete global source realization must be chosen before the packet is
contracted.  Piecewise source realizability plus endpoint age inequalities
does not imply hypothesis 4.

There is a separate shared-root gluing model: declared common endpoint
roots are identified once, rather than concatenated as repeated positions.
If the deduplicated owner list is a simple Johnson path with distinct q1
colours and has one concrete literal source \(B^+\), the reversal conclusion
still holds.  Its palette ledger must be recomputed after identification,
and no pre-identification component count is asserted.

### Corollary 5.3 (the owner/lower-q1 host is no longer existential)

The theorem

```text
MATH_THEOREM_RESET_OPEN_PATH_PHASE_COMMON_Q1_HOST_20260801.md
```

proves that, for

\[
                              m\ge8d+4,                     \tag{5.2}
\]

the common undirected incidence path of the two packet phases extends to
one spanning middle-levels two-factor.  It protects exactly

\[
 4d+2\text{ roots},\qquad4d+1\text{ lower colours},
 \qquad8d+2\text{ incidence edges}.                        \tag{5.3}
\]

Thus root and immediate-lower planting of one opened packet is
unconditional at the phase-common q1 level; the \(4d+1\) adjacent upper
labels on the protected path are also retained.  The residual component
containing the packet must reverse as a whole.  The theorem does not make
the residual factor globally upper-surjective, bounded-component, resident
at the packet joins, source-realizable, duplicate-witness protected, or
equipped with even one terminal compiler.  In particular, it does not
supply the short screened source socket of Theorem 4.5.  Failure to provide
a fixed-address compiler common to both orientations is harmless in the
global quotient mode once one oriented terminal matching has been built.

### Corollary 5.4 (one-oriented quotient host)

Assume \(m\ge22d\) in the endpoint-bank/two-collar layout (or
\(m\ge26d\) when both banks are internal and four collars are used), and
choose the corresponding protected q1 host containing the opened packet
and both Ferrers banks from Theorem 4.6.  Suppose one orientation extends
to a complete literal state

\[
 {\sf S}^+=(B^+,C^+,{\cal W}^+,{\cal M}^+,{\cal E}^+,\Xi^+) \tag{5.4}
\]

such that:

1. \(D^dB^+=C^+\) realizes the containing owner chronology with all flat,
   Johnson, palette and residence conditions;
2. \({\cal W}^+\) is a complete upper-witness bank;
3. the Ferrers intervals realize every packet cut-loss target and the
   ambient count in Theorem 4.3 covers every exterior target endangered by
   joining/opening; and
4. \({\cal M}^+\), its cap word, endpoint state and sidecar are one valid
   terminal compiler certificate.

Then global reversal gives a complete opposite representative
\({\sf S}^-={\cal R}{\sf S}^+\).  Every witness, compiler edge, cap address,
run and derivative cell is reflected bijectively.  No perfect matching in a
fixed-address intersection \(G^+\cap G^-\), no second ambient check, and no
phase-common exterior are required.

This implication constructs no \({\sf S}^+\).  It also changes neither the
opening deficit \(\mu_c\), component count, upper holes nor matching
deficiency.

If the host has \(c\) independently named component phases
\(\varepsilon\in{\mathbb F}_2^c\) and reversal fixes every component label,
then it sends \(\varepsilon\) to \(\varepsilon+\mathbf1\).  A named
requirement \(\rho\) is therefore reachable by the gauge exactly when

\[
 \varepsilon_i+\varepsilon_j=\rho_i+\rho_j
                    \qquad(1\le i,j\le c).                \tag{5.5}
\]

Thus one common orientation bit disappears and \(c-1\) relative bits
remain when every component label is fixed individually.  More generally,
if reversal permutes
component labels by an involutive permutation matrix \(P\), its action is

\[
                         \varepsilon\longmapsto
                         \mathbf1+P\varepsilon .           \tag{5.6}
\]

Then a named \(\rho\) is reachable exactly when it equals either
\(\varepsilon\) or \(\mathbf1+P\varepsilon\); reversal still removes at
most one binary choice, but the pairwise parities in (5.5) need not be
literal invariants.

More exactly, let \(P\) have \(r_0\) fixed component labels and \(s\)
transposed pairs, so \(c=r_0+2s\).  The number of affine reversal orbits is

\[
 \#\bigl({\mathbb F}_2^c/\langle\varepsilon\mapsto
       \mathbf1+P\varepsilon\rangle\bigr)
 =
 \begin{cases}
   2^{c-1},&r_0>0,\\
   2^{c-1}+2^{s-1},&r_0=0.
 \end{cases}                                               \tag{5.7}
\]

Indeed a fixed component makes the fixed-state equation
\(\varepsilon=\mathbf1+P\varepsilon\) impossible.  With only transposed
pairs, each pair has the two fixed assignments \(01,10\), giving \(2^s\)
fixed phase vectors; Burnside's formula gives (5.7).  Thus a permuting
reversal can remove strictly less than one full bit of phase information.

Likewise directed voltage changes sign: primitivity and a
\(\{\pm V\}\)-condition are quotient-invariant, while a named \(+V\)
relative to a fixed generator is not.

## 6. Exact one-oriented certificate and compiler boundary

The frozen cyclic theorem gives an isomorphism of every target--cell
incidence wholly inside the **cyclic** packet.  Theorems 1.3 and 4.3 give
the general opening deficit.  Theorem 4.6 now gives one exact local payment:
the \(d\)-overlap has no lower/middle leave, and the twin bank supplies every
upper packet target still absent.  Constructing the **one oriented plus
state** therefore has four coupled obligations:

1. realize the \(d\)-overlap and its \(d-q\) derivative restitution
   occurrences at every depth \(q<d\);
2. embed the two collared Ferrers banks so their interval witnesses pay the
   complete packet leave without losing their owner/q1/residence guards;
3. preserve or replace every old exterior/crossing witness affected when
   the three protected paths are joined; and
4. choose one occurrence-labelled terminal lower compiler and cap
   certificate compatible with all these source positions.

Once one occurrence-labelled matching and cap certificate solves these
four obligations in \(B^+\), global reversal transports it to \(B^-\).
There is no additional Hall problem on \(G^+\cap G^-\), and addresses need
not be fixed across the two representatives.

A different statement applies if the packet alone is flipped against a
frozen exterior, or if independently named component phases must coexist.
That **local relative-phase mode** does require compatibility of the two
residual boundary incidence systems, equivalently the appropriate
intersection/common-cap Hall audit after the internal matching is
contracted.  No such local common matching is claimed here.

The opening amount transported by the quotient is the cut-dependent
deficit, not one universal scalar:

\[
 \mu_{c^*}^{{\cal R}A}(T)=\mu_c^A(T),
 \qquad N_-(T)=N_+(T),                                    \tag{6.1}
\]

where \(c^*\) is the reflected cut.  Thus the \(d(2d-1)\) figure in the
global-reversal opening discussion is the **bare \(M\)-cell** ledger.  The
forward \(M+d\) antecedent (1.4) has the smaller still-forced
\(\binom d2\) family, and an arbitrary ambient overlap is governed exactly
by \(\mu_c(T)\).  Reversal preserves whichever of these debts is present;
it does not increase it back to the bare value and does not repay it.
For the protected \(d\)-overlap plus embedded twin bank, the combined
unpaid set deficit \([\mu_c(T)-N_+(T)]_+\) is zero on every packet target.
The packet's internal \(\mu_c\) itself is not erased; it is paid by the
bank.  Any remaining unpaid deficit belongs to the exterior
joining/global-host operation, not to the local packet.

## 7. Precise surviving gate

The complete-reversal packet has closed the formerly local obstructions:

* no owner or immediate-palette collision;
* no cyclic residence debt;
* no phase discrepancy in the cyclic upper deck or derivative inventories;
* a phasewise isomorphism of cyclic internal compiler incidence;
* a literal one-attachment/two-predecessor return lift; and
* unconditional phase-common root/lower-q1 planting for the packet at
  \(m\ge8d+4\), and conditional protected-factor planting for the
  packet-plus-twin-bank graph at \(m\ge22d\) in the endpoint-bank layout
  or \(m\ge26d\) with four internal collars.

The cut debt remains an invariant of the opened packet, but Theorem 4.6 now
closes its **local payment** exactly.  The coefficient-one \(d\)-overlap
leaves two known upper triangles, and the \(O(d)\)-owner twin bank covers
both.  What remains is to embed and join this whole protected object inside
one global carrier without creating new exterior or compiler debt.

What remains is exactly:

\[
\boxed{
 \begin{array}{c}
 \text{construct one oriented upper-surjective host containing packet+twin bank;}\\
 \text{join its three protected paths with low component count and literal source;}\\
 \text{preserve exterior all-width witnesses and the chosen collar/global-end states;}\\
 \text{find one terminal compiler/cap matching in that orientation;}\\
 \text{regenerate the protected packet in the next same-parity step.}
 \end{array}}
\]

The first line includes the still-open rooted correlation among the lower
matching, chosen heads, and graphic basis.  The corrected
`MATH_THEOREM_HEAD_INJECTIVE_COMPLETION_AND_PROTECTED_INDUCED_PATH_20260801.md`
is used, if at all, only for its disjoint second-facet projection.  It does
not establish the fixed-\(M_0\) condition
\(M_0(\psi(R)\cap\phi(R))=\psi(R)\), and this note makes no such claim.
Nor can this row be closed by the generic degree-only rainbow shortcut:
the Wdowinski counterexamples refute that implication at the relevant
degree/colour-size threshold.  A positive host theorem must exploit the
Boolean identity and fixed-\(M_0\) correlation.

The q-port construction in
`MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md` proves that
the closed-doubleton and equal-support serial-history gates can be removed
simultaneously across all q-gon ports.  Its endpoint and middle reversal
pairs inherit the conclusions above.  For a one-component
orientation-class induction, the complete-reversal role conversion itself
is gauge and need not be executed.  The q-port/local converter remains
relevant for an actual packet-only flip, for the nonreversal
\(H_0\leftrightarrow H_1\) rethread, or for \(c>1\) components carrying
the surviving relative phase data (exactly \(c-1\) bits when their labels
are fixed individually).  The two individual q-gon
rethreads remain deeper-OR-active, so they still require a protected
compound use or external witnesses.

## 8. Audit boundary

The decisive steps were independently derived in two different forms:

* a coordinate-class replay of the reset/rail joins and complete q1
  separation; and
* a reversal/last-occurrence audit of the linear antecedent, exact
  exterior current, and natural-cut boundary ages; and
* an independent count/scope audit of the imported \(d\)-overlap and
  Ferrers-bank theorem.

No finite search is used in Sections 1--7.  The private-context no-go is a
symbolic arbitrary-mask counterexample with the stated fresh-coordinate
hypothesis; the unconditional literal-source no-go is Theorem 1.3.  Every
positive composition statement is conditional on the explicitly listed
owner, palette, source, duplicate-witness, and join-age hypotheses.  Two
independent proof audits checked the restitution ledger, the natural-cut
prefix/suffix schedules, the four-case age test, the sharp post-tail loss,
the screened-socket bound, and the topology counts.

The frozen H100 audit through \(2\le d\le40\) checks the raw Ferrers deck,
raw bank witnesses, owner/q1 collisions and internal runs.  It does not
check the collar construction, phase reversal, global host, exterior joins
or compiler.  Those conclusions use the symbolic theorems and retain the
scopes stated above.
