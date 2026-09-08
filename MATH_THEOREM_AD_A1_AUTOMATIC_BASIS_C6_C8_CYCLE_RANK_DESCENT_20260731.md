# Fixed-basis physical-circuit descent and the compensated asymmetric packet

Date: 2026-07-31  
Status: exact all-dimension cycle-rank and degree ledger for a supplied
fixed-basis packet; exact compensation of the minimum asymmetric `C6` by a
palette-neutral physical `C6` or `C8`; audited at the first active fibre and
under suspension through ambient `m=6`; no all-dimension packet-supply theorem

## 0. Verdict

The automatic common-basis theorem removes `Q`/Hall from this lane, but it
does **not** make the literal minimum asymmetric `C6` admissible.  With the
two diagonal palettes fixed, that packet still has a repeated old palette
vertex and nonzero flux, so it is not an exchange inside either punctured
side matching.

There are two sharper physical conclusions.

1. Every strict physical alternating `C_(2t)` is pointwise
   degree-balanced: every port loses and gains one edge.  Hence neither the
   asymmetric `C6`, any palette-neutral physical `C6`, nor its compensated
   physical `C8` can reduce a side degree collision or a seam-anchor degree
   collision.  Their only possible service is topology.
2. Topological service has an exact rank formula.  If `A` is the old half,
   `B` the new half, `T=S-A`, and `rho_T(E)` is the graphic rank of `E`
   after contracting the components of `T`, then

   \[
        \beta(S-A+B)-\beta(S)=\rho_T(A)-\rho_T(B).       \tag{0.1}
   \]

   Thus the packet is strictly cycle-decreasing exactly when the new half
   has larger contracted graphic rank than the old half.

A single asymmetric `C6` cannot pass the frozen-palette row.  A simultaneous
opposite-flux compensation can.  In the complete five-active-coordinate
fibre there are exactly three strict-`C6` opposite-flux mates: reversal
(trivial cancellation), one noncanonical mate reducing with the source to a
palette-neutral physical `C6`, and the unique mate inside the ordered
canonical asymmetric family reducing to a common-exterior physical `C8`.
The reduced `C6` can lower cycle rank by at most two; the `C8` by at most
three.  Both bounds are sharp as abstract contraction statements.

The remaining gate is therefore not common-basis Hall.  It is occurrence of
one of these old circuit halves in a chosen diagonal representative, followed
by the global contracted-rank and signed endpoint tests.

## 1. Frozen diagonal bases

Use the two-coordinate notation with child parameter `n`.  The theorem
`MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md`
proves for every `n>=4` that the two pulled-back diagonal matroids have a
common basis `Q` of order `Cat_(n+1)`.  Inherited tail/head ports then fix the
two punctured rank-`n` banks

\[
 D^-\subseteq\binom{[2n]}n,\qquad D^+\subseteq\binom{[2n]}n. \tag{1.1}
\]

A diagonal atom is a containment pair `(L,U)` with `|U-L|=2`.  Its unique
physical lift is the Johnson edge

\[
 \psi(L,U)=\{L+x,L+y\},\qquad U-L=\{x,y\}.             \tag{1.2}
\]

Once the bases in (1.1) are fixed, a legal rematching must retain every
lower and upper palette vertex once.  No aggregate cancellation between the
two sides is allowed: their collar traces are different resource rows.

## 2. The literal asymmetric `C6` remains impossible

Let `H` be disjoint from five distinct active coordinates `a,b,r,c,d`.  The
minimum asymmetric packet has cyclic ports

\[
 H+ar, H+br, H+rd, H+rc, H+cd, H+ac,              \tag{2.1}
\]

with old even edges and new odd edges.  Suppressing `H`, write this packet as
`P(a,b,r,c,d)`.  Its exact palette flux is

\[
 \Phi_L(P)={\bf e}_{H+a}-{\bf e}_{H+r},               \tag{2.2}
\]

\[
 \Phi_U(P)={\bf e}_{H+arc}+{\bf e}_{H+brd}
            -{\bf e}_{H+abr}-{\bf e}_{H+acd}.          \tag{2.3}
\]

