# A controlled crossed double factor with an exact shallow augmented code

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The naive crossed product

\[
 P_1^\times(u,v)=
 \begin{cases}(u,G_1v),&|u|+|v|=0,\\
 (G_1u,v),&|u|+|v|=1
 \end{cases}
\]

is not a double factor: it compares the base direction functions at two
different vertices.  For the displayed `Q_4` seed, `(u,v)=(0000,1100)`
already gives proposed directions `R1` and `R3`.

There is an exact repair.  Keep the zeroth parity-alternating product, but
make the crossed column move controlled by the half used by the zeroth
factor.  This gives a literal same-owner double factor with a
fixed-point-free coordinate involution.  Cross once at dimension eight
and recurse in parallel thereafter.  In every dimension

\[
                         R=8\,2^t,                  \tag{0.1}
\]

the final affine family has the following exact property.  For both
forward and reverse trajectories and every

\[
                         1\le d\le R/8,             \tag{0.2}
\]

the augmented aligned code requested in the double-factor lane,

\[
 \boxed{
 \mathcal C_d^\pm(p,x)=
 \left(J_d^\pm(S_Rp+x),
       p|_{(J_d^\pm)^c},x|_{(J_d^\pm)^c}\right),}
\tag{0.3}
\]

is injective on `Q_R^even x Q_R`.  Thus its cap-one collision excess is
exactly zero, not merely `o(2^(2R))`, throughout every Gaussian band.
With the full/partial boundary roles included in the tag, the same result
holds for every physical start parity and every physical length
`q<=R/4-1`; the four-case reduction is recorded in
`MATH_AUDIT_REPAIRED_LATE_CROSS_HALF_STEP_CODES_20260726.md`.

The distinction between (0.3) and a literal lower or upper OR target is
essential.  A raw target does not determine `J`: an untouched `00` pair
and a completed `00 -> 01 -> 11` pair have the same lower trace on that
pair.  Therefore this theorem closes the explicitly tagged code
`(J,p_out,x_out)`, but it does not prove raw physical-trace injectivity.

This loss is realized inside the `Q_4` seed already at depth one.  With
`p=0000`, the starts

\[
 x=1010\quad(J=\{1\}),
 \qquad x'=0010\quad(J'=\{2\})
\tag{0.4}
\]

have the same lower target, pairwise

\[
                         (00,00,11,00).              \tag{0.5}
\]

Likewise `x=0101` with `J={1}` and `x'=1101` with `J'={2}` have the same
upper target `(11,11,00,11)`.  Thus the raw-tag gap is an actual collision,
not merely missing decoder information.

## 1. The controlled crossed operation

Let `H` be a neighbour permutation of `Q_h`, with

\[
                         H(z)=z+e_{\delta(z)},       \tag{1.1}
\]

and let `S` be any coordinate permutation of `[h]`.  For
`(u,v) in Q_h^L x Q_h^R`, put

\[
                         \epsilon(u,v)=|u|+|v|\pmod2.
\tag{1.2}
\]

Define

\[
 P_0(u,v)=
 \begin{cases}
  (Hu,v),&\epsilon=0,\\
  (u,Hv),&\epsilon=1,
 \end{cases}                                         \tag{1.3}
\]

and define the controlled column factor

\[
 C_S(u,v)=
 \begin{cases}
  (u,v+e_{S\delta(u)}),&\epsilon=0,\\
  (u+e_{S\delta(v)},v),&\epsilon=1.
 \end{cases}                                         \tag{1.4}
\]

Finally define a coordinate permutation of the `2h` child directions by

\[
 S^\times(Li)=R(Si),\qquad
 S^\times(Ri)=L(Si).                                \tag{1.5}
\]

### Theorem 1.1 (controlled crossed double factor)

Both `P_0` and `C_S` are neighbour permutations, and their outgoing
directions satisfy

\[
                         \delta_{C_S}(u,v)
                         =S^\times\delta_{P_0}(u,v) \tag{1.6}
\]

at every common owner.  If every component of `H` is an isometric
`C_(2h)`, every component of `P_0` is an isometric `C_(4h)`.

#### Proof

The assertions about `P_0` follow from

\[
                         P_0^{2s}(u,v)=(H^su,H^sv). \tag{1.7}
\]

The two halves alternate.  The first `2h` child directions consist of
`h` consecutive parent directions in each half, hence form a permutation
of all `2h` child coordinates; the next `2h` repeat them.  This proves
permutation, cycle length `4h`, and isometry.

For `C_S`, restrict first to the even shore.  Given an odd target `(u,w)`,
its unique even preimage is

