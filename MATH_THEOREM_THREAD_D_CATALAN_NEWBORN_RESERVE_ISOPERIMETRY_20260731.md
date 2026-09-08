# Strict DERF newborn banks: exact reserve isoperimetry and the row-atomic obstruction

Date: 2026-07-31  
Status: dimension-uniform equivalence and conditional induction theorem
proved; one literal failure and one literal regeneration step audited.  The
natural row-atomic sufficient certificate is refuted on every authenticated
output at parameters five through seven.  Universal inherited-orientation
absorption at parameters six and seven remains **UNKNOWN**.

## 0. Result

Let a strict DERF output at parameter `m` split, as it must, into

\[
                 F_m=(c+F_{m-1})\;\dot\cup\;B_m .       \tag{0.1}
\]

The paths in `c+F_(m-1)` are the inherited bank `I`; those in `B_m` are
the newborn bank `B`.  Fix the orientations of the newborn paths and allow
every inherited path to be reoriented independently.  For either strict
occurrence shore, write `Gamma(H)` for the outer boundary of a set `H` of
middle vertices.  Let

* `kappa_I(H)` be the number of inherited endpoint blocks touched by `H`;
* `Z_B` be the selected newborn terminal bank on that shore; and
* `e(H)=kappa_I(H)+|Z_B intersect H|`.

Then the fixed newborn orientation absorbs **every** inherited orientation
if and only if

\[
 R|H|+Ce(H)\ \le\ N|\Gamma(H)|\qquad(H\subseteq X).   \tag{0.2}
\]

Equivalently, with the exact reserve

\[
                       \rho(H)=|H|-e(H),               \tag{0.3}
\]

one has

\[
 \boxed{\quad
 C\rho(H)\ \ge\ N\bigl(|H|-|\Gamma(H)|\bigr)
 \quad(H\subseteq X).\quad}                           \tag{0.4}
\]

Thus only middle sets with positive ordinary Hall defect
`|H|-|Gamma(H)|` matter.  Each unit of such defect costs `N/C` reserve
units.  The reserve is literal:

\[
 \rho(H)=
 |H\setminus(E_I\cup Z_B)|+
 \sum_{i:\,a_i\ne b_i}
       {\bf1}[a_i\in H,\ b_i\in H],                  \tag{0.5}
\]

where `E_I` is the set of distinct inherited endpoint vertices and
`{a_i,b_i}` is the endpoint block of inherited path `i`.  A singleton
inherited path contributes no second-endpoint reserve.  Formula (0.5) is
the requested numerical invariant: every occurrence-deficient middle set
must contain enough unprotected vertices and complete nontrivial inherited
endpoint pairs.

The invariant is not automatic under strict DERF.  The authenticated
`n=3 -> 4` output has on its upper shore a set with

\[
 (|H|,|\Gamma(H)|,\kappa_I,|Z_B\cap H|,\rho)
                      =(17,10,5,3,9),                 \tag{0.6}
\]

and hence

\[
                    42\cdot9-56\cdot7=-14.            \tag{0.7}
\]

By contrast, the stored newborn bank in the authenticated `n=4 -> 5`
step satisfies (0.4) on both shores for all inherited orientations.  This
is an exhaustive `2^10=1,024` effective-orientation replay; four inherited
singleton directions are immaterial.

There is a tempting purely local proof: give each outer row `N` units,
give every middle vertex an `R`-capacity resource, and give every inherited
endpoint pair and selected newborn terminal a `C`-capacity resource.  An
outer row may use a pair resource only when it sees both endpoints.  A
complete flow is sufficient for (0.2), but it is not necessary.  It fails
sharply on all six authenticated shores at `m=5,6,7`: the numbers of
inherited pairs with no common outer neighbour are

\[
 (8,8),\qquad(25,22),\qquad(98,86),                   \tag{0.8}
\]

and the exact flow deficits are respectively

\[
 (1056,1056),\quad(10725,9438),\quad(140140,122980),  \tag{0.9}
\]

which are exactly `C` times (0.8).  In particular even the robust positive
`n=4 -> 5` bank has no row-atomic proof of this form.  Any uniform proof
must pool reserve across several outer rows or use the exact joint reserve
profile; a single common-neighbour allocation cannot work.

