# K17 candidate 1911: exact second-circuit service, age, and residence gate

Date: 2026-08-01  
Lane: A  
Status: proved reduction; complete targeted no-go for every single
one-side service circuit changing at most nine matching rows; and complete
no-go for the phase-loop, `C6`+phase-loop, and simultaneous `D`-`C6`/
`H`-`C6` compound shells.  No occurrence-age state bank or terminal repair
is claimed.

## 1. Authenticated inputs and exact scope

The frozen seed is the complement-dual factor

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/best.tsv
```

with SHA-256
`a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3`.
The extended one-side catalogue is

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/
  dual_splice_dev5_20260801/
```

and its audit has SHA-256
`7c659cddfd4c37b3829d7c74fa0599e2db80709640a58c153d78fc6fa6bf4ff2`.

Two rows matter here.

* Strict-dual candidate `72` changes six `D` rows, has assignment voltage
  zero, makes `A=CD` Hamilton, and leaves the complementary hole pair

  \[
        \mathcal H_{10}=\{0x03e4f\},\qquad
        \mathcal H_7=\{0x00d87\}.                                \tag{1.1}
  \]

  Indeed the canonical complement of `0x00d87` is `0x03e4f`.  Its factor
  still has two 715-owner quotient cycles, each of voltage 15.

  Its owner rows, old incidences, and new incidences are

  ```text
  owners  425,375,1221,1332,655,135
  old_D   3825,3380,10992,11993,5895,1222
  new_D   3830,3376,10990,11988,5903,1219
  ```

* One-side `H` candidate `1911` changes eight `H` rows.  The resulting
  factor is one 1,430-owner quotient cycle of voltage 9, has complete
  rank-ten palette, and has precisely

  \[
                  \mathcal H_7=\{0x00e0f,0x01547\}.               \tag{1.2}
  \]

  Its factor certificate has SHA-256
  `c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587`.

  The exact switched rows are

  ```text
  owners  425,395,396,665,650,608,157,135
  old_H   3829,3559,3567,5988,5854,5477,1415,1216
  new_H   3826,3558,3569,5989,5856,5478,1417,1219
  ```

  The old/new lower turn lists are respectively

  ```text
  old  00e0f,00e87,01547,01c55,00b0f,0091f,007c5,00b4d
  new  00787,00ea3,01457,00f15,0091f,0083f,0074d,00b0f
  ```

  so `0x0091f` is the exposed lower ticket that is recreated, while the two
  targets in (1.2) are precisely the unrecreated exposed tickets.  Both
  exposed upper tickets are recreated, which is why the upper palette is
  complete.

The candidate-1911 assignment-cycle voltage is 13, not zero.  Thus the
quoted `C16` is a quotient `C16`; in the physical `Z_17` cover it is one
`C_(16*17)=C272`, not 17 disjoint literal `C16`s.  Its residence effect
cannot be audited on eight quotient seams alone.

This note addresses only a second one-side `H` or `D` circuit applied to
the materialized candidate 1911, and the corresponding strict-dual repair
interface for candidate 72.  Ranks above ten and the common compiler remain
outside scope.

## 2. Current one-side normal form

Write the candidate-1911 matchings as `D,H` and its oriented owner
successor as

\[
                         \pi=H^{-1}D.                              \tag{2.1}
\]

Here `pi` is one 1,430-cycle with physical voltage 9.

### 2.1 An `H`-assignment circuit

For each owner `p`, write `F_p=H(p)`.  Form the phase-labelled directed
graph `G_H` whose arc

\[
                       p\buildrel e\over\longrightarrow q        \tag{2.2}
\]

means that the literal incidence `e=(p,F_q)` exists and is not `D(p)`.
Parallel incidences are separate arcs.  Label it by

\[
\begin{aligned}
 \ell_H(e)&=D(p)\cap F_q,\\
 u_H(e)&=D^{-1}(F_q)\cup p,\\
 s_H(e)&=s(e).                                                     \tag{2.3}
\end{aligned}
\]

All sets are evaluated in the common physical gauge of `e` and then
canonicalized.  A simple directed circuit

\[
                    \sigma=(p_0p_1\cdots p_{t-1})                 \tag{2.4}
\]

replaces `H(p_i)=F_(p_i)` by `H'(p_i)=F_(p_(i+1))`.  It is matching-exact,
and

\[
                         \pi'=\sigma^{-1}\pi.                    \tag{2.5}
\]