\[
                         (u,w+e_{S\delta(u)}).       \tag{1.8}
\]

It is even because it differs from the odd target in one bit.  Thus the
even-to-odd restriction is bijective.  Given an even target `(w,v)`, its
unique odd preimage under the second clause of (1.4) is

\[
                         (w+e_{S\delta(v)},v).       \tag{1.9}
\]

Hence the odd-to-even restriction is also bijective, and `C_S` is a
neighbour permutation.

At an even owner, `P_0` uses `L delta(u)` and `C_S` uses
`R S delta(u)`.  At an odd owner, they use `R delta(v)` and
`L S delta(v)`.  These are exactly the two clauses of (1.6).  \(\square\)

The column factor `C_S` need not have long or isometric cycles.  The
affine complete-mapping lemma uses it only to certify the column
bijections.  The physical row cycles are translations of `P_0`, so the
isometry conclusion for `P_0` is the required one.

For the present `Q_4` seed one gets more.  Its four phase classes split
the directions into the two wires `{1,3}` and `{2,4}`.  The chosen
`S_4=(2 4)` preserves these wires.  The phase-synchronization calculation
in `MATH_THEOREM_PHASE_SYNCHRONIZED_CROSSED_Q8_ASSOCIATOR_20260726.md`
shows that `C_(S_4)` itself is an isometric `C_16`-factor: after every two
moves the two `Q_4` phases advance by `-1` and `+1`.  Hence the subsequent
parallel recursion makes **both** members isometric long-cycle factors.
The repaired construction is therefore a strict recursive double factor,
not merely a row factor with an auxiliary column witness.

## 2. Parallel continuation

If neighbour permutations `(A,B)` satisfy

\[
                         \delta_B(z)=T\delta_A(z),  \tag{2.1}
\]

define their parallel children by applying `A`, respectively `B`, in the
left half at even total parity and in the right half at odd total parity.
Both are neighbour permutations, and their directions obey the same-owner
relation with coordinate permutation `T sqcup T`.  No incoming-direction
identity and no cycle hypothesis on `B` is needed.  If `A` has isometric
`C_(2h)` components, its child has isometric `C_(4h)` components by
Theorem 1.1's argument.

Take `H=G_4^0` from the audited `Q_4` certificate and
`S=S_4=(2 4)` in Theorem 1.1.  This gives at dimension eight

\[
                         (G_8^0,G_8^1,S_8)
                         =(P_0,C_{S_4},S_4^\times), \tag{2.2}
\]

where `S_8` is fixed-point-free.  Continue only in parallel.  At
dimension (0.1), `S_R` is the direct sum of `R/8` copies of `S_8`, and
`G_R^0` is an exact isometric `C_(2R)`-factor.  Thus
`(G_R^0,G_R^1,S_R)` satisfies the hypotheses of the affine
complete-mapping theorem at every scale.

## 3. The bottom-block decoder

The outgoing direction fibres of `G_4^0` are the four cosets of

\[
 L=\langle0101,1010\rangle.                         \tag{3.1}
\]

Every nonzero member of `L` has weight at least two.  Hence deleting
coordinate `i` is injective on the fibre where the outgoing direction is
`i`.  The incoming direction-`i` fibre is the outgoing fibre translated
by `e_i`, so it has the same puncture property.

Write a bottom state as `(u,v) in Q_4^L x Q_4^R`.  The zeroth factor in
(2.2) is

\[
 G_8^0(u,v)=
 \begin{cases}
  (G_4^0u,v),&|u|+|v|=0,\\
  (u,G_4^0v),&|u|+|v|=1.
 \end{cases}                                         \tag{3.2}
\]

Suppose its selected direction is `q=Li`.  Then the block has even
parity and the outgoing base direction of `u` is `i`.  The six bits
outside `{q,S_8q}` include the other three bits of `u`; puncture
injectivity recovers `u_i`, and block parity recovers the last bit
`v_(S_4i)`.  The case `q=Ri` is identical with odd block parity and the
halves exchanged.  For a reverse move, `Li` means odd current block
parity and `Ri` means even current block parity; use the incoming fibre
and the same recovery.

Consequently, for either sign,

\[
 \left(q,
 z|_{[8]\setminus\{q,S_8q\}}\right)                \tag{3.3}
\]

determines the complete bottom state `z`.

## 4. Round-robin transversality and phase injectivity