## 1. Parameters and endpoint blocks

At output parameter `m`, put

\[
 \begin{aligned}
 M&=\binom{2m}{m},&N&=\binom{2m}{m-1},
 &P&=\binom{2m}{m-2},\\
 C&=M-P,&R&=N-C,&K&=M-N.
 \end{aligned}                                       \tag{1.1}
\]

The occurrence graph on one shore is

\[
                         G=(O,X),\qquad |O|=P, |X|=M. \tag{1.2}
\]

There are `K` output paths in total.  Their endpoint supports are disjoint
because the paths partition `X`.  The inherited bank has
`Cat_(m-1)` paths and the newborn bank has
`Cat_m-Cat_(m-1)` paths.

For an inherited path `i`, let `{a_i,b_i}` denote its two endpoints; for a
singleton path these are the same vertex.  A fixed orientation of a
newborn path selects one terminal on the upper shore and the complementary
terminal on the lower shore.  Denote the resulting shore-specific newborn
terminal set by `Z_B`.

For a middle set `H`, define

\[
 \kappa_I(H)=
   |\{i:\{a_i,b_i\}\cap H\ne\varnothing\}|,\qquad
 e(H)=\kappa_I(H)+|Z_B\cap H|.                       \tag{1.3}
\]

The endpoint blocks and newborn terminal singletons have disjoint
supports.  Hence one may inject every counted block in (1.3) into a
distinct vertex of `H`, so

\[
                         0\le e(H)\le |H|.             \tag{1.4}
\]

This proves that the reserve (0.3) is nonnegative.  Counting the first
endpoint of a touched inherited block against `e(H)` leaves one reserve
unit exactly when a nontrivial block is wholly in `H`; every vertex outside
all protected supports also leaves one unit.  This proves (0.5), including
the necessary exclusion of singleton paths from its second sum.

The Catalan parameter identities give the total scaled capacity identity

\[
                         RM+CK=NP.                    \tag{1.5}
\]

## 2. Exact complement theorem

For an outer family `U subseteq O`, let

\[
                         W=\Gamma(U)\subseteq X.       \tag{2.1}
\]

Let `p_I(W)` count inherited endpoint blocks wholly contained in `W`, and
let `t_B(W)=|Z_B intersect W|`.

### Theorem 2.1 (absorbing-newborn reserve equivalence)

For a fixed newborn orientation on one shore, the following are equivalent.

1. Every orientation of all inherited paths satisfies every terminal-
   buffer row; equivalently, the orientationwise minimum of each row obeys
   \[
   N|U|\le R|W|+C\bigl(p_I(W)+t_B(W)\bigr)
                         \qquad(U\subseteq O).         \tag{2.2}
   \]
2. Every middle set satisfies the endpoint-block isoperimetric inequality
   \[
        R|H|+Ce(H)\le N|\Gamma(H)|.                   \tag{2.3}
   \]
3. Every middle set satisfies the reserve inequality (0.4).

Consequently a newborn orientation absorbs every inherited orientation on
both shores if and only if (0.4) holds for both shore occurrence graphs,
using complementary newborn terminal choices.

#### Proof

For fixed `W`, minimizing inherited terminal incidence over all inherited
orientations selects an endpoint outside `W` whenever possible.  Therefore
the minimum is exactly one for each inherited endpoint block wholly in
`W`, and zero for every other inherited block.  The newborn contribution
is fixed.  This gives (2.2).

Put `H=X\setminus W`.  An inherited block is wholly in `W` precisely when
it is not touched by `H`; similarly a selected newborn terminal is in `W`
precisely when it is absent from `H`.  Since the inherited and newborn
path counts sum to `K`,

\[
             p_I(W)+t_B(W)=K-e(H).                    \tag{2.4}
\]

Using (1.5), the right side of (2.2) becomes

\[
 R(M-|H|)+C(K-e(H))
       =NP-\bigl(R|H|+Ce(H)\bigr).                    \tag{2.5}
\]

For `H=X\setminus Gamma(U)`, every outer neighbour of `H` lies outside
`U`.  Thus (2.3) gives

