# The planted coatom breakers generate the full integral depth product, but not a compiler return

Date: 2026-08-01  
Lane: R, coupled lower flags and compiler linkage  
Status: unconditional labelled-catalogue theorem, independently audited.
The complete signed occurrence lattice at depths `q=2,...,d` is saturated.
The result is not a fixed-carrier or nonnegative-reachability theorem.  The
immediate q1 boundary Hall row and the nonlinear common-cap linkage remain
separate exact gates.

## 0. Main theorem

Fix

\[
 d\ge3,\qquad r\ge d+4,
 \qquad |\Omega|=v,\qquad v-r\ge4.
\]

Use the current endpoint planting with upper-screen transitions

\[
                         E=\{0,2,4,6,8,10\},          \tag{0.1}
\]

first `Iab` omission order

\[
                         (p,f_1,\ldots,f_d,f_0),      \tag{0.2}
\]

and standard omission order in every other block.  In the label-attached
`Ica` block, allow an adjacent transposition of any internal pair
`f_s,f_(s+1)` in both packet phases.  Allow every admissible injective
assignment of the packet roles to `Omega`, and allow packet reversal.

For `2<=q<=d`, put

\[
 M_q=\mathbb Z^{\binom{\Omega}{r-q}},\qquad
 \partial_qe_X=\sum_{x\in X}e_x.                    \tag{0.3}
\]

Let `L_d` be the integer span of the direct sums of the signed
depth-`2,...,d` occurrence increments of this complete labelled catalogue.

### Theorem 0.1 (integral full product)

\[
 \boxed{
 L_d=\bigoplus_{q=2}^{d}\ker_{\mathbb Z}\partial_q.
 }
 \tag{0.4}
\]

There is no finite index, parity obstruction, higher congruence, or
cross-depth linear invariant beyond the point degrees in the individual
layers.  Only twists with

\[
                         1\le s\le\lfloor d/2\rfloor          \tag{0.5}
\]

are needed.

The qualifier “complete labelled catalogue” is load-bearing.  The proof
subtracts packet actions with different global role assignments.  It does
not place those packets in one common physical slot.

## 1. Exact adjacent-twist derivative

Write the internal fillers as `u_1,...,u_d`, put `x=u_s`,
`y=u_(s+1)`, and let `K` have size `r-d-4`.  For disjoint labels define the
primitive Johnson square

\[
 Q_H(\alpha,\beta;x,y)=
 e_{H\alpha x}+e_{H\beta y}-e_{H\alpha y}-e_{H\beta x}.
 \tag{1.1}
\]

Let `Delta^0` be the signed action of the untwisted endpoint-planted packet,
let `Delta^s` be the action after twisting `u_s,u_(s+1)` only in `Ica`, and
put

\[
                              C_s=\Delta^s-\Delta^0.           \tag{1.2}
\]

For `1<=s<=floor(d/2)`, define

\[
\begin{aligned}
 H_s^+&=K\cup\{\mathord\infty,c\}
              \cup\{u_{s+2},\ldots,u_d\},\\
 H_s^-&=K\cup\{\mathord\infty,c\}
              \cup\{u_1,\ldots,u_{s-1}\},\\
 H_{s,t}^{\rm tail}&=K\cup\{\mathord\infty\}
              \cup\{u_{s-t},\ldots,u_{s-1}\}.
\end{aligned}                                                \tag{1.3}
\]

Empty filler ranges are omitted.

### Lemma 1.1 (unit boundary formula)

The nonzero depth components of `C_s` are exactly

\[
\begin{array}{c|c}
q&(C_s)_q\\ \hline
s+1&Q_{H_s^+}(a,p;x,y),\\[1mm]
d+1-s&Q_{H_s^-}(a,f_0;x,y),\\[1mm]
q>d+1-s&Q_{H_{s,d+1-q}^{\rm tail}}(a,c;x,y).
\end{array}                                                  \tag{1.4}
\]

If `2s=d`, the first two squares occur in the same central row and are
added.  Every other row is zero.

#### Proof

An intersection window changes only if one boundary separates the two
transposed coatoms.  Windows internal to the common label-attached `Ica`
block occur in both phases and cancel.  At the first exterior crossing, the
common filler tail is `u_(s+2),...,u_d`, the active alternatives are `a,p`,
and the first separating width has depth `s+1`.  This gives the first row.

At the reflected crossing, the common prefix is `u_1,...,u_(s-1)` and the
alternatives are `a,f_0`, giving depth `d+1-s`.  After that crossing, a
width with `t=d+1-q<s` retains exactly the preceding filler tail in (1.3)
and distinguishes `a,c`.  These are the last rows of (1.4).  Before the
first crossing and between the two crossings, both transposed coatoms are
simultaneously present or absent.  Every surviving boundary contribution
is the four-term square (1.1) with unit coefficients. \(\square\)

