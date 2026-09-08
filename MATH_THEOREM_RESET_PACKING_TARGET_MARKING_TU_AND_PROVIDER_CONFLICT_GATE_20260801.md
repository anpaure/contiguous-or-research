# Optional high-target marks over a reset packing: the SDR is TU and coverage is the only obstruction

Date: 2026-08-01

Status: unconditional exact formulation, fractional and integral Hall
theorems, collision identities, and a protected-port criterion.  The result
removes target **assignment** as an extra integrality gate after a cycle
packing is fixed.  It does not construct a root/owner packing which covers
every target, nor a target-transparent support-three connector system.

## 0. Outcome

Fix any root/owner-disjoint packing `P` of bidirectional reset blocks.  A
block offers one depth-labelled occurrence token for each of its `N` flags
at every depth `1,...,d-1`.  A token has exactly one set value.  The same
block may mark arbitrarily many of its different suffix cells; there is no
one-mark-per-block capacity.

Therefore different target values never compete for one occurrence token.
For a fixed packing:

\[
 \boxed{
 \text{an exact target marking exists}
 \iff
 \text{every target is offered at least once}.}               \tag{0.1}
\]

The target-to-occurrence matching matrix is a disjoint union of simplex
rows and is totally unimodular.  Its Hall inequalities reduce to singleton
coverage.  No Rado or transversal-matroid theorem beyond this is needed.

The uniform fractional reset-block factor proves fractional coverage:
every depth-`j` target has load

\[
                         \rho_j={\binom{2m+1}m
                                  \over\binom{2m+1}{m-j}}\ge1. \tag{0.2}
\]

Nested block codegrees show that provider correlations in the **complete
block family** are small, but this does not imply that an integral
root/owner packing covers every target.  At the conjectural depth, the
loads (0.2) are only constant order, not logarithmic.

For a selected packing with `b` blocks, define target multiplicity
`mu_j(T)`.  The exact hole/collision identity is

\[
 h_j=\binom{2m+1}{m-j}-bN
       +\sum_T(\mu_j(T)-1)_+.                         \tag{0.3}
\]

Thus complete coverage requires the collision excess to attain its minimum
possible value `bN-W_j`; every extra duplicate creates one hole.

Connector ports introduce no new global matching theorem either.  For a
fixed forbidden occurrence set `D`, marking survives exactly when every
target has one provider outside `D`.  If `q` occurrence tokens are
invalidated, at most `q` formerly covered targets can be lost.  Exact
coexistence with many connectors therefore needs target-transparent trades
or an explicit provider-avoidance conflict system.

## 1. Occurrence-labelled target graph

Let `P` be a selected collection of pairwise root/owner-disjoint reset
blocks.  For a block `B`, phase `epsilon` (forward or reverse), cyclic
position `a`, and depth `j`, let

\[
                         \omega=(B,\epsilon,a,j)                \tag{1.1}
\]

denote the physical suffix occurrence.  Its value is a unique set

\[
                         v(\omega)\in\binom{[k]}{m-j}.          \tag{1.2}
\]

The two orientations of a bidirectional block have the same value multiset
at every depth.  Fix either orientation, or identify the occurrences under
the phase bijection.

For a named target `T`, put

\[
 \Omega_j(T)=\{\omega:\omega\text{ belongs to a selected block},
                         \ v(\omega)=T\},
 \qquad
 \mu_j(T)=|\Omega_j(T)|.                              \tag{1.3}
\]

Make a bipartite graph from targets to occurrence tokens, joining `T` to
`omega` exactly when `v(omega)=T`.

### Lemma 1.1 (provider sets are disjoint)

For distinct targets `T != T'`,

