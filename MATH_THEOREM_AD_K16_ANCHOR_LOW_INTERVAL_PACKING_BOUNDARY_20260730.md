# K16 gap one: anchor-low interval packing boundary

Date: 2026-07-30  
Lane: AD  
Status: proved solver-free cuts and a sharp obstruction to low-only anchor
pruning; no profile SAT/UNSAT verdict and no length-12,873 word are claimed

## 1. Frozen scope

The physical source is

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

and the three fixed-gap shortening profiles are

\[
                 (4,9,4),\qquad(5,8,4),\qquad(5,9,3).
\tag{1.1}
\]

The exact 57-target repair ledger is

```text
scratch/k16_12873_three_profile_closure_model_20260730.audit.json
SHA-256 2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892
```

The imported chart-intersection theorem and its independent audit are

```text
MATH_THEOREM_AD_K16_CHART_INTERSECTION_ELIMINATION_AND_ANCHOR_PRUNING_20260730.md
SHA-256 2f52bc0bbcbc61d7ac0d22113bceb951d46610c0c526c0482160da6785f5a156

MATH_AUDIT_AD_K16_CHART_INTERSECTION_ELIMINATION_AND_ANCHOR_PRUNING_20260730.md
SHA-256 52ad1912058c0086b9e4a7cfbd6a1203d31939fe372d02fc56587c152c02ee66
```

All positions are the 17 surviving collar positions, ordered separately in
their three collars.  A selected chart for target \(T\) is denoted by
\(I_T\), and \(b_T(I_T)\) is its maximal compatible fixed context.  We use
the exact one-chart-per-target convention throughout; every feasible word
admits such a selection.  Put

\[
                         H=\mathtt{8000}.
\tag{1.2}
\]

The targets omitting \(H\) are exactly

\[
\begin{split}
\mathcal L=\{&\mathtt{142d},\mathtt{146d},\mathtt{246d},
\mathtt{286d},\mathtt{2879},\mathtt{287d},\mathtt{2c6d},
\mathtt{346d},\mathtt{4671},\\
&\mathtt{4879},\mathtt{4e71},\mathtt{4ef7},\mathtt{542d},
\mathtt{546d},\mathtt{562d},\mathtt{56ad},\mathtt{6879},
\mathtt{766d}\}.
\end{split}                                                   \tag{1.3}
\]

Thus \(|\mathcal L|=18\), while the other 38 repair targets besides \(H\)
contain \(H\).  Direct bit intersection gives

\[
       \bigcap_{L\in\mathcal L}L=\mathtt{0021},\qquad
       \bigcup_{L\in\mathcal L}L=\mathtt{7eff}.          \tag{1.4}
\]

In particular, the low family has a two-bit common core.  A counting or
Helly argument may not treat its intervals as mutually incompatible.

## 2. Exact interval cuts

The following consequences use only the already proved chart-intersection
criterion.

### Lemma 2.1 (zero-intersection Helly cut)

Let \(\mathcal Q\) be a set of selected target charts lying in one collar.
If

\[
                         \bigcap_{T\in\mathcal Q}T=0,
\tag{2.1}
\]

then the intervals \(\{I_T:T\in\mathcal Q\}\) are not pairwise
intersecting.  Equivalently, at least one pair of these charts is disjoint.

#### Proof

Finite intervals on a line have the Helly property.  If the charts were
pairwise intersecting, they would have a common collar position \(x\).  The
active-target intersection at \(x\) would then be contained in (2.1),
contradicting the nonzero-intersection condition of the exact chart theorem.
\(\square\)

### Lemma 2.2 (anchored-fan cut)

Fix a singleton \(H\)-anchor at position \(p\).  Let \(J=I_L\) be a low
chart in the anchor collar; necessarily \(p\notin J\).  Let \(\mathcal Q\)
be any family of high-target charts in that collar, all containing \(p\).
If \(J\) meets every chart in \(\mathcal Q\), then

\[
                         L\cap\bigcap_{U\in\mathcal Q}U\ne0.
\tag{2.2}
\]

Consequently, whenever the mask intersection in (2.2) is zero, \(J\) must
be disjoint from at least one chart in \(\mathcal Q\).

#### Proof

The high charts pairwise meet at \(p\), and by hypothesis \(J\) meets each
of them.  The whole interval family is pairwise intersecting, so it has a
common point.  The chart-intersection condition at that point gives (2.2).
\(\square\)

### Lemma 2.3 (durable-bit protrusion)

Suppose a high chart \(I_U\) contains the anchor \(p\), a low chart \(J=I_L\)
lies on one side of \(p\), and the two charts intersect.  If a coordinate
\(q\) satisfies