### 2.2 A `D`-assignment circuit

For each owner `x`, write `G_x=D(x)`.  Form `G_D` with a phase-labelled arc

\[
                       x\buildrel e\over\longrightarrow y        \tag{2.6}
\]

when `e=(x,G_y)` exists and is not `H(x)`.  Its labels are

\[
\begin{aligned}
 \ell_D(e)&=G_y\cap H(x),\\
 u_D(e)&=x\cup H^{-1}(G_y),\\
 s_D(e)&=s(e).                                                     \tag{2.7}
\end{aligned}
\]

A directed circuit `sigma` replaces `D(x)` by `D(sigma x)` and gives

\[
                         \pi'=\pi\sigma.                          \tag{2.8}
\]

Equations (2.2)--(2.8) are literal incidence statements.  Merely having
the quotient owner/facet endpoints is insufficient when parallel phases
are present.

## 3. Exact palette service-return theorem

Let `mu_10,mu_7` be the occurrence loads in candidate 1911.  For a chosen
`H` circuit, the deleted lower and upper labels are

\[
 \ell_H(p_i,p_i),\quad u_H(p_i,p_i),                              \tag{3.1}
\]

and the added labels are

\[
 \ell_H(p_i,p_{i+1}),\quad u_H(p_i,p_{i+1}).                      \tag{3.2}
\]

For a `D` circuit use the corresponding labels from (2.7).

### Theorem 3.1 (terminal two-hole criterion)

A one-side circuit repairs candidate 1911 while preserving both immediate
palettes if and only if

\[
 \mu_r(T)-\operatorname{loss}_r(T)
          +\operatorname{gain}_r(T)\ge1
 \quad (r\in\{7,10\},\ \text{every target }T),                   \tag{3.3}
\]

and

\[
 \operatorname{gain}_7(0x00e0f)\ge1,qquad
 \operatorname{gain}_7(0x01547)\ge1.                             \tag{3.4}

\]

Since the two holes are distinct and have current load zero, no one added
occurrence can serve both.  Hence any nontrivial repair circuit contains
at least two distinct **service arcs**.  Every remaining selected arc is a
return arc needed to close the matching circuit and its palette debt.

#### Proof

At an `H` owner `p_i`, only the lower turn between `D(p_i)` and its `H`
facet changes; at the destination facet only the upper turn between its
fixed `D` owner and the new `H` owner changes.  This gives (3.1)--(3.2).
The `D` statement is symmetric.  Subtracting and adding the exact local
occurrences proves (3.3).  Because both targets in (1.2) have load zero,
surjectivity is equivalent to (3.4), and distinct targets require distinct
new occurrences.  \(\square\)

This theorem must be applied to the materialized candidate-1911 loads.
Adding an isolated delta to the original complement-dual seed is unsafe
when the second circuit overlaps one of the first eight rows.

## 4. Phase loops and the minimal endpoint-changing circuit

Because the quotient incidence graph is a multigraph, an apparent
support-one exception must be separated first.  Replacing a selected
incidence `(x,f,s)` by a distinct parallel incidence `(x,f,s')` preserves
the endpoint matching and hence the quotient successor permutation.  It
changes one lower occurrence at owner `x`, one upper occurrence at facet
`f`, and one chronology phase.  Such a phase loop can serve at most one of
the two holes.

The exact candidate-1911 provider census contains no phase-loop provider
for either `0x00e0f` or `0x01547`, on either the `D` or `H` side.  Hence no
pair of endpoint-map-preserving phase loops can repair the named pair.  The
next shell must change quotient endpoints.

### Theorem 4.1 (odd-support topology condition)

If one simple one-side endpoint-changing assignment circuit preserves the
connected quotient topology of candidate 1911, its support `t` is odd.
Therefore the smallest possible endpoint-changing second circuit is a
`C6`, with `t=3` selected matching rows.

For any fixed three selected rows, cutting the current Hamilton cycle gives
three directed fragments.  Of the two cyclic endpoint orientations,
exactly one reconnects those fragments into one cycle; the other gives
three cycles.  Thus topology can be decided from the cyclic order of the
three cut darts before any palette replay.

#### Proof

The sign of a permutation on 1,430 owners is `-1` exactly when its number
of cycles is odd.  The current Hamilton permutation has sign `-1`.
Composing on either side with a `t`-cycle changes sign by `(-1)^(t-1)`, so
a new Hamilton permutation requires `t` odd.  For `t=3`, the old fragment
permutation and the endpoint reassignment are both 3-cycles.  Their product
is a 3-cycle for one relative orientation and the identity for the other.
\(\square\)