\[
 R|H|+Ce(H)\le N|\Gamma(H)|\le N(P-|U|),             \tag{2.6}
\]

which is (2.2) after (2.5).

Conversely, fix an arbitrary `H subseteq X` and set

\[
                  U=O\setminus\Gamma(H),\qquad
                  H'=X\setminus\Gamma(U).             \tag{2.7}
\]

Then `H subseteq H'`.  Every neighbour of a vertex in `H'` lies in
`Gamma(H)`, while `H subseteq H'` gives the reverse boundary inclusion.
Hence

\[
                         \Gamma(H')=\Gamma(H).         \tag{2.8}
\]

Applying (2.2) to `U`, then using (2.5), gives

\[
 R|H'|+Ce(H')\le N|\Gamma(H)|.                       \tag{2.9}
\]

Both terms on the left are monotone under `H subseteq H'`, so (2.3)
follows for `H`.  This proves `(1) iff (2)`.

Finally `R=N-C` gives the identity

\[
 R|H|+Ce(H)
    =N|H|-C\bigl(|H|-e(H)\bigr)
    =N|H|-C\rho(H),                                   \tag{2.10}
\]

so (2.3) is exactly (0.4). \(\square\)

### Corollary 2.2 (sharp reserve profile)

Define

\[
 \mu_s(I,B)=
 \min_{\varnothing\ne H\subsetneq X}
   \left[C\rho_s(H)-N\bigl(|H|-|\Gamma_s(H)|\bigr)\right]. \tag{2.11}
\]

The empty set gives a zero row.  The complete strict outer palettes give
`Gamma(X)=O`; then (1.5) makes the full set a zero row as well.  A fixed
newborn orientation is absorbing on
shore `s` if and only if

\[
                            \mu_s(I,B)\ge0.            \tag{2.12}
\]

Equivalently, every set of ordinary Hall defect

\[
                    d(H)=|H|-|\Gamma_s(H)|>0          \tag{2.13}
\]

must obey the integer lower bound

\[
                    \rho_s(H)\ge
                    \left\lceil {N\over C}d(H)\right\rceil. \tag{2.14}
\]

This is a coordinate-free, dimension-uniform, exactly checkable inductive
condition on the inherited endpoint blocks and the oriented newborn bank.
An exact separator uses Boolean OR variables for `Gamma(H)` and for the
touched inherited blocks.  No relaxation of the pair ORs is sound.

### Corollary 2.3 (conditional orientation-forgetting induction)

Suppose that at every strict DERF step one can choose the newborn path
orientations so that (2.12) holds on both shores.  Then both output shores
are SBE for every inherited orientation.  Therefore no ancestral
orientation bits need be transported: after constructing the undirected
output, choose the newborn orientation, forget all inherited orientations,
and only then choose the next common `Q` and direct SDRs.

This is a conditional induction theorem.  It does not construct such a
newborn orientation, and it does not supply rooted graphic support,
residence, deep shadows, or a compiler.

## 3. A natural local certificate and its exact failure

The reserve inequalities permit nonlocal pooling over an outer family.
The following stronger certificate tries to allocate the capacities one
outer row at a time.

Construct a bipartite resource network.  Every outer vertex has demand
`N`.  The resource side contains

* one capacity-`R` resource `r_v` for each middle vertex `v`;
* one capacity-`C` resource `q_i` for each inherited endpoint block
  `{a_i,b_i}`; and
* one capacity-`C` resource `q_z` for each selected newborn terminal `z`.

An outer row `o` may use `r_v` when `v in Gamma(o)`, may use `q_i` only
when both `a_i,b_i in Gamma(o)`, and may use `q_z` when
`z in Gamma(o)`.

### Proposition 3.1 (row-atomic flow is sufficient)

If this network has a flow meeting every outer demand, then the newborn
orientation is absorbing on that shore.

#### Proof

Fix `U subseteq O` and put `W=Gamma(U)`.  All flow leaving `U` enters base
resources indexed by `W`, inherited resources whose two endpoints are
both in `W`, or newborn resources indexed by `Z_B intersect W`.  Their
total capacity is at most

\[
                   R|W|+C\bigl(p_I(W)+t_B(W)\bigr).   \tag{3.1}
\]

