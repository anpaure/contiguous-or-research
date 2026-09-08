# Thread D: run-transversal `c`-space and the exact erosion/compiler tower

Date: 2026-07-29

Status: exact theorem and lightweight finite regression.  The note proves
the eager Johnson normal form, including composite odd `k`, and the erosion
identity used by the one-core compiler.  It does not use the three-width
upper approximation, `ready15` forced ports, or a new heavy search.  It does
not claim a new `k=15` carrier.

## 1. Setup and indexing

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r}=kN,
\]

and identify coordinates with \(\mathbb Z_k\) and physical positions with
\(\mathbb Z_W\).  Given a cyclic binary word
\(c\in\{0,1\}^{\mathbb Z_W}\), put

\[
 T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.                 \tag{1.1}
\]

All subscripts are cyclic.  Then

\[
 T_{i+N}=\rho T_i,                                   \tag{1.2}
\]

where \(\rho(x)=x+1\).  A unit-voltage chronology
\(T_{i+N}=\rho^vT_i\) is reduced to (1.2) by the coordinate multiplier
\(x\mapsto v^{-1}x\); this is valid for composite odd `k` precisely because
`v` is a unit.

For \(a\in\mathbb Z_N\), define

\[
\begin{aligned}
 C_a&=\sum_{p\equiv a\pmod N}c_p,\\
 S_a&=\sum_{p\equiv a\pmod N}(1-c_p)c_{p+1},\\
 E_a&=\sum_{p\equiv a\pmod N}c_p(1-c_{p+1}).         \tag{1.3}
\end{aligned}
\]

Thus `S_a` counts `01` edge tails in residue `a`; the actual first `1` is
at residue `a+1`.  The variable `E_a` counts `10` edge tails, equivalently
last-`1` endpoints, in residue `a`.  This convention is the one implemented
by `scratch/threadD_cspace_compiler_benders.py`.

## 2. The exact seam identities

### Theorem 2.1 (run-transversal Johnson normal form)

For every \(i\in\mathbb Z_W\),

\[
\boxed{
 |T_i|=C_i,\qquad
 |T_{i+1}\setminus T_i|=S_i,\qquad
 |T_i\setminus T_{i+1}|=E_i.}                       \tag{2.1}
\]

Consequently,

\[
 C_{i+1}-C_i=S_i-E_i,
 \qquad
 |T_i\mathbin\triangle T_{i+1}|=S_i+E_i.            \tag{2.2}
\]

In particular, under the rank equations \(C_a=r\) for every
\(a\in\mathbb Z_N\),

\[
 \boxed{
 T_i,T_{i+1}\text{ form a Johnson edge for every }i
 \iff S_a=E_a=1\text{ for every }a\in\mathbb Z_N.}  \tag{2.3}
\]

#### Proof

For fixed `i`, the map

\[
 x\longmapsto p=i-xN
\]

is a bijection from \(\mathbb Z_k\) to the `k` positions congruent to `i`
modulo `N`.  Equation (1.1) therefore gives the first identity of (2.1).
The coordinate `x` is inserted at the seam \(T_i\to T_{i+1}\) exactly when

\[
 c_{i-xN}=0,\qquad c_{i+1-xN}=1,
\]

which is one `01` edge tail in residue `i`; it is deleted exactly when the
same pair is `10`.  This proves all of (2.1).  Subtraction and addition give
(2.2).

If all class sums are `r`, (2.2) gives \(S_i=E_i\).  A Johnson edge has
symmetric difference two, so \(S_i+E_i=2\), whence
\(S_i=E_i=1\).  Conversely those equalities give one insertion and one
deletion, hence a Johnson edge between two rank-`r` sets.  Equivariance
propagates the `N` quotient seams to all `W` physical seams.  \(\square\)

The sometimes quoted global argument that one run start supplies `k`
translated insertion events proves only that the total number of runs is
`N`.  It does not prove one start in each residue.  Identities (2.1)--(2.2)
are the required residuewise argument.

### Corollary 2.2 (rank may be reduced to one total equation)

If \(S_a=E_a=1\) for every `a`, then (2.2) shows that all `C_a` are equal.
Thus the `N` class-sum equations are equivalent to the single equation

\[
 \sum_{p\in\mathbb Z_W}c_p=rN                          \tag{2.4}
\]

once both transversals are imposed.  The individual class equations remain
the stronger propagation form and are retained in the implementation.

