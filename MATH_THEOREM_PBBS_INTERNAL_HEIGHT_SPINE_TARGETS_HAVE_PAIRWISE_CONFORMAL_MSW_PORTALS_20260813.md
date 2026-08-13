# Every correct-rank internal PBBS height-spine target has a pairwise conformal MSW portal

**Date:** 2026-08-13  
**Status:** unconditional explicit portal theorem.  It closes the
negative-row-disjoint matching problem for the **set of distinct
correct-rank targets whose complete owner interval lies on the PBBS height
spine**.  It also yields a componentwise resident exact wreath factor
containing one literal clean source package for every such target.  It does
not yet cover cells whose owner interval enters the exterior PBBS return,
embed the compound low-spine path or another frozen module in the same
factor, or fuse the resulting wreath components.

## 1. The internal height-spine target set

Put

\[
                         n=2m+1,
 \qquad                  R=m+1,
\tag{1.1}
\]

and use coordinates `0,1,...,2m`.  The PBBS role-zero height spine is

\[
 U_h=\{0\}\mathbin{\dot\cup}[h+1,2h]
          \mathbin{\dot\cup}\{2h+2,2h+4,\ldots,2m\}.
\tag{1.2}
\]

Thus `|U_h|=R` and

\[
                         U_{h+1}=U_h-\{h+1\}+\{2h+1\}.
\tag{1.3}
\]

For integers `q>=2` and `A>=2`, let

\[
                         S_{A,q}:=\bigcap_{t=A}^{A+q}U_t,
\tag{1.4}
\]

whenever the displayed interval stays on the spine.

Fix a deadline `d` and henceforth assume

\[
                         m\ge3d+2,
 \qquad                  2\le q\le d.               \tag{1.4a}
\]

### Lemma 1.1 (correct-rank target classification)

One has

\[
 S_{A,q}=\{0\}
 \mathbin{\dot\cup}[A+q+1,2A]
 \mathbin{\dot\cup}\{2A+2,2A+4,\ldots,2m\},
\tag{1.5}
\]

where the ordinary interval is empty when its lower endpoint exceeds its
upper endpoint.  Moreover,

\[
                         |S_{A,q}|=R-q
\tag{1.6}
\]

if and only if `A>=q`.  The two boundary values agree:

\[
                         S_{q,q}=S_{q+1,q}.
\tag{1.7}
\]

Consequently every distinct correct-rank internal target has a unique
normal form `(S_{A,q},q)` with

\[
                         A\ge q+1,
 \qquad                  A\le m-q,                 \tag{1.8}
\]

#### Proof

Coordinate `0` belongs to every `U_t`.  An odd coordinate can survive
through `(1.4)` only in all ordinary intervals `[t+1,2t]`, giving
`[A+q+1,2A]`.  An even coordinate `2j>=2A+2` starts in the alternating
tail; if `t` reaches `j`, it moves into `[t+1,2t]` and remains there through
the end of the displayed interval.  Hence, outside the common ordinary
interval, all and only the even coordinates from `2A+2` onward survive.
This proves `(1.5)`.

If `A>=q`, its rank is

\[
 1+(A-q)+(m-A)=m+1-q=R-q.
\tag{1.9}
\]

If `A<q`, the ordinary interval is empty and the rank is `m-A+1>R-q`.
Equation `(1.7)` follows by comparing `(1.5)` at `A=q` and `A=q+1`.
For fixed `q`, formula `(1.5)` then recovers every normalized `A` from the
initial consecutive block, proving uniqueness. \(\square\)

For universal coverage, repeated lost occurrences of one value require
only one new literal source occurrence.  Thus the target bank in this note
is the **set** supplied by Lemma 1.1, not the occurrence multiset.  An
occurrence-labelled transport theorem with additional tickets would be a
strictly stronger problem.

## 2. An exact MSW flip-list identity

For a Dyck word `w`, let `rho(w)` be its one-based MSW flip permutation.
Write

\[
                         \mathsf O(w)
  =(\rho_1(w),\rho_3(w),\ldots)                    \tag{2.1}
\]

for its odd-position sublist.  We use the standard identities

