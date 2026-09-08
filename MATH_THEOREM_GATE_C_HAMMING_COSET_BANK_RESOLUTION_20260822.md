# Gate C: Hamming-coset tour banks form an exact fourfold resolution

**Status (2026-08-22).**  Every assertion below is proved.  For one fixed
perfect pairing and cyclic pair order, a full-rank binary parity-check
matrix with distinct nonzero columns partitions the initial states into
middle-target-disjoint coherent-tour banks.  Its coset banks form an exact
fourfold resolution of the entire defect-one middle stratum: every target
belongs to exactly four banks.

Across all pairings this gives a regular tour-bank orbit with exact uniform
target marginal and normalized pair codegree at most that of the underlying
pairing-incidence orbit.  Random banks near-cover the middle layer at the
right exponential pairing-diversity scale, but they overlap one another;
the fourfold resolution does not by itself round them into a matching.

Let `b>=3` be odd and fix a labelled pairing

\[
                         \mathcal P=\{P_0,\ldots,P_{b-1}\}        \tag{0.1}
\]

with one directed cyclic order.  Put

\[
 q=b(b-1),\qquad W={2b\choose b},\qquad
 S_1=q2^{b-2}.                                         \tag{0.2}
\]

The last quantity is the size of the defect-one middle stratum of `P`.

## 1. Coset banks

Let `H` be an `r`-by-`b` binary matrix of full row rank whose columns

\[
                         h_0,\ldots,h_{b-1}\in\mathbb F_2^r      \tag{1.1}
\]

are nonzero and pairwise distinct.  Thus necessarily `2^r>=b+1`.  For a
syndrome `z in F_2^r`, define the state coset and its coherent-tour bank by

\[
 X_z=\{x\in\mathbb F_2^b:Hx=z\},\qquad
                         \mathcal B_z=\{\mathcal T(x):x\in X_z\}. \tag{1.2}
\]

Every coset has size `2^(b-r)`.  Distinct states in one coset differ by a
nonzero kernel word.  Such a word cannot have weight one, since no column
is zero, or weight two, since no two columns agree.  Hence its weight is at
least three.  For one fixed pair order, two coherent tours are internally
middle-target-disjoint exactly when their state distance is at least three.
It follows that every `B_z` is a middle-target-disjoint bank of

\[
                         m=2^{b-r}                      \tag{1.3}
\]

tours and therefore contains

\[
                         K=q2^{b-r}                     \tag{1.4}
\]

distinct middle targets.

## 2. Exact fourfold resolution

Fix a defect-one target `C`.  Its empty and doubled pairs are a unique
ordered pair `(P_t,P_i)`, `t!=i`.  For the fixed cyclic order, the target's
split choices determine every state bit outside `{t,i}`; the two omitted
state bits are free.  Thus `C` has exactly four preimage states

\[
                         x_0+\{0,e_t,e_i,e_t+e_i\}.      \tag{2.1}
\]

Their syndromes are

\[
 Hx_0+\{0,h_t,h_i,h_t+h_i\}.                           \tag{2.2}
\]

The four vectors in braces are distinct: `h_t,h_i` are distinct nonzero
vectors and hence linearly independent over `F_2`.

### Theorem 2.1 (fourfold bank resolution)

Every defect-one middle target of `P` belongs to exactly four of the
`2^r` coset banks.  Equivalently,

\[
 \boxed{\sum_{z\in\mathbb F_2^r}\mathbf1_{\{C\in\mathcal B_z\}}=4,
 \qquad
 \Pr_z(C\in\mathcal B_z)={4\over2^r}.}                 \tag{2.3}
\]

Consequently the `2^r` banks have total target multiplicity `4S_1`, in
agreement with `2^rK=4S_1`.

#### Proof

Equations (2.1)--(2.2) put the four preimage states in four distinct cosets,
and no other state produces `C`.  This proves every assertion. \(\square\)

The conclusion is stronger than a fractional statement: it is an exact
integral fourfold resolution by banks, each of which is already a middle
matching.  Different banks need not be disjoint from one another.

## 3. The all-pairing bank orbit

Let

\[
 \mathfrak P={(2b)!\over2^b b!},\qquad
 D_1={b\choose2}^2(b-2)!,\qquad p={D_1\over\mathfrak P}={S_1\over W}. \tag{3.1}
\]

Choose uniformly a perfect pairing, a labelled directed cyclic order of
its pairs, and a syndrome coset bank as above.  Pair labels carry the fixed
distinct columns (1.1).  Relabelling the ground coordinates permutes this
full labelled family, so every middle target has the exact global marginal

\[
 \boxed{p_{\rm bank}=p{4\over2^r}={K\over W}.}          \tag{3.2}
\]

For two targets at Johnson distance `d`, put `a=b-d`.  The number of
pairings compatible with both, divided by the one-target pairing degree, is

\[
 R_d={4ad(ad-1)+a(a-1)+d(d-1)
       \over b(b-1){b\choose d}}.                      \tag{3.3}
\]

For any fixed compatible pairing and order, each target belongs to four
cosets, while the two four-element coset sets intersect in at most four
elements.  Therefore

\[
 \boxed{
 {\Pr(C,D\in\mathcal B)\over\Pr(C\in\mathcal B)}
 \le R_d.}                                             \tag{3.4}
\]

After quotienting complementary targets, (3.3) has maximum
`5(b-2)/b^2` for `b>=7`.  Thus bundling does not worsen the exact pairing
codegree scale.  Inequality (3.4) may be strict; determining the exact
average intersection of the two syndrome planes in (2.2) is a finer
order-dependent question and is not needed for the present bound.

Finally, sample `R` labelled banks independently.  A fixed target is
uncovered with probability `(1-K/W)^R`, so some list of `R` banks has union
leave at most

\[
                         W\exp(-RK/W).                 \tag{3.5}
\]

Taking `R=ceil(a_b W/K)` with `a_b->infinity` gives an `o(W)` union leave
using

\[
 R=(a_b+o(1)){2^rW\over q2^b}
   =a_b\,\Theta\!\left({2^b\over b^{3/2}}\right)       \tag{3.6}
\]

banks.  Each bank is internally middle-target-disjoint, but different
banks in this random near-cover generally collide.  Selecting a
cross-bank-disjoint sublist that covers `(1-o(1))W` targets is precisely the
remaining middle-rounding theorem; adjacent ranks require the stronger
three-rank Cayley pruning rather than the raw Hamming cosets.

The companion checker
`scratch/verify_gate_c_hamming_coset_bank_resolution_20260822.py` exhausts
small states and fibers, verifies the exact fourfold multiplicity, bank
sizes, and within-bank middle disjointness.
