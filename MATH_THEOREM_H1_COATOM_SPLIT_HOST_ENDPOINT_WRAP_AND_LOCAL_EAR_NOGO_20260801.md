# Planting the two-ray coatom host: endpoint wrap and the linear local-ear obstruction

Date: 2026-08-01  
Lane: additive-constant regeneration / split-pivot host  
Status: exact conditional endpoint-wrap construction and exact local
obstructions.  The remaining global condition is one protected safe cut.

## 0. Result

The two-ray split theorem needs an old local trace of length `2d-3` around
one merged source letter.  That trace is not hidden inside the native
`d+1`-position coatom connector, and a bounded local extension cannot put it
there: at least `d-4` additional or imported positions are necessary.

There is, however, a natural nonlocal source.  The already-proved prepared
left and right boundary carves contain the two required half-traces.  One
cyclic block rotation brings their global endpoints together.  At the new
seam the complete two-ray host appears with **no new side positions**.  The
rotation is valid precisely when its cut is protected: every named old
target lost at the old cut has another occurrence after rotation.  After
that check, contracting the two seam bases produces the actual merged
source letter `X`; splitting it back costs one position and restores both
coatom flags.

Thus the host problem is no longer local envelope planting.  It is one
global protected-cut/gammoid condition.

## 1. A linear lower bound for every local full-ray host

Consider two strict target chains, each of length `d-1`, assigned to the
two consecutive exclusive rays of one split, including both singleton ray
bases.

### Theorem 1.1 (physical span lower bound)

The old word before the split contains at least

\[
                  (d-2)+1+(d-2)=2d-3                         \tag{1.1}
\]

positions in the host span: `d-2` positions strictly left of the merged
letter, the merged letter itself, and `d-2` positions strictly right.

#### Proof

After the singleton base, each strict target chain has `d-2` further
values.  Along a ray the value can change only when its endpoint passes a
new physical source position.  Strictness therefore requires at least
`d-2` distinct positions on that shore.  The two shores are disjoint and
the merged source is a third part.  \(\square\)

The canonical native connector source trace has only `d+1` positions from
its left endpoint base to its right endpoint base.  Therefore a replacement
confined to that span must add at least

\[
                         (2d-3)-(d+1)=d-4                     \tag{1.2}
\]

positions.  Equivalently, any zero- or constant-length construction must
import/rethread at least `d-4` existing positions from outside the native
connector.  A constant-support local ear is impossible for unbounded `d`.

This count does not obstruct an `O(d)`-support, zero-length rethreading;
that is exactly what the endpoint-wrap construction below supplies.

## 2. The native filler bridge cannot be contracted to the host

Suppress the common core.  Around the canonical `A/B` upper screen, the
maximal-erosion trace has the form

\[
 A+f_1,quad (A\cap B)+f_1f_2,quad
 (A\cap B)+f_2f_3,quad\ldots,quad
 (A\cap B)+f_{d-1}f_d,quad B+f_d.                           \tag{2.1}
\]

The desired merged source is

\[
                         X=A\cup B\cup\{f_1,f_d\}.           \tag{2.2}
\]

### Theorem 2.1 (filler-separator obstruction)

No contiguous interval of (2.1) has union `X` for `d>=3`.  In fact, every
interval containing both an `A-B` exclusive coordinate and a `B-A`
exclusive coordinate contains the whole filler set

\[
                            \{f_1,\ldots,f_d\}.               \tag{2.3}
\]

Consequently no operation which first contracts a contiguous native block
to its union and then splits that union can manufacture (2.2).

#### Proof

An interval seeing both exclusive active coordinates must contain the two
endpoint letters of (2.1), hence every intervening letter.  The endpoint
and consecutive-pair filler labels in those letters have union (2.3).
For `d>=3`, (2.2) omits at least `f_2`, so the two unions differ.  \(\square\)

Together with the envelope obstruction in the two-ray theorem, this rules
out both elementary monotone ways of producing `X` inside the native
connector: splitting one old letter, and contracting then splitting one
contiguous old block.

## 3. Prepared endpoints already contain the two half-traces

Let

\[
 Z=A\cup\{f_1\},\qquad T=B\cup\{f_d\}.                       \tag{3.1}
\]

Orient the prepared right-boundary carve so that the terminal source suffix
is

\[
                  Q=(\{f_{d-1}\},\ldots,\{f_2\},Z),          \tag{3.2}
\]

and orient the prepared left-boundary carve in reverse filler order so that
the initial source prefix is

\[
                  P=(T,\{f_{d-1}\},\ldots,\{f_2\}).          \tag{3.3}

\]

These are literal subwords of the boundary antecedents: Theorem 1.1 and its
reversal in the prepared-endpoint theorem give every displayed letter and
the exact carrier replay.

Write the complete source word as