\[
 \rho(PQ)=\rho(P)\mathbin\Vert(|P|+\rho(Q)),        \tag{2.2}
\]

\[
 \rho(1u0)=\bigl(2s,\ 2s-\rho(\mu u),\ 1\bigr),    \tag{2.3}
\]

when `1u0` has semilength `s`, together with the exact reflection law

\[
 2s+1-\rho(w)=\operatorname {rev}(\rho(\mu w)).    \tag{2.4}
\]

Fix a normalized pair `(A,q)` from `(1.8)` and put

\[
 a=2q-3,
 \qquad b=A-q,
 \qquad c=m-A-q+1.                                  \tag{2.5}
\]

Thus `a` is positive odd, `b>=1`, and `c>=1`.  Define

\[
 z_{A,q}=1^{a+b}0^b(10)^c0^a
 =1^{A+q-3}0^{A-q}(10)^{m-A-q+1}0^{2q-3}.
\tag{2.6}
\]

It is a Dyck word of semilength `m-2`: it is

\[
 1^a\bigl(1^b0^b(10)^c\bigr)0^a.                  \tag{2.7}
\]

### Lemma 2.1 (the PBBS tail occurs in the MSW odd list)

If the entries of `mathsf O(z_(A,q))` are numbered from one, then

\[
 \boxed{
 \{\mathsf O_j(z_{A,q}):q\le j\le m-2\}
 =[A+q-2,2A-3]
  \mathbin{\dot\cup}
  \{2A-1,2A+1,\ldots,2m-5\}.}
\tag{2.8}
\]

Empty progressions are omitted.

#### Proof

Put

\[
 V=1^b0^b(10)^c,
 \qquad W_j=1^jV0^j,
 \qquad M_j=j+b+c.
\tag{2.9}
\]

Applying `(2.3)` and then `(2.4)` gives the one-shell recurrence

\[
 \rho(W_j)=
 \bigl(2M_j,\operatorname {rev}(\rho(W_{j-1})+1),1\bigr).
\tag{2.10}
\]

Applying it twice yields

\[
 \rho(W_{j+2})=
 \bigl(2M_j+4,\ 2,\ \rho(W_j)+2,\ 2M_j+3,\ 1\bigr),
\tag{2.11}
\]

and hence

\[
 \mathsf O(W_{j+2})=
 \bigl(2M_j+4,\mathsf O(W_j)+2,2M_j+3\bigr).
\tag{2.12}
\]

For the base shell `j=1`, `(2.10)` gives

\[
 \mathsf O(W_1)\setminus\{2M_1\}
 =\operatorname {rev}(\mathsf O(V)+1)
\tag{2.13}
\]

as ordered lists.  The mountain formula and concatenation `(2.2)` give

\[
 \{\mathsf O(V)\}
 =[b+1,2b]
 \mathbin{\dot\cup}\{2b+2,2b+4,\ldots,2b+2c\}.
\tag{2.14}
\]

(The mountain part follows immediately by induction from `(2.3)`; its
odd-position values are exactly `[b+1,2b]`.  Each appended `10` then adds
the next even value by `(2.2)`.)

Thus `(2.8)` holds at `a=1`, equivalently `q=2`.

Increasing `a` by two increases `q` and `A=b+q` by one and increases the
ambient parameter `m` by two; that is,
`(A,q,m)` becomes `(A+1,q+1,m+2)`.  In `(2.12)`, the new leading entry enlarges
the discarded prefix from `q-1` to `q` entries; the old retained set is
translated by two; and the new terminal odd-position entry `2M_j+3`
supplies the new largest element `2m-5`.  Therefore

\[
 [A+q-2,2A-3]\mapsto[A+q,2A-1]
\]

and

\[
 \{2A-1,\ldots,2m-5\}_{\rm odd}
 \mapsto
 \{2A+1,\ldots,2m-3\}_{\rm odd}\cup\{2m-1\}.
\]

These are exactly the two sets in `(2.8)` for the incremented parameters.
Induction over odd `a=2q-3` proves the lemma. \(\square\)

## 3. The explicit applicable trade portal

