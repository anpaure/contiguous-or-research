# Coatom-screen OR/AND duality and the one-opening obstruction

> **Scope correction (2026-08-01).** The tensor statements in this note use
> the older raw all-lower-screen expansion and retain four repeated screen
> owners.  In particular, its equal-internal-AND-deck claim must not be
> transferred to the authoritative zero-defect mixed-screen tensor.  The
> latter is simple and owner-exact but is one-polarity; see
> `MATH_AUDIT_A_MIXED_COATOM_SCREEN_COMPLEMENT_GAP_AND_U5_20260801.md`.

Date: 2026-08-01  
Lane: additive-constant upper-shadow / even-birail interface  
Status: exact raw-tensor audit, exact gap dual, and an exhaustive one-opening
obstruction on the complete twelve-owner ECO connector bank; superseded as
a description of the zero-defect mixed-screen packet.  No additive-constant
theorem is claimed.

## 0. Result

The coatom-screen tensor is stronger internally, and weaker at its boundary,
than its original statement suggests.

* On each of the three authenticated physical ECO rethreads, the expanded
  old and new words have equal **distinct internal OR and AND decks** for
  every tensor depth.
* The OR-oriented opening has equal pointwise prefix/suffix OR signatures,
  but its compressed prefix/suffix AND decks are incomparable.
* The same physical connector matching has a different opening that is
  compressed-AND transparent.  Thus the tensor recipe works on either
  semilattice, but the two shores require different cuts.
* This is unavoidable inside the complete contracted catalogue.  Among all
  1,368 common Hamilton connector matchings and all cuts/orientations there
  is no pair that preserves both compressed OR and compressed AND profiles,
  in either directed sense.  The six all-Johnson matchings have
  12 OR-positive and 12 AND-positive pairs, with empty intersection.
* Coordinatewise complementation gives an exact singleton-block/empty-screen
  **gap tensor**.  It exchanges OR with AND and positive residence with gap
  residence.  This is the correct complement/birail analogue, but it does
  not remove the one-opening obstruction.

Consequently the current tensor can protect both internal banks, and two
separately opened rails can protect their respective crossing banks.  A
single common chronology cannot be certified by this ECO connector bank.

## 1. Two compressed semilattice profiles

Let (W=(W_0,\ldots,W_{L-1})) be a word of subsets of a finite universe
(\Omega).  For (\star\in\{\cup,\cap\}), define

\[
 \mathsf P_\star(W)=
   \left\{\mathop\star_{j=0}^{i}W_j:0\le i<L\right\},\qquad
 \mathsf S_\star(W)=
   \left\{\mathop\star_{j=i}^{L-1}W_j:0\le i<L\right\},                \tag{1.1}
\]

and let (\mathsf I_\star(W)) be the set of all nonempty internal interval
(\star)-values.  The compressed profile is

\[
 \mathsf D_\star(W)=
 (\mathsf P_\star(W),\mathsf S_\star(W),
  \mathsf I_\star(W),\mathop\star_{j=0}^{L-1}W_j).                    \tag{1.2}
\]

The usual exterior-context proof for unions has an exact intersection
dual: if every component of (\mathsf D_\cap(X)) is contained in the
corresponding component of (\mathsf D_\cap(Y)), with equality of the total
intersection, then replacing (X) by (Y) preserves every old interval-
intersection value.  This also follows by complementing all letters and
applying the union theorem.

Thus simultaneous exterior transparency is exactly the pair of directed
conditions

\[
                 \mathsf D_\cup(X)\preceq\mathsf D_\cup(Y),\qquad
                 \mathsf D_\cap(X)\preceq\mathsf D_\cap(Y).           \tag{1.3}
\]

These are coverage statements.  They say nothing about witness addresses,
multiplicities, owner simplicity, or residence.

## 2. A semilattice transfer lemma for the coatom screen

Let (A) be an active universe and let
(V=(V_0,\ldots,V_{t-1})) be an active Johnson word.  Put

\[
 F=\{f_0,\ldots,f_{n-1}\},\qquad C_i=F-\{f_i\},                       \tag{2.1}
\]

with (A,F,K) disjoint.  Define

\[
 B(V_j)=(K\cup V_j\cup C_0,\ldots,K\cup V_j\cup C_{n-1}),\qquad
 S_j=K\cup(V_j\cap V_{j+1})\cup F.                                  \tag{2.2}
\]

