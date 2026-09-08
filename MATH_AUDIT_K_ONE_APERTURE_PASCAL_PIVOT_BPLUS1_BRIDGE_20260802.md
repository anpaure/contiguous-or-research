# Audit of the one-aperture Pascal/pivot `B+1` bridge

**Date:** 2026-08-02  
**Verdict:** the asymmetric pivot, monotone transport, and persistent Pascal
port are exact.  The claimed literal repayment by the opposite fan is not
correct for the ordinary lower compiler or for the native full-width `q1`
row.  The opposite fan promotes an already existing shorter occurrence of
one internal colour.  The aperture leaves a different internal colour
unrealized.  A one-credit regenerative theorem survives only with one
explicit exterior discharge socket, and only when the aperture edge is also
the unique open boundary edge; otherwise two rank-`(r-1)` boundary
obligations remain.  Upper shadows, residence, and the global common-cap
compiler are not audited as consequences.

This note audits Sections 4--7 of
`MATH_THEOREM_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md`.

## 1. The literal pivot formulas pass

Fix `d>=2`, `r>=d+2`, a set `X` of size `r-d-1`, and pairwise-disjoint
singleton coordinates

\[
 \alpha,\ell,\mu,\lambda_1,\ldots,\lambda_{d-1},
 \rho_1,\ldots,\rho_{d-1}.
\]

Use the post-insertion source

\[
\begin{array}{c|c}
p&A_p\\ \hline
-d&\{\ell\}\\
-i&\{\lambda_i\}\quad(2\le i\le d-1)\\
-1&X\cup\{\alpha,\lambda_1\}\\
0&X\\
i&\{\rho_i\}\quad(1\le i\le d-1)\\
d&\{\alpha,\mu\}.
\end{array}                                                \tag{1.1}
\]

The `d+1` length-`(d+1)` windows through zero are exactly

\[
\begin{aligned}
 M_0&=X\cup\{\alpha,\ell\}\cup\lambda[1,d-1],\\
 M_j&=X\cup\{\alpha\}\cup\lambda[1,d-j]
                         \cup\rho[1,j] \quad(1\le j<d),\\
 M_d&=X\cup\{\alpha,\mu\}\cup\rho[1,d-1].
\end{aligned}                                             \tag{1.2}
\]

They are distinct rank-`r` sets and form a Johnson path.  Before inserting
`A_0`, the crossing length-`(d+1)` windows are

\[
                         M_{j-1}\cup M_j\quad(1\le j\le d),
                                                               \tag{1.3}
\]

of rank `r+1`.  Moreover `X subseteq A_(-1) union A_1`, so every old
interval value transports literally.  These parts of the proposed theorem
are correct.

The two longest fan values are also exactly

\[
 \begin{aligned}
 N&=\bigcup_{p=-(d-1)}^0 A_p
      =X\cup\{\alpha\}\cup\lambda[1,d-1],\\
 Q_*&=\bigcup_{p=0}^{d-1} A_p
      =X\cup\rho[1,d-1].
 \end{aligned}                                             \tag{1.4}
\]

Thus `|N|=r-1`, `|Q_*|=r-2`, and the ordered right fan is the desired
aperture predecessor `(X,{rho_1},...,{rho_(d-1)})`.

## 2. The missing native colour is not `N`

For `1<=j<=d`, let `H_j` be the union of the `d` source letters shared by
the consecutive owner windows `M_(j-1),M_j`.  Directly from (1.1),

\[
\begin{aligned}
 H_1&=N=M_0\cap M_1,\\
 H_j&=X\cup\{\alpha\}\cup\lambda[1,d-j]
                    \cup\rho[1,j-1]
       =M_{j-1}\cap M_j \quad(2\le j<d),\\
 H_d&=Q_*.
\end{aligned}                                             \tag{2.1}
\]

But the last owner intersection is

\[
 J:=M_{d-1}\cap M_d
    =X\cup\{\alpha\}\cup\rho[1,d-1]
    =Q_*\cup\{\alpha\}.                                 \tag{2.2}
\]

Therefore the local full-width head row has `d-1` correct central colours
and one deficient aperture `Q_*`; its missing central colour is `J`, not
`N`.  The value `N` is already the correct first internal colour.

This is not merely a failure at the designated shared address.

### Proposition 2.1 (no local occurrence of `J`)

No interval of the local source (1.1) has union `J`.

#### Proof

The only source letters containing `alpha` are

\[
 A_{-1}=X\cup\{\alpha,\lambda_1\},
 \qquad A_d=\{\alpha,\mu\}.
\]

An interval containing the first also contains the unwanted coordinate
`lambda_1`; an interval containing the second also contains the unwanted
coordinate `mu`.  Since neither belongs to `J`, no interval can equal
`J`. \(\square\)

Thus a full literal lower row needs an exterior occurrence of `J` or a
different local source.  The left fan `N` cannot supply it.