\[
                  q\in L\setminus b_L(J),\qquad q\notin U,
\tag{2.3}
\]

then

\[
                            J\setminus I_U\ne\varnothing.       \tag{2.4}
\]

Hence, if \(J\) is left of \(p\), its left endpoint is strictly left of the
left endpoint of \(I_U\); if it is right of \(p\), its right endpoint is
strictly right of the right endpoint of \(I_U\).

#### Proof

The private-bit form of the chart theorem requires a point of \(J\) not
covered by any selected chart whose target omits \(q\).  The chart \(I_U\)
is one such chart, proving (2.4).  Because \(I_U\) contains \(p\) outside
\(J\) and meets \(J\), the only possible protrusion is away from \(p\),
which gives the endpoint statement. \(\square\)

This is the exact form of the durable-bit ordering toll.  It is stronger
than merely requiring two charts to have distinct endpoints.

## 3. A two-target high fan

Two repair targets singled out by the frozen ledger are

\[
                    A=\mathtt{8c62},\qquad B=\mathtt{9009}.
\tag{3.1}
\]

They obey

\[
                         A\cap B=H.                    \tag{3.2}
\]

The four fixed boundary chains have the following states compatible with
these two targets:

\[
\begin{array}{c|cc}
\text{boundary chain}&A&B\\ \hline
\text{prefix of }G_1&\{0\}&\{0,\mathtt{1009}\}\\
\text{suffix of }G_1&\{0\}&\{0\}\\
\text{prefix of }G_2&\{0\}&\{0\}\\
\text{suffix of }G_2&\{0\}&\{0\}.
\end{array}                                             \tag{3.3}
\]

These are direct entries of the byte-pinned maximal-context ledger.  In
particular,

\[
             b_A(I)=0\quad\hbox{for every chart }I,      \tag{3.4}
\]

and \(b_B(I)\) never contains \(H\).  The value
\(b_B(I)=\mathtt{1009}=B\setminus H\) is possible only when \(I\) reaches
the right boundary of the first collar.

For a selected low-chart family put

\[
                         Z=\bigcup_{L\in\mathcal L}I_L. \tag{3.5}
\]

### Theorem 3.1 (anchor-fan gap dichotomy)

Every full 57-target chart selection satisfies

\[
             I_A\setminus Z\ne\varnothing,qquad
             I_B\setminus Z\ne\varnothing,             \tag{3.6}
\]

and

\[
                         I_A\cap I_B\subseteq P\setminus Z,    \tag{3.7}
\]

where \(P\) is the set of 17 collar positions.

If the low charts cover all positions except the chosen anchor,

\[
                            P\setminus Z=\{p\},          \tag{3.8}
\]

then

\[
                         p\in I_A\cap I_B,qquad
                         I_A\cap I_B=\{p\}.              \tag{3.9}
\]

Consequently either one of \(I_A,I_B\) is the singleton \(\{p\}\), or,
after possibly exchanging their names, one ends at \(p\) and the other
starts at \(p\); their non-anchor arms point in opposite directions.

#### Proof

Both \(A\) and \(B\) require the bit \(H\), and (3.3)--(3.4) show that no
fixed context supplies it.  Since the targets omitting \(H\) are exactly
the 18 members of \(\mathcal L\), the durable-\(H\) condition is precisely
(3.6).

If a point belonged to \(I_A\cap I_B\cap Z\), it would also belong to some
low chart \(I_L\).  But

\[
                          A\cap B\cap L=H\cap L=0,
\]

contradicting the active-intersection condition.  This proves (3.7).
Under (3.8), the two nonempty sets in (3.6) force both charts through \(p\),
and (3.7) then gives (3.9).  The final assertion is the elementary endpoint
classification of two intervals whose intersection is one point. \(\square\)

### Corollary 3.2 (five exact endpoint co-anchoring exclusions per profile)

The chart \(I_A\) can never be the singleton anchor, because its context is
always zero.  The chart \(I_B\) can be the singleton anchor only at the
rightmost cell of the first collar, where the context `0x1009` supplies its
entire low projection.

It follows that, at every collar endpoint except that one special endpoint,

\[
                     \neg\bigl(p\in I_A\ \wedge\ p\in I_B\bigr),
                                                               \tag{3.10}
\]

and consequently

\[
                              |P\setminus Z|\ge2.        \tag{3.11}
\]

In absolute zero-based positions, the five locations at which
(3.10)--(3.11) are forced are

\[
\begin{array}{c|l}
(4,9,4)&0,6435,6443,12869,12872,\\
(5,8,4)&0,6436,6443,12869,12872,\\
(5,9,3)&0,6436,6444,12870,12872.
\end{array}                                               \tag{3.12}
\]

