# Thread D: the `k=17` complement-dual singleton splice obstruction and even-circuit gate

Date: 2026-08-01  
Status: exact theorem and independently replayed finite census for the frozen
seed `a3f9eac0...`.  Every single non-dual cross rectangle is excluded at
the incidence-geometry layer.  All singleton-supported non-dual `H` circuits
of support 4, 6, and 8 are exhaustively closed by exact palette ledgers.
Deeper upper opening, residence, type pins, and compilation are outside the
finite census.

## 0. Outcome

Let `D` be the frozen incidence perfect matching and `H=C(D)` its complement
dual.  The seed has

\[
  A=CD:\quad 1429^1,1^1,qquad
  \pi=H^{-1}D=A^2:\quad 1429^1,1^1.                \tag{0.1}
\]

The two `A`-cycle voltages are `2,13`; the two factor voltages are `4,9`.
Both immediate palettes are complete and each has exactly 286 repeat units.

The singleton is owner orbit `425`, representative `0x01e1f`.  Its selected
incidences are

\[
 D_*=(3825,\ {m facet} 295,\ {m shift} 1),\qquad
 H_*=(3829,\ {m facet} 295,\ {m shift} 9).      \tag{0.2}
\]

The two owner sets needed for a cross rectangle are

\[
\begin{aligned}
 I&=\{130,131,135,145,426,430,440\},\\
 O&=\{251,314,369,390,395,442,470\}.                 \tag{0.3}
\end{aligned}
\]

They are disjoint.  Hence all 1,429 possible cross-component edge pairs
fail before voltage or palette tests.  Two independent catalogue programs
both return exactly zero geometric rectangles.

The next single matching move must have even assignment-cycle length.
Support two is (0.3), so support four is minimal.  The exhaustive results
are

| support | geometric cycles | Hamilton factors | both-palette survivors |
|---:|---:|---:|---:|
| 4 | 5 | 1 | 0 |
| 6 | 134 | 38 | 0 |
| 8 | 4,473 | 1,168 | 0 |

The unique Hamilton support-four switch has voltage 14 but creates three
rank-ten and four rank-seven holes.  Thus the smallest topology actuator is
real but not palette-safe.

## 1. Exact single-rectangle theorem

Let a spanning incidence factor be written as the disjoint union of perfect
matchings `D` and `H`, and suppose it has exactly two alternating quotient
cycles.  Retain `D`.  Choose old `H` edges

\[
                 e_0=(p,F),\qquad e_1=(q,G)           \tag{1.1}
\]

from different factor components.

### Theorem 1.1 (iff cross rectangle)

There is a connected factor differing from `H` in exactly these two
matching rows if and only if both crossed incidences

\[
                       e'_0=(p,G),\qquad e'_1=(q,F)   \tag{1.2}
\]

exist, are distinct from the corresponding `D` edges, have nonzero joined
voltage, and satisfy the two exact palette ledgers below.

#### Proof

After deleting (1.1), perfectness leaves two unmatched owners and two
unmatched facets.  The old pairing restores `H`; the crossed pairing (1.2)
is the only other perfect matching.  Cutting one edge in each old component
and crossing the endpoints joins the two paths into one cycle.  Conversely,
edges from the same component split rather than join, so different
components are necessary.  The remaining conditions are exactly
edge-disjointness, primitive lift, and palette survival.  \(\square\)

If `s(e)` is the stored incidence shift and the old component voltages sum
to `V_0`, then

\[
 V'=V_0+s(e_0)+s(e_1)-s(e'_0)-s(e'_1)\pmod {17}.     \tag{1.3}
\]

The physical lift is one cycle exactly when `V'!=0`.

Only the turns at facets `F,G` and owners `p,q` change.  For shore
`r in {7,10}`, target `T`, old load `mu_r(T)`, and local loss/gain counts,
the necessary and sufficient palette row is

\[
          \mu_r(T)-\operatorname{loss}_r(T)
                   +\operatorname{gain}_r(T)\ge1.    \tag{1.4}
\]

Because the new factor is no longer complement dual, both shores must be
checked.  Baseline complementarity reduces the four deleted tickets to one
upper-labelled ledger, but it does not identify the four new tickets.

