# Adjacent coatom-order twists give a full planted quadratic breaker basis

Date: 2026-08-01  
Status: unconditional local planted-template theorem  
Scope: the authoritative repaired endpoint planting on connector row 1.
This removes the reflected quadratic invariant of the common-order fibre;
it does not prove global planted-slot availability or bounded compiler
deletion.

## 0. Outcome

The reflected pair-current law of the unplanted common-order tensor is not
an invariant of the actual packet catalogue.

Use the repaired endpoint planting

\[
 C_p,C_{g_1},\ldots,C_{g_d},C_{g_0}                  \tag{0.1}
\]

in the first `Iab` block, standard order

\[
 C_{g_0},C_{g_1},\ldots,C_{g_d},C_p                 \tag{0.2}
\]

in every other block, and the upper-screen set

\[
                         E_0=\{0,2,4,6,8,10\}.       \tag{0.3}
\]

For every

\[
                  1\le p_0\le h:=\left\lfloor{d-1\over2}\right\rfloor,
\]

make one additional label-attached change: in the unique `Ica` block of
each phase, interchange the adjacent missing-filler positions
`g_(p_0),g_(p_0+1)`.

Every resulting old/new pair still has exact owner set, simple Johnson
topology, immediate palettes, complete interval-OR support, and depth-`d`
residence.  Relative to the untwisted planted packet, these `h` variants
give an exact diagonal basis for the `h` reflection-odd quadratic depth
coordinates.  In particular, after these variants and coordinate
relabelings are admitted, **no nonzero reflected pair-degree difference is
invariant**.

This is the positive resolution of the apparent quadratic obstruction.  It
also corrects the scope of the common-order reflection theorem: that theorem
classifies a useful subfibre, not the physical safe-move component.

## 1. The planted adjacent-order variants

Let `T^0_old,T^0_new` denote the authoritative planted pair (0.1)--(0.3).
For `1<=p_0<=h`, let `T^(p_0)_old,T^(p_0)_new` be obtained by changing only
the omission order in the block whose active label is `Ica`:

\[
 (g_0,\ldots,g_{p_0},g_{p_0+1},\ldots,g_d,p)
 \longmapsto
 (g_0,\ldots,g_{p_0+1},g_{p_0},\ldots,g_d,p).        \tag{1.1}
\]

The change is attached to the active label, not to a physical block index:
`Ica` occurs at index 6 in the old active word and index 5 in the new one.

### Theorem 1.1 (safe-above-compiler exactness)

For every `d>=3` and every `1<=p_0<=h`, the pair
`T^(p_0)_old,T^(p_0)_new` has:

1. the same distinct rank-`r` owner set and the same planted endpoints;
2. simple Johnson topology;
3. equal immediate intersection and union counters;
4. equal pointwise prefix/suffix OR signatures and equal complete internal
   interval-OR support; and
5. minimum internal positive run `d+1` with equal clipped boundary state.

#### Proof

Reordering a coatom block does not change its owner set, and any two
distinct coatoms are Johnson adjacent.  The swap in (1.1) is internal, so
the first and last owners of the `Ica` block and every screen are unchanged.
This gives the owner, endpoint and topology claims.

The identical label-attached `Ica` block occurs once in each phase, so its
changed internal immediate edges cancel between the two counters.  Its
exterior screen edges are unchanged.  The authoritative planted active
table therefore continues to give both immediate counter equalities.

For OR support, one block letter is determined by the unchanged owner set,
while any two distinct coatoms fill the entire filler set.  The exceptional
screen-adjacent intervals see the unchanged first and last block owners.
Thus the standard finite-active / symbolic-filler deck proof is unaffected.

It remains to check residence.  Across the transition into the twisted
block, `g_(p_0+1)` moves earlier by exactly one place and every other filler
moves no earlier; across the transition out, `g_(p_0)` moves earlier by
exactly one.  An intersection screen contains every filler, and an upper
screen omits only `g_0,p`, neither of which was moved.  Hence every new
positive gap is at least `(d+2)-1=d+1`.  The endpoints of the complete
fragment are unchanged, so the clipped boundary states agree.  \(\square\)

## 2. Exact reflection-odd current

For a carrier fragment `Z`, let `mu_q(Z)` count intersections of `q+1`
consecutive owners.  Put

\[
 \Delta_q^{p_0}
   =\mu_q(T^{p_0}_{\rm new})-\mu_q(T^{p_0}_{\rm old}),
 \qquad
 R_q^{p_0}=\Delta_q^{p_0}-\Delta_q^0.              \tag{2.1}
\]

For a signed occurrence vector `z`, define the filler-pair functional

\[
 \psi_{p_0}(z)
  =\deg_z^{(2)}(g_0,g_{p_0})
    -\deg_z^{(2)}(g_0,g_{p_0+1}).                    \tag{2.2}
\]

### Theorem 2.1 (diagonal breaker identity)

For `1<=j,p_0<=h`,

\[
 \boxed{
 \psi_{p_0}
   \left(R_{j+1}^{p_0}-R_{d+1-j}^{p_0}\right)
   =2\,{\bf1}_{\{j=p_0\}}.}
                                                               \tag{2.3}
\]

#### Proof

