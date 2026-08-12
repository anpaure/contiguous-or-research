# One adjacent coatom transposition destroys the reflected quadratic invariant

Date: 2026-08-01  
Status: exact all-`d` local packet theorem and complete quadratic-projection
theorem.  It enlarges the serial safe-move lattice, but does not prove that
the required packets are globally planted or that the terminal compiler has
bounded deletion number.

## 0. Result

The reflected pair-degree obstruction of the canonical coatom packet is an
artifact of using the same coatom order in every active block.  It is not an
invariant of zero-owner, resident, upper-OR-transparent packet replacements.

Keep the canonical mixed screens, but in the active `Ica` block use

```text
f0, f2, f1, f3, ..., f_(d+1)
```

as the missing-coatom order, in both phases.  Every other block retains the
standard order.  For every `d>=3` this is a second packet of the same length
`12d+35` which preserves:

* the complete distinct owner set and both endpoints;
* simple Johnson-path topology;
* both immediate palettes as multisets;
* pointwise prefix and suffix OR signatures;
* complete internal interval-OR support;
* clipped boundary residence state; and
* minimum internal positive-run length `d+1`.

Nevertheless its lower signed action has

\[
 \deg^{(2)}_{\Delta_2}-\deg^{(2)}_{\Delta_d}\ne0.       \tag{0.1}
\]

It changes no owner and adds no cell.  In the fixed-owner block-order fibre
it is smallest possible: one adjacent transposition of two physical owner
positions.

There is a stronger planted version.  In the corrected endpoint-planted
packet, transposing omission positions `s,s+1` of `Ica`, for
`1<=s<d`, gives a family of safe packets.  At the reflected depth pair

\[
                  q=s+1,\qquad q'=d+2-q=d+1-s,        \tag{0.2}
\]

its pair-current defect is the single integral four-cycle

\[
 [f_0f_s]+[f_{s+1}f_{d+1}]
 -[f_0f_{s+1}]-[f_sf_{d+1}].                         \tag{0.3}
\]

The packet has zero defect at every later noncentral reflected pair.  These
packets form a triangular basis.  Together with the canonical packets, their
pair-degree projection is the full product of the point-degree kernels at
all depths.  Thus **no cross-depth quadratic invariant remains** in the
enlarged local catalogue.

This conclusion is about the safe reachability lattice.  Reflection was
independently shown not to be a necessary terminal-compiler invariant: a
fixed carrier can change its compiler-row signature inside its legal erosion
interval.  The present theorem removes reflection even before that compiler
bypass is used.

## 1. Base packet

Use the active triples

```text
Ad=e a delta, Bd=e b delta, Cd=e c delta,
ab=e a b, bc=e b c, ca=e c a,
Iab=inf a b, Ibc=inf b c, Ica=inf c a,
Ia=inf e a, Ib=inf e b, Ic=inf e c
```