Combining Theorems 3.1 and 4.1 gives the smallest exact search object:

> a phase-labelled directed triangle in `G_H` or `G_D` containing one arc
> labelled `0x00e0f`, one arc labelled `0x01547`, and one return arc, in
> the topology-preserving orientation, satisfying the two palette ledgers.

This is a targeted service-return triangle problem, not a new whole-splice
enumeration.

## 5. Voltage and physical locality

For an `H` circuit `C`, put

\[
 \omega_H(C)=\sum_{p\in C}\big(s(H(p))-s(H'(p))\big).             \tag{5.1}
\]

For a `D` circuit put

\[
 \omega_D(C)=\sum_{x\in C}\big(s(D'(x))-s(D(x))\big).             \tag{5.2}
\]

If the terminal quotient factor is connected, its voltage is respectively

\[
                         V'=9+\omega_H(C),\qquad
                         V'=9+\omega_D(C)\pmod {17}.              \tag{5.3}

\]

Thus primitive physical topology requires `V'` nonzero.  A quotient
assignment circuit is 17 disjoint literal physical `C_(2t)` circuits
exactly when its assignment voltage `omega` is zero.  If `omega` is
nonzero, it lifts to one physical `C_(34t)` circuit.  In particular, a
zero-voltage service-return `C6` preserves the current factor voltage 9
and acts as 17 disjoint physical `C6`s; it is the sharp bounded-local
subclass.

## 6. Exact fixed-state age filter

Let a phase-labelled occurrence-age state be

\[
       S_x=(T_x;C_{x,0},C_{x,1},C_{x,2},C_{x,3}),
       \qquad C_{x,3}=\{\alpha_x\}.                               \tag{6.1}
\]

For a physical Johnson arc `x->rho^delta y`, write
`R^delta(S_x,S_y)=1` when

\[
\begin{aligned}
 T_x-\rho^\delta T_y&=C_{x,3},\\
 \rho^\delta C_{y,j+1}&\subseteq C_{x,j}\quad(0\le j\le2),\\
 \rho^\delta C_{y,0}&=\{\beta\}\mathbin{\dot\cup}
   \bigcup_{j=0}^2(C_{x,j}-\rho^\delta C_{y,j+1}),                \tag{6.2}
\end{aligned}
\]

where `rho^delta T_y-T_x={beta}`.

### Theorem 6.1 (local age score)

For a fixed cyclic-equivariant state bank, an `H` circuit changes age tests
only on the tails `pi^{-1}(P)`, where `P` is its selected owner set.  Its
exact score change is

\[
 \Delta_{\rm age}^{H}=
 \sum_{p\in P}\left[
 R^{\delta'_p}(S_{\pi^{-1}p},S_{\sigma^{-1}p})
 -R^{\delta_p}(S_{\pi^{-1}p},S_p)\right].                        \tag{6.3}
\]

For a `D` circuit the changed tails are `P` and

\[
 \Delta_{\rm age}^{D}=
 \sum_{x\in P}\left[
 R^{\delta'_x}(S_x,S_{\pi\sigma x})
 -R^{\delta_x}(S_x,S_{\pi x})\right].                            \tag{6.4}
\]

The terminal circuit preserves a literal fixed-state age chronology iff
every new term in (6.3) or (6.4) equals one and every unchanged old term
was already legal.

#### Proof

Equations (2.5) and (2.8) identify exactly the successor tails that change.
Equation (6.2) is the necessary-and-sufficient literal survivor/refresh
relation on one phase-labelled arc.  All other successor arcs and their
states are identical.  Subtraction gives (6.3)--(6.4).  \(\square\)

The candidate-1911 factor file records only incidence matchings; it has no
`C_0,C_1,C_2,C_3` state bank.  Therefore neither (6.3) nor (6.4) can be
evaluated from the authenticated factor alone.

If states may vary, let `M_e` be the Boolean matrix of all admissible state
pairs on each phase-labelled arc.  Cut the current Hamilton cycle at the
selected successor darts and multiply the `M_e` along each unchanged
fragment.  The Boolean trace of their topology-preserving cyclic product
is positive if and only if a terminal age decoration exists.  Tropical
products give the exact minimum number of illegal transitions, and a
polynomial/graded semiring retains prescribed type masses.  Independent
new-edge compatibility counts are not sufficient because the same state
must serve the incoming and outgoing fragment at each owner.

## 7. Phase-expanded residence filter

A second circuit on `t` quotient edge orbits cuts `17t` physical successor
darts.  Let `P_1,...,P_(17t)` be the resulting physical path words in the
current candidate-1911 owner cycle.  For threshold four, summarize each
coordinate trace on each piece by

* first and last bit;
* prefix and suffix run lengths truncated at four;
* a constant-piece flag; and
* the number of internal short runs.

These summaries form the associative boundary-run monoid.  Let `kappa(pi)`
be the total short-run count after concatenating pieces according to an
endpoint permutation `pi` and cyclically closing every resulting component.
If `pi_old` is the current pairing and `pi_new` the circuit pairing, then

\[
             B_{\rm new}-B_{\rm old}
                    =\kappa(\pi_{\rm new})-\kappa(\pi_{\rm old}). \tag{7.1}
\]

Restricting the charge to one-runs gives the positive-residence delta;
its vanishing, not its numerical value, is equivalent to the depth-three
four-deletion spine.  Including both bits gives signed residence.

Equation (7.1) is exact even when a whole path piece is constant in one
coordinate.  A quotient-only prefix/suffix test without the 17 phases is
unsound.  Candidate 1911's nonzero first-circuit voltage makes this warning
essential.

The factor certificate and incidence atlas determine all path words and
phase shifts, so (7.1) is evaluable without an occurrence-age state bank.
The independent replay below gives candidate 1911

\[
                         R_{<4}=4352,
                         \qquad \mathcal D=5525.                  \tag{7.2}
\]

These are raw positive-run diagnostics.  They do not instantiate the
literal state relations (6.2).

## 8. Candidate 72: the strict-dual repair interface

Candidate 72 remains complement-dual.  Let its Hamilton odd-graph
permutation be `A`, so the factor successor is `B=A^2`.  A second strict-dual
`D` circuit changing tails `X` has two different collars:

\[
       P=X\cup A(X)\quad\text{for turn palettes},\qquad
       Q=X\cup A^{-1}(X)\quad\text{for }B\text{-chronology}.       \tag{8.1}
\]

It repairs both holes in (1.1) exactly when the upper ledger gains
`0x03e4f`; complement duality then gains `0x00d87` automatically.  Since
`A` is Hamilton, a single circuit preserving Hamiltonicity must have odd
support, so `C6` is again minimal.  It must also retain nonzero `A` voltage.

For fixed age states, only the `Q` successor arcs need (6.2) rescoring.  For
variable states, the same fragment-transfer trace criterion applies to
`B=A^2`.  This route can repair the paired palettes while remaining in the
strict-dual face, but it cannot make the final factor connected: `A^2`
still has two parity cycles.  A later non-dual connector remains necessary.

## 9. Complete provider-cycle census through nine rows

For each side and each missing lower target, the materialized factor has
exactly ten direct service atoms:

\[
\begin{array}{c|cc}
 &0x00e0f&0x01547\\ \hline
D&10&10\\
H&10&10
\end{array}                                                       \tag{9.1}
\]

Starting from these 40 atoms, the proof-safe catalogue enumerates every
simple one-side matching circuit containing at least one service atom.
Any one-side repair must contain such an atom, so this is a complete
service-conditioned enumeration, not a heuristic sample.

The exact circuit counts are:

| changed rows `t` | unique circuits | upper-safe | quotient-connected and upper-safe | physical-connected and upper-safe |
|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 | 0 |
| 3 | 3 | 0 | 0 | 0 |
| 4 | 18 | 1 | 0 | 0 |
| 5 | 90 | 2 | 0 | 0 |
| 6 | 528 | 8 | 0 | 0 |
| 7 | 3,383 | 21 | 6 | 6 |
| 8 | 22,512 | 81 | 0 | 0 |
| 9 | 154,929 | 260 | 36 | 31 |

All `181,464` candidates are valid matching circuits.  None of the 37
physical-connected upper-safe candidates repairs both lower holes.

### Theorem 9.1 (scoped support-nine no-go)

No single simple one-side `D` or `H` assignment circuit changing at most
nine selected rows transforms candidate 1911 into a connected physical
factor with complete rank-ten and rank-seven palettes.

The best terminal debt within this shell occurs at `t=9`.  It is the
`D`-circuit

```text
owners     426,425,230,602,636,396,125,406,428
new edges  3838,3832,2076,5422,5724,3564,1128,3657,3855
```

and transports, rather than removes, the debt:

\[
 \{0x00e0f,0x01547\}\longmapsto\{0x00755,0x01547\}.              \tag{9.2}
\]

It remains connected and upper-complete, but its raw residence worsens to

\[
                         R_{<4}=4471,
                         \qquad\mathcal D=5661.                   \tag{9.3}
\]

#### Proof

With the opposite matching frozen, every new lower occurrence is the
label of one changed incidence atom.  Therefore a circuit repairing either
named hole contains at least one of the 40 atoms in (9.1), and a circuit
repairing both is present in the service-conditioned enumeration.  The
DFS fixes the first service atom, follows the exact matching exchange
digraph, keeps owners distinct, and closes only at the starting owner;
canonical owner/edge keys remove multiple generation when a circuit has
two service atoms.  Exact replay then checks both matching degrees, edge
disjointness, both complete palette ledgers, quotient connectedness,
nonzero physical voltage, and the physical run word.  The displayed counts
and absence of a hit prove the theorem.  \(\square\)

### Theorem 9.2 (small compound shells)

The same exact replay closes the smallest parity-evading and phase-return
compounds:

1. Candidate 1911 has exactly one parallel phase loop in total.  Hence no
   pair of phase loops exists.
2. Combining that loop with every `D`- or `H`-side `C6` gives `1247`
   assignments, `777` of them factor-valid, and none with a complete lower
   palette.  A two-loop augmentation is impossible.
3. There are `627` `D`-side and `621` `H`-side `C6` circuits.  All
   `389367` simultaneous pairs were replayed; `151655` are factor-valid,
   but none completes the lower palette even before the upper and topology
   tests.

Thus no pair of endpoint-preserving phase loops, no `C6` plus up to two
phase loops, and no simultaneous `D`-`C6`/`H`-`C6` compound repairs
candidate 1911.

#### Proof

Parallel loops are enumerated directly by equal owner and facet endpoints
with a different incidence phase.  The `C6` lists are the complete simple
directed triangles of the two matching exchange multigraphs, with parallel
arcs retained.  Applying each indicated product and replaying the two
matching degrees gives the valid counts; the exact lower occurrence ledger
has no hit in any class.  \(\square\)

The frozen artifacts are

```text
scratch/threadA_k17_candidate1911_age_local_repair_20260801/
  catalogue_k17_candidate1911_targeted_second_cycles_20260801.cpp
  SHA256 8c7924463259f286967878b9fad95d14355eb9b1c60280efe2e46366f931bd5d

  candidate1911_second_cycles_upto9.audit.json
  SHA256 936a49e852f5007bf156fb17cfd92ed1d46f02aee393f31ccfa28656fd161939

  candidate1911_second_cycles_upto9.tsv
  SHA256 836f72ae8aa84689f1911460761764f6c77f524fa3ffbef09177a5241a18294a

  audit_candidate1911_small_shell.py
  SHA256 e4e41e16cd29f15a0d7a6c90552aeb2afaca0f675f19c887390794e0be0b6017

  independent_small_shell.audit.json
  SHA256 32df045c06e0ceb5237f330426fb3ed6af7d7276d8b7c96300ce9d66079f10a5
```

The independent checker reconstructs the factor from the frozen incidence
atlas, reproduces the four direct-provider counts, independently enumerates
the one-side shell through support five, and replays all `389367` simultaneous
`C6` pairs and all `1247` `C6`-plus-loop assignments.  It obtains the same
zero lower-complete counts.  An earlier checker draft tested only colours
changed by the circuit and therefore admitted assignments that left one of
the two original holes unfilled; that draft and its counts are retracted.
The frozen checker above explicitly requires positive final multiplicity for
both `0x00e0f` and `0x01547`.

The no-go proved by the artifacts in this note is deliberately narrow:
it closes one-side support through nine and the three compound shells in
Theorem 9.2.  Independently, handoff item `2524D` has since extended the
one-side provider-anchored census through support eleven, finding no
terminal-palette-exact repair; therefore the first untested *single
one-side* shell is support thirteen (`C26`), not support eleven.  Neither
result excludes a longer simultaneous `D/H` compound, two interlacing
same-side circuits, occurrence-state redecoration, or a different first
splice.  Exact occurrence-age compatibility remains untestable until a
state bank is attached.
