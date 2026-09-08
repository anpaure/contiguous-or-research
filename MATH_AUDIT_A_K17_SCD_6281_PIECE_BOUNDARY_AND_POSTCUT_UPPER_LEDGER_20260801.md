# The `6,281`-piece `m=9` SCD bank: exact boundary monoid and post-cut upper ledger

Date: 2026-08-01  
Lane: A / finite `k=17` SCD seam braid  
Status: exact lightweight replay; global ordered braid and common compiler remain open

## 1. Frozen face and scope

The authenticated forest input is

```text
scratch/ad_k17_scd_multicomponent_20260801/phase_m9.selected.tsv
SHA-256 49d3854140ed2ef3a1e2119013dc9b21e51176e4b69e5aa1a36a9a177d21d8de
```

It consists of `24,310` distinct rank-nine owners and `19,448` Johnson
edges in `4,862` directed path components.  The present canonical cut bank
is the **earliest-right-endpoint** minimum transversal of all short internal
positive owner runs.  It has

\[
       1,419\text{ cuts},\qquad
       P=4,862+1,419=6,281\text{ pieces}.                 \tag{1.1}
\]

This choice of minimum transversal is part of the scope.  The number
`1,419` alone does not determine the higher-shadow ledger: different
minimum transversals can cut different interval witnesses.

Local validity here means:

1. the maximal depth-three source has no empty letter;
2. its four-letter windows reconstruct every owner; and
3. no positive owner run of length below four is wholly internal.

The third item is the flat depth-three source/residence condition used by
the cut construction.  If a later model requires **both** zero and one runs
to have length at least four, that is a stronger face and must first refine
the piece bank.  The theorem below gives the boundary monoid for either
choice of constrained signs and therefore prevents this distinction from
being hidden in a seam graph.

## 2. Minimum cutting and the exact lower ledger

Let one original owner path be

\[
                        O_0,O_1,\ldots,O_t.
\]

For every coordinate, an internal positive run on owner indices
`[a,b)` of length below four contributes the closed cut interval

\[
                        I=[a,b]                         \tag{2.1}
\]

on the edge-boundary positions.  A cut at any `c in I` makes both remaining
parts of this run touch piece boundaries.  Thus locally valid segmentation
is exactly interval transversal on each original path.  Earliest right
endpoint gives a minimum transversal, and the usual disjoint-interval
certificate proves optimality.  Summing over all `4,862` paths gives
`1,419` cuts.

### Theorem 2.1 (exact raw lower omission count)

The canonical cut bank preserves exactly

\[
                    19,448-1,419=18,029                 \tag{2.2}
\]

original Johnson adjacencies.  Their rank-eight intersection colours are
all distinct.  Hence, before adding any new seams, the number of missing
rank-eight colours is exactly

\[
                    \binom{17}{8}-18,029
                    =24,310-18,029=6,281=P.             \tag{2.3}
\]

Consequently the scalar omission allowance `7,401` leaves precisely

\[
                              7,401-6,281=1,120          \tag{2.4}
\]

units before accounting for any further compiler loss.  New seam
intersections may repair some of the `6,281`; they cannot make the raw
count larger unless additional preserved edges are released.

#### Proof

The authenticated forest is lower-colour injective on its `19,448` edges.
Every cut deletes one distinct old edge, so (2.2) colours remain.  There
are `24,310` rank-eight targets.  Equations (2.3)--(2.4) follow.  The
independent replay also verifies that all `1,419` deleted lower colours and
all `1,419` deleted upper colours are pairwise distinct.  \(\square\)

## 3. Exact oriented boundary state

For a piece `P` and coordinate `x`, let its trace be a nonempty binary word
`w_x(P)`.  Record

\[
 (f_x,p_x,\ell_x,s_x,c_x,n_P),                         \tag{3.1}
\]

where `f_x,l_x` are the first and last bits, `p_x,s_x` are prefix and suffix
run lengths capped at four, `c_x` says the trace is constant, and `n_P` is
the piece length capped at four.  Reversing `P` swaps the prefix and suffix
data.  This is the exact capped run monoid state.