This formula uses the actual endpoint-planted packet.  Its untwisted
baseline has an eight-term action, not the four-term action of the
unplanted common-order tensor; taking the derivative (1.2) avoids that
scope error.

## 2. A role commutator isolates one primitive depth

Let `tau_p` be the coordinate relabelling which interchanges the coordinates
assigned to packet roles `p` and `b`, fixing every other assigned role.
The active role `b` does not occur in any row of (1.4), while `p` occurs
only in the first row.  Hence

\[
 \boxed{
 C_s-\tau_pC_s
   =\mathbf e_{s+1}\otimes Q_{H_s^+}(b,p;x,y).
 }                                                            \tag{2.1}
\]

Likewise, interchanging the role coordinates `f_0,b` gives

\[
 \boxed{
 C_s-\tau_0C_s
   =\mathbf e_{d+1-s}\otimes Q_{H_s^-}(b,f_0;x,y).
 }                                                            \tag{2.2}
\]

Indeed,

\[
 Q_H(a,p;x,y)-Q_H(a,b;x,y)=Q_H(b,p;x,y),             \tag{2.3}
\]

and every other row is fixed by `tau_p`; (2.2) is identical.  In the even
central case the other central square is fixed, so it cancels and (2.1)
still isolates one primitive square.

Each `C_s` is the difference of two reversible catalogue columns, and its
relabelled copy is another such difference.  Therefore (2.1)--(2.2) are
integer combinations of catalogue columns, not rational projections.
They cover every depth `q=2,...,d` as `s` runs through (0.5).

## 3. Arbitrary square labels and saturation

At the shallow depth `q=s+1`, the square core in (2.1) has size

\[
                         |H|=r-s-3.                  \tag{3.1}
\]

Given an arbitrary core of this size, assign its labels to `K`,
`infinity,c`, and `u_(s+2),...,u_d`.  Assign the four square labels to
`b,p,x,y`.  The roles still to be assigned outside `H` are

\[
                         a,e,\delta,f_0,u_1,\ldots,u_{s-1},
\]

so altogether `s+7` outside labels are required.  But

\[
                         v-|H|=v-r+s+3\ge s+7.        \tag{3.2}
\]

The deep row has the same count.  Thus every abstract primitive Johnson
square in every target layer is a relabelled instance of (2.1) or (2.2).

For `2<=m<=v-2`, the integer kernel of

\[
 \mathbb Z^{\binom{\Omega}{m}}\longrightarrow\mathbb Z^\Omega,
 \qquad e_X\longmapsto\sum_{x\in X}e_x             \tag{3.3}
\]

is generated by primitive Johnson squares.  Here

\[
                         r-d\ge4,qquad r-2\le v-2,
\]

so the statement applies to every depth.  Equations (2.1)--(2.2) therefore
give

\[
                  \bigoplus_{q=2}^d\ker_{\mathbb Z}\partial_q
                       \subseteq L_d.               \tag{3.4}
\]

Every packet action is point-balanced at each depth, giving the reverse
inclusion.  This proves Theorem 0.1 integrally.

## 4. Independent central-range harmonic cross-check

Assume in this section only that

\[
                         v-r\ge r-2,                         \tag{4.0}
\]

as holds in the central settings `v=2r-1,2r`.  There is then a separate
rational proof which is useful as an audit of the depth endpoints.  On rank
`r-q`, the point kernel decomposes into Boolean
harmonics `H_j=S^(v-j,j)`, `j>=2`.  The planted primitive-square theorem
gives the complete `H_2` multiplicity.  For every `j>=3`, pair the canonical
four-term action with a disjoint-pair polytabloid whose first positive label
is `a` and whose first negative mate is exterior to the action support.
The `b`-terms vanish, and suitable prefix filler sets give the exact unit
step

\[
                         \langle\Phi_s,\Delta_t\rangle
                              ={\bf1}_{\{t\ge s\}}.   \tag{4.1}
\]

The construction uses `j` distinct exterior mates; (4.0) supplies them for
every occurring `j<=r-2`.  The step vectors are triangular on the interval
of depths where `H_j` occurs.  This independently recovers the full rational
product in the central range.  Unit triangularity alone would not prove
integral saturation because the Boolean permutation lattices do not split
integrally into their Specht summands; the literal primitive isolation
(2.1)--(2.2) is the sharp-corank integral argument.

## 5. The exact q1 boundary remains frozen

The lattice in Theorem 0.1 starts at q2.  Every current packet replacement
preserves its immediate lower-palette multiset and its two attachment
endpoints.  Let a simple rank-`r` carrier with a nonzero depth-`d` factor
have q1-hole endpoint classes `Z,L,R,B` of sizes `z,ell,rho,b`, and put

\[
                         u_L=\min(\ell,d),\qquad
                         u_R=\min(\rho,d).
\]