Since the flow sends `N|U|` units from `U`, (2.2) follows.  Apply
Theorem 2.1. \(\square\)

This implication is not reversible.  Replacing the common-neighbour
condition by the union
`Gamma(a_i) union Gamma(b_i)` is unsound: for `H={a_i}` the exact reserve
row charges the endpoint block but its boundary is only `Gamma(a_i)`; a
union-resource could escape through an outer vertex seen only by `b_i`.
Adding `b_i` changes both `|H|` and its boundary and cannot normalize that
row.

### Proposition 3.2 (zero-common obstruction)

If an inherited nontrivial endpoint block satisfies

\[
                  \Gamma(a_i)\cap\Gamma(b_i)=\varnothing, \tag{3.2}
\]

then its `C`-capacity atomic resource is inaccessible.  Since the total
outer demand and total resource capacity are both `NP`, a complete atomic
flow is impossible and its deficit is at least `C`.

The authenticated outputs have the following exact census.  Independent
max-flow replay shows that all remaining accessible resources saturate, so
the displayed lower bounds are equalities.

\[
\begin{array}{c|rr|rr|r}
m&z^{\rm upper}_0&z^{\rm lower}_0&
\text{upper deficit}&\text{lower deficit}&C\\ \hline
5&8&8&1056&1056&132\\
6&25&22&10725&9438&429\\
7&98&86&140140&122980&1430
\end{array}                                           \tag{3.3}
\]

Here `z_0` is the number of inherited endpoint blocks satisfying (3.2)
on the indicated shore.  Thus the row-atomic certificate already fails at
the first robustly absorbing output and becomes farther from feasible in
the next two fixtures.  This is a precise obstruction to that local proof
strategy, not a counterexample to the exact reserve inequalities.

## 4. Exact finite ledger

The output parameters and bank sizes are

\[
\begin{array}{c|rrrrrrr}
m&M&N&P&C&R&|I|&|B|\\ \hline
5&252&210&120&132&78&14&28\\
6&924&792&495&429&363&42&90\\
7&3432&3003&2002&1430&1573&132&297.
\end{array}                                           \tag{4.1}
\]

### 4.1 Literal failure at `n=3 -> 4`

For the stored upper orientation, take the outer family

```text
{0x3f,0x5f,0x9f,0xaf,0xcf,0xb7,0xe7,0xbb,0xdb,
 0xeb,0xf3,0xbd,0xdd,0xf9,0xbe,0xde,0xee,0xf6}.
```

Its middle neighbourhood has order `53`; its complement is

```text
H={0x55,0x5a,0x5c,0x66,0x69,0x6c,0x71,0x72,0x74,
   0x95,0xac,0xb2,0xb4,0xc5,0xe4,0xe8,0xf0}.
```

The outer boundary of `H` is

```text
{0x6f,0x77,0x7b,0x7d,0x7e,0xd7,0xed,0xf5,0xfa,0xfc}.
```

It has the profile (0.6).  Since `(N,C,R)=(56,42,14)`, its exact
complement deficit is `14`, or reserve margin `-14`, proving that this
fixed newborn bank is not absorbing.  This is also the known stored SBE
violation `1008-994=14` in complement form.

### 4.2 Exact regeneration at `n=4 -> 5`

For the stored newborn orientation, all `1,024` effective assignments of
the ten nontrivial inherited path directions pass both shore min-cuts.
The four inherited singleton components multiply the advertised orientation
count by `16` without changing any terminal set.  Therefore the newborn
bank satisfies Theorem 2.1 for every inherited orientation.  The existing
independent audit also verifies the same fact for the two finite conventions
that orient every newborn path toward its numerically smaller, respectively
larger, upper terminal.

### 4.3 Honest status at `n=5 -> 6` and `n=6 -> 7`

The stored complete orientations at output parameters six and seven are
SBE on both shores.  That checks one inherited orientation, not the
universal quantifier in Theorem 2.1.

The exact pseudo-Boolean separator maximizes

\[
 D(H)=R|H|+C\bigl(\kappa_I(H)+|Z_B\cap H|\bigr)
                  -N|\Gamma(H)|.                     \tag{4.2}
\]

