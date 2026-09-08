# The exact three-primary spiral-braid anatomy of the K16 optimum

Date: 2026-07-31  
Status: proved finite anatomy and general spiral-braid lemma; no all-dimension
existence claim

## 1. Result and scope

Put

\[
 \Omega=\mathbb Z_{15}\sqcup\{\infty\},\qquad
 R(x)=x+1\quad(x\in\mathbb Z_{15}),\qquad R(\infty)=\infty,
\]

and let

\[
 H=\langle R^3\rangle\cong\mathbb Z_5.
\]

The authenticated K16 target carrier

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

has an exact structure which was not visible in the construction
certificate:

> It is the concatenation of four **strict, co-oriented
> \(\mathbb Z_{15}\)-spirals**.  Their base lengths are
> \(426,426,3,3\), their common sheet voltage is \(+4\), and every one of
> the four blocks contains all three residual \(\mathbb Z_{15}/H\)-sectors.
> Opening the four spiral cycles and inserting three Johnson connectors
> gives the rank-eight Hamilton path used by the optimum.

This is stronger than saying that the vertex deck is (H)-invariant.  It
also identifies precisely where symmetry stops:

* the **carrier vertices and four spiral cycles** have full
  \(\mathbb Z_{15}\) structure;
* the **braided edge set and outer palettes** break that symmetry in four
  selected representatives; and
* the **common-cap compiler word** is not even (H)-invariant as a
  multiset.

Thus the K16 optimum is evidence for a sector-braid construction, but not
for an equivariant compiler.

## 2. General strict-spiral braid lemma

Let (R) generate a free action of (mathbb Z_q) on a vertex family.  Let

\[
 P=(p_0,\ldots,p_{n-1})
\]

contain one representative from each of (n) selected (R)-orbits, and
let (gcd(a,q)=1).  Define

\[
 \operatorname{Sp}(P,a)
 =P\Vert R^aP\Vert R^{2a}P\Vert\cdots\Vert R^{(q-1)a}P.       \tag{2.1}
\]

### Lemma 2.1 (spiral, residual sectors and braid)

1. The cyclic edge set of (operatorname{Sp}(P,a)) is
   (mathbb Z_q)-invariant.
2. Suppose (q=sh) and (H=\langle R^s\rangle\cong\mathbb Z_h).  The
   sheets split into exactly (s) residual sectors.  In a gauge based at
   (P), sector (c) consists of the sheets satisfying
   (aj\equiv c\pmod s).  Each sector contains (h n) vertices.
3. If (t) such cyclic blocks are opened at one edge each and their ends
   are joined in cyclic order, the new edge set is obtained by deleting
   exactly the (t) closure edges and inserting exactly (t) connector
   edges.  Omitting the last connector gives a path with (t-1) internal
   seams.
4. Reversing a cyclic block about a chosen anchor changes its voltage from
   (a) to (-a), preserves its undirected cyclic edge set, and changes
   only the connector choices in a braid.

#### Proof

Rotation by (R^a) sends every within-sheet edge to the corresponding edge
in the next sheet and sends each sheet boundary to the next sheet boundary.
Since (a) generates (mathbb Z_q), the closed edge set is invariant under
(R).  The (H)-orbit of a sheet has phase differences in
(s\mathbb Z_q), so its residual phase (aj\pmod s) is constant; every
residual value occurs and has (h) sheets.  The braid statement is the
literal comparison of the old closures
((\operatorname{end}P_i,\operatorname{start}P_i)) with the new connectors
((\operatorname{end}P_i,\operatorname{start}P_{i+1})).  Reversal changes
the order of the sheet exponents and therefore replaces (a) by (-a),
without changing the undirected edges of the closed block. \(\square\)

The lemma is an identity, not an existence theorem: it does not supply
palette-safe connectors or a compiler.

## 3. The four K16 spiral blocks

Write (z=\infty), call a rank-eight set (A)-type when it avoids (z)
and (B)-type when it contains (z).  The endpoint-rerooted carrier has
the exact block decomposition

| block | positions, half-open | vertices | base length | full \(\mathbb Z_{15}\)-orbits | (H)-orbits |
|---|---:|---:|---:|---:|---:|
| (B_{\rm large}) | `[0,6390)` | 6390 | 426 | 426 | 1278 |
| (A_{\rm large}) | `[6390,12780)` | 6390 | 426 | 426 | 1278 |
| (A_{\rm small}) | `[12780,12825)` | 45 | 3 | 3 | 9 |
| (B_{\rm small}) | `[12825,12870)` | 45 | 3 | 3 | 9 |

For each row of this table, if (P) is its first base-length subsequence,
then the block is literally

\[
              P\Vert R^4P\Vert R^8P\Vert\cdots\Vert R^{56}P.   \tag{3.1}
\]

Every one of the 12,870 equalities in (3.1) was replayed directly.