There are exactly `N` cyclic one-runs.  Equivalently, `c` is a cyclic
placement of `N` disjoint one-intervals whose first-`1` and last-`1`
residues are both transversals, and whose lengths sum to `rN`.  This is not
a free product of two permutations and a composition: disjointness,
positive zero gaps, and the relation between a start, its length, and its
endpoint must also hold.

## 3. Residence, Hamiltonicity, and the first lower row

For every coordinate `x`, its membership trace is

\[
 \mathbf 1_{\{x\in T_i\}}=c_{i-xN}.                 \tag{3.1}
\]

Hence depth-`d` residence is exactly the assertion that every cyclic
one-run of `c` has length at least `d+1`.

The rotation action on each central rank is free for every odd `k`, including
composite `k`.  Indeed, if a nonidentity rotation fixes a set, its coordinate
orbits have one common length \(L>1\) dividing `k`, so `L` divides the set's
rank.  But

\[
 \gcd(k,m)=\gcd(k,m+1)=1.                            \tag{3.2}
\]

Therefore all rank-`r` and rank-`r-1` rotation orbits have size `k`, and
there are exactly `N` of each.  It follows that the physical chronology is
a Hamilton Johnson cycle if and only if
\(T_0,\ldots,T_{N-1}\) lie in pairwise different rotation orbits.

Under Theorem 2.1, every

\[
 X_i=T_i\cap T_{i+1}
\]

has rank `r-1` and satisfies \(X_{i+N}=\rho X_i\).  Exact lower-`q1`
rainbow is therefore equivalent to pairwise distinct rotation orbits among
\(X_0,\ldots,X_{N-1}\).  Rank is automatic; rainbow is not.  A collision
cut must allow either complete adjacent-column motif to change.  Banning one
column or one endpoint alone is not a valid consequence.

## 4. The exact erosion tower

For \(0\le q\le d\), define the backward erosion row

\[
 P_i^{(q)}=\bigcap_{a=0}^{q}T_{i-a}.                 \tag{4.1}
\]

Thus \(P^{(0)}=T\), and the compiler envelope is
\(P=P^{(d)}\).  Let the cyclic Boolean derivative be

\[
 (DZ)_i=Z_i\cup Z_{i+1}.                             \tag{4.2}
\]

### Theorem 4.1 (rank-exact Johnson erosion tower)

Assume the rank, run-transversal, and depth-`d` residence conditions.  Then
for every \(0\le q\le d\),

\[
 \boxed{|P_i^{(q)}|=r-q}                             \tag{4.3}
\]

for every `i`; and for every \(0\le q<d\),

\[
 \boxed{DP^{(q+1)}=P^{(q)}.}                        \tag{4.4}
\]

In particular every row \(P^{(q)}\), \(0\le q\le d\), is itself a cyclic
Johnson chronology at rank `r-q`, and

\[
 D^jP^{(d)}=P^{(d-j)}\quad(0\le j\le d),
 \qquad D^dP^{(d)}=T.                               \tag{4.5}
\]

#### Proof of the ranks

Write the Johnson seam \(T_j\to T_{j+1}\) as deletion of `a_j` followed by
insertion of `b_j`.  In the window
\(T_{i-q},\ldots,T_i\), the intersection is

\[
 P_i^{(q)}
 =T_{i-q}\setminus\{a_{i-q},a_{i-q+1},\ldots,a_{i-1}\}.              \tag{4.6}
\]

The displayed deleted coordinates are distinct.  If one coordinate were
deleted twice within at most `q<=d` seams, it would have to be reinserted
between the two deletions and then have a positive residence interval of
length at most `d`, contrary to depth-`d` residence.  Every element never
deleted remains throughout the window.  Moreover every displayed deletion
already belongs to the initial state \(T_{i-q}\): otherwise its current
one-run would have started at an insertion strictly inside the same
`q`-seam window and ended at the displayed deletion, again giving a positive
run of length at most `d`.  Thus (4.6) removes exactly `q` distinct members
of the initial rank-`r` set, and (4.3) follows.

#### Proof of the derivative identity

Both \(P_i^{(q+1)}\) and \(P_{i+1}^{(q+1)}\) are contained in
\(P_i^{(q)}\), because their windows respectively add the left or right
endpoint to the common window \(T_{i-q},\ldots,T_i\).