Write (\mathcal T_n(V)) for the word obtained by placing (S_j) between
(B(V_j)) and (B(V_{j+1})).

### Lemma 2.1 (OR/AND support transfer)

Suppose active words (V,V') have the same vertex support and the same
adjacent-intersection support.  Then:

1. equality of (\mathsf I_\cup(V),\mathsf I_\cup(V')) implies equality
   of the expanded internal OR decks;
2. equality of (\mathsf I_\cap(V),\mathsf I_\cap(V')) implies equality
   of the expanded internal AND decks;
3. if the active compressed prefix/suffix profile for one operation is
   equal and the first and last active owners agree, then the corresponding
   expanded compressed boundary profile is equal.

The claims remain true with multisets in the hypotheses when physical owner
current is also required.  They assert equality of distinct interval-value
support, not equality of interval multiplicities.

#### Proof

For OR, two different coatoms cover (F), and every screen contains (F).
Hence an expanded interval is one of:

* a singleton block owner (K\cup V_j\cup C_i);
* a singleton screen (K\cup(V_j\cap V_{j+1})\cup F); or
* a value (K\cup F\cup U), where (U) is an active interval union.

This gives assertion 1 and the analogous prefix/suffix decomposition.

For AND, classify by the number of screens met.  An interval contained in
one block has value

\[
 K\cup V_j\cup\left(F-\{f_i,\ldots,f_k\}\right).                    \tag{2.3}
\]

An interval meeting exactly one screen has active part
(V_j\cap V_{j+1}); its filler part is a (possibly empty or full)
contiguous interval of the ordered filler set.  An interval meeting at least
two screens contains a whole intervening coatom block, so its filler
intersection is empty and its active part is an active interval
intersection.  Values with empty filler for active intervals of lengths one
and two are already supplied by (2.3) and the one-screen class.  Therefore
the complete expanded AND support depends only on the active vertex support,
adjacent-intersection support, and (\mathsf I_\cap(V)).  This proves 2.

For clarity, the expanded prefix-AND deck is

\[
 \{K\cup V_0\cup(F-\{f_0,\ldots,f_i\}):0\le i<n\}
 \ \cup\ 
 \{K\cup(V_0\cap\cdots\cap V_j):1\le j<t\},                        \tag{2.4}
\]

and the suffix formula is its reversal.  Formula (2.4), and its OR dual,
prove assertion 3. \(\square\)

## 3. What the authenticated ECO tensor actually preserves

Use the active words

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

Their vertex multisets and adjacent-intersection multisets agree.  Direct
calculation gives

\[
 \mathsf I_\cup(P)=\mathsf I_\cup(Q),\qquad
 \mathsf I_\cap(P)=\mathsf I_\cap(Q).                              \tag{3.1}
\]

The OR boundary signatures agree pointwise.  Lemma 2.1 therefore proves,
for every (n=d+2\ge2),

\[
 \mathsf D_\cup(\mathcal T_n(P))
  =\mathsf D_\cup(\mathcal T_n(Q)),\qquad
 \mathsf I_\cap(\mathcal T_n(P))
  =\mathsf I_\cap(\mathcal T_n(Q)).                                \tag{3.2}
\]

The second identity is a genuine extra positive result: every **internal**
OR and AND value survives the same physical tensor exchange.

It does not extend across the AND boundary.  Suppressing the common core
(K), the exact differences, independent of (d), are

\[
\begin{array}{c|c|c}
 &P\setminus Q&Q\setminus P\\ \hline
 \mathsf P_\cap&\{b,b\infty\}&\{a,a\infty\}\\
 \mathsf S_\cap&\{eb\}&\{ea\}.
\end{array}                                                         \tag{3.3}
\]

With a core, add (K) to every displayed value.  Thus neither direction
of AND-deck inclusion holds.

There is nevertheless an AND-oriented opening of the same physical
connector matching:

```text
P_and = Ad ca Ia Ica Ibc Ic Cd bc Ib Iab ab Bd,
Q_and = Ad ab Iab Ia ca Cd Ic Ica Ibc Ib bc Bd.
```

It satisfies

\[
        \mathsf D_\cap(\mathcal T_n(P_{and}))
       =\mathsf D_\cap(\mathcal T_n(Q_{and})),                       \tag{3.4}
\]

and its two expanded internal decks are again equal.  Its OR boundary
profile fails.  Hence the same matching and the same tensor recipe can
serve either rail, but not with one common cut.

## 4. Complete one-opening obstruction

Consider every perfect connector matching on the twelve active owners that
is disjoint from the two six-edge ECO phases.  Retain the 1,368 matchings
for which both resulting degree-two graphs are Hamilton cycles, and test all
(24^2) pairs of cuts and orientations.

### Theorem 4.1 (exact contracted census)

The exact numbers of directed serialization pairs are

\[
\begin{array}{c|cc}
 &\text{profile equality}&\text{directed inclusion}\\ \hline
 \mathrm{OR}&642&1224\\
 \mathrm{AND}&642&1224\\
 \mathrm{OR\ and\ AND}&0&0.
\end{array}                                                         \tag{4.1}
\]

Restricting to the six matchings whose connector edges are all literal
Johnson edges gives

\[
\begin{array}{c|cc}
 &\text{profile equality}&\text{directed inclusion}\\ \hline
 \mathrm{OR}&12&12\\
 \mathrm{AND}&12&12\\
 \mathrm{OR\ and\ AND}&0&0.
\end{array}                                                         \tag{4.2}
\]

Exactly three physical matchings support the positive rows.  Each has four
OR openings and four different AND openings.  In particular, the zero in
(4.2) is not a shortage of physical connector matchings; it is a cut-phase
incompatibility.  Reversing the replacement direction also gives zero
simultaneous directed pairs, both in the full catalogue and in the physical
subcatalogue.

This theorem is scoped to this complete twelve-owner ECO connector bank.
It is not a no-go for a larger compound packet or for two rails with
independent openings.

## 5. Complement/gap tensor

Let (L) be a further fixed set and complement (2.2) in the universe
(K\sqcup A\sqcup F\sqcup L).  After deleting the now-absent core notation,
the dual blocks and screens are

\[
 G(V_j)=\bigl(L\cup(A-V_j)\cup\{f_0\},\ldots,
                 L\cup(A-V_j)\cup\{f_{n-1}\}\bigr),                \tag{5.1}
\]

\[
 R_j=L\cup\bigl(A-(V_j\cap V_{j+1})\bigr).                         \tag{5.2}
\]

Every letter has rank (|L|+4), and every consecutive pair is Johnson-
adjacent.  This is the singleton-block/empty-filler-screen gap tensor.

### Corollary 5.1 (exact duality)

Coordinatewise complementation sends

\[
 \mathsf D_\cup(W)\longleftrightarrow\mathsf D_\cap(\overline W),
 \qquad
 \mathsf D_\cap(W)\longleftrightarrow\mathsf D_\cup(\overline W). \tag{5.3}
\]

It also sends positive runs of a coordinate to zero runs of that coordinate.
Consequently the complement of the OR-oriented tensor is pointwise-AND
transparent, has equal internal OR and AND decks, and every internal zero
run has length at least (d+2).  The complement of the AND-oriented tensor
is compressed-OR transparent with the same internal and gap-residence
properties.

The dual is therefore suitable for a complementary/gap rail.  It is not a
positive-resident replacement: each filler coordinate occurs only once per
block, so it has singleton positive runs.  Nor does pairing a tensor with
its complement create a common opening; Theorem 4.1 remains the exact local
phase obstruction.

## 6. Consequence for the additive-constant lane

The coatom screen has now closed the following local rows:

* literal Johnson adjacency and common physical current;
* scalable positive residence on the primal tensor, or scalable gap
  residence on the complement tensor;
* both internal OR and AND decks; and
* either crossing OR or crossing AND transparency after a suitable opening.

The minimum missing birail interface is precise:

> choose compatible primal and dual openings, or enlarge the packet so that
> one common chronology satisfies both directed boundary-deck systems.

The existing twelve-owner ECO bank cannot supply the latter.  Even after
that phase problem is solved, the four repeated screen owners, compiler
deletion address, and regenerative restoration remain separate gates.

## 7. Audit

The dependency-free exact replay is

```text
scratch/audit_a_coatom_screen_or_and_decks_20260801.py
scratch/a_coatom_screen_or_and_decks_20260801.audit.json
```

It exhausts all common connector matchings and all cut/orientation pairs,
then checks the three authenticated expanded rows for every
(0\le d\le12).  The symbolic proofs above, not the finite depth range,
establish the all-(d) statements.