These four blocks are the two-rail lift of the authenticated K15 parent's
two components.  The parent component lengths are (6390=15\cdot426) and
(45=15\cdot3); each appears once on the (A)-rail and once on the
(B)-rail.  Thus a parent factor with (c=2) components becomes (2c=4)
strict spiral blocks before the even braid.

The natural pre-reroot chronology has voltage signs

\[
                        (-4,+4,+4,-4).                         \tag{3.2}
\]

The two endpoint reversals co-orient the two (B)-blocks, producing

\[
                        (+4,+4,+4,+4).                         \tag{3.3}
\]

This gives an exact interpretation of the reroot: it is an anchored
orientation choice on two strict spiral cycles, not an unstructured global
rethread.

## 4. Where the three primary sectors are

Because (4\equiv1\pmod3), the three residual sectors in each block are
the sheets

\[
\begin{aligned}
 \mathcal S_0&:\quad 0,3,6,9,12,\\
 \mathcal S_1&:\quad 1,4,7,10,13,\\
 \mathcal S_2&:\quad 2,5,8,11,14.
\end{aligned}                                                \tag{4.1}
\]

Rotation (R^3) sends sheet (j) to sheet (j+12), since

\[
                         4\cdot12\equiv3\pmod{15}.             \tag{4.2}
\]

It therefore stays inside one row of (4.1) and cycles through its five
sheets.  Each sector has

\[
              5(426+426+3+3)=4290                           \tag{4.3}
\]

carrier vertices.

The three sectors are **not three independent physical blocks**.  Every
one of the four blocks in Section 3 contains all three sectors, and their
sheet order is (0,1,2,0,1,2,\ldots).  This agrees with the qualification
in the three-primary theorem: an (s)-sector braid is a symmetry-breaking
construction on the residual action, not a partition into (s) unrelated
packets.

## 5. Opening and braiding the four cycles

Close each of the four blocks in Section 3 separately.  The resulting
four-cycle factor has 12,870 edges and is exactly
(mathbb Z_{15})-invariant.  The target chronology opens all four cycles
and inserts the following connectors:

| from | deleted closure | inserted connector | connector type | used in linear carrier? |
|---|---|---|---|---|
| (B_{\rm large}) | `c3ca--c3cc` | `c3cc--43ce` | Johnson | yes |
| (A_{\rm large}) | `43ce--53cc` | `53cc--33cc` | Johnson | yes |
| (A_{\rm small}) | `33cc--738c` | `738c--b38c` | Johnson | yes |
| (B_{\rm small}) | `b38c--f30c` | `f30c--c3ca` | symmetric difference 6 | no |

Consequently the first three connectors produce one Hamilton **path** in
(J(16,8)).  The cyclic wrap is not a Johnson edge and is not used by the
word compiler.

If the wrap is nevertheless included only to audit orbit support, the
cyclic edge set has exact orbit occupancies

\[
 \begin{array}{c|ccc}
 \text{group}&\text{full orbits}&\text{deficient orbits}&\text{singletons}\\ \hline
 \mathbb Z_{15}&854\text{ of size }15&4\text{ of size }14&4\text{ of size }1\\
 H=\mathbb Z_5&2570\text{ of size }5&4\text{ of size }4&4\text{ of size }1.
 \end{array}                                                \tag{5.1}
\]

Exactly 12,862 of its 12,870 edges are carried to another selected edge by
the generator (R^3).  Thus the carrier is an invariant four-cycle factor
plus four literal phase defects, rather than an invariant final cycle.

## 6. Outer palettes and the short-orbit test

The full rotation orbit census is

\[
\begin{array}{c|cc|c}
\text{rank}&\text{orbits of length }15&\text{orbits of length }5&H\text{-orbits}\\ \hline
7&762&2&2288\\
8&858&0&2574\\
9&762&2&2288.
\end{array}                                                \tag{6.1}
\]

The endpoint-rerooted linear path covers both adjacent palettes completely:

\[
\begin{array}{c|c}
\text{rank-seven intersections}&1^{10066}2^{1319}3^{55},\\
\text{rank-nine unions}&1^{10111}2^{1229}3^{100}.
\end{array}                                                \tag{6.2}
\]

The natural chronology already covers every rank-seven colour but misses
the two rank-nine colours

```text
0xb3cc  0xd3cc.
```

The reroot changes only two linear edges in each direction:

| operation | edge | lower | upper |
|---|---|---|---|
| remove | `b38c--f30c` | `b30c` | `f38c` |
| remove | `c3ca--c3cc` | `c3c8` | `c3ce` |
| add | `b1cc--b38c` | `b18c` | `b3cc` |
| add | `c3cc--d38c` | `c38c` | `d3cc` |

This fills both upper holes while retaining all lower colours.