Conversely, take \(x\in P_i^{(q)}\).  It is present in the `q+1`
consecutive states \(T_{i-q},\ldots,T_i\).  If it is also present in
\(T_{i-q-1}\), then \(x\in P_i^{(q+1)}\).  Otherwise its current one-run
starts at \(T_{i-q}\).  Since `q<d` and every one-run has length at least
`d+1`, it is still present in \(T_{i+1}\), and hence
\(x\in P_{i+1}^{(q+1)}\).  This proves (4.4).

Applying (4.4) with `q-1` gives

\[
 P_i^{(q)}\cup P_{i+1}^{(q)}=P_i^{(q-1)}.
\]

The two left sets have equal rank `r-q` and their union has rank `r-q+1` by
(4.3), so they differ by exactly one deletion and one insertion.  Thus every
erosion row is Johnson.  Iterating (4.4) gives (4.5).  \(\square\)

The scalar version is also useful.  Put

\[
 e_q(p)=\bigwedge_{a=0}^{q}c_{p-a}.
\]

Then

\[
 P_i^{(q)}=\{x:e_q(i-xN)=1\},
\qquad
 e_{q+1}(p)\vee e_{q+1}(p+1)=e_q(p)                 \tag{4.7}
\]

for `q<d`.  The only possible failure of the reverse scalar implication
would be a maximal one-run of length `q+1`, which residence excludes.

### Corollary 4.2 (one-core sandwich)

Let \(P=P^{(d)}\), let \(C_i\subseteq A_i\subseteq P_i\), and suppose

\[
 DC=DP.                                              \tag{4.8}
\]

Then `DA` is sandwiched between the equal sets `DC` and `DP`, so

\[
 D^jA=D^jP=P^{(d-j)}\quad(1\le j\le d).             \tag{4.9}
\]

In particular the physical compiler reaches the exact middle chronology
\(D^dA=T\).  This is the structural reason the compiler must solve an exact
one-core problem rather than trust forced ports alone.

## 5. Sound Benders interface

The eager master may replace all `kN=W` Johnson XOR variables by exact
reifications

\[
 s_p\leftrightarrow(\neg c_p\wedge c_{p+1}),
 \qquad
 e_p\leftrightarrow(c_p\wedge\neg c_{p+1}),          \tag{5.1}
\]

and the `2N` equations

\[
 \sum_{p\equiv a}s_p=1,
 \qquad
 \sum_{p\equiv a}e_p=1.                             \tag{5.2}
\]

Together with class sums and residence these are equivalent to the former
Johnson rows.  The global equality `#01=N` is now redundant.

The remainder of a proof-safe loop is unchanged:

1. middle and lower-`q1` orbit collisions generate joint relation cuts;
2. for lower depth `q<=d`, containment of a rank-`r-q` target in a
   `(q+1)`-column intersection is already equality by Theorem 4.1, so no
   outside-coordinate or rank auxiliaries are needed;
3. upper rank `r+1` may use adjacent Johnson-edge unions; every deeper target
   is separated by the exact next-occurrence all-width oracle and a
   maximal-good-run blocker no-good, with the complete arbitrary-width
   contained-suffix recurrence retained as an independently tested fallback;
4. the fixed carrier is passed to exact one-core enumeration, exact weighted
   quotient Hall, a physical matching, and a safe-cut scan;
5. `PASS` is permitted only after the word emitted in that same run has the
   compiler-recorded hash and passes literal exhaustive verification.

The positive predicate also carries an explicit `upper_audited` bit.  An
audit constructed with upper enumeration disabled has an empty missing list
but must fail closed; emptiness is not itself evidence that the oracle ran.
It recomputes the forced target count
(sum_{j=1}^{r-d}inom{k}{j}), requires both Hall totals and the physical
matching to equal it, checks every compiler dimension against the carrier,
and recomputes the complete safe-cut list before accepting `used_cut`.
From the retained word it then reconstructs the oriented compiled row `A`,
checks the cyclic collar, `A_i subseteq P_i`, `DA=DP`, and the literal
occurrence of every low target.  Thus the integral matching/one-core witness
is replayed from the word rather than inferred only from scalar solver fields.
Self-consistent fake zero-sized Hall ledgers therefore fail even when paired
with a separately valid literal word.
Negative architecture statuses likewise emit a c-assignment no-good only
after an independent complete carrier replay and exact dimension/target/Hall
metadata checks.  Missing metadata emits `NO_CSPACE_CUT`; at `k=9` the
globally undersized cyclic architecture emits the stronger explicit
`COMPILER_ARCHITECTURE_UNSUPPORTED_NO_CUT` scope.