There are `B=R/8=2^t` bottom `Q_8` blocks.  At each parallel recursion
level the two children alternate.  Inductively, every cyclic forward or
reverse interval of exactly `B` moves visits each bottom block once;
therefore every interval of `d<=B` moves visits each block at most once.

Let `J=J_d^\pm(y)`.  Since `S_R` is fixed-point-free and preserves each
bottom block,

\[
                         J\cap S_RJ=\varnothing.     \tag{4.1}
\]

An untouched block is fully recorded by
`y|_{[R]\setminus(J\cup S_RJ)}`.  A touched block has one selected
direction `q`; before that unique visit it is still in its initial state.
Equation (3.3) recovers its two missing bits.  Hence the maps

\[
 y\longmapsto
 \left(J_d^\pm(y),
 y|_{[R]\setminus(J_d^\pm(y)\cup S_RJ_d^\pm(y))}
 \right)                                             \tag{4.2}
\]

are injective for every `d<=R/8`, forward and reverse.

## 5. Exact augmented-code fibres

Put `y=S_Rp+x`, with `p` even.  From a value of (0.3), equation (4.1)
lets one read

\[
                         y|_{[R]\setminus(J\cup S_RJ)}
                         =(x+S_Rp)|_{[R]\setminus(J\cup S_RJ)}.
\tag{5.1}
\]

The phase decoder (4.2) recovers all of `y`.  For every `j in J`, the
mate `S_Rj` lies outside `J`; hence `x_(S_Rj)` and `p_(S_Rj)` are both
recorded.  The erased bits are then recovered by

\[
 p_j=y_{S_Rj}+x_{S_Rj},
 \qquad
 x_j=y_j+p_{S_Rj}.                                  \tag{5.2}
\]

Thus (0.3) is injective.  Since its domain has size

\[
                         N_R=2^{2R-1},               \tag{5.3}
\]

its image also has size `N_R`, and its exact cap-one collision excess is

\[
                         N_R-|\operatorname {im}\mathcal C_d^\pm|=0
                         \qquad(d\le R/8).           \tag{5.4}
\]

For a fixed support `J`, (4.2) has at most `2^(R-2d)` exterior words.
Therefore the forward and reverse support catalogues satisfy

\[
                         |\mathscr J_d^\pm|\ge 2^{2d}=4^d.
\tag{5.5}
\]

At `d=Theta(sqrt R)`, this is the exact exponential support entropy which
the bounded-order affine-lift recursion lacks.

## 6. Factor-type degeneracy is not augmented-code degeneracy

The exact translation stabilizer of the recursive zeroth direction rule
is

\[
                         L_R=L^{\oplus R/4},
 \qquad                  \dim L_R=R/2.              \tag{6.1}
\]

It is preserved by `S_R`.  Hence the `2^(R-1)` even contexts use exactly

\[
                         2^{R/2-1}                   \tag{6.2}
\]

distinct whole factor types, each repeated on exactly

\[
                         2^{R/2}                     \tag{6.3}
\]

contexts.  Thus phase-shift-only dependence remains exponentially
degenerate at the level of whole factors.  Equations (5.4)--(5.5) prove
that this is not an augmented shallow-code obstruction: the direction
support and visible exterior state separate every start.

## 7. Exact boundary

Proved:

1. the naive crossed product is false, with an explicit `Q_4` owner
   counterexample;
2. the controlled crossed column (1.4) is an exact neighbour permutation
   and supplies the required same-owner relation; for the `Q_4` phase
   seed it is itself an isometric `C_16`-factor;
3. cross once and then continue in parallel to obtain exact growing
   double factors;
4. the requested augmented codes `(J,p_out,x_out)` are exactly injective
   for both orientations and all `d<=R/8`;
5. all augmented half-step sectors are injective through `q<=R/4-1`;
6. their collision excess is zero and their support catalogues contain at
   least `4^d` supports; and
7. whole factor types nevertheless remain `2^(R/2)`-fold repeated.

Not proved:

1. that a raw lower or upper OR target recovers `J`;
2. raw physical trace injectivity or the untagged half-step codes;
3. the outer packet coupling; or
4. the coefficient-one theorem.

Moreover, the explicit depth-one pairs (0.4)--(0.5) refute raw
injectivity for the finite seed itself.

The next exact local statement is therefore a support-recovery theorem
for literal OR targets, not another parity complete-mapping identity.
In a coordinate-disjoint Johnson interface where every untouched swap
pair has occupancy one and every varied pair has occupancy zero/two, that
interface supplies the tag and the augmented theorem becomes literal.
Establishing such visibility in the intended outer installation is a
separate hypothesis, not a consequence of the cube factor alone.