\[
                              W=P\,M\,Q.                      \tag{3.4}

\]

The prefix and suffix are disjoint once the carrier is longer than the two
endpoint collars.

This factorization is genuinely supplied by the prepared-endpoint theorem,
but only under that theorem's host hypothesis.  On the left, relabel its
local omission order by

\[
 g_1=f_d,\ g_2=f_{d-1},\ldots,g_{d-1}=f_2;
\]

then its first `d-1` antecedent letters are exactly (3.3).  Apply the
reversed theorem at the right endpoint to obtain (3.2).  The two cap
modifications are disjoint and coexist in one antecedent when the carrier
is long enough.  What is **not** proved is that every Pascal child has the
two required prepared endpoint owner blocks.

## 4. Exact endpoint-wrap theorem

Rotate the prefix `P` to the end:

\[
                         \rho(W)=M\,Q\,P.                    \tag{4.1}

\]

The new seam is

\[
 \ldots,\{f_3\},\{f_2\},Z,T,
          \{f_{d-1}\},\{f_{d-2}\},\ldots,\{f_2\}.           \tag{4.2}

\]

### Theorem 4.1 (zero-length two-ray host by endpoint wrap)

At the seam (4.2), the intervals ending at `Z` realize

\[
                       A\cup P_q\qquad(2\le q\le d),          \tag{4.3}

\]

and the intervals beginning at `T` realize

\[
                       B\cup S_q\qquad(2\le q\le d).          \tag{4.4}

\]

No source position is added.  Every interval of `W` wholly contained in
`P` or wholly contained in `M Q` transports to an interval of `rho(W)` with
the same value.

More explicitly, let `pre` and `suf` include all nonempty prefixes and
suffixes, and put

\[
 \begin{aligned}
  \mathcal C_{\rm old}
    &=\{\operatorname{OR}(U)\cup\operatorname{OR}(V):
          U\in\operatorname{suf}(P),\
          V\in\operatorname{pre}(MQ)\},\\
  \mathcal C_{\rm new}
    &=\{\operatorname{OR}(U)\cup\operatorname{OR}(V):
          U\in\operatorname{suf}(MQ),\
          V\in\operatorname{pre}(P)\}.
                                                               \tag{4.5}
 \end{aligned}
\]

Then the interval languages decompose exactly as

\[
 \begin{aligned}
  \operatorname{Deck}(W)
    &=\operatorname{Deck}(P)\cup\operatorname{Deck}(MQ)
         \cup\mathcal C_{\rm old},\\
  \operatorname{Deck}(\rho(W))
    &=\operatorname{Deck}(P)\cup\operatorname{Deck}(MQ)
         \cup\mathcal C_{\rm new}.                            \tag{4.6}
 \end{aligned}
\]

For an arbitrary protected target family `mathcal U`, the rotation preserves
all of `mathcal U` if and only if

\[
             \mathcal U\cap
       \bigl(\operatorname{Deck}(W)-\operatorname{Deck}(\rho(W))\bigr)
                         =\varnothing.                        \tag{4.7}
\]

Equivalently, a protected target is lost precisely when every old witness
crosses the cut `P|M` and no new witness (including a new `Q|P` seam
witness) has its value.  A sufficient occurrence-labelled form is: each
protected target has one named witness avoiding `P|M`.

For preservation of the **entire old OR language**, the exact condition is

\[
 \boxed{\mathcal C_{\rm old}\subseteq
   \operatorname{Deck}(P)\cup\operatorname{Deck}(MQ)
      \cup\mathcal C_{\rm new}.}                             \tag{4.8}
\]

#### Proof

Equations (4.3)--(4.4) are the ray calculation of the split-pivot theorem
applied directly to the adjacent bases `Z,T`.  Rotation preserves the
relative order inside each of the two blocks `P` and `M Q`, proving the
transport statement.  Every interval is either internal to one block or
crosses its unique boundary, proving (4.6).  Equations (4.7)--(4.8) follow
immediately; the witness formulation partitions old intervals into those
which cross the cut and those which do not.  \(\square\)

The criterion is deliberately global.  Separate survival of the endpoint
chains does not imply (4.7) for the arbitrary-width upper bank.

## 5. Recovering an actual merged source letter

In `rho(W)`, contract the adjacent letters `Z,T` to

\[
                              X=Z\cup T.                     \tag{5.1}

\]

Call the contracted word `W_0`.  It has one fewer position.  Splitting its
actual source letter `X` back into `Z,T` recovers `rho(W)` literally.

### Corollary 5.1 (exact `+1` host conditional on one safe cut)

Let `mathcal U_0` be any target/witness bank realized in `W_0`.  Splitting
`X` adds one source position, preserves every member of `mathcal U_0` by
block contraction, and creates both complete coatom flags (4.3)--(4.4).
Every named owner or upper witness of `W_0` is transported with deadline
increased by one exactly when it contains `X`.