\[
                         \Omega_j(T)\cap\Omega_j(T')=\varnothing. \tag{1.4}
\]

#### Proof

One occurrence token has the one literal set value (1.2). \(\square\)

This trivial-looking fact is load-bearing.  A target occurrence is not a
generic cell capable of serving several lower masks; that later common-cap
phenomenon is outside the all-high marked-selector row considered here.

## 2. Integral marking is automatic from coverage

Introduce binary variables `y_omega` and impose

\[
 \sum_{\omega\in\Omega_j(T)}y_\omega=1
 \qquad\text{for every target }T.                    \tag{2.1}
\]

There is no cross-target capacity row because tokens in (1.4) are disjoint.

### Theorem 2.1 (marking projection theorem)

For a fixed packing, the following are equivalent at every depth `j`.

1. Every target can be marked exactly once.
2. `mu_j(T)>=1` for every target `T`.
3. The target--occurrence graph has a matching saturating every target.
4. The linear relaxation

   \[
   y\ge0,\qquad
   \sum_{\omega\in\Omega_j(T)}y_\omega=1             \tag{2.2}
   \]

   is feasible.

Moreover the polytope (2.2) is integral.

#### Proof

Necessity of item 2 is immediate.  If every provider set is nonempty,
choose one token independently from each `Omega_j(T)`.  Lemma 1.1 makes all
choices distinct, giving items 1 and 3.

After permuting columns by target value, the matrix of (2.2) has exactly one
`1` in every column and disjoint row supports.  It is a direct sum of
one-row simplex matrices and is totally unimodular.  Feasibility is exactly
nonemptiness of every row support. \(\square\)

### Corollary 2.2 (Hall collapses to singletons)

For every target family `X`,

\[
 |N(X)|=\sum_{T\in X}\mu_j(T).                       \tag{2.3}
\]

Hence all Hall inequalities follow from the singleton inequalities
`mu_j(T)>=1`.

This is the exact “Rado theorem” on this face: the transversal matroid is a
direct sum of free rank-one choices.  There is no hidden collective Hall
cut after coverage is known.

## 3. Joint block and mark formulation

Before a packing is fixed, use binary block variables `x_B` and occurrence
mark variables `y_(B,a,j)`.  The exact rows are

\[
\begin{aligned}
 \sum_{B\ni Q}x_B&\le1 &&\text{(root capacity)},\\
 \sum_{B\ni O}x_B&\le1 &&\text{(owner capacity)},\\
 y_{B,a,j}&\le x_B,\\
 \sum_{(B,a):v(B,a,j)=T}y_{B,a,j}&=1
                         &&\text{(target mark)}.       \tag{3.1}
\end{aligned}
\]

### Theorem 3.1 (exact elimination of mark variables)

For binary `x`, the `y`-system in (3.1) is feasible if and only if

\[
                         \sum_{B:T\in B_j}x_B\ge1
                         \qquad(T\in\mathcal T_j),    \tag{3.2}
\]

where `T in B_j` means that block `B` offers `T` at depth `j`.

#### Proof

After `x` is fixed, delete occurrences belonging to unselected blocks and
apply Theorem 2.1. \(\square\)

Thus the exact cycle-level object is the mixed system

\[
                         \text{root/owner packing}
                         +\text{target set cover}.              \tag{3.3}
\]


The mark variables add no integrality gap of their own.  All correlation is
already present in selecting blocks satisfying the packing and cover rows.

## 4. Fractional Hall from the block ledger

Let `D` be the reset-block degree at every root and owner, and assign every
block weight

\[
                         x_B={1\over D}.                       \tag{4.1}
\]

The cycle-first block theorem gives target incidence degree

\[
                         D_j=D{W\over W_j}.                    \tag{4.2}
\]

### Theorem 4.1 (fractional occurrence Hall)

Give every selected occurrence in block `B` capacity `x_B`.  Then for every
target family `X` at depth `j`,

\[
 \sum_{\omega\in N(X)}x_{B(\omega)}
 =\rho_j|X|\ge|X|,                                    \tag{4.3}
\]

where `rho_j=W/W_j`.  Consequently the fractional target-mark system is
feasible simultaneously with exact fractional root/owner packing.

#### Proof

Every target has `D_j` incident block occurrences, each of capacity `1/D`,
so its total capacity is `rho_j`.  Provider supports of distinct targets are
disjoint at occurrence level, and summing gives (4.3).  Assign every target
`1/rho_j` of its incident capacity. \(\square\)

The exact nested block codegrees

\[
 {\lambda(T_i,T_j)\over D_i}
 ={j-i+1\over\binom{m-i}{j-i}}                       \tag{4.4}
\]

show that two nested target provider families have relative overlap
`O(1/m)` on adjacent central layers.  This is useful input for a prospective
packing theorem.  It is not needed for fractional Hall itself, because
occurrence supports split by target value.

## 5. Collision identity and the actual integral target gate

Let `b=|P|`.  At every depth the packing has exactly `bN` occurrence tokens.
Define

\[
 E_j=\sum_T(\mu_j(T)-1)_+,
 \qquad
 h_j=|\{T:\mu_j(T)=0\}|.                             \tag{5.1}
\]

### Theorem 5.1 (holes equal excess collisions beyond slack)

\[
                         h_j=W_j-bN+E_j.                       \tag{5.2}
\]

In particular, if `bN>=W_j`, complete coverage is equivalent to

\[
                         E_j=bN-W_j.                           \tag{5.3}
\]

#### Proof

The number of covered targets is

\[
 |\{T:\mu_j(T)>0\}|=\sum_T\mu_j(T)-E_j=bN-E_j.      \tag{5.4}
\]

Subtract from `W_j`. \(\square\)

Equation (5.3) is sharp: `bN-W_j` duplicates are forced by the pigeonhole
principle, and every duplicate beyond that minimum creates one target hole.

For the `k=17,d=3` quotient ledger, **if** a pure reset packing reaches the
scalar maximum number of disjoint blocks, then

\[
                         b=\lfloor1430/8\rfloor=178,
 \qquad bN=1424.                                      \tag{5.5}
\]

Therefore complete target coverage requires exact collision excess

\[
 \begin{array}{c|c|c}
 \text{target rank}&W_j& E_j\text{ required}\\ \hline
 7&1144&280\\
 6&728&696.
 \end{array}                                                   \tag{5.6}
\]

The average multiplicities are only `1424/1144 approximately 1.245` and
`1424/728 approximately 1.956`.  Fractional load above one is therefore not
an automatic integral coverage theorem; the block packing must control
collisions almost optimally.

## 6. Protected connector ports

Let `D_j` now denote a fixed set of occurrence tokens invalidated by opening,
connector ports, or exterior-guard commitments.  Define the safe providers

\[
                         \Omega_j^{\rm safe}(T)
                         =\Omega_j(T)-D_j.             \tag{6.1}
\]

### Theorem 6.1 (protected marking criterion)

An exact marking avoiding every forbidden token exists if and only if

\[
                         \Omega_j^{\rm safe}(T)\ne\varnothing
                         \qquad\text{for every }T.     \tag{6.2}
\]

If the original packing covered every target, the number of targets made
unmarkable is at most

\[
                         |D_j|.                                \tag{6.3}
\]

#### Proof

Apply Theorem 2.1 to the safe occurrence graph.  For (6.3), assign to every
new hole its nonempty original provider set, now contained in `D_j`.
Provider sets of distinct targets are disjoint, so choose a distinct
forbidden token from each. \(\square\)

### Corollary 6.2 (bounded-port sidecar)

If a bounded connector construction invalidates at most `C` target
occurrences in total, it creates at most `C` target holes.  Those holes may
be carried as a bounded sidecar or appended terminally.

For an exact zero-sidecar theorem, choose one safe occurrence per target
first and restrict every later connector to avoid those protected tokens,
or choose connectors first and verify the singleton conditions (6.2).

When connector choices are still variable, the obstruction is not Hall.
It is the monotone conflict family

\[
 \text{bad}_T:
 \quad\text{the chosen connectors invalidate every token in }
                   \Omega_j(T).                       \tag{6.4}
\]

A connector-selection theorem must avoid all events (6.4).  If a target has
only one provider in the packing, that occurrence is a mandatory protected
ticket.

### Theorem 6.3 (conditioned packing--port projection)

Fix a connector/port state `p`.  For every block `B`, let
`A_p(B,j)` be the occurrences at depth `j` which remain legal under `p`.
For binary packing variables `x_B`, an exact target marking avoiding the
ports exists if and only if

\[
 \sum_B x_B\,
  \mathbf 1\{\exists\omega\in A_p(B,j):v(\omega)=T\}\ge1
 \qquad\text{for every }T.                            \tag{6.5}
\]

#### Proof

After `x` and `p` are fixed, the legal provider sets for distinct targets
remain disjoint.  Apply Theorem 2.1. \(\square\)

Thus the protected Rado problem also degenerates to singleton cover rows
**conditioned on the ports**.  If `p` is selected jointly with the packing,
the new difficulty is exactly avoiding the all-provider conflicts (6.4);
there is still no separate capacity-one target SDR.

## 7. Why a generic cycle nibble does not finish target coverage

The fractional target loads `rho_j` are constant order when
`d=Theta(sqrt(m))`.  Indeed

\[
 \rho_j=\prod_{s=0}^{j-1}{m+2+s\over m-s}.           \tag{7.1}
\]

For `j=Theta(sqrt(m))`, its logarithm is `Theta(j^2/m)=Theta(1)`.

Thus the exact block ledger supplies constant average provider multiplicity,
not the growing redundancy normally used to obtain simultaneous coverage of
exponentially many targets by an unconditioned random choice.  Small nested
codegrees (4.4) control pair correlations in the complete family, but they
do not force the collision equality (5.3) in an integral root/owner packing.

This is a quantitative warning, not a probabilistic no-go: a highly
correlated design may attain (5.3), just as the exact finite selectors do.
It shows why a black-box almost-perfect matching/nibble theorem on roots and
owners is insufficient.

## 8. Exact remaining theorem

The target row after cycle selection is now completely localized:

> **Collision-optimal reset packing.**  Choose a root/owner-disjoint reset
> packing such that, at every high depth, its offered target multiplicities
> satisfy `E_j=bN-W_j+O(1)`, and protect one provider of every covered target
> from the support-`>=3` connector system.  For a mixed reset/decorated-hex
> packing, replace `bN` by its actual number `M_j` of offered depth-`j`
> occurrences, so the condition is `E_j=M_j-W_j+O(1)`.

When the `O(1)` term is zero, Theorems 2.1 and 6.1 mark every target exactly.
When it is bounded, the unmatched targets form a bounded literal sidecar.

No separate integral SDR theorem remains.  The open construction problem is
collision control in the cycle packing plus provider-transparent topology.