Moreover its three old lower labels are `H+r,H+r,H+c`.  Therefore its old
half is not a subset of any diagonal matching.  Reversal moves the collision
to the terminal half, and complement moves it to the dual shore.

### Theorem 2.1 (fixed-basis and degree no-go)

No relabelling, common suspension, reversal, complement, or cross-side use
of one copy of `P` is a legal exchange with the two guaranteed diagonal
bases held fixed.  More generally, if `(A,B)` is any strict physical
alternating circuit on the same `2t` ports, then

\[
                 \deg_{S-A+B}(v)=\deg_S(v)             \tag{2.4}
\]

for every physical owner `v`.  Hence such a circuit cannot reduce any
undirected degree overload.

#### Proof

Equations (2.2)--(2.3) and the repeated old lower label prove the first
claim.  The two tagged diagonal palettes form a direct sum, so flux on one
side cannot cancel flux on the other.  For (2.4), every circuit port is
incident with exactly one old and one new edge; every other owner is
incident with neither.  \(\square\)

Thus automatic `Q` removes no part of this obstruction.  It only guarantees
that some bases exist before physical representatives are chosen.

## 3. Exact cycle-rank descent theorem

All graphs below use one fixed spanning owner set, so isolated owners count
in the component number.  Let `S` be the complete edge-labelled physical
support, including both punctured sides, the central bank and fixed seams.
Let `A subseteq E(S)`, let `B` be a disjoint replacement set with
`|A|=|B|=t`, and put

\[
                         T=S-A,\qquad S'=T+B.          \tag{3.1}
\]

For an edge set `E`, define its relative graphic rank

\[
             \rho_T(E)=\kappa(T)-\kappa(T+E).          \tag{3.2}
\]

Equivalently, contract every component of `T` and take the graphic rank of
the resulting multigraph, retaining loops and parallel edges.

### Theorem 3.1 (rank transfer)

Put `s=rho_T(A)` and `r=rho_T(B)`.  Then