Thus a prepared-endpoint word plus the protected safe-cut condition (4.7)
plants the desired actual host.  No native maximal envelope containing `X`
is required; `X` is produced by contracting the newly adjacent endpoint
bases.

The length ledger is purely relative and must not be blurred:

\[
 |W|=|\rho(W)|=L,\qquad |W_0|=L-1.                           \tag{5.2}
\]

The final split has length `L`, namely `+1` relative to the contracted
reference `W_0`, but **zero** relative to the original endpoint word `W`.
Nothing here proves `L=B(k)+1` or `|W_0|=B(k)`; that equality is part of the
global Pascal host theorem still missing.

The unresolved point is whether one can choose the endpoint orientation and
rotation cut so that the contracted word `W_0` still carries the entire
required old bank and common-cap state.  This is a single guarded
cut/gammoid condition, not a label-supply or cardinality question.

## 6. Consequence for pivot count

There are now three sharply distinct statements.

1. **Native local connector:** one split is impossible in the full-ray
   normal form, and a bounded local ear has the linear deficit (1.2).
2. **Two separately prepared endpoints:** two one-sided duplicate splits
   always carry the two chains, at cost `+2`, once those endpoint antecedents
   coexist.  This is the unconditional geometric fallback under the
   prepared-endpoint hypothesis.
3. **Endpoint wrap:** one merged split, cost `+1`, carries both chains if the
   single rotation cut is protected.

The number of pivots is therefore absolute (`<=2`) after endpoint planting.
The difference between one and two is exactly the safe-wrap condition.

## 7. Frozen flat carriers usually forbid the wrap

There is a sharp reason not to search for (4.8) after freezing a generic
coefficient-one flat owner row.  Let a word have length `W+d`, and suppose
its `W` consecutive length-`d+1` windows are a bijection onto the `W`
middle owners.  Regard all `W+d` length-`d+1` windows cyclically.  A cyclic
rotation by `c` replaces the old interval of `W` cyclic start positions by
another interval of `W` starts.

### Proposition 7.1 (exact owner recut criterion)

A rotation preserves the flat owner palette if and only if every owner
value whose unique old start leaves the selected start interval is supplied
by one of the newly admitted cyclic windows.

In particular, if each old owner value occurs at exactly one of **all**
cyclic starts, then the identity is the only owner-preserving rotation.

#### Proof

The retained old starts keep their owner values.  Since the old row is a
bijection, the only missing values are those at dropped starts, and the only
possible new providers are the gained starts.  Under cyclic uniqueness every
old start must therefore be retained.  Two proper cyclic intervals of the
same length `W<W+d` are equal only at the identity shift.  \(\square\)

This is an owner-row statement, not a full-language theorem.  It can be
escaped in exactly the ways relevant here:

* rotate/rethread **before** assigning the owner bijection;
* recompile the owners simultaneously in a nonflat deadline staircase; or
* work at `B+1`, where the owner row may have one surplus window.

The saved-answer census supports the warning.  Among the flat answers for
`k=3,6,7,...,15`, the identity is the only middle-preserving cyclic shift
for

```text
k = 3,7,8,9,10,11,12,13,14,15.
```

The sole finite exception is `k=6`, which also admits shift `14`.  Thus the
endpoint wrap is not a generic postprocessing move on a frozen flat
coefficient-one carrier.  The positive theorem must choose the wrap and the
owner/common-cap assignment jointly.  No `B+1` flat carrier satisfying the
prepared endpoint hypotheses has yet been audited, so the one-surplus case
remains open rather than refuted.

Audit:

```text
scratch/audit_h1_flat_carrier_cyclic_recut_20260801.py
scratch/h1_flat_carrier_cyclic_recut_20260801.audit.json
```

Canonical payload SHA-256:

```text
774a6c8bcbbcedbb3e02dcf720cb415484da0ccd7f55c3f8972ca457b0a9d4b0
```

## 8. Scope

This note does not prove the protected cut exists in every Pascal child.
It proves where the missing global work resides and rules out spending more
effort on a bounded native-connector ear.  A positive completion may be
stated in either of two equivalent languages:

* find a rotation cut satisfying (4.7) together with the carrier/common-cap
  pins; or
* find an alternating gammoid path which moves the prepared prefix past the
  middle block without consuming a unique protected witness.

Dependencies:

* `MATH_THEOREM_H1_SPLIT_PIVOT_TWO_COATOM_RAYS_AND_NATIVE_HOST_GATE_20260801.md`;
* `MATH_THEOREM_COATOM_TWO_PHASE_BOUNDARY_CHAIN_CARVING_20260801.md`;
* `MATH_THEOREM_MONOTONE_PIVOT_INSERTION_AND_RAY_REPAIR_20260801.md`.