Fix a constrained-sign set `Sigma subset {0,1}`.  For the present
depth-three source face, `Sigma={1}`.  For genuinely signed residence,
`Sigma={0,1}`.  Define the one-coordinate transition by scanning a trace
from left to right while carrying `(b,a)`, the current terminal bit and its
age capped at four:

* on the same bit, replace `a` by `min(4,a+1)`;
* on a changed bit, reject iff `b in Sigma` and `a<4`, then start the new
  state with age one.

At the global left end there is no incoming state, and the final terminal
run at the global right end is clipped and is not rejected.

### Theorem 3.1 (boundary-monoid residence criterion)

An ordered oriented list of locally valid pieces has no forbidden internal
run exactly when the above transition accepts independently in all
seventeen coordinates.

#### Proof

Every run wholly inside a piece is valid by hypothesis.  Every other run is
the unique current terminal run while successive pieces are scanned.  It
becomes internal exactly at the first subsequent bit change, when the
transition performs precisely the required length test.  The first and
last global runs are clipped, exactly as encoded.  \(\square\)

### Corollary 3.2 (a static pairwise seam graph is not exact)

The legality of `P|Q` can depend on the run age entering `P` whenever the
relevant coordinate trace of `P` is constant.  In the frozen bank every
one of the `6,281` pieces has at least one constant coordinate trace, and
there are `360` singleton pieces.  Therefore an unlabelled pairwise seam
graph cannot encode exact residence.  One must either carry the capped
seventeen-coordinate monoid state, or impose a stronger conservative
pairwise rule which is not equivalent.

The Johnson condition remains separately necessary at every seam:

\[
             |\operatorname{last}(P)\triangle
               \operatorname{first}(Q)|=2.             \tag{3.2}
\]

Under (3.2), the new lower and upper q1 colours are their intersection and
union.  The monoid condition then gives the exact cross-seam maximal-source
run test; intersections of at most four consecutive rank-nine Johnson
owners are automatically nonempty.

## 4. Post-cut upper holes

For a family of owner blocks `B`, let `D_r(B)` be the set of all rank-`r`
OR values of intervals wholly contained in one block.  Let `F` be the
original `4,862`-component forest and `P` the canonical `6,281`-piece bank.
The replay computes the following exact table.

| rank | holes in `F` | new losses caused by cuts | holes in `P` | overlap old/new |
|---:|---:|---:|---:|---:|
| 10 | 0 | 1,419 | 1,419 | 0 |
| 11 | 911 | 1,543 | 2,454 | 0 |
| 12 | 608 | 1,047 | 1,655 | 0 |
| 13 | 135 | 473 | 608 | 0 |
| 14 | 8 | 114 | 122 | 0 |

Thus the requested rank-10--14 bank contains

\[
  1,662\text{ old holes}+4,596\text{ cut-induced holes}
      =6,258\text{ distinct targets}.                  \tag{4.1}
\]

In particular, the `1,419` cut edges were unique rank-ten providers, so
all their colours must be redelivered by new seams or other crossing
intervals.  Restoring the same old adjacency is sufficient for its colour
but may restore the short run which forced the cut.

For completeness, an all-width audit cannot stop at rank fourteen: this
canonical cut bank also creates `15` rank-fifteen holes.  Ranks sixteen and
seventeen have no post-cut holes.  Therefore the complete post-cut upper
bank has `6,273` holes in ranks 10--15.  The rank-fifteen row is not part of
the user's requested 10--14 count, but it must either be proved automatic
under the final braid or included in the exact solver.

The zero entries in the final column mean that within each fixed rank the
old-hole set and the newly lost set are disjoint.  Sets in different ranks
are automatically disjoint by cardinality.

## 5. Exact crossing-deck formula

For an oriented piece `P=(v_1,...,v_s)`, define its prefix, suffix and full
ORs