Only windows meeting the `Ica` block can distinguish the two orders in
(1.1).  Windows internal to that block cancel between phases because their
active label is the same.  The remaining windows form the four entry/exit
boundary families.

An intersection can distinguish `g_(p_0)` from `g_(p_0+1)` only when its
boundary falls between their adjacent omission positions.  Comparing depth
`j+1` with its reflected depth `d+1-j`, all four boundary families cancel
unless `j=p_0`.  At `j=p_0`, the surviving signed pair current is the filler
square

\[
 \begin{aligned}
 &[g_0g_{p_0}]+[g_{p_0+1}p]\\
 &\hspace{20mm}-[g_0g_{p_0+1}]-[g_{p_0}p],            \tag{2.4}
 \end{aligned}
\]

where `[xy]` records pair incidence, not a Boolean target.  Applying
`psi_(p_0)` to (2.4) gives `2`.  This is (2.3).

Equivalently, the complete boundary check has one row per `j`; its only
nonzero entry under (2.2) is the row whose window boundary separates the
two swapped omissions.  No asymptotic or generic-position argument is
used.  \(\square\)

### Corollary 2.2 (full reflection-odd quadratic span)

The `h by h` matrix of the currents (2.3) is `2I_h`.  Hence over `Q` the
adjacent-order variants span all reflection-odd quadratic depth profiles.
After coordinate relabeling, they span

\[
 S^{(k-2,2)}\otimes
 \{(v_2,\ldots,v_d):v_q=-v_{d+2-q},
                         \ v_{(d+2)/2}=0\}.           \tag{2.5}
\]

Consequently no nonzero functional

\[
 \deg_q^{(2)}(x,y)-\deg_{d+2-q}^{(2)}(x,y)
\]

is invariant under the enlarged planted catalogue.

#### Proof

Equation (2.3) gives a basis of the depth multiplicity space.  The
nontrivial pair-degree vectors lie in the irreducible quadratic Johnson
module `S^(k-2,2)` because every point degree is zero.  The diagonal
coordinate-relabeling orbit of any nonzero vector spans that irreducible
module, proving (2.5).  \(\square\)

### Corollary 2.3 (the projected odd lattice is saturated)

Let

\[
 {cal Q}_k=\ker\left(
   \partial_2:\mathbb Z^{\binom{[k]}2}\longrightarrow\mathbb Z^k
                    \right)
\]

be the integer lattice of pair currents with zero point degrees.  In the
reflection-odd pair-current projection, the adjacent-order packet catalogue
and all coordinate relabelings generate exactly

\[
                              \boxed{{\cal Q}_k^{\oplus h}}.     \tag{2.6}
\]

In particular this projected lattice has index one; there is no hidden
parity obstruction behind the scalar `2` in (2.3).

#### Proof

Order the reflected depth pairs by `j=1,...,h`.  The full boundary
calculation used in Theorem 2.1 has two triangular properties for twist
`p_0`:

1. its reflection-odd pair current is zero at every `j>p_0`; and
2. at `j=p_0` it is exactly the primitive pair square (2.4).

Pair squares generate `Q_k` over the integers: this is Theorem 3.1 of
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`
specialized to rank two.  For `p_0=1`, coordinate conjugates therefore
generate the first copy of `Q_k`.  Inductively assume the first `p_0-1`
copies are generated.  A conjugate of twist `p_0` has one prescribed
primitive square in coordinate `p_0` and only earlier-coordinate junk.
Subtract the already generated earlier currents.  This isolates every pair
square in coordinate `p_0`, hence the complete `p_0`-th copy of `Q_k`.
Induction proves (2.6), integrally.  \(\square\)

This saturation concerns the **pair-current image**.  It does not claim
that the full occurrence-vector lattice is saturated or that a prescribed
integer combination is realizable through nonnegative physical carrier
states.

## 3. What this changes for the additive-constant route

The lower packet algebra now has two sharply separated facts.

1. With one common coatom order, the canonical flags obey reflected pair
   balance.
2. Within the actual planted owner/upper/residence-safe catalogue, internal
   adjacent-order twists provide every missing reflection-odd quadratic
   direction.

Therefore a failure of bounded terminal compiler reachability cannot be
attributed to the reflected quadratic invariant.  The remaining gates are
physical and nonlinear:

* a fixed incumbent slot need not offer all `h` order variants;
* an algebraically prescribed sequence still needs plantable owner halos;
* nonnegative occurrence paths are stronger than rational span; and
* terminal common-cap deficiency depends on full target--cell incidence,
  not only natural-shadow moments.

The precise next routing target is consequently a planted-order actuator
theorem: prepare or reach enough `Ica` blocks with selectable adjacent
omission swaps, and couple their exact filler squares (2.4) to compiler
augmenting paths.

## 4. Audit

Run

```text
python3 scratch/audit_coatom_variable_order_quadratic_span_20260801.py
```

The audit uses the authoritative first-block order (0.1), transition zero
upper, and screen set (0.3).  For every `3<=d<=24` and every
`1<=p_0<=floor((d-1)/2)`, it checks Theorem 1.1 literally and verifies that
the matrix in (2.3) is exactly `2I_h`.

The endpoint-planted baseline is also checked to obey the reflected law,
so the audited current is genuinely the incremental direction supplied by
the adjacent-order twist.