Boundary and pair-hit variables are literal ORs.  A positive optimum is a
counterexample; proving optimum zero certifies robust absorption.  The
first `m=5` upper deficit-feasibility run remained `UNKNOWN` after the
bounded audit (`120` seconds, one worker, about `8.3` million branches and
`6.3` million conflicts, about `107` MiB).  Therefore no robust claim is
made for `m=6` or `m=7`; resource/time exhaustion is not UNSAT.

The finite facts currently established are exactly:

\[
\begin{array}{c|c|c}
\text{transition}&\text{fixed-newborn universal status}&
                   \text{row-atomic status}\\ \hline
3\to4&\text{FAIL, margin }-14&\text{not needed}\\
4\to5&\text{PASS, exhaustive}&\text{FAIL }(8,8)\\
5\to6&\text{UNKNOWN}&\text{FAIL }(25,22)\\
6\to7&\text{UNKNOWN}&\text{FAIL }(98,86).
\end{array}                                           \tag{4.3}
\]

## 5. Scope and surviving gate

Theorem 2.1 and the reserve formula (0.5) are dimension-uniform.  They give
the smallest noncircular state presently justified for orientation-
forgetting strict DERF:

\[
 \boxed{\text{the two shore occurrence graphs, inherited endpoint blocks,
 and a newborn terminal choice with }\mu^\pm\ge0.}     \tag{5.1}
\]

This state is strictly weaker than a row-atomic common-neighbour flow and
strictly stronger than SBE for one stored orientation.  The `n=3 -> 4`
witness proves it is not automatic under strict DERF, while the `n=4 -> 5`
certificate proves that a newborn bank can regenerate it completely.

No preservation theorem for all parameters is proved.  In particular:

* the atomic deficits in (3.3) do not refute exact absorption;
* stored SBE at parameters six and seven does not prove robust absorption;
* the theorem does not choose `Q`, direct representatives, rooted graphic
  support, residence, deep shadows, or a compiler; and
* no `nu(k)=B(k)` or all-parameter existence conclusion follows.

The surviving preservation gate is to prove (2.14) from a genuinely
nonlocal newborn dispersion theorem, or to produce an exact positive-
`D(H)` witness in a later authenticated output.

## 6. Audit

The reusable exact complement model is

```text
scratch/audit_threadD_catalan_newborn_terminal_buffer_n5_n7_20260731.py
```

Its SHA-256 is
`5aa407a1390088279bd5e058e23193fe06f67eba1c7f0d61953b29381f6e55d7`.
The bounded `m=5` upper feasibility attempt is retained, with status
`UNKNOWN`, as

```text
scratch/n5_upper.audit.json
  SHA 2444b9ca2bd1079a21a478337f5c96d7c44c7fa208856f7445858733353cd5f1
scratch/n5_upper.resource.log
  SHA 6af7a3f00dddd96cd2b91b4a89aad4fd3a3c06afac6c6e30603ec3d4e3967a61
```

The solver-free status consumer independently reconstructs the literal
`n=3 -> 4` witness, all six atomic flows, their zero-common blocks, and the
scope of every exact/unknown result:

```text
scratch/audit_threadD_catalan_newborn_buffer_finite_status_20260731.py
  SHA 647fd9a19fe5026caf46858a528619fc522c42776973879c3780807a4b58185f
scratch/threadD_catalan_newborn_buffer_finite_status_20260731.audit.json
  SHA 2d48cc7b987a5922cf06929fab56fb72e3ca0f3aa2378a5c7607d4dcd4df33ee
  payload 2fd60e074fa6a52edaadead16e4f48bffdc78188cfafe8a72731f9181f71db98
```

The `n=4 -> 5` universal-orientation replay and its clean-room audit remain

```text
scratch/audit_catalan_sbe_ancestral_orientation_forgetting_20260731.py
scratch/catalan_sbe_ancestral_orientation_forgetting_20260731.audit.json
scratch/independent_audit_catalan_sbe_n4_face_in_n5_20260731.py
scratch/catalan_sbe_n4_face_in_n5_20260731.independent.audit.json
```

The authenticated structural source is

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
```

Any absent or bounded exact solve is reported as `UNKNOWN`, never as a
terminal-buffer proof or obstruction.