\[
 A_P(j)=v_1\cup\cdots\cup v_j,\qquad
 Z_P(i)=v_i\cup\cdots\cup v_s,\qquad
 G_P=A_P(s).                                           \tag{5.1}
\]

### Theorem 5.1 (multi-piece crossing formula)

For an ordered list `P_1,...,P_k`, every interval OR which starts in
`P_i`, ends in `P_j`, and crosses at least one seam has the unique form

\[
 Z_{P_i}(a)\ \cup\
 \bigcup_{i<t<j}G_{P_t}\ \cup\
 A_{P_j}(b),                                           \tag{5.2}
\]

for `i<j` and suitable endpoint indices `a,b`.  Conversely every value in
(5.2) is the OR of such a physical interval.

#### Proof

Intersect the physical interval with each piece.  It contains a suffix of
its first piece, every intervening piece in full, and a prefix of its last
piece.  This gives (5.2), and concatenating those portions proves the
converse.  \(\square\)

Equation (5.2), with masks of rank above the target discarded, is the exact
upper separation oracle.  A direct pairwise seam catalogue covers only the
case `j=i+1`.

### Proposition 5.2 (six-owner memory is insufficient here)

In the frozen canonical bank, original component `1482` contains an
interval of `16` owners, crossing two canonical cuts, whose union is

\[
                         86015=\mathtt{0x14fff}
\]

of rank fourteen.  Component `1790` contains a ten-owner interval crossing
three cuts with rank-fourteen union `97790`.  Hence even on this literal
fixture, arbitrary-width rank-10--14 service cannot be recovered from only
the last six owners or from independent pairwise seam edges.  The solver
must carry the prefix/full/suffix union state of (5.2), or an exactly
equivalent truncated union automaton.

For a **fixed-width** q-step flag row, retaining `q+1<=6` owners would of
course suffice.  That is a different objective from the arbitrary-width
upper deck tested here.

## 6. Exact remaining finite object

For this fixed canonical piece bank, an ordered-braid certificate consists
of a permutation and orientation of all `6,281` pieces satisfying:

1. the Johnson seam equation (3.2) at all `6,280` joins;
2. the seventeen-coordinate boundary-monoid acceptance of Theorem 3.1;
3. coverage, through (5.2), of all `6,258` requested rank-10--14 holes
   (and the additional `15` rank-fifteen holes unless separately proved
   automatic);
4. the generalized lower omission budget at most `7,401`, whose raw
   starting charge is exactly `6,281`;
5. after the owner chronology is fixed, one common maximal source and the
   exact lower compiler.

These conditions are exact for the stated fixed segmentation.  They do not
show that the earliest-right cut bank is optimal for upper repair.  A
stronger solver may expose alternative minimum cut locations jointly with
the braid; its upper-hole bank must then be recomputed from the selected
cuts.

## 7. Independent audit artifacts

The independent replay is

```text
scratch/audit_a_k17_scd_6281_piece_boundary_postcut_20260801.py
SHA-256 1c745b2348103f15bcb7cb8b5f9051ea0afbb76232163094069cda3217337212
```

and its output is

```text
scratch/a_k17_scd_6281_piece_boundary_postcut_20260801.audit.json
SHA-256 3b9632a98609feb3a94f405db47581c45232e6e5dbc87053185a430ffebb9fd9
canonical payload 208762f3f608a0fa33ad773d6037e7c2951063517ee12fdab3842dd9f7f3f435
```

The frozen segmentation inputs replayed by that audit are

```text
scratch/ad_k17_scd_multicomponent_20260801/resident_pieces.json
SHA-256 f1e8ca31601e5e4af4430a33b453faa78133701da374f4d73dbe3c405791913b

scratch/ad_k17_scd_multicomponent_20260801/resident_piece_static.audit.json
SHA-256 c381e11350c236eb557b6e477348ba9f0cccdeacabdffc5b5868b593422d3f20
```

No SAT, exhaustive search, or H100 job was used in this audit.
