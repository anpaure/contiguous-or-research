# Audit: facet-absorber owner packing and the joint interval-target gate

Date: 2026-08-02  
Status: independent proof audit PASS, with explicit scope corrections for
the post-labeling/LLL claims.  No whole-layer mixed decomposition, global
target packing, or additive-constant conclusion is proved here.

## 1. Authenticated source

```text
MATH_THEOREM_FACET_ABSORBER_MIXED_STAR_DECOMPOSITION_AND_TARGET_COLLISION_GATE_20260802.md
  submitted SHA-256 532e405e26c24054c305396cd64b3eb2e5c97fdfb0161b8f27502c3963833f27
  corrected SHA-256 917cd7078bd9fa942c1aa51122c485e7a417fb4f6507fe83dda289ecd6c124f1
```

The submitted hash agrees with the authoritative handoff.  The corrected
file adds only the independently required hypotheses `k>=r+1` for the star
reductions, `d>=2,c>=1` for the literal primitive module, and the exact
eventual inequality `c-1>d` where both Ferrers corrections are discarded.
The canonical sufficiently-large conclusion is unchanged.

Put

\[
 c=r-d-1,\qquad q=d+2,\qquad W={k\choose r}.
\]

## 2. Exact star reduction and divisibility

A facet block has the form

\[
 B(Z,V)=\{Z-\{v\}:v\in V\},
 \qquad |Z|=r+1,\quad |V|=q.
\]

Complementing its owners gives the `q` edges

\[
                  K+\{v\}\quad(v\in V),qquad K=[k]-Z,
\]

of a star in the complete `(k-r)`-uniform hypergraph.  Hence a perfect
facet-block owner matching is equivalent to orienting every `(k-r)`-set to
one of its facets so every orientation fibre has size divisible by `q`.
This equivalence is exact.

For the partial simplex `F_(r,q)`, an `i`-set `S` has degree

\[
                         q-|S\cap V|.
\]

At `i=0` the gcd is `q`.  For every `1<=i<r`, two consecutive positive
degrees occur, so the gcd is one.  Thus the complete design-divisibility
list reduces to

\[
                             q\mid W.                    \tag{2.1}
\]

This is a necessary divisibility calculation, not a growing-pattern design
existence theorem.

## 3. The consecutive-size module

In the intended `d>=2` regime, the explicit common-core construction with
`q+1` source states has owners

\[
 K\cup\bigl(U-\{u_i,u_{i+1}\}\bigr),
 qquad i\in\mathbb Z/(q+1),quad |U|=q+1.
\]

They are distinct rank-`r` owners and carry a literal owner-simple primitive
cycle.  One high state is the primitive partner and the remaining
`q-1=d+1` high states are buffers.  Its marked target deck is internally
injective.

Since `gcd(q,q+1)=1`, for `W>=q^2-1`, setting

\[
 B=W\bmod q,qquad A={W-(q+1)B\over q}
\]

gives `A,B>=0`, `B<q`, and

\[
                         W=Aq+B(q+1).                   \tag{3.1}
\]

Therefore the two module sizes remove the scalar owner-count congruence.
Equation (3.1) does **not** select disjoint owner blocks.  The mixed
whole-layer star-decomposition statement remains an external input.

## 4. Maximal-matching leave bound

Let `R` be the owner leave of a maximal matching in the facet-block
hypergraph.  Every `(r+1)`-set contains at most `q-1` members of `R`, since
any `q` of its facets would be a new disjoint block.  Double-counting
containments gives

\[
 (k-r)|R|\le(q-1){k\choose r+1}
             =(q-1){k-r\over r+1}W,
\]

and hence

\[
                       |R|\le {q-1\over r+1}W.          \tag{4.1}
\]

Consequently the hypergraph contains `t` disjoint blocks whenever

\[
                 tq\le W-{q-1\over r+1}W.              \tag{4.2}
\]

This is an exact finite owner-packing statement.

## 5. Canonical primitive capacity

The canonical aggregate ledger bounds the number `t` of adjacent-buffer
primitives by `A_(d+1)`.  For large `k`, the Ferrers correction vanishes at
the two relevant ranks and

\[
 A_{d+1}={k\choose c}-{k\choose c-1}.
\]

Write `h=d+1`.  The corrected triangular definition gives

\[
 {d\over\sqrt r}\longrightarrow {\sqrt\pi\over2},
\]