The exact deficiency of the q1 candidate-cap graph is

\[
 \boxed{
 \delta_{\rm top}=
 z+\ell+\rho+b-u_L-u_R-
       \min\{b,2d-u_L-u_R\}.
 }                                                            \tag{5.1}
\]

It is invariant along every serial walk from the present packet catalogue,
and every compiler has deletion number at least `delta_top`.  The proof is
the two-bank argument: if an interior short cap contained a missing
rank-`r-1` target `Q`, it would be contained in an adjacent rank-`r-1`
intersection and hence equal that already present q1 colour.  Only the `d`
repeated cells at each endpoint remain.

Thus a regenerative additive-constant input must already export

\[
                         \delta_{\rm top}=O(1),       \tag{5.2}
\]

or introduce a q1/endpoint-moving packet.

## 6. Compiler linkage after a physical lift

One adjacent twist changes exactly `2d+2` marginal compiler-cell signatures
in each phase.  If `m` is the first swapped owner address, the changed starts
are

\[
\begin{aligned}
 \mathcal D_1(m)&=\{m-1,m,m+d+1,m+d+2\},\\
 \mathcal D_h(m)&=\{m,m+d+2-h\},\qquad 2\le h\le d.
\end{aligned}                                                \tag{6.1}
\]

Suppose a physical transition `T^- -> T^+` has been constructed.  Choose an
old optimizing cap state and a maximum compiler matching `M`.  For a legal
new cap state `theta`, retain the old matching edges still present, let
`ell(theta)` be the number lost, and let `alpha(theta)` be the maximum
number of pairwise vertex-disjoint augmenting paths from the retained
matching.  Then the exact optimized deficiency change is

\[
 \boxed{
 \lambda(T^+)-\lambda(T^-)
 =\min_{\theta\in\Theta(T^+)}
      \bigl(\ell(\theta)-\alpha(\theta)\bigr).
 }                                                            \tag{6.2}
\]

Thus nonworsening is equivalent to one legal new state with
`alpha>=ell`, and strict improvement to one with `alpha>ell`.  Full
integral occurrence span supplies no lower bound on `alpha`: the exact
two-target/two-cell common-cap example has marginal graph `K_(2,2)` and the
full primitive square, but both perfect matchings violate one protected
cap-union row, so its exact common-cap rank is only one.

## 7. Physical scope and the sharp remaining theorem

The pure-depth direction (2.1) is the four-column signed combination

\[
 (\Delta^s-\Delta^0)-\tau_p(\Delta^s-\Delta^0).      \tag{7.1}
\]

The two labelled packet pairs generally have different attachment
endpoints and owner slots.  Equation (7.1) is therefore not a literal
four-step walk in one exact factor.  It also supplies no freed physical
compiler cell.  The returned-catalyst square router can connect an induced
even-cycle matching fibre, but it preserves the used physical basis and
cannot replace an open augmenting ear.

The two currently proved host ingredients also live in different fibres.
In the canonical common-order orbit, fixing the endpoint and varying one
action-invisible active label gives `v-r-3` prospective copies of one fixed
all-depth action.  The corrected endpoint-planted breaker has the required
nested residence collar, but that active-label variation changes its lower
action and is not a fixed-action menu.  Therefore a physical lift of (7.1)
still needs either a collar for the canonical fixed-action menu or a new
fixed-action menu inside the corrected planted fibre.

The formal algebra is now closed.  A theorem yielding `B(k)+O(1)` through
this route must still provide all three of:

1. a resource-compatible or regenerative physical realization of the
   required pure-depth square/circuit combinations;
2. the q1 boundary export (5.2); and
3. one coexistent common-cap state satisfying `alpha>=ell`, with strict
   surplus when a compiler defect must be reduced.

No claim of a bounded compiler or of `B(k)+O(1)` is made here.

## 8. Audit ledger

The decisive role-swap calculation was independently checked coefficient by
coefficient:

\[
 Q_H(a,p;x,y)-Q_H(a,b;x,y)=Q_H(b,p;x,y),
\]

and all other rows of (1.4) are fixed under `p<->b`; the `f_0<->b` audit is
identical.  The central even-depth case and the `v-r=4` label count were
checked separately.  This independent audit agrees with the literal replay
in

```text
MATH_THEOREM_COATOM_ENDPOINT_BREAKER_PRODUCT_LATTICE_20260801.md
scratch/audit_coatom_endpoint_breaker_product_lattice_20260801.py
scratch/coatom_endpoint_breaker_product_lattice_20260801.audit.json
```

whose payload is

```text
34d67c5726976a840c6b049adc915c544fcf6e2d664f4c8954195ab3681c3d22
```

The q1 proof was also adversarially corrected: a deeper consecutive
intersection can still have rank `r-1`; the valid proof is the adjacent-
palette equality argument used in Section 5.