Thus (1.2)--(1.4), together with opposite old components, are the exact
necessary and sufficient algebra requested for a one-rectangle splice.

## 2. The seed-specific incidence cut

Let `s=425` be the singleton owner and let `f_*=295` be its old `H` facet.
For a long-component owner `x`, write `f_x` for its old `H` facet.  A cross
rectangle using the singleton exists exactly when

\[
                       x\longrightarrow f_*,qquad
                       s\longrightarrow f_x          \tag{2.1}
\]

are both quotient incidences, including some choice among parallel gauges.

Equivalently, define the `H`-compatibility digraph `K` on owner indices by

\[
 x\to y\quad\Longleftrightarrow\quad
 \text{owner }x\text{ has a non-}D\text{ incidence to old facet }H(y).
                                                               \tag{2.2}
\]

Then a rectangle through `s` is a directed two-cycle `s<->x` in `K`.
The exact neighbourhoods are

\[
          N^-_K(s)=I,qquad N^+_K(s)=O,              \tag{2.3}
\]

with `I,O` given in (0.3).  Since `I intersect O` is empty, `K` has no
such two-cycle.  Parallel incidences do not help: the literal parallel
rectangle count is zero.

In the `A` normal form, (2.3) says that the 1,429-cycle contains no arc
whose two endpoints lie in the seven-vertex odd-graph halo of `s`.

This is a geometric obstruction, not a consequence of unique palette
providers.  It also excludes every cross-cycle two-edge switch of `D`,
because that switch has the same two crossed incidence requirements.

## 3. Why two ordinary rectangles still cannot work

Put `pi=H^{-1}D`.  Reassigning two `H` rows by a rectangle composes `pi`
with a transposition.  Since `N=1430`,

\[
             \operatorname{sgn}(\pi)=+1
             \quad(c(\pi)=2),\qquad
             \operatorname{sgn}(\pi_{\rm Ham})=-1.  \tag{3.1}
\]

Two `H` rectangles have even net sign, including overlapping rectangles,
so they cannot produce one quotient cycle.

The natural “dual preparatory `D` rectangle, then one non-dual `H`
rectangle” is also closed on this seed:

* a `D` rectangle between the two odd `A` cycles would merge them, but its
  geometry is exactly the empty cut (2.3);
* a `D` rectangle internal to the 1,429-cycle splits it into one odd and one
  even cycle, in addition to the singleton odd cycle.  Its complement-dual
  factor has `1+2+1=4` components.  One later `H` transposition changes the
  component count by only one, so it cannot reach one.

Therefore no sequence in either of these two ordinary-rectangle classes is
the requested extension.

## 4. The exact even-circuit formulation

Let

\[
                  \sigma=(x_0\ x_1\ \cdots\ x_{t-1})              \tag{4.1}
\]

be a simple directed cycle of `K`.  Replace the old `H` facet at `x_i` by
the old `H` facet at `x_{i+1}` using the literal incidence certified by the
arc of `K`.  Then

\[
                    H'=H\sigma,\qquad
                    \pi'=\sigma^{-1}\pi.             \tag{4.2}

\]

The move is matching-exact by construction.  It is connected if and only
if a literal traversal of `pi'` has one cycle.  Its voltage is

\[
 V'=V_0+\sum_i s(H(x_i))-\sum_i s(H'(x_i))\pmod {17},              \tag{4.3}
\]

and palette survival is (1.4), now with `t` changed occurrences on each
shore.

Since `sgn(sigma)=(-1)^(t-1)`, (3.1) forces `t` even.  Every switch that
absorbs the singleton must contain `s`, so fixing `x_0=s` removes cyclic
duplication.  Equations (2.2), (4.2), (4.3), and (1.4) are therefore a
complete, duplicate-free finite census for each support `t`.

### Theorem 4.1 (exact supports 4, 6, and 8)

The counts in the table of Section 0 are exhaustive.  Every Hamilton row
at these supports has nonzero voltage.  None preserves both immediate
palettes.

The unique Hamilton support-four row is

\[
 (425,369,109,426),\qquad
 (3833,3329,985,3838),                               \tag{4.4}
\]

where the second tuple lists the new `H` incidence IDs.  Its voltage is 14.
Its holes are