while the central-binomial product gives

\[
 {{k\choose c}\over W}longrightarrow e^{-\pi/4}.
\]

Moreover,

\[
 {A_{d+1}\over {k\choose c}}=
 \begin{cases}
 (2d+3)/(r+d+2),&k=2r,\\
 (2d+2)/(r+d+1),&k=2r-1.
 \end{cases}
\]

Therefore

\[
 {qA_{d+1}\over W}longrightarrow
              {\pi\over2}e^{-\pi/4}=0.716\ldots<0.717. \tag{5.1}
\]

The right side of (4.2), divided by `W`, tends to one.  Hence for every
sufficiently large canonical `k`, all `t<=A_(d+1)` primitives can be assigned
pairwise owner-disjoint length-`q` facet absorbers.  This conclusion is
owner-only and assumes the required short-buffer occurrences have been
reserved.  It does not select named targets or pack the other rotor types.

## 6. A genuine post-hoc labeling obstruction

For `q>=5`, fix a common rank-`(r-1)` target

\[
                         P=C\mathbin{\dot\cup}I,
                         \qquad |I|=q-2,
\]

and construct `m` owner-disjoint blocks by adjoining a different private
tag pair to each block.  In any cyclic order, at most four cycle edges meet
the two private tags.  Each block therefore emits at least `q-4` rank-
`(c+2)` targets from the common pool

\[
                         \{C\cup e:e\in {I\choose2}\}.
\]

Target simplicity forces

\[
                         m(q-4)\le {q-2\choose2}.        \tag{6.1}
\]

Above this threshold no cyclic orders and no choices of the low parameters
`b,w,h` label this explicit family target-simply.  The maximal family has
`m=floor((k-r+1)/2)=Theta(k)`, while the threshold in (6.1) is `Theta(q)`.
For canonical `q=Theta(sqrt(k))` it is eventually unlabelable.

This refutes a universal strategy which first chooses an arbitrary
owner-disjoint facet-block matching and then labels it.  It does not show
that every owner matching fails, rule out co-designed block/order selection,
or construct an unlabelable perfect whole-layer owner factor.

## 7. Exact scope of the LLL barrier

For a selected `t`-block matching, let `mu(P)` count blocks whose potential
menu contains target `P`, and let `R` be the maximum blockwise potential-menu
conflict load.  At rank `c+2`, Cauchy--Schwarz gives

\[
 R\ge {t {q\choose2}^2\over {k\choose c+2}}-{q\choose2}. \tag{7.1}
\]

If `eta=qt/W` is bounded below by a positive constant along a canonical
sequence, then

\[
 R\ge\left({\eta e^{\pi/4}\over4}+o(1)\right)q^3.      \tag{7.2}
\]

Thus the displayed symmetric independent-label criterion

\[
                         4e(2R-1)\le(q-1)^2             \tag{7.3}
\]

fails by a factor of order `q` at positive density, for every owner matching.
A greedy rule forbidding every potential-menu overlap reaches only
`O(W/q^2)`, rather than the required `Theta(W/q)` scale.

Equations (7.1)--(7.3) do not rule out every asymmetric, lopsided or
correlated local-lemma argument.  The unconditional no-labeling statement is
the explicit common-core family in Section 6.

## 8. Exact remaining primitive row

For the actual fixed primitive count, residual target allocation and
protected/preused bank, the missing selection must jointly choose

1. pairwise owner-disjoint facet blocks;
2. one cyclic order on each tag set; and
3. the low parameters `b,w,h`,

so all emitted cyclic interval targets at every `2<=j<=q-2`, and both low
targets, are globally injective, available, and avoid the protected bank.
Scalar capacities alone are not proved sufficient for every allocation.

The proof-safe implication is conditional: if such a jointly spread family
exists, the entire primitive inventory has an owner- and target-simple
literal lift with no added occurrences.  This is only the primitive row.
The whole-layer mixed-star factor, other rotor packages, component fusion,
residence, upper decks, protected interfaces and compiler remain separate.

## 9. Verdict

The source theorem is valid with the scopes above.  It unconditionally
closes owner-disjoint packing for the canonical primitive subinventory at
large `k` and removes the scalar congruence by a second local module size.
It also proves that owner selection and target labeling cannot be separated.
The live constructive gate is a correlated facet-block/interval selection
for the actual residual target bank.  No `O(1)` bound follows.