\[
 \beta(S)=\beta(T)+t-s,\qquad
 \beta(S')=\beta(T)+t-r,                              \tag{3.3}
\]

and hence

\[
 \boxed{\beta(S')-\beta(S)=s-r.}                      \tag{3.4}
\]

Consequently the exchange strictly lowers cycle rank iff `r>s`, and the
exact drop is `r-s`.

#### Proof

Adding `E` to `T` adds `|E|` edges and lowers the component count by
`rho_T(E)`.  The identity

\[
 \beta(T+E)=|E(T)|+|E|-|V|+\kappa(T)-\rho_T(E)
             =\beta(T)+|E|-\rho_T(E)
\]

gives (3.3)--(3.4).  \(\square\)

### Corollary 3.2 (strict physical-circuit bound)

If `A union B` is one strict physical alternating `C_(2t)` on `2t`
distinct ports, then one exchange lowers cycle rank by at most `t-1`.
Thus a physical `C6` has maximum drop two and a physical `C8` maximum drop
three.

#### Proof

If `s>=1`, then `r-s<=t-s<=t-1`.  If `s=0`, the endpoints of every old
edge already lie in one `T`-component.  Contracting those `t` old pairs
turns the new matching into a quotient of a `t`-cycle, on at most `t`
vertices, so its graphic rank is at most `t-1`.  Hence again `r-s<=t-1`.
\(\square\)

This bound is sharper than the generic equal-size bound `t` because the two
halves use the same physical ports.

### Corollary 3.3 (pseudoforest form)

Assume `S` has maximum degree at most two, and let `q` be the number of
cyclic components of `S` met by `A`.  Then

\[
                     s=t-q,\qquad
 \beta(S')-\beta(S)=t-q-r.                            \tag{3.5}
\]

If the new edges are independent after contracting `T`, so `r=t`, the
packet removes exactly those `q` cycles.  It finishes a forest precisely
when `A` meets every old cyclic component and `r=t`.

#### Proof

In a path component every deleted edge is a bridge.  In a cyclic component
the first deleted edge kills its unique cycle without increasing the
component count; every further deleted edge is then a bridge.  Summing gives
`s=t-q`, and Theorem 3.1 gives (3.5).  \(\square\)

The case `q=t` cannot finish under a strict physical `C_(2t)`: Corollary
3.2 forces recreation of at least one cycle.

## 4. Degree, forest and signed endpoint rows

For a general equal-size exchange put

\[
 d_v=\deg_S(v),\qquad a_v=\deg_A(v),\qquad b_v=\deg_B(v).
\]

Then

\[
             \deg_{S'}(v)=d_v-a_v+b_v.                \tag{4.1}
\]

Thus all degree collisions disappear exactly when

\[
                     d_v-a_v+b_v\le2\quad(v\in V).  \tag{4.2}
\]

For a strict physical circuit, (4.1) equals `d_v` identically, so (4.2)
can only preserve an already valid degree ledger.

### Theorem 4.1 (complete supplied-packet gate)

The terminal support `S'` is a linear forest iff:

1. `T` is a linear forest;
2. (4.2) holds at every owner; and
3. the multigraph formed by `B` after contracting the components of `T` is
   loopless and acyclic, with a parallel pair counted as a 2-cycle.

When the packet is a fixed-basis palette-neutral circuit, these three
conditions are necessary and sufficient for the undirected physical row
without changing `Q` or either diagonal palette.

#### Proof

Conditions 1--2 are necessary.  A quotient loop expands through the unique
path in one `T`-component to a physical cycle, and a quotient cycle
(including a parallel pair) expands through the unique paths of its
components.  Conversely every terminal cycle contracts to such a quotient
loop or cycle.  \(\square\)

The test must use the **full** support.  Separate success on the two
punctured sides does not exclude a cycle through the central seams.

For fixed tail/head data, label the endpoint slots of each nontrivial
`T`-path by `0,1`; give a `T`-isolate two abstract slots and inject its zero,
one or two new incidences into them.  Let `x_P in F_2` reverse component
`P`; the role of slot `i` is `i xor x_P`, with `0=tail` and `1=head`.
A freely orientable new edge joining slot `i` of `P` to slot `j` of `Q` is
legal exactly when

\[
                  x_P\mathbin\oplus x_Q=1\oplus i\oplus j. \tag{4.3}
\]

A prescribed arrow `P -> Q` instead imposes the two unary conditions

\[
                  i\oplus x_P=1,\qquad j\oplus x_Q=0. \tag{4.4}
\]

Internal preoriented edges of a residual path must first agree with one of
its two coherent orientations.  Since the successful quotient is a forest,
the unpinned system is always soluble.  If two components on one quotient
path have pins `x_P=pi_P,x_Q=pi_Q`, compatibility is exactly

\[
 \pi_P\oplus\pi_Q
   =\bigoplus_{e\text{ on the }P\text{-}Q\text{ path}}
      (1\oplus i_e\oplus j_e),                         \tag{4.5}
\]

existentially over the isolate slot choices.  Every required exposed seam
socket must occupy an unconsumed endpoint slot.

## 5. Exact compensation of the asymmetric packet

The lower flux (2.2) identifies the ordered pair `(a,r)`.  Inside the
ordered canonical family `P(a,b,r,c,d)`, demanding the opposite upper flux
then successively forces

\[
                         P^*=P(r,c,a,b,d).              \tag{5.1}
\]

Indeed the signed triple containing both `a,r` forces `c'=b`, the other
signed terms force `b'=c`, and then `d'=d`.  This is literal uniqueness only
inside the forward ordered canonical family.  Ambient relabelling and common
suspension transport the statement.  Simultaneous reversal and dual
complement describe the resulting actuator orbit, but leave that forward
family.

Neither `P` nor `P^*` is a legal sequential fixed-basis move.  In their
simultaneous signed composition, however, two physical edges cancel
crosswise and the net packet is

\[
\begin{aligned}
A_8={}&\{rd-rc,\ cd-ac,\ ad-ab,\ bd-br\},\\
B_8={}&\{br-rd,\ rc-cd,\ ac-ad,\ ab-bd\}.              \tag{5.2}
\end{aligned}
\]

Its union is the simple physical cycle

\[
             rd-rc-cd-ac-ad-ab-bd-br-rd.              \tag{5.3}
\]

Both halves have lower palette `{r,c,a,b}` and upper palette
`{rcd,acd,abd,bdr}`.  Thus (5.2) preserves the fixed diagonal banks
literally.  It is exactly the common-exterior-star `C8` from
`MATH_THEOREM_R_PROTECTED_C8_SPLICE_AND_K17_FOUR_INCIDENCE_FLOOR_20260731.md`,
now derived as the canonical flux compensation of the minimum asymmetric
packet.

There is one further nontrivial strict-`C6` opposite-flux mate on the same
five active coordinates:

\[
\begin{aligned}
A^*={}&\{ar-ac,\ br-bd,\ bc-cd\},\\
B^*={}&\{ar-br,\ ac-cd,\ bc-bd\}.                     \tag{5.4}
\end{aligned}
\]

After cross-cancellation with `P`, it leaves the palette-neutral physical
`C6`

\[
\begin{aligned}
A_6={}&\{rd-rc,\ bc-cd,\ bd-br\},\\
B_6={}&\{br-rd,\ rc-cd,\ bc-bd\}.                     \tag{5.5}
\end{aligned}
\]

The two palettes in (5.5) are `{r,c,b}` and `{rcd,bcd,bdr}`.  This is one
of the two nearest zero-flux `C6` replacements from the prior local
catalogue.

### Theorem 5.1 (complete five-coordinate opposite-flux classification)

For the fixed labelled packet `P` in `J(5,2)`, exactly three oriented strict
physical `C6` packets have flux `-Phi(P)`:

1. the reverse of `P`, giving trivial cancellation;
2. (5.4), reducing to the fixed-basis `C6` (5.5); and
3. the canonical mate (5.1), reducing to the fixed-basis `C8` (5.2).

The statement is complete in this ten-owner local fibre.  Common suspension
preserves it, but it does not classify arbitrary larger-support compound
packets.

#### Finite proof

Enumerate the ten rank-two owners on the five active coordinates.  For each
six-owner subset, enumerate its Johnson perfect matchings and retain ordered
disjoint pairs whose union is one alternating `C6`.  Comparing the two exact
signed palette counters with `-Phi(P)` leaves precisely the three rows
above.  An independent replay instead enumerates cyclic walks of six
distinct owners.  Both constructions give the same three reduced sizes
`0,3,4`.

### Corollary 5.2 (exact topological capacities)

The compensated `C6` (5.5) is pointwise degree-invariant and has maximum
cycle-rank drop two.  The canonical compensated `C8` (5.2) is pointwise
degree-invariant and has maximum drop three.  These bounds are sharp at the
contraction level: if internally disjoint residual paths join the endpoints
of any nonempty proper subset of the old matching edges, and no other packet
ports share a residual component, then the old graph has one cycle per such
path while the new graph is a forest.  Contracting all old pairs leaves one
new cycle, giving profiles

```text
C6: q=0,1,2,3  gives (old beta,new beta)=(0,0),(1,0),(2,0),(3,1);
C8: q=0,...,4 gives (0,0),(1,0),(2,0),(3,0),(4,1).
```

These are graph/contraction sharpness witnesses.  They are not asserted to
be complete five-sector collar fixtures: a residual path using repeated
side colours need not itself lie in a saturating diagonal matching.

Exactly `2/8` frozen old-edge role assignments extend across (5.5), and
`2/16` extend across (5.2), before any additional pins.  They are the two
alternating bipartitions of the reduced physical circuit with freely
orientable inserted edges.  They neither prove sequential legality of the
invalid constituent `C6`s nor override extra pins.  The actual inherited
ledger is still (4.3)--(4.5).

## 6. Two-side packet theorem

Let a palette-neutral packet be chosen independently on each edited side;
cross-side flux cannot cancel.  Add the signed edge changes of every
constituent.  Require every resulting coefficient to lie in `{-1,0,1}`;
let `A` be the coefficient-`-1` edges and `B` the coefficient-`+1` edges.
Assume

\[
 |A|=|B|,\qquad A\cap B=\varnothing,\qquad A\subseteq E(S),\qquad
 B\cap E(S-A)=\varnothing,                              \tag{6.1}
\]

and form the single global residual graph `T=S-A`.  Same-sign multiplicity
two is not silently collapsed to a set edge: it lies outside this reduced
compound theorem.  This is a direct net exchange, not a claim that its
invalid constituent packets can be applied sequentially with fixed arrows.

### Theorem 6.1 (fixed-basis cycle-breaking packet)

The compound preserves the automatic common basis and both diagonal
palettes.  It strictly lowers global cycle rank iff

\[
                         \rho_T(B)>\rho_T(A).          \tag{6.2}
\]

It completes the physical row iff Theorem 4.1 and the signed system
(4.3)--(4.4) hold on the full support.  For physical `C6/C8` constituents,
the degree vector is unchanged, so the theorem can repair cycles only; any
degree collision must be removed by a different representative-changing
packet whose old and new physical port multisets differ.

#### Proof

Palette preservation is sidewise and literal.  Theorem 3.1 proves (6.2),
Theorem 4.1 proves the undirected finish, and (4.3)--(4.4) are the exact
orientation conditions.  Pointwise degree invariance follows from Theorem
2.1 and survives disjoint union and cross-cancellation.  \(\square\)

## 7. Finite audit and exact boundary

At ambient `m=3`, the `a=1` collar has negative retained-deep count and is
already scalar-impossible.  At `m=4`, the desuspended packets (5.2),(5.5)
are literal rank-two Johnson circuits with exact palette equality.  Common
suspension checks the same ledgers at `m=5,6`; complement gives the dual
side.  The audit also verifies the three opposite-flux rows, pointwise
degree invariance, the `2/8` and `2/16` role counts, and every contraction
profile in Corollary 5.2.

What is now closed:

* common-basis `Q` and ordinary diagonal Hall are not actuator debts;
* one literal asymmetric `C6` cannot preserve a fixed diagonal basis;
* no strict physical `C6/C8` can repair a degree collision;
* cycle descent and a linear-forest finish have the exact graphic-rank,
  capacity and signed-parity tests above; and
* among strict six-port compensators in the complete five-active-coordinate
  fibre, the two nontrivial two-copy reductions are exactly the zero-flux
  `C6` and canonical zero-flux `C8` described above.

What remains open:

* selecting diagonal representatives that contain one of the required old
  circuit halves;
* proving their global contraction rank beats their cut rank;
* satisfying inherited endpoint pins simultaneously on both sides; and
* repairing degree collisions, which necessarily requires a packet that
  changes the physical port multiset.

No all-`n` side-forest theorem, residence theorem, deep-shadow theorem,
compiler theorem, or `nu=B` conclusion is claimed.

## 8. Reproducible audits

Primary symbolic/set audit:

* `scratch/audit_ad_a1_fixed_basis_c6_c8_descent_20260731.py`,
  SHA-256 `f8777088c2b10051bf1faa571dae00fcf1e7848ea0270e918f57d7c7c10f7081`;
* `scratch/ad_a1_fixed_basis_c6_c8_descent_20260731.audit.json`,
  SHA-256 `243f5c4848e9aa94c04b7f1cb6e131c44f35e752201abacff81c780f0d322767`,
  payload `7722d0d8a83123bcf3de9bba5c2652eface5faca90ab8fd5db145c594b38f0c8`.

Independent bitmask/cyclic-walk replay:

* `scratch/verify_ad_a1_fixed_basis_c6_c8_descent_20260731.py`,
  SHA-256 `cfa50564b530ba7553534acb3a9d1ed3c49de211d23001a261dc663f2f11daa5`;
* `scratch/ad_a1_fixed_basis_c6_c8_descent_20260731.independent.audit.json`,
  SHA-256 `ac65e67ebde3ffa1aefb425963a4500ac5795d0d907efea1432d1efa8a646485`,
  payload `adebc2e18f2597ba75ac5da919b27182e43b0b973808c0afb72f6a624e6eb7c9`.

The primary audit enumerates Johnson perfect-matching pairs; the independent
audit enumerates cyclic six-owner walks.  Both recover three opposite-flux
mates, reduced sizes `0,3,4`, role counts `2/8,2/16`, and the complete
contraction profiles in Corollary 5.2.  Neither performs a global factor
search.