\[
\begin{aligned}
 \mathcal H_{10}&=\{0x01c7f,0x01f1f,0x01fa7\},\\
 \mathcal H_{7}&=\{0x0061f,0x00c1f,0x00e0f,0x00e2b\}.              \tag{4.5}
\end{aligned}
\]

The best support-six row leaves one upper and two lower holes.  At support
eight, three Hamilton rows preserve the complete upper palette, but every
row loses lower colours; the best leaves exactly

\[
                         \{0x00e0f,0x01547\}.         \tag{4.6}

\]

These are scoped single-circuit no-gos, not a compound-packet obstruction.
The next untested single `H` circuit has support ten.

## 5. Smallest still-live two-stage extension

If the final move is required to be the rectangle of Theorem 1.1, the
smallest unclosed preparation is not another rectangle.  It is a
dual-preserving three-row assignment circuit on `D`.

Let `D_1` be the result of such a circuit, `H_1=C(D_1)`, `A_1=CD_1`, and
`F_1=D_1 union H_1`.  A subsequent non-dual rectangle gives a connected
immediate-palette factor if and only if:

1. `D_1,H_1` are perfect, disjoint, and retain the protected pins;
2. `F_1` is palette-complete and has exactly two components, equivalently
   `A_1` consists of one even cycle or two odd cycles;
3. the final old `H_1` edges lie in different `F_1` components and their
   crossed incidences exist outside `D_1`;
4. the **terminal**, composed rank-seven and rank-ten loads satisfy (1.4);
5. the joined voltage

   \[
      2u(A_1)+s(pP)+s(qQ)-s(pQ)-s(qP)\ne0\pmod {17}               \tag{5.1}
   \]

   in the corresponding gauge.

If the two stages overlap in an owner or facet, their isolated palette
deltas cannot be added: the final turns must be reconstructed from
`D_1 union H_2`.  For an atomic compound packet, intermediate palette
holes are allowed; for a serialized construction they are not.

A preparatory state with more than two holes on either shore cannot be
finished by one rectangle, because the rectangle adds only two occurrences
per shore.  This gives the first exact pruning row for a future MITM.

There is a second, smaller-in-stage-count alternative: one support-four
`H` circuit.  Its unique topology row is already excluded by (4.5), so a
compound repair must either extend that row or move to support at least ten.

## 6. Reproducibility and scope

The frozen seed is

`scratch/threadD_k17_complement_dual_splice_20260801/seed.best.tsv`,  
SHA `a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3`.

K's complete rectangle postprocessor and the independently frozen direct
postprocessor both audited all 1,429 cross-component pairs and returned
zero geometric rectangles.  The small Thread-D audit independently derives
the two halo sets and the topology consequences.  The even-circuit audit is
a separate implementation of (4.1)--(4.3).

Heavy enumeration ran as one O3 C++ process on one H100 CPU under a 1 GiB
virtual-memory cap in

`/home/amodo/or15/work/threadD_k17_complement_dual_splice_20260801`.

The rectangle catalogues each used 6,144 KiB peak RSS and 0.03 s wall; the
support-4/6/8 audit used 6,144 KiB and 0.16 s wall.

Frozen artifacts:

* `scratch/threadD_k17_complement_dual_splice_20260801/primary.audit.json`;
* `scratch/threadD_k17_complement_dual_splice_20260801/independent.audit.json`;
* `scratch/threadD_k17_complement_dual_splice_20260801/obstruction.audit.json`;
* `scratch/threadD_k17_complement_dual_splice_20260801/even_switch.audit.json`;
* `scratch/threadD_k17_complement_dual_splice_20260801/even_switch.catalogue.tsv`;
* `scratch/threadD_k17_complement_dual_splice_20260801/run_manifest.json`;
* `scratch/audit_threadD_k17_complement_dual_singleton_splice_obstruction_20260801.cpp`;
* `scratch/audit_threadD_k17_complement_dual_singleton_even_switches_20260801.cpp`.

No connected factor, no deep-shadow certificate, and no `k=17` word is
claimed.  The exact next finite choices are the three-row dual preparation
plus rectangle, a compound repair of (4.4), or the support-ten single
`H` circuit.