#### Proof

The singleton assertions follow from (3.3): at a singleton anchor the
variable OR is exactly \(H\), so the context must equal the target's low
projection.

More strongly, suppose both charts contain a collar endpoint \(p\).  They
are nested.  If \(I_A\subseteq I_B\), then every variable cell of the
\(A\)-chart is also active for \(B\), and hence is a submask of
\(A\cap B=H\).  Since \(b_A=0\), the chart cannot supply the low projection
of \(A\), a contradiction.  Thus a possible co-anchoring would require
\(I_B\subsetneq I_A\).  Every variable cell of \(I_B\) is again restricted
to \(H\), so \(B\) can be completed only by context `0x1009`.  This context
requires \(I_B\) to reach the right endpoint of the first collar.  If \(p\)
is its left endpoint, that makes \(I_B\) the whole collar, contradicting
the strict containment; at every other nonspecial endpoint the context is
unavailable.  The sole surviving endpoint is therefore the right endpoint
of the first collar, where \(I_B=\{p\}\) is possible.  This proves (3.10).

Finally, (3.8) and (3.6) would force both charts through \(p\), contradicting
(3.10).  Hence (3.11) holds at the positions in (3.12). \(\square\)

This is an anchor-location-dependent **cut**, not an elimination of any
anchor branch: the low union may simply leave another position uncovered.

### Corollary 3.3 (dead-boundary-neighbour cuts)

Call a collar side *low-dead* when every nonempty fixed context on that side
contains \(H\), or when there is no fixed context on that side.  The
low-dead sides are

* the left side of the first collar (the beginning of the word);
* the right side of the middle collar (a prefix of \(G_2\));
* the left side of the third collar (a suffix of \(G_2\)); and
* the right side of the third collar (the end of the word).

If the anchor is one position inward from a low-dead collar endpoint, so
that exactly one non-anchor collar cell lies on that side of the anchor,
then (3.11) again holds.  Combining these cuts with Corollary 3.2 gives the
following exact anchor positions at which the low union must leave at least
two cells uncovered:

\[
\begin{array}{c|l}
(4,9,4)&0,1,6435,6442,6443,12869,12870,12871,12872,\\
(5,8,4)&0,1,6436,6442,6443,12869,12870,12871,12872,\\
(5,9,3)&0,1,6436,6443,6444,12870,12871,12872.
\end{array}                                               \tag{3.13}
\]

Thus (3.11) is proved at 9, 9, and 8 of the 17 anchor locations,
respectively.

#### Proof

Assume instead that (3.8) holds.  At an interior anchor neither \(I_A\) nor
\(I_B\) can be a singleton, by (3.3), so Theorem 3.1 orients their
non-anchor arms in opposite directions.  One of these two arms occupies the
one-cell side between \(p\) and the low-dead boundary; call its high target
\(U\), and call that boundary cell \(x\).  Since \(Z=P\setminus\{p\}\),
some selected low chart \(J=I_L\) contains \(x\).  It cannot cross the
anchor, and the side has only one cell, so \(J=\{x\}\).

Every low target contains both coordinates `0x0001` and `0x0020`, by
(1.4).  If \(U=A\), use `0x0001`, which \(A\) omits; if \(U=B\), use
`0x0020`, which \(B\) omits.  At a low-dead side the singleton low chart has
zero compatible fixed context, so its chosen coordinate is not in
\(b_L(J)\).  Lemma 2.3 then requires \(J\setminus I_U\ne\varnothing\),
contradicting \(J=\{x\}\subseteq I_U\).  Translating the four low-dead
sides into the three absolute-position profiles and adjoining (3.12) gives
(3.13). \(\square\)

The protrusion lemma yields additional exact endpoint clauses.  For example,
every low target contains coordinates `0x0001` and `0x0020`; target \(A\)
omits `0x0001`, while target \(B\) omits `0x0020`.  Therefore a low chart
intersecting an anchored \(A\)-chart must protrude beyond it whenever its
fixed context does not supply `0x0001`; the analogous statement holds for
an anchored \(B\)-chart and `0x0020`.  No aggregate count stronger than
(3.11) is inferred here, because boundary contexts can supply these bits for
some charts.

## 4. Sharp obstruction to low-only anchor pruning

The next theorem shows that the anchor and the 18 low targets, by
themselves, eliminate none of the 17 anchor positions.

### Theorem 4.1 (all-location literal realization of the anchor-low subsystem)

Fix any profile in (1.1) and any one of its 17 collar positions \(p\).
There is an assignment of nonzero masks to all 17 collar cells such that