## 3. `N` is promoted, not newly covered

Before insertion, the one-sided old interval

\[
                         [-(d-1),-1]                    \tag{3.1}
\]

already has union `N`.  Its length is `d-1`, so it is already an admissible
ordinary lower-compiler cell.  After insertion, the new full fan
`[-(d-1),0]` is a second occurrence of the same set value, now of exact
width `d`.

Consequently the insertion has two different interpretations.

1. **Exact-width head interpretation.**  It genuinely promotes `N` to a
   full predecessor-head occurrence.  This can repair a head-table width
   requirement.
2. **Ordinary compiler interpretation.**  It does not add the target `N`
   to the interval-OR deck: `N` was already present in (3.1).  In
   particular, any old matching which omitted `N` could already be extended
   to `N` using (3.1), provided that cell was not artificially excluded by
   an address guard.

Therefore the matching construction in the draft's Theorem 4.1 is a valid
matching identity for its deliberately restricted target bank, but it is
not evidence of a new ordinary lower-compiler credit.

## 4. Exact matching release ledger

The `d-1` old crossing width-`d` cells expelled from the short band have
values

\[
                         M_1,\ldots,M_{d-1},             \tag{4.1}
\]

in reverse positional order.  They all have rank `r`.  Hence a strict-lower
reference matching uses none of them, and every selected old lower edge
transports unless it is deliberately replaced by a fan occurrence.

Let `U` be the set of already-covered logical targets whose new fan cells
are selected.  The exact replacement is

\[
 \Phi\bigl(M_{\rm old}-M_{\rm old}(U)\bigr)
       \ \dot\cup\
 \{S\longmapsto f_S:S\in U\},                           \tag{4.2}
\]

where `Phi` is monotone transport and the `f_S` are distinct fan cells.
Thus:

* release the old `Q_*` edge exactly when the new right full fan is chosen
  as the compiler representative of `Q_*`;
* release the old `N` edge exactly when `N` already had a selected
  representative and the new left full fan replaces it;
* release one old edge for every other already-covered fan target chosen;
  and
* release nothing for a genuinely previously unmatched logical target.

Repeated equal fan values are one logical target and never give multiple
matching units.  The other `2d-3` fan addresses may simply remain unused.

If a reference matching is artificially defined on a bank `T` containing
`Q_*` but omitting `N`, then deleting the old `Q_*` edge and adding both
full-fan edges yields a matching on `T union {N}` of size `|T|+1`.  But the
pre-insertion matching already has the extension

\[
                    N\longmapsto [-(d-1),-1].           \tag{4.3}
\]

So (4.2) proves relocation and exact-width promotion, not a physical
one-unit reduction of the unrestricted compiler deficiency.

## 5. Local common-`Q` scope

The explicit word (1.1) is a simultaneous witness for:

* all transported old interval equalities;
* the owner windows (1.2);
* the full-fan occurrences (1.4); and
* any selected fan-target rows whose values are their literal unions.

It remains a common-`Q` witness after caps are imposed exactly when every
displayed source letter lies in its final source envelope and every
protected row through that position retains its required coordinates.  In
the maximal-word formulation, for every source position `p`,

\[
 K_p=P_p\cap\bigcap_{I\ni p}T_I\ne\varnothing,
 \qquad
 T_I=E_I\cup\bigcup_{p\in I}K_p,                       \tag{5.1}
\]

where `E_I` is the frozen exterior contribution.  Exhibiting (1.1) inside
these caps is a sufficient local certificate.  Separate marginal
incidences are not.

Nothing in this local certificate proves that a complete ambient compiler
matching uses the same cap state.  In particular, an exterior occurrence
of `J` must be included in (5.1) before claiming q1 completion.

## 6. Suspension carries one debt; it does not discharge it

Under fixed-depth rank suspension, adding a fresh coordinate `z` to `X`
changes

\[
 Q_*\mapsto Q_*\cup\{z\},
 \qquad J\mapsto J\cup\{z\}.
\]

Under `(r,d)->(r+1,d+1)` depth suspension, the new terminal `rho`
coordinate is added to both values.  In either case

\[
                         J=Q_*\cup\{\alpha\}             \tag{6.1}
\]

and the defect remains exactly one.  The same protected aperture occurrence
can therefore be propagated through arbitrarily many same-parity nodes
without creating one new debt per node.  This proves a regenerative
**one-debt state**.

It does not prove that the one-cell insertion paid the debt.  A terminal
construction must still realize the single carried value `J` once in an
ambient cell, or change the opening as in the next section.

## 7. Exact Hamilton-path boundary count

A spanning alternating Middle-Levels Hamilton path on `W` owners has
`W-1` internal owner transitions.  Their intersection colours account for
`W-1` rank-`(r-1)` masks; the remaining mask `E` is the lower-shore endpoint
colour and needs a boundary/short-cell occurrence.

If all edges of the local owner segment

