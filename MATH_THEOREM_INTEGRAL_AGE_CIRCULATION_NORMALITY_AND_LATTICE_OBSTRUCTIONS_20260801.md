# Integral age circulation: the TU face, a first-moment lattice, and a saturated marked hole

Date: 2026-08-01  
Status: unconditional first-moment identity, fixed-multiplicity TU
reduction, and a saturated marked-age semigroup hole.  The separate
owner-colour modular obstruction is reconciled with the stronger existing
coloured-Euler theorem.  These results do not refute the special triangular
Boolean profile and do not change the certified bounds on `nu(k)`.

## 0. Verdict

The stationary pull-clock theorem proves a rational marked circulation.  It
cannot be rounded by a generic network-flow or denominator-clearing theorem.
There are two distinct integral layers.

1. Even before owner names are imposed, the projection from integral age
   circulations to `(number of occurrences, marked-rank histogram)` has
   holes.  A minimal-depth **saturated single-rotation-face** hole occurs at

   \[
                       (r,d,W)=(7,3,2).
   \]

   The required histogram is one occurrence of every rank `1,...,6`.  It
   has a connected rational realization, but no integral stationary age
   circulation of two occurrences.
2. After owner names are imposed, the existing coloured-Euler theorem gives
   the complete Smith/modular-potential obstruction and literal linear-cost
   examples.  The age-semigroup hole below occurs strictly before that
   owner-colour layer.

There is also a positive exact statement.  Once the **integer multiplicity
of every age type** has been fixed, legal successor counts form an ordinary
bipartite transportation polytope and hence round integrally.  Rank-only
marks then round independently.  Thus the missing integrality is precisely
the correlated selection of the integer type multiset and the owner/target
colours, not the later successor flow on a fixed multiset.

## 1. Fixed integer type multiplicities are a TU face

Let

\[
 \mathcal C_{r,d}=\{c=(c_0,\ldots,c_d):c_0>0, c_i\ge0,
                                      \sum_i c_i=r\},
\]

and write `c -> c'` when

\[
                         c'_{i+1}\le c_i\qquad(0\le i<d).       \tag{1.1}
\]

Fix nonnegative integer multiplicities `m_c`.  A successor table is a
nonnegative matrix `f_(c,c')`, supported on (1.1), satisfying

\[
             \sum_{c'}f_{c,c'}=m_c,
             \qquad
             \sum_c f_{c,c'}=m_{c'}.                            \tag{1.2}
\]

### Theorem 1.1 (fixed-multiplicity TU theorem)

For integral `m`, (1.2) has an integral solution if and only if it has a
fractional solution.  Equivalently, it is feasible exactly when

\[
             \sum_{c\in X}m_c\le \sum_{c'\in N(X)}m_{c'}
             \qquad(X\subseteq\mathcal C_{r,d}).                \tag{1.3}
\]

Moreover, if `n_s` is an integer marked-rank demand and

\[
 n_s\le \sum_{c:s\in R(c)}m_c,
 \qquad
 R(c)=\{c_0+\cdots+c_{j-1}:1\le j\le d,\ c_0+\cdots+c_{j-1}<r\}, \tag{1.4}
\]

then the marks can be assigned integrally to the selected type occurrences.

#### Proof

Make a bipartite graph with a left and a right copy of every age type and
put the legal transitions between them.  Equations (1.2) are the
transportation problem with vertex demands `m`.  Its constraint matrix is
the bipartite vertex-edge incidence matrix, hence is totally unimodular.
Hall's capacitated theorem gives (1.3), and integral max flow gives an
integral table.

For (1.4), fix a rank `s` and choose any `n_s` of the occurrences whose type
offers `s`.  Choices for different ranks do not compete: one trace
occurrence may mark all of its distinct available suffix ranks.  Therefore
the choices can be made independently for every `s`. `square`

The directed multigraph supplied by an integral table is Eulerian and hence
decomposes into directed cycles.  TU does not make it connected.  It also
does not choose the integer multiplicities `m_c`; that projection is where
the saturated hole below occurs.

This theorem is only at the age-type quotient.  The biregular lift from a
type transition to labelled age partitions is fractional in general and may
require multiplying the occurrence counts.  Thus Theorem 1.1 does not claim
an exact literal-state successor table at the same `m`; that is part of the
owner--flag transversal gate.

## 2. The exact first-moment/slack identity

Let `f` be any finite stationary age circulation, integral or rational, and
put

\[
 m_c=\sum_{c'}f_{c,c'}=\sum_{c'}f_{c',c},
 \qquad W=\sum_c m_c,
 \qquad M_i=\sum_c m_c c_i.                                  \tag{2.1}
\]

For an arc `c -> c'`, define its coordinate slack