1. the singleton at \(p\) is exactly \(H\);
2. every target in \(\mathcal L\) has a literal interval witness avoiding
   \(p\); and
3. selecting those 19 witnesses satisfies the exact chart-intersection and
   durable-bit conditions.

#### Proof

Regard each collar as a path on its positions and delete \(p\).  The
remaining graph is a disjoint union of at most four paths with a total of
16 vertices.  If their orders are \(n_1,\ldots,n_t\), then

\[
       \sum_{i=1}^t\left\lfloor\frac{n_i}{2}\right\rfloor
       \ge \frac{16-t}{2}\ge6.                          \tag{4.1}
\]

Thus there are two vertex-disjoint collar edges.  Put, in either order,

\[
                 \mathtt{246d},\mathtt{286d}             \tag{4.2}
\]

on the first edge and

\[
                 \mathtt{2879},\mathtt{4879}             \tag{4.3}
\]

on the second.  Their exact ORs are

\[
 \mathtt{246d}\vee\mathtt{286d}=\mathtt{2c6d},\qquad
 \mathtt{2879}\vee\mathtt{4879}=\mathtt{6879}.          \tag{4.4}
\]

Assign the other twelve members of

\[
 \mathcal L\setminus
 \{\mathtt{246d},\mathtt{286d},\mathtt{2c6d},
   \mathtt{2879},\mathtt{4879},\mathtt{6879}\}
\]

bijectively to the twelve remaining non-anchor cells, and put \(H\) at
\(p\).  Select singleton witnesses for the sixteen low values actually
written, the two edge witnesses in (4.4), and the singleton \(H\)-witness.
All are literal intervals contained in one collar, and every low witness
avoids \(p\).

For the chart-intersection replay, an ordinary singleton cell has active
intersection equal to its written target.  At an endpoint of the first
special edge the active targets are its operand and `0x2c6d`; their
intersection is the operand.  The second edge is identical with target
`0x6879`.  The anchor intersection is \(H\).  Hence every active
intersection is exactly the displayed nonzero cell value, and (4.4)
supplies every required durable bit.  A maximal compatible fixed context
can only add a submask of the same target and therefore changes none of
these equalities.  This proves all three assertions. \(\square\)

### Corollary 4.2 (precise boundary of anchor-only Helly pruning)

No one of the 17 anchor locations in any profile can be ruled out by a
necessary condition involving only the literal witness requirements for
\(H\) and the 18 low targets.  In particular, the anchor exclusion together
with every durable-bit or Helly constraint internal to this 19-target
subsystem cannot yield an anchor-location no-go.  Any stronger argument must
recruit at least one of the other 38 high repair targets.

Theorem 3.1 and Corollary 3.2 do recruit two such targets and therefore give
a nontrivial anchor-dependent interval cut.  They still do not prove any
profile infeasible.

### Corollary 4.3 (the full 57-target Helly relaxation keeps every anchor)

For every profile and anchor location, one can select one chart for every
one of the 57 repair targets so that every active target intersection is
nonzero.  Hence condition (3.2) of the chart-intersection theorem, including
all of its interval-Helly consequences, eliminates no anchor location by
itself.

#### Proof

Use the 19-target construction of Theorem 4.1.  For each of the remaining
38 targets, all of which contain \(H\), select the singleton chart
\(\{p\}\).  The active intersection at the anchor remains exactly \(H\),
and no new chart meets a low cell.  Every other active intersection is the
one already checked in Theorem 4.1. \(\square\)

These additional singleton charts generally fail their low-coordinate
durable rows.  Thus the corollary is exactly a no-go for **pure Helly**
pruning, not a relaxation-feasibility claim that includes condition (3.3).
The high-fan cuts of Section 3 work precisely because they use those durable
rows.

## 5. Exact remaining boundary

The proved information is:

* every empty-mask-intersection family gives an exact interval-Helly
  disjointness cut;
* durable bits give exact one-sided protrusion cuts;
* the high pair `0x8c62,0x9009` forces the low-union dichotomy and the
  endpoint/dead-boundary cover inequalities (3.10)--(3.13); and
* the anchor plus all 18 low targets is literally feasible at every anchor
  position, so low-only anchor pruning is exhausted; and
* even the full 57-target nonempty-intersection/Helly relaxation retains all
  17 anchor positions, so a genuine anchor elimination must use durable-bit
  coverage.

What remains open is simultaneous realization of all 57 targets.  The
present note says nothing about words outside the three fixed-gap profiles,
and it does not convert the currently unknown profile solver dispositions
into SAT or UNSAT.