A tempting interpretation is false: the four deficient edge orbits do not
service the four shortened outer-colour orbits one-for-one.  Of all eight
changed lower/upper colours in the table, only `0xb18c` belongs to a short
(mathbb Z_{15})-orbit; none of the changed upper colours does.  In fact,
after rerooting both short rank-seven orbits and both short rank-nine orbits
have constant load three on all five members.  The upper completion itself
is a repair inside long colour orbits.

The three-primary obstruction therefore predicts the need for residual
symmetry breaking, but it does not prescribe one connector for each short
orbit.

## 7. The compiler is not equivariant

The final word

```text
answers/k16.word
SHA-256 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

uses starts (P_i=i) and the sorted deadline set

\[
          \{0,\ldots,12872\}\setminus\{0,1,6388\}.           \tag{7.1}
\]

Thus 6,386 middle rows have depth two and 6,484 have depth three.  Their
literal ORs reproduce the spiral carrier exactly.  Position 6389 is pinned
to `0x8000`.

Let (ho_H) be the position permutation induced by (R^3) on the four
spirals.  Then

\[
 \#\{i:T_{\rho_H(i)}=R^3T_i\}=12870.                         \tag{7.2}
\]

The maximal pinned envelope is still nearly equivariant:

\[
 \#\{i:E_{\rho_H(i)}=R^3E_i\}=12852.                         \tag{7.3}
\]

But the decoded common-cap word satisfies only

\[
 \#\{i:A_{\rho_H(i)}=R^3A_i\}=6535,                         \tag{7.4}
\]

among the 12,870 acted-on positions.  Moreover its letter multiset differs
from its (R^3)-rotation by (L^1)-distance 3,148.  It is therefore not
(H)-invariant even after forgetting chronology.

This is the important separation:

> K16 uses symmetry to construct and organize the carrier, but the integral
> lower compiler spends that symmetry.  Requiring an equivariant common-cap
> matching would exclude the known optimum.

## 8. K10 contrast

Three independently retained K10 carriers were replayed:

```text
scratch/even_two_rail_joint_order_k10_20260730.PASS.json
scratch/even_two_rail_joint_deep_k10_20260730.PASS.json
scratch/even_two_rail_q3pattern_k10_20260730.PASS.json
```

Each cyclic carrier has 252 edges forming exactly 28 complete
(mathbb Z_9)-edge orbits.  This does not contradict the three-primary
short-orbit obstruction: those carriers are not fully invariant **exact
directed-repair transversals**.  The necessary symmetry breaking can occur
at the distinguished cut or in the compiler.  K16 exhibits both
possibilities simultaneously: an almost-invariant carrier edge set and a
strongly asymmetric compiler.

## 9. Generalizable construction rule

The finite certificate supports the following carefully scoped rule.

### Co-oriented spiral-braid rule

1. Build a small number of closed strict spirals at the maximal clean
   subgroup scale.
2. Use anchored reversal to choose a common voltage sign for the blocks.
3. Choose phases and openings so that (t-1) cross-block connectors are
   physical Johnson edges and preserve the required outer palettes.
4. Keep the resulting object linear if the final wrap is not physical.
5. Solve the lower compiler after the braid, without imposing equivariance
   on its integral matching.

At K16 the rule is exact with (t=4), common voltage (4), three physical
connectors, and depth three.  What is **not** proved is that a bounded number
of suitable spirals or palette-safe connectors exists in every dimension.
Those are the genuine recursive gates.

Conditionally, the component count propagates cleanly: an odd parent made
of (c) strict cyclic components yields (2c) (A/B)-rail blocks, so a
linear even child asks for (2c-1) physical connectors.  For the
authenticated parent (c=2), this predicts exactly the three seams that
occur.  This conditional count is an identity; it does not prove that the
required connectors preserve the palettes.

The main reusable gain is conceptual and algorithmic: instead of searching
all chronologies, search orientations, phases and connectors of strict
spiral blocks, then hand the fixed chronology to the common-cap compiler.
The K16 optimum proves that this restricted search space can contain an
exact answer even when full residual equivariance is arithmetically
impossible.

## 10. Reproducer and frozen hashes

The solver-free replay is

```text
scratch/audit_k16_three_primary_spiral_braid_anatomy_20260731.py
SHA-256 4966e10fae8fc959597f905092cdded959837c1d09b67465a4f80e0da398102f
```

and its output is

```text
scratch/k16_three_primary_spiral_braid_anatomy_20260731.audit.json
SHA-256 3eac8320442d39fcacf4d0f54c762b83f682bfcbf6e04a20855297f60da78546
payload SHA-256 b072e033234c8ca6107298d074529f3f1e94e8abb7ede8944aed4d3858f013b6
```

The replay authenticates the optimum, the natural and rerooted carriers,
the three-primary theorem, and all three K10 contrast artifacts; checks all
65,535 masks directly; and runs no search or SAT solver.