and active paths

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.          (1.1)
```

Put `n=d+2`, let

\[
 F=(f_0,f_1,\ldots,f_d,f_{d+1}),
 \qquad C_i=F-\{f_i\},                               \tag{1.2}
\]

and let `K` be a disjoint fixed core.  The standard block over an active
triple `V` is

\[
                         B(V)=(K\cup V\cup C_i)_{i=0}^{d+1}.  \tag{1.3}
\]

At transitions `E={1,3,5,7}` use the upper common neighbour

\[
 K\cup(V_j\cup V_{j+1})\cup(F-\{f_0,f_{d+1}\});      \tag{1.4}
\]

at every other transition use the full-filler lower neighbour.  This is the
authoritative unplanted mixed-screen packet.

For the **adjacent-order breaker**, replace (1.3), only for `V=Ica`, by

\[
 (K\cup Ica\cup C_0, K\cup Ica\cup C_2,
  K\cup Ica\cup C_1, K\cup Ica\cup C_3,\ldots,
  K\cup Ica\cup C_{d+1}).                            \tag{1.5}
\]

The same order is used in `P` and `Q`.

## 2. All local geometric rows survive

### Theorem 2.1

The two expansions using (1.5) satisfy every U1--U4 assertion listed in
Section 0.

### Proof

The unordered set of coatom owners in `B(Ica)` is unchanged.  Its first and
last owners are unchanged.  Therefore every screen owner, both exterior
endpoints, and the complete owner set are literally those of the canonical
packet.  Any two different coatoms differ by exchanging their two missing
fillers, so the transposed block is still a simple Johnson path.  Owner
simplicity follows from the unchanged owner set.

Inside the transposed block, adjacent intersections change, but the exact
same ordered `Ica` block occurs once in each phase.  These contributions
cancel in the old/new comparison.  Every internal adjacent union is
`K union Ica union F`.  Screen-boundary values are unchanged because the
block endpoints are unchanged.  Hence both immediate palettes remain equal.

By the time a global prefix reaches `Ica`, a preceding lower screen has
already filled `F`; the analogous statement holds for suffixes.  The
pointwise prefix/suffix OR signatures are therefore insensitive to this
interior order change.  An interval contained in one coatom block either is
a singleton or contains two different coatoms and hence fills `F`.  An
interval leaving the block and using only one block cell necessarily uses a
block endpoint.  Thus the complete interval-OR support of each phase is
unchanged, and upper transparency follows from the base packet.

Only fillers `f1,f2` can have different run lengths.  Between the zero of a
filler at position `u` of one `n`-block and its zero at position `v` of the
next block there are

\[
                              n-u+v                 \tag{2.1}
\]

positive positions, including the screen.  At the two boundaries of the
transposed block the possibilities are `n-1,n+1`; elsewhere the value is
`n`.  Thus the minimum is `n-1=d+1`.  Active, core and extreme-filler runs
are unchanged.  The modified block is internal, so the clipped boundary
state is unchanged.  This proves every claim.  \(\square\)

Exactly the same proof applies to any adjacent transposition of internal
positions `s,s+1`, `1<=s<d`.

## 3. Exact signed action of the smallest breaker

Write

\[
 G=K\cup\{\mathord\infty,c\},\quad
 P_t=\{f_1,\ldots,f_t\},\quad
 S_t=\{f_{d-t+1},\ldots,f_d\}.                       \tag{3.1}
\]

For the canonical packet, with `t=d+1-q`, the new-minus-old lower counter is

\[
 \Delta_q^0=
 [Gafill P_t]-[Gbfill P_t]+[Gbfill S_t]-[Gafill S_t], \tag{3.2}
\]

where brackets denote a basis vector on the displayed set and `fill` means
ordinary union.

Let `R_q=Delta_q-Delta_q^0` be the correction caused by (1.5), and put

\[
                         H=\{f_3,\ldots,f_d\},qquad p=f_{d+1}. \tag{3.3}
\]

Then

\[
\begin{aligned}
R_2={}&[K\infty acf_2H]-[K\infty acf_1H]\\
     &+[K\infty cf_1Hp]-[K\infty cf_2Hp],             \tag{3.4}\\
R_d={}&[K\infty acf_2]-[K\infty acf_1]\\
     &+[K\infty af_0f_1]-[K\infty af_0f_2],           \tag{3.5}\\
R_q={}&0\qquad(3\le q\le d-1),                        \tag{3.6}
\end{aligned}
\]

and `R_1=0`.

To prove these identities, observe that a `q+1`-window distinguishes the
two orders only when one of its ends cuts between `C1,C2`.  Windows internal
to the common `Ica` block cancel phasewise.  Enumerating the four adjacent
screen shores leaves the two cuts in (3.4) at depth two and the two cuts in
(3.5) at depth `d`; for intermediate depths the left- and right-shore cuts
occur with the same active intersection and cancel.  This is a four-row
boundary calculation, independent of `d`; the replay performs it literally.

For a signed occurrence vector `z`, define

\[
 D_z(x,y)=\sum_{S\supseteq\{x,y\}}z(S).               \tag{3.7}
\]

The canonical part has `D_(Delta_2^0)=D_(Delta_d^0)`.  Applying (3.7) to
(3.4)--(3.5), all common-core and common-tail pairs cancel, leaving

\[
\begin{aligned}
 D_{\Delta_2}-D_{\Delta_d}
 ={}&[af_2]-[af_1]+[cf_1]-[cf_2]\\
    &+[f_0f_2]-[f_0f_1]+[f_1p]-[f_2p].               \tag{3.8}
\end{aligned}
\]

The eight pair coordinates in (3.8) are distinct for `d>=3`, proving
(0.1).

## 4. The corrected endpoint-planted triangular family

The current endpoint planting uses first-block omission order

```text
p, f1, f2, ..., fd, f0
```

and, in its smallest immediate-palette-exact form, upper screens

```text
{0,2,4,6,8,10}.                                      (4.1)
```

All later blocks have standard endpoints.  Thus (1.5), or its
`s,s+1` analogue, changes no planted owner or attachment.  Theorem 2.1
applies verbatim.

### Theorem 4.1 (triangular four-cycle law)

Let `Delta^(s)` be the lower signed action of the corrected planted packet
whose `Ica` omission positions `s,s+1` are transposed.  For a noncentral
reflected pair put

\[
       \Theta_q^{(s)}=D_{\Delta_q^{(s)}}-
                      D_{\Delta_{d+2-q}^{(s)}}.        \tag{4.2}
\]

For `2<=q<d+2-q`, if `q>s+1`, then

\[
                         \Theta_q^{(s)}=0.             \tag{4.3}
\]

At the diagonal `q=s+1<d+1-s`,

\[
 \Theta_{s+1}^{(s)}=
 [f_0f_s]+[f_{s+1}p]-[f_0f_{s+1}]-[f_sp].             \tag{4.4}
\]

### Proof

The adjacent transposition can affect a window only when a boundary cuts
between omission positions `s,s+1`.  On the left shore this first occurs at
depth `s+1`.  On the right shore it first occurs at depth `d+1-s`.
Consequently, when `q<d+2-q` and `q>s+1`, both that depth and its reflection
lie strictly between the two cut thresholds, proving (4.3).

At the two thresholds, put `x=f_s`, `y=f_(s+1)`.  The low-depth correction
has pair current

\[
                    [ax]+[py]-[ay]-[px],              \tag{4.5}
\]

whereas the reflected high-depth correction has pair current

\[
                    [ax]+[f_0y]-[ay]-[f_0x].          \tag{4.6}
\]

Their difference is (4.4).  The base corrected planting has equal reflected
pair currents, as follows by the same two-shore calculation.  \(\square\)

For `q<s+1`, the packet may create earlier triangular terms.  Their values
are irrelevant to the spanning argument because packets are processed in
decreasing diagonal depth.

## 5. Complete quadratic-projection lattice

Let

\[
 \mathcal K_2=\ker\!\left(
   \mathbb Z^{{\Omega\choose2}}\longrightarrow\mathbb Z^\Omega,
   [xy]\longmapsto [x]+[y]\right).                  \tag{5.1}
\]

This lattice is generated by the alternating four-cycles

\[
                      [ux]+[vy]-[uy]-[vx].            \tag{5.2}
\]

Every lower packet action has zero point degree at every depth, so its pair
current belongs to `K_2`.

### Theorem 5.1

Let `h=floor((d+1)/2)`.  Under arbitrary coordinate relabellings and packet
reversal, the defect map from the adjacent-order planted catalogue onto
the noncentral reflected pairs is surjective:

\[
  \operatorname{span}_{\mathbb Z}
    \{(\Theta_2,\ldots,\Theta_h)\}
                         =\mathcal K_2^{\,h-1}.        \tag{5.3}
\]

Together with the canonical coatom packets, the pair-current projection at
all depths is the full product of the individual point-degree kernels.

### Proof

For diagonal `q=s+1`, (4.4) is literally (5.2).  Relabelling the four roles
`f0,fs,f_(s+1),p` realizes every generator (5.2).  By (4.3), the packet has
zero defect at all later diagonals.  Start at `q=h` and descend.  Choose an
integer combination of `s=h-1` packets to realize the prescribed component
at `h`; its unwanted terms occur only at earlier components.  Then use
`s=h-2`, and continue.  Reversal supplies negative coefficients.  This
proves (5.3) over the integers.

The canonical maximal-chain theorem supplies the diagonal copy of
`K_2` at each reflected pair, independently pair by pair; at a central
self-reflected depth it supplies `K_2` directly.  Combining a diagonal
current `(g,g)` with arbitrary differences from (5.3) gives independent
currents on the two shores.  Thus the full pair-current image is the product
of its per-depth kernels.  \(\square\)

The theorem characterizes the **quadratic projection**, not the complete
occurrence-labelled compiler lattice.  Higher-order flag invariants,
positivity, physical packet availability and terminal Hall deficiency remain
separate questions.

## 6. Consequence and scope

The global reflected pair-degree invariant in the canonical-only notes must
now be scoped to the uniform-block-order subcatalogue.  It cannot obstruct a
serial safe walk once block-specific coatom orders are admitted.  More
strongly, every noncentral reflected quadratic current can be controlled
independently by an all-`d`, zero-owner, zero-length-overhead packet family.

What is still missing for `nu(k)<=B(k)+O(1)` is not this algebra:

1. the prepared carrier must physically contain or exchange into the needed
   packet slots;
2. serial safe reachability must drive the terminal compiler deletion
   number to `O(1)`; and
3. the bounded interface must regenerate under the Pascal lift.

The compiler-bypass theorem shows separately that a terminal compiler need
not inherit a carrier's reflected signature.  Therefore (5.3) should be used
as reachability freedom, not imposed as an extra compiler requirement.

## 7. Replay

The dependency-free replay checks all local U1--U4 rows for every internal
adjacent transposition through `d=10`, the exact formulas (3.4)--(3.8)
through `d=24`, and the corrected planted triangular law through `d=18`:

```text
scratch/audit_coatom_adjacent_order_reflection_breakers_20260801.py
scratch/coatom_adjacent_order_reflection_breakers_20260801.audit.json
```

It reports

```text
PASS_COATOM_ADJACENT_ORDER_REFLECTION_BREAKERS
```

The finite replay supports, but does not replace, the all-`d` boundary-cut
proofs above.