A timeout, `UNKNOWN`, sampled core failure, forced-port `READY`, or a model
using only three candidate upper widths is not a proof-positive or a proof of
infeasibility.  A fixed-carrier compiler failure may forbid the complete
current `c` assignment inside the declared compiler architecture; it may not
forbid an isolated column.

## 6. Exact `k=9` and `k=11` regression boundary

The following are lightweight replays of the retained spirals.

| field | `k=9` | `k=11` |
|---|---:|---:|
| `W,N,r,d` | `126,14,5,2` | `462,42,6,3` |
| source voltage | `4` | `2` |
| ones in `c` | `70` | `252` |
| cyclic one-runs | `14` | `42` |
| start/end count in every residue | `1/1` | `1/1` |
| class-sum value | `5` | `6` |
| Johnson/middle/q1/residence defects | `0` | `0` |
| lower and complete-upper holes | `0` | `0` |

The run histograms are

\[
\begin{aligned}
 k=9:&\quad 3^6,4^3,6,7^2,8,12,\\
 k=11:&\quad 4^{13},5^{17},6^4,7^2,9^2,11,12,15,21.
\end{aligned}                                       \tag{6.1}
\]

At `k=9`, the terminal erosion row \(P^{(2)}\) covers every rank-three
target, so the carrier itself passes.  Nevertheless the pure one-core
envelope Hall value is exactly

\[
 126/129.                                            \tag{6.2}
\]

There are 129 nonempty targets of ranks at most three but only 126 cyclic
one-core positions; choosing a nonzero core can only delete adjacencies.
Even the final length satisfies `W+d=128<129`, so a row-zero-only compiler
cannot be optimal.  The unrestricted depth-two sandwich compiler uses its
linear boundary/derivative slots and emits the verified length-128 word

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/k09_equi_new.word
SHA-256 0f282a2c5bb61c0ea48d49c5966eafba3ceb8a30cc40150a92764c1321c21b7c
```

covering all 511 nonempty masks.  Thus the correct one-core regression
status is carrier-positive/compiler-architecture-inapplicable, not a carrier
nogood and not an obstruction to \(\nu(9)=128\).

At `k=11`, the zero-core envelope weighted Hall value is `231/231`.  The
retained end-to-end repository compilation emits

```text
/Users/amir.nuriyev/Documents/problem/scratch/sound_cword_cegar_k11_radius0.word
SHA-256 0f80c3295248a862b0fd5ad6a594a4162c346e0d9e404d351e9a28dbdcba38a0
```

of length 465.  Literal replay covers all 2,047 nonempty masks and verifies
the middle row exactly.  The independently generated fresh word
`k11_equi_new.word` (SHA-256 `0dee7330...`) is a second literal regression,
not the artifact used by the compiler-ready predicate here.  A fail-closed
`k=11` pipeline must independently
reconstruct the carrier, solve the core/Hall/physical matching and safe-cut
subproblems, and then reproduce this kind of literal positive certificate;
the retained word alone is a regression oracle, not a solver shortcut.

As a tiny exhaustive check of Theorem 2.1, at `k=3` all three rank-correct
binary words are both Johnson and run-transversal.  At `k=5`, exactly 35 of
the 100 rank-correct words satisfy either condition, with no mismatch.

## 7. Audited source boundary

The run-transversal claim was read from the complete current copies of

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/GENERAL_CONSTRUCTION.md
/Users/amir.nuriyev/Downloads/opusproblem/work/LEDGER.md
/Users/amir.nuriyev/Downloads/opusproblem/work/cword.py
```

whose observed SHA-256 values were respectively

```text
3254248dfe29c425d12f0f7ba814eeb96366bf18586413cd83717d475ecbba25
3dd211ae6109a7a88f0f39aa323b43bd57773f2b9629c7960f12aecc88f89923
ba2860ac948a438a2a8d08e8389e783a2a87ea6243947c352a8682911bb9a166
```

The last source correctly reifies the run transversals, but its legacy
finite-width upper rows and single-column nogood helper are not imported as
proof rules.  The exact all-width upper oracle, joint collision rows, and
literal compiler verifier remain mandatory.

Finally, the retained two-run endpoint-swap portfolio
`scratch/k15_runtrans_swap_portfolio_20260729.audit.json` exhausted 4.499
billion proposals across twelve seeds without improving energy 661.  This is
a scoped negative experiment, not an invariant or a Benders row.  The current
master therefore uses global/multi-run CP motion and compiler-derived cuts;
it does not spend another search on that local neighborhood.