\[
                         M_0,M_1,\ldots,M_d              \tag{7.1}
\]

remain internal to that path, then `J` is one of those internal intersection
colours but is not realized by the local source.  The ordinary path endpoint
colour `E` is not an internal intersection.  Hence

\[
                         J\ne E,                         \tag{7.2}
\]

and there are two distinct q1 obligations, not one.

There is exactly one way for the aperture to represent the unique carried
boundary debt: the transition `M_(d-1)M_d` must itself be the opened path
edge.  Then its colour `J` may be chosen as the endpoint colour `E`, and one
exterior occurrence of `J` discharges both roles.  This requires a literal
rethread which retains `M_d` elsewhere in the spanning path and preserves
the exterior source interfaces; merely declaring the edge open does not
construct that rethread.

The left fan `N=M_0\cap M_1` is an internal edge colour and cannot be this
endpoint colour while both `M_0,M_1` remain adjacent.

## 8. Corrected conditional bridge

The local construction proves a conditional additive-one bridge only under
the following strengthened global hypotheses.

1. A fixed perfect incidence class `M^(0)` and a near-perfect matching `Q`
   of size `W-1` give an upper-surjective alternating Hamilton path; after
   contracting `M^(0)`, the links of `Q` are graphic-independent.
2. The protected Pascal port and owner block (1.1)--(1.4) embed in that
   path, and the aperture transition is the designated open edge.
3. One ambient, address-distinct, cap-compatible cell realizes
   `J=Q_*+alpha`, thereby supplying the unique endpoint colour.  It is an
   existing `B+1` address, not an additional appended letter.
4. The pre-insertion chronology has the required rank-`(r+1)` crossing
   block and one controlled boundary surplus; the post-insertion selected
   owner cells form one consecutive path.
5. Every transported lower edge, the exterior `J` edge, and all protected
   port rows coexist in one global common-cap state.

Under these hypotheses the aperture debt is paid once, and Section 6 shows
that it remains one under same-parity suspension rather than accumulating
with recursion depth.  Without item 2, one needs distinct exterior cells
for `J` and the Hamilton-path endpoint colour `E`; without item 3, the debt
is merely carried.

This is a conditional `B+1`/`B+O(1)` interface, not an unconditional source
construction.

## 9. Gate ledger

The formulas unconditionally close:

1. the local nonflat-to-flat pivot chronology;
2. one simple rank-`r` Johnson owner segment;
3. all-width transport of old interval values;
4. the literal right-hand aperture predecessor and its Pascal cap
   rectangle; and
5. exact-width promotion of the left internal colour `N`.

They do **not** close:

1. the missing native colour `J`;
2. the Hamilton-path endpoint colour unless it is identified with `J` by
   an actual opening/rethread;
3. any positive reduction of the unrestricted ordinary lower-compiler
   deficiency;
4. global common-cap matching;
5. arbitrary upper-shadow completion; or
6. ambient residence across the clipped ends of the local block.

The sharp reusable conclusion is therefore “one persistent aperture debt
plus one explicit terminal discharge,” not “the opposite fan pays the
aperture automatically.”

## 10. Replay of the corrected exterior discharge port

The corrected theorem does not claim that the opposite fan realizes `J`.
It supplies `J` with the ordinary port of the second child.  Fix
`x_0 in X`, put `R={rho_1,...,rho_(d-1)}`, and choose a fresh `nu`.  Take

\[
 c_*=X,\qquad c_1=X\cup\{\alpha\},
\]

and closing roles with

\[
\begin{aligned}
 D_0&=(X-\{x_0\})\cup\{\ell,\alpha\},&
 T_0&=X\cup R\cup\{\ell,\alpha\},\\
 D_1&=(X-\{x_0\})\cup\{\alpha,\nu\},&
 T_1&=X\cup R\cup\{\alpha,\nu\}.
\end{aligned}
\tag{10.1}
\]

Both lower cap endpoints are `{x_0}`.  The crossed tests are exactly

\[
                    c_1\subseteq T_0,\qquad c_*\subseteq T_1.
\tag{10.2}
\]

The ordinary predecessor support is

\[
                         R\cup c_1=Q_*\cup\{\alpha\}=J.
\tag{10.3}
\]

Thus the second child is a literal exterior discharge occurrence, and the
rectangle switch retains `p_*` as claimed.  It does not contradict
Proposition 2.1: the token `(c_1,w)` is protected host data and is not an
interval of the pivot block.  The fresh `nu`, the missing `x_0` signatures
in the two closing heads, and the disjoint lambda/rho banks make all
displayed owners and actual head supports distinct.

The combined local coordinate demand is `r+d+1`, at most `2r-1` exactly
when `r>=d+2`.  This independently confirms the corrected two-child
incidence algebra.  Physical placement of the exterior token, opening the
aperture transition, and one-star consolidation remain hypotheses of the
conditional `B+1` theorem.