\[
                         \sigma_i(c,c')=c_i-c'_{i+1}\ge0.
\]

Summing over the circulation gives

\[
 D_i:=M_i-M_{i+1}
     =\sum_{c,c'}f_{c,c'}\sigma_i(c,c')\ge0.                  \tag{2.2}
\]

For an arbitrary circulation define its full positional suffix moment

\[
 F_{\rm pos}=\sum_c m_c\sum_{j=1}^d
                   (c_0+\cdots+c_{j-1}),                       \tag{2.3a}
\]

counting repeated suffix values separately and also counting a rank-`r`
suffix when it occurs.  The identity below always holds with `F=F_pos`.

Assume every occurrence has `d` distinct proper suffix ranks and all are
marked.  Let `n_s` be their total rank histogram and put

\[
                         F=\sum_{s=1}^{r-1}s n_s=F_{\rm pos}.  \tag{2.3}
\]

### Theorem 2.1 (first-moment gradient identity)

\[
 \boxed{
  2F-rdW=\sum_{i=0}^{d-1}(i+1)(d-i)D_i.}                      \tag{2.4}
\]

In particular, `F >= rdW/2`.  Equality holds if and only if every used arc
is the forced block rotation

\[
                         c'=(c_d,c_0,c_1,\ldots,c_{d-1}).      \tag{2.5}
\]

#### Proof

The sum of the `d` suffix ranks of type `c` is

\[
 \sum_{j=1}^d(c_0+\cdots+c_{j-1})
       =\sum_{i=0}^{d-1}(d-i)c_i.
\]

Consequently

\[
                         F=\sum_{i=0}^{d-1}(d-i)M_i,
 \qquad rW=\sum_{i=0}^d M_i.                                 \tag{2.6}
\]

Write `M_i=M_d+sum_(h=i)^(d-1)D_h` in (2.6).  The coefficient of `D_h` in
`2F-rdW` is

\[
 2\sum_{i=0}^h(d-i)-d(h+1)=(h+1)(d-h),
\]

which proves (2.4).  All coefficients and all `D_i` are nonnegative.  At
equality, (2.2) says every used arc has zero slack in every row, so
`c'_(i+1)=c_i`.  Equality of total size then forces `c'_0=c_d`, proving
(2.5).  The converse is immediate. `square`

This is an exact lattice test.  In the integral case

\[
 2F-rdW\in
 \left\langle (i+1)(d-i):0\le i<d\right\rangle_{\mathbb Z_{\ge0}}. \tag{2.7}
\]

The gcd of the displayed generators is `2` for even `d` and `1` for odd
`d`; the more informative restrictions are the small gaps of this numerical
semigroup and, on the equality face, the rotation-orbit divisibilities.

There is also an **integral** component budget.  For an integral circulation
put `S=sum_i D_i`.  Since every positive-slack arc copy consumes at least one
unit of `S`, their number is at most `S`, and

\[
 S\le {2F-rdW\over d}.                                        \tag{2.8}
\]

Contract all occurrences whose types lie in the same nonempty rotation
orbit, and let `kappa` be the number of resulting type-orbit blocks.  Every
zero-slack arc stays inside one block, even though it may cross-connect
several copies within that block.  Any integral successor permutation on
those occurrences with at most `C` components therefore needs

\[
              \kappa-C\le S\le {2F-rdW\over d}.               \tag{2.9}
\]

This turns the marked first moment into an exact upper budget for
off-rotation fusion arcs.  For a nonsaturated marked system, (2.4) applies
to the full offered suffix histogram; unmarked suffixes must not be silently
discarded from `F`.

There is nevertheless a marked-only corollary.  If `n_s` is the selected
histogram, put

\[
 N=\sum_s n_s,\qquad U=dW-N,\qquad F=\sum_s s n_s.
\]

The `U` unmarked suffix positions have ranks between one and `r`.  Hence
their contribution to the full first moment is at most `rU`, and every
integral circulation obeys

\[
 \boxed{
 S\le {2F+2rU-rdW\over d}.                               \tag{2.10}
\]

In particular the right side must be nonnegative.  If its occurrence types
meet `kappa` nonempty rotation-orbit blocks, a terminal circulation with at
most `C` components requires

\[
 \kappa-C\le {2F+2rU-rdW\over d}.                         \tag{2.11}
\]

This bound can be weak when the triangular scalar slack `U` is large, but
it is a proof-safe fusion diagnostic using only the prescribed marked
histogram.

If every suffix position is proper, equivalently every used type has
\(c_d>0\), then \(rU\) in (2.10)--(2.11) sharpens to \((r-1)U\).

## 3. A first saturated marked hole

Take

\[
                         r=7,\qquad d=3,qquad W=2.             \tag{3.1}
\]

Consider the four positive compositions

\[
\begin{aligned}
 c^0&=(1,1,2,3),&R(c^0)&=\{1,2,4\},\\
 c^1&=(3,1,1,2),&R(c^1)&=\{3,4,5\},\\
 c^2&=(2,3,1,1),&R(c^2)&=\{2,5,6\},\\
 c^3&=(1,2,3,1),&R(c^3)&=\{1,3,6\}.
\end{aligned}                                                 \tag{3.2}
\]

They form the directed rotation cycle

\[
                         c^0\to c^1\to c^2\to c^3\to c^0.    \tag{3.3}
\]

This is literal, not only a type cycle.  Partition one seven-element owner
into ordered blocks of sizes `(1,1,2,3)` and cyclically rotate the four
blocks through the age classes.  At each step append the old oldest block.
All blocks are nonempty, and the four labelled age partitions form a
literal trace cycle projecting to (3.3).

Give every edge of (3.3) weight `1/2` and mark all three suffix ranks.  The
total occurrence mass is two, and every rank `1,...,6` occurs twice around
the four-cycle, hence has marked mass one.  Thus the integral right-hand
side

\[
                         (W;n_1,\ldots,n_6)=(2;1,1,1,1,1,1)   \tag{3.4}
\]

has a connected rational stationary realization.

### Theorem 3.1 (nonroundability)

There is no integral stationary age circulation with the right-hand side
(3.4), even if every age type and every legal transition in
`C_(7,3)` is allowed.

#### Proof

All six demanded marks must be supplied by the two occurrences.  Since an
occurrence offers at most three distinct proper suffix ranks, both
occurrences offer and mark all three; in particular all four age classes of
each used type are positive.

The marked first moment is

\[
                         F=1+2+3+4+5+6=21
                          ={rdW\over2}.
\]

Theorem 2.1 therefore forces every selected transition to be a block
rotation.  Every positive four-part composition of seven has rotation orbit
four: period one would make its sum divisible by four, and period two would
make its sum even.  An integral stationary circulation supported on such
orbits consequently has total occurrence mass divisible by four, contrary
to `W=2`. `square`

This is a genuine semigroup hole, not merely a failure of one chosen
support.  To see failure of normality in its standard lattice sense, use the
semigroup element given by the unmarked self-loop type `(7,0,0,0)`.
The semigroup contains `(1;0)` and, by taking
one integral copy of the four-cycle and marking only one suitable
occurrence, it contains `(4;e_s)` for every rank `s`.  Hence (3.4) belongs
to the group generated by the semigroup.  It belongs to its rational cone
by (3.3), but Theorem 3.1 says that it is not in the semigroup.  Therefore
the projected marked-age semigroup is not normal.

The normalized vector here is simply

\[
                         q_1=\cdots=q_6={1\over2},
                         \qquad\sum_s q_s=d.                   \tag{3.5}
\]

It lies on the clean monotone-rotor face.  Thus monotonicity, exact integer
rank marginals after scaling, connected fractional support, and scalar
capacity still do not imply one-copy integral chronology.

### Proposition 3.2 (minimal depth on the saturated single-rotation face)

The phenomenon in Theorem 3.1 cannot occur at `d=1` or `d=2` by scaling one
nontrivial rotation orbit to a smaller integral marked histogram.

#### Proof

For `d=1`, a nontrivial orbit is `(a,b),(b,a)` and its two marked ranks are
`a,b`.  Scaling the orbit by one half gives an integral histogram only when
`a=b`, which collapses the orbit to a self-loop.

For `d=2`, a nontrivial orbit has parts `(a,b,c)`.  Across its three phases,
the six offered ranks form the multiset

\[
                         \{a,b,c,r-a,r-b,r-c\}.                 \tag{3.6}
\]

Scaling by one third or two thirds can be integral only if every
multiplicity in (3.6) is divisible by three.  Hence (3.6) consists of two
complementary values, each three times.  If `p` of the parts equal one value
`x` and the other `3-p` equal `r-x`, the identity

\[
                         r=px+(3-p)(r-x)
\]

forces either a zero part or `a=b=c=r/3`.  The latter is the period-one
orbit.  Thus no nontrivial smaller-depth example exists. `square`

This is minimal only for the stated saturated single-rotation mechanism;
it is not a claim that every possible coloured-circulation matrix at depths
one and two is integral.

The distinction is necessary.  The aggregate role semigroup in
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`
already has the smaller unsaturated hole `(d,r,W)=(2,4,2)` with
`A_0=A_3=1`.  Theorem 3.1 adds two properties absent from that example:
all `dW` suffix slots are load-bearing, and the witnessing rational support
is one connected literal rotation cycle.  It is therefore the relevant
minimal warning for a saturated pull-clock rounding argument, not a
replacement for the earlier aggregate-semigroup theorem.

## 4. Reconciliation with the existing owner-colour lattice theorem

The owner-colour obstruction is already treated more strongly in
`MATH_THEOREM_THREAD_D_TPC_ONE_COPY_COLOURED_EULER_ROUNDING_20260801.md`.
That theorem gives the complete Smith/modular-potential certificates, a
determinant-two minor, an exact reversible-menu orientation criterion, and a
literal complete-Boolean linear route-cost family.  The star below is kept
only as a compact special-case illustration; it is not a new contribution.

The new obstruction in Section 3 is orthogonal: it occurs before owner rows
are introduced, inside the saturated marked-age projection itself.

For comparison, owner names themselves already destroy total unimodularity
in the smallest reversible menu.

Let `B` be the directed state-incidence matrix and let `O` have one row per
owner, with a one on every option of that owner.  For one owner with options
`u->v` and `v->u`, the submatrix on its owner row and the state-`u` row is

\[
                         \begin{pmatrix}1&1\\-1&1\end{pmatrix},
\]

whose determinant is two.  Thus `[O;B]` is not TU in general.

The corresponding exact lattice law has a literal realization.  Fix a set
`K` of size `r-2`, and distinct labels `0,1,...,m` outside it.  Put

\[
 X_i=K\cup\{i\},
 \qquad T_i=K\cup\{0,i\}\quad(1\le i\le m).                  \tag{4.1}
\]

For owner `T_i`, allow the two depth-one trace edges

\[
                         X_0\to X_i,qquad X_i\to X_0.         \tag{4.2}
\]

Each edge has owner `T_i`.  Giving both orientations weight `1/2` uses every
owner with mass one and is balanced at every literal state.  Its positive
support is the connected star on `X_0,...,X_m`.

### Theorem 4.1 (reversible-owner parity obstruction)

Any integral one-edge-per-owner choice in (4.2) is an orientation of the
star.  Its state divergence `b_v=out(v)-in(v)` satisfies

\[
                         b_v\equiv\deg(v)\pmod2.                \tag{4.3}
\]

In particular it cannot be balanced, and every decomposition into directed
trails needs at least `ceil(m/2)` open trails.

#### Proof

Every selected incident edge contributes either `+1` or `-1` to `b_v`, so
(4.3) follows modulo two.  Every leaf has odd degree one and hence nonzero
divergence.  A directed trail has at most two boundary endpoints.  There are
`m` leaf endpoints, and if `m` is odd the centre is also odd, giving the
lower bound `ceil(m/2)`.  Orienting half the edges each way (with the one
unpaired edge arbitrary when `m` is odd) attains this bound. `square`

More generally, for a reversible owner menu graph `G`, zero-boundary
one-copy rounding is possible only if every vertex of `G` has even degree;
with prescribed boundary `b`, the exact lattice condition includes

\[
                         b_v\equiv\deg_G(v)\pmod2.              \tag{4.4}
\]

The star family proves that weak connectedness of a rational owner-perfect
literal circulation does not imply an `O(1)`-boundary integral rounding.
It is an incomplete owner family and carries no named lower palette, so it
does not refute the complete Boolean triangular instance.  It does refute
any black-box rounding theorem which uses only owner masses, literal flow
balance, and connected fractional support.

## 5. Exact frontier for the triangular pull clock

There is an important target-specific qualification.  The conductor theorem
in
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`
already proves that the canonical binomial/Ferrers **aggregate role vector**
belongs to the integer uniform-rotor semigroup for every `k>=31`.  Therefore
Theorem 3.1 is not evidence that the actual large-`k` rank vector misses the
integer age semigroup.  Rather, it proves that this target-specific conductor
is essential: it cannot be replaced by a generic normality assertion.

Combining that conductor theorem with Theorem 1.1 closes the unlabelled
rank/type successor arithmetic for the canonical large-`k` vector.  It still
does not turn the rotor occurrences into one primitive occurrence of every
named rank-`r` owner, nor does it assign every named lower target, fuse the
literal owner fibres, or provide the upper/compiler guards.

The results above separate the integral sequel into the following rows.

1. **Choose integer age-type multiplicities.**  They must meet the marked
   rank capacities and every type-Hall cut.  Fractional membership in
   `ST_(k,r,d)` does not imply this: Theorem 3.1 is a saturated hole.
2. **Choose owner- and target-labelled trace atoms.**  Their option-difference
   lattice must contain the required literal boundary.  The existing
   coloured-Euler theorem shows that this lattice may have both parity and
   unbounded boundary debt.
3. **Round successors.**  Once the integer type occurrences are fixed, this
   row is TU by Theorem 1.1.
4. **Fuse components.**  Equation (2.9) is an exact first-moment budget for
   off-rotation fusion.  Connectivity is not supplied by TU.

For the actual triangular vector, the full complete Boolean owner and target
incidence may cancel the small semigroup and parity obstructions.  The exact
next theorem must prove that cancellation using that complete structure; it
cannot be a generic consequence of the rational pull circulation.

No upper bound on `nu(k)` follows from this note.