The two words

\[
                         1100z_{A,q},
 \qquad                  1010z_{A,q}               \tag{3.1}
\]

are Dyck roots of semilength `m`.  Their canonical MSW rows form the
standard inverse-triple degree-two trade.  This is the universal identity
`(5.1)--(5.2)` in
`MATH_THEOREM_CLEAN_PACKAGE_CONFORMAL_WREATH_TRADE_PORTAL_AND_MATCHING_GATE_20260813.md`,
with the four exceptional labels in the initial `1100/1010` block.  In that
notation, its common tail has even-position shore

\[
 E=\bigl(4+\mathsf O(z_{A,q}),\ 2m+1\bigr)          \tag{3.2}
\]

in one-based labels, and one positive row is

\[
                         (3,4,E,1,2,O).             \tag{3.3}
\]

Here `O` is the other parity shore and is irrelevant to the displayed
portal.

After subtracting one from labels, the cyclic interval consisting of the
suffix of `E` beginning with `mathsf O_q(z_(A,q))`, followed by the label
`0`, has set

\[
 \begin{aligned}
 &\{0,2m\}
 \cup\{3+x:x\in[A+q-2,2A-3]\}\\
 &\hspace{28mm}\cup
 \{3+x:x\in\{2A-1,2A+1,\ldots,2m-5\}\}\\
 &\qquad=\{0\}\cup[A+q+1,2A]
             \cup\{2A+2,2A+4,\ldots,2m\}\\
 &\qquad=S_{A,q}.
 \end{aligned}                                      \tag{3.4}
\]

Its length is `m+1-q=R-q`.  Thus it is exactly the oriented pointed
interval portal required by the clean-package theorem.

### Theorem 3.1 (pairwise conformal portals for the distinct target set)

Let `mathcal S` be any set of distinct correct-rank targets represented by
normalized pairs `(A,q)` satisfying `(1.4a)` and `(1.8)`.  Then all trades
`(3.1)` are
simultaneously applicable to the canonical MSW exact factor, their
negative row pairs are pairwise disjoint, and simultaneous substitution
produces an exact wreath factor containing one literal clean collared
package for every target in `mathcal S`.

All owner and immediate-lower resources of the packages are mutually
disjoint.  No positive row or source interval is reused by two distinct
targets.

#### Proof

The initial positive and zero runs of `z_(A,q)` have lengths

\[
                         A+q-3,qquad A-q.
\tag{3.5}
\]

The following `(10)` block is nonempty.  These runs recover the
normalized pair `(A,q)`.  Hence distinct pairs give distinct `z` words.
The roots `1100z` are mutually distinct, the roots
`1010z` are mutually distinct, and no root of the first family equals one
of the second family.  Therefore their MSW factor rows are pairwise
distinct.  The negative row pairs are disjoint.  In fact they form a subset
of the offset-zero first-aligned-block MSW packet: for every selected pair,
the first aligned four-bit block is exactly `1100/1010`.

Each inverse-triple trade is individually applicable to the MSW factor.
Conformal simultaneous substitution now applies every trade at once and
preserves the exact rank-`m` window partition.  Complementation gives exact
rank-`R` owner incidence, while the rank-`m` windows are the immediate-lower
resources.  Equation `(3.4)` and the interval-to-clean-package theorem give
the required literal packages.  Pairwise disjoint negative supports imply
pairwise disjoint positive middle supports, so positive rows and their
selected middle occurrences cannot be reused. \(\square\)

### Corollary 3.2 (one target-independent aligned-packet host)

Apply the **entire** offset-zero first-aligned-block packet to the canonical
MSW factor.  The resulting one deterministic exact factor contains the
positive trade rows `(3.3)` for every normalized internal target satisfying
`(1.4a)` and `(1.8)`.  Hence it hosts all those clean packages
simultaneously; the factor does not have to be chosen after seeing the
target set.

#### Proof

Every root pair `(3.1)` has its first eligible aligned block at positions
`0,1,2,3`.  It is therefore one of the disjoint pairs selected by the
first-block involution.  Applying the whole packet includes all trades used
in Theorem 3.1, together with further row-disjoint exact trades.  The latter
cannot remove or collide with the selected positive rows. \(\square\)

### Corollary 3.3 (the deleted low-spine internal bank is quadratic as a set)

Delete the edges `U_hU_(h+1)` for `4<=h<=d`.  Among correct-rank
`q`-edge owner intervals lying wholly on the height spine, every lost target
has a normalized representative satisfying

\[
                         q+1\le A\le d              \tag{3.6}
\]

except for the single depth-`d` boundary value represented by `A=d+1`.
Consequently the number of **distinct** internal lost values is at most

\[
 \sum_{q=2}^{d-1}(d-q)+1
 =\frac{(d-2)(d-1)}2+1=O(d^2).                    \tag{3.7}
\]

All of them are installed simultaneously by Theorem 3.1.

#### Proof

An interval crossing a deleted edge has literal start `A<=d`.  Correct rank
forces `A>=q` by Lemma 1.1.  The value at `A=q` is normalized to `A=q+1`;
for `q<d` this is already in `(3.6)`, while for `q=d` it gives the one
displayed exception.  Count the remaining integer pairs and apply Theorem
3.1. \(\square\)

## 4. Componentwise residence is automatic

Every wreath row on `2m+1` labels has one cyclic run of `m` consecutive
owners omitting a fixed coordinate and one cyclic run of `m+1` consecutive
owners containing it.  Consequently every row is positive- and zero-safe
at every aperture

\[
                         d+1\le m.                  \tag{4.1}
\]

### Corollary 4.1 (resident exact row host)

Under `(4.1)`, the exact factor in Theorem 3.1 is componentwise
`d`-resident.  In the maximal depth-`d` antecedent of each selected positive
row, the portal `(3.4)` supplies the literal source interval of the clean
package and hence the exact target `S_(A,q)`.

Thus the internal-spine package bank does not require an age-Hall
completion: it is installed by exact row trades inside a factor whose every
component is already resident.

This conclusion is componentwise.  It does not join the exponentially many
wreath rows into one cyclic chronology, and it does not assert that an
independently frozen PBBS compound path, rigid packet, socket state, history
ticket, or cap endpoint lies in the same exact factor.

## 5. Exact remaining boundary

The theorem closes the following formerly open compatibility gate:

\[
 \boxed{
 \begin{gathered}
 \text{distinct correct-rank internal height-spine targets}\\
 \Longrightarrow
 \text{explicit pairwise negative-row-disjoint applicable MSW trades}\\
 \Longrightarrow
 \text{one componentwise resident exact factor with literal packages.}
 \end{gathered}}
\tag{5.1}
\]

It does **not** yet close:

1. correct-rank casualties whose owner interval leaves the explicit
   height spine and enters an exterior PBBS return context;
2. coexistence with the compound low-spine palette path and the frozen
   rigid/module bank in the same row-trade factor;
3. exact nonmiddle tickets not encoded by owner/immediate-lower incidence;
4. protected fusion of the wreath components and the final typed cap.

Those are now the genuine remaining rows.  The negative-row rainbow
matching for the internal-spine target **set** is no longer one of them.

## 6. Finite replay data

The standard-library verifier

* `scratch/audit_pbbs_internal_spine_conformal_msw_portals_20260813.py`

reconstructs the canonical MSW factor and, for every normalized pair in its
test range, checks `(1.5)`, Dyck legality, `(2.8)`, the literal positive-row
portal, the inverse-trade support identity, pairwise negative-row
disjointness, and the exact simultaneous substituted factor.  The H100 run
for `m=4,...,11` passed, with respectively

\[
                         1,1,3,4,7,9,13,16
\tag{6.1}
\]

simultaneously selected normalized targets.  Its output is

* `scratch/h100_results/pbbs_internal_spine_conformal_m4_m11_20260813.json`.

A separate H100 formula replay checked `(2.8)` in `54,144` deadline-range
parameter cases through `m=150`; its transcript is

* `scratch/h100_results/pbbs_internal_spine_formula_m150_20260813.stdout`.

These computations audit the formulas; the theorem itself is the symbolic
proof above.
