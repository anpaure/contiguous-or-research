# MSW owner-star lift versus all-depth exchanges: exchange circularity, star locality, and the lag-\(H\) braid obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad
 N_H=\binom{2m}{m-H},\qquad
 R_H=\binom mH,
\tag{0.1}
\]

and work at the promotion calibration

\[
 H=o(m),\qquad H^2/m=\log m+o(1),\qquad
 MN_H=(1+o(1))W.
\tag{0.2}
\]

The exact MSW owner-star theorem supplies a literal frame witness for
every incidence

\[
                       A\subset D,\qquad
 |A|=m-H,\quad |D|=m.
\tag{0.3}
\]

The audited triangle, directed-cycle, quartet, and higher-cube theorems
supply exact all-depth exchanges between *complete frame columns*.  This
report proves that these two positive statements do not compose into the
missing global braid.

The obstruction has four exact layers.

1. **Exchange circularity.**  Every audited exchange preserves the
   number of complete frame columns at each promotion root.  Literalizing
   a near-perfect clone assignment incidence by incidence through the
   MSW lift produces a formal multiset of \(W-o(W)\) complete witness
   columns, each certifying only its designated phase.  A promotion
   factor has exactly one column at each root, hence only \(N_H\)
   columns.  Their top-margin vectors lie in different exchange fibres.
   Thus the complete-frame exchanges cannot perform the grouping which
   is needed before they are applicable.

2. **Exact lag-\(H\) holonomy.**  If \(J_i\) are the proposed cyclic
   \(H\)-windows at one root, with deletion labels \(x_i\) and insertion
   labels \(y_i\), then one common frame exists exactly when

   \[
                           y_i=x_{i+H}.
   \tag{0.4}
   \]

   Equivalently, the insertion permutation is conjugate to rotation by
   \(H\) on \(\mathbb Z_M\).  Separate clone Hall does not impose this
   nonabelian condition.

3. **Packet-star locality.**  A \(d\)-pair higher cube, even with
   root-scale dimension, meets the provider star of any fixed middle
   target in at most

   \[
                              2^H=o(R_H)
   \tag{0.5}
   \]

   roots.  A complete fixed-core cycle sector meets it in at most
   \(\binom{m-H+2}{2}=O(m^2)=o(R_H)\) roots.  Hence no single exchange
   packet supplies a positive fraction of the correlation required by a
   target star.  A positive construction must correlate at least
   \(R_H/2^H\) overlapping cube packets, or \(R_H/O(m^2)\) cycle
   sectors, for a typical star.

4. **Statewise Markov obstruction.**  For every fixed maximum cube rank
   \(R\), there are two literal one-frame-at-every-root tables in the
   same complete phase-refined all-depth fibre which are isolated under
   every directed-cycle move and every coherent cube move of rank at
   most \(R\).  They differ on \(N_H-o(N_H)\) roots, and every one of
   their middle incidences has an MSW owner-star certificate.  Hitting
   all traps by complete-frame replacements exposes at least

   \[
        \left(2^{-(R+1)}-o(1)\right)MN_H
        =\left(2^{-(R+1)}-o(1)\right)W
   \tag{0.6}
   \]

   phase incidences.  Thus no fixed-rank version of the exchange library
   is a universal \(o(W)\)-repair compiler.

There is a genuine positive local theorem: inside one fixed-core
two-placeholder sector, triangle reversals connect every tournament
fibre with fixed score sequence, preserving every phase, depth, tag,
lag-\(H\) identity, top margin, and selected frame-column count.  The triangle bank
therefore solves local nonnegative connectivity **after** the flags have
already been grouped.  It does not perform the grouping.

The conclusion is not a no-go for coefficient one.  A growing-rank
library, a recyclable catalytic state, the nonneutral moving-hole seam,
or a direct integral construction of the common-core tight-path columns
remains possible.  What is rigorously closed is the proposed direct
pipeline

\[
 \text{incidencewise MSW lift}
 \quad+\quad
 \text{load-neutral complete-frame exchanges}
 \quad\Longrightarrow\quad
 \text{global lag-\(H\) braid}.
\tag{0.7}
\]

The subsequently available squarefree four- and eight-top moving-hole
exchanges sharpen this caveat: they preserve exact middle ownership but
have nonzero signed-depth action, so they genuinely escape the
load-fibre invariant.  They still replace one complete frame by one
complete frame at every touched top and therefore do not evade Theorem
2.1.  No positive-density charged packing or MSW endpoint-splice theorem
for them is presently proved.

## 1. Complete frame columns and the audited exchange library

For a promotion root

\[
                         A\in\binom V{m-H},
 \qquad U_A=V\setminus A,
\tag{1.1}
\]

a legal column consists of

1. a labelled directed cyclic order \(\pi\) on \(U_A\);
2. a retained phase set, with one deleted phase in the repaired-ring
   model; and
3. one common nested phase-to-depth tag schedule.

Let \(\mathcal E_A\) be the set of such columns and
\(\mathcal E=\bigsqcup_A\mathcal E_A\).  Define the top-row map

\[
 T:\mathbb Z^{\mathcal E}\longrightarrow
       \mathbb Z^{\binom V{m-H}},
 \qquad
 T_A(e)=\mathbf 1_{\{e\in\mathcal E_A\}}.
\tag{1.2}
\]

Let \(\mathsf A\) be the finer matrix whose rows are the top rows and
all retained phase/target/depth incidences.  Thus \(T\) is a row
projection of \(\mathsf A\).

The audited directed-cycle exchange uses tops

\[
 C\cup\{z_i,z_{i+1}\},\qquad i\in\mathbb Z_r,
\tag{1.3}
\]

and reverses the directed cycle.  The two shores use one complete
column at each of the same \(r\) tops.  The higher-cube exchange uses

\[
 U_\epsilon=C\cup
       \{a_{j,\epsilon_j}:1\le j\le d\},
 \qquad \epsilon\in\{0,1\}^d,
\tag{1.4}
\]

and the two shores use one complete column at every one of the same
\(2^d\) tops.  Their common phase and tag schedules make the identities
valid phase by phase and depth by depth.

Consequently every audited exchange vector \(z\) satisfies

\[
                         \mathsf A z=0,
 \qquad                         Tz=0.
\tag{1.5}
\]

### Proposition 1.1 (complete load-fibre invariance)

Along every sequence of these load-neutral exchanges, the complete
phase-refined all-depth vector \(\mathsf A x\) is fixed.  Consequently
every individual target multiplicity, every hole and collision set, the
collision energy \(\sum_S\binom{\mu(S)}2\), and every floor-corrected
energy obtained from it by subtracting a fixed linear baseline are fixed
at every depth.

#### Proof

Equation (1.5) fixes \(\mathsf A x\) after one move and hence after a
sequence.  Every listed statistic is a function of this vector. \(\square\)

Thus these moves can re-pair histories inside an already chosen good-load
fibre, but they cannot improve a bad fibre.  More fundamentally, the
separate clone-Hall point lies only in a projection of the frame-column
system; a kernel move cannot create a nonnegative integral preimage of a
projected point whose frame-table fibre has not yet been shown nonempty.

## 2. The exchange-circularity theorem

Let a retained clone assignment choose, at root \(A\), incidences

\[
                         (A,i,D_{A,i}),
 \qquad i\in I_A,qquad A\subset D_{A,i}.
\tag{2.1}
\]

The exact MSW owner-star lift gives a complete witness frame

\[
              \Phi_F(A,D_{A,i})
              =\pi_{x_F(D_{A,i})}|_{A^c}
\tag{2.2}
\]

for every selected incidence.  Rotate its phase origin so that the
certified target occupies phase \(i\), and form the incidencewise
literalization

\[
 x_{\rm lift}=
   \sum_A\sum_{i\in I_A}
      e\bigl(A,i,\Phi_F(A,D_{A,i})\bigr).
\tag{2.3}
\]

This is a nonnegative integral multiset of individually legal complete
witness columns.  Only the designated phase of each column carries the
asserted MSW provenance; its other phases are uncontrolled baggage.  The
multiset is not asserted to be a promotion factor or a simultaneous
all-phase selection.  That missing assembly is precisely the issue.

### Theorem 2.1 (top-margin obstruction)

For every root \(A\),

\[
                         T_Ax_{\rm lift}=|I_A|.
\tag{2.4}
\]

Every table reachable from \(x_{\rm lift}\) by triangle, directed-cycle,
quartet, or higher-cube exchanges has the same top margins.  In
contrast, a promotion factor \(y\) satisfies

\[
                         T_Ay=1
 \qquad\text{for every }A.
\tag{2.5}
\]

Hence \(y-x_{\rm lift}\) does not belong to the lattice generated by
the audited exchanges unless \(|I_A|=1\) at every root.

#### Proof

Equation (2.4) follows directly from (2.3).  Equation (1.5) makes every
coordinate of \(T\) invariant under every allowed move and therefore
under every sequence of them.  Equation (2.5) is the definition of one
selected promotion frame at every top.  The last assertion follows.
\(\square\)

For the near-perfect middle clone assignment,

\[
                         \sum_A|I_A|=W-o(W),
\tag{2.6}
\]

whereas

\[
                         \sum_AT_Ay=N_H
 =m^{-1+o(1)}W=o(W).
\tag{2.7}
\]

Thus the direct literalization contains \(W-o(W)\) formal complete
witness columns, while the desired table contains \(N_H\) columns.  If
each witness column is separately linearized, these are the corresponding
numbers of frame blocks.  Every audited exchange replaces the same number
of complete columns that it consumes.  It cannot reduce the former count
to the latter.

Identical witness columns do not invalidate the theorem.  Combining two
copies and letting different phases of one physical ring serve them is a
nonlinear *grouping* operation, not an integer-kernel exchange.  Proving
that such a combination respects the lag-\(H\) chronology is exactly the
missing interface theorem.

### Partial-column version

One may try to retain only the certified phases rather than complete
witness columns.  For a phase mask \(I\subseteq\mathbb Z_M\), let
\(c(I)\) be the number of connected components of the induced cyclic
phase subgraph, with \(c(\mathbb Z_M)=1\).  Every audited identity with
a phase restriction uses the same mask and tag schedule on both shores.
Therefore, in the marked partial-column category, it preserves

\[
                         \sum_e c(I_e).
\tag{2.8}
\]

For unchanged MSW provenance, a consecutive owner piece assigned to one
fixed \((m+H)\)-top has length at most \(H+1\): a length-\(\ell\)
geodesic piece has union size \(m+\ell-1\le m+H\).  Hence retaining
\(W-o(W)\) owner phases requires at least

\[
                         (1-o(1))\frac{W}{H+1}
\tag{2.9}
\]

marked runs.  At (0.2),

\[
 \frac{W/(H+1)}{N_H}
      =\frac{m^{1+o(1)}}H\longrightarrow\infty.
\tag{2.10}
\]

Thus common-schedule exchanges do not reduce the cut-only MSW run
ledger to \(O(N_H)\).  Coalescing marked runs after an exchange, or
joining endpoints belonging to different columns, is a new physical
splice operation outside the audited identities.  This is exactly the
operation which (2.8) is meant to isolate; no claim is made against a
future theorem constructing it.

## 3. Exact lag-\(H\) holonomy

Fix one root \(A\) and put \(U=A^c\).  Suppose a proposed completed
middle deck is

\[
                         J_i\in\binom UH,
 \qquad i\in\mathbb Z_M,
\tag{3.1}
\]

with

\[
 x_i=J_i\setminus J_{i+1},\qquad
 y_i=J_{i+1}\setminus J_i,
\tag{3.2}
\]

and suppose the \(x_i\)'s are distinct and exhaust \(U\).  Closure then
makes the \(y_i\)'s exhaust \(U\) as well.  Define a permutation
\(\sigma\) of \(U\) by

\[
                         \sigma(x_i)=y_i.
\tag{3.3}
\]

### Theorem 3.1 (nonabelian rotor criterion)

The sets in (3.1) are the cyclic \(H\)-windows of one labelled directed
frame if and only if

\[
                         y_i=x_{i+H}
 \qquad(i\in\mathbb Z_M).
\tag{3.4}
\]

Equivalently, if \(\xi(i)=x_i\) and \(\rho_H(i)=i+H\), then

\[
                         \sigma=\xi\rho_H\xi^{-1}.
\tag{3.5}
\]

In particular, writing \(g=\gcd(M,H)\), every legal insertion
permutation has exactly \(g\) cycles, all of length \(M/g\).

#### Proof

For a frame \((x_0,\ldots,x_{M-1})\), advancing its \(H\)-window one
phase deletes \(x_i\) and inserts \(x_{i+H}\), proving necessity.

Conversely, (3.4) gives

\[
                         J_{i+1}=J_i-x_i+x_{i+H}.
\tag{3.6}
\]

The cyclic windows

\[
                         K_i=\{x_i,\ldots,x_{i+H-1}\}
\tag{3.7}
\]

satisfy the same recurrence.  The label \(x_k\) is inserted at
transition \(k-H\), deleted at transition \(k\), and is unchanged in
between, so it belongs to exactly the same \(H\) consecutive members of
the two decks.  Hence \(J_i=K_i\) for every \(i\).  Equation (3.5)
follows, and rotation by \(H\) on \(M\) points has the stated cycle
type. \(\square\)

The scalar conditions

\[
 |J_i\cap J_{i+1}|=H-1,
 \qquad \{x_i:i\in\mathbb Z_M\}=U
\tag{3.8}
\]

do not imply (3.5).  Thus even an adjacent clone matching with perfect
label margins can have the wrong holonomy.  The complete-frame exchange
theorems start with columns already satisfying (3.5); they do not impose
it on an ungrouped clone table.

## 4. Exact packet-star locality

For a middle target \(D\), its provider star is

\[
                         \mathcal R(D)=\binom D{m-H},
 \qquad |\mathcal R(D)|=R_H.
\tag{4.1}
\]

### Theorem 4.1 (higher-cube star intersection)

Consider the \(d\)-pair cube (1.4) and put

\[
 B=V\setminus
 \left(C\cup\{a_{j,0},a_{j,1}:1\le j\le d\}\right).
\tag{4.2}
\]

Its root at corner \(\epsilon\) is

\[
 A_\epsilon
 =B\cup\{a_{j,1-\epsilon_j}:1\le j\le d\}.
\tag{4.3}
\]

For a fixed \(D\in\binom Vm\), the compatible corners form either the
empty set or one Boolean face of dimension

\[
 t(D)=\#\{j:\{a_{j,0},a_{j,1}\}\subseteq D\}.
\tag{4.4}
\]

Moreover \(t(D)\le H\), and therefore

\[
 \boxed{
 |\{\epsilon:A_\epsilon\subset D\}|
       =2^{t(D)}\le2^H=o(R_H).}
\tag{4.5}
\]

#### Proof

Since \(|C|=M-d\), one has \(|B|=m-H-d\).  Compatibility requires
\(B\subseteq D\).  In each label pair, if neither label belongs to
\(D\) there is no compatible corner; if exactly one belongs to \(D\),
the bit is forced; and if both belong to \(D\), the bit is free.  This
proves the face description and the equality in (4.5).

Compatibility already places \(B\), at least one label from every one
of the \(d\) pairs, and one extra label from every full pair into \(D\).
Thus

\[
 m=|D|\ge |B|+d+t(D)=m-H+t(D),
\]

so \(t(D)\le H\).  Finally

\[
 \binom mH\ge(m/H)^H
 \quad\Longrightarrow\quad
 \frac{2^H}{R_H}\le(2H/m)^H=o(1),
\]

because \(H=o(m)\). \(\square\)

### Theorem 4.2 (cycle-sector star intersection)

Fix an \((M-2)\)-core \(C\).  Among all pair tops

\[
                         C\cup\{u,v\},
 \qquad \{u,v\}\in\binom{V\setminus C}{2},
\tag{4.6}
\]

the provider star of any \(D\in\binom Vm\) contains at most

\[
                         \binom{m-H+2}{2}
\tag{4.7}
\]

roots.  An individual directed-cycle packet contains at most
\(m-H+2\) of them.

#### Proof

Put \(Z=V\setminus C\), so \(|Z|=m-H+2\).  The root belonging to
\(\{u,v\}\) is \(Z\setminus\{u,v\}\).  With

\[
                         E=Z\setminus D,
\]

compatibility is equivalent to \(E\subseteq\{u,v\}\).  If
\(|E|>2\) there is no compatible pair; for \(|E|=2,1,0\) the numbers
are respectively \(1,|Z|-1,\binom{|Z|}{2}\).  This proves (4.7).
A simple directed cycle uses at most \(|Z|\) pair tops. \(\square\)

Theorems 4.1--4.2 do not forbid overlapping compositions.  They give the
exact price of one: almost all of a target star must be assembled from a
superpolynomial number of packet incidences, and their shore choices must
belong to one correlated dependency block.  Disjoint or independently
rounded packets cannot furnish the required near-monochromatic root star.

## 5. A bounded-rank statewise Markov obstruction

Fix \(R\ge2\), put \(r=R+1\), and choose one rank-\(r\) top cube as in
(1.4).  Put its \(r\) placeholders in distinct core gaps, and let

\[
                         \gamma=(A_1A_2\cdots A_r).
\tag{5.1}
\]

At corner \(\epsilon\), let \(\pi^1_\epsilon\) and
\(\pi^\gamma_\epsilon\) be the identity and \(\gamma\)-specialized
frames.  Define

\[
 T_0(\epsilon)=
 \begin{cases}
  \pi^1_\epsilon,&|\epsilon|\text{ even},\\
  \pi^\gamma_\epsilon,&|\epsilon|\text{ odd},
 \end{cases}
 \qquad
 T_1(\epsilon)=
 \begin{cases}
  \pi^\gamma_\epsilon,&|\epsilon|\text{ even},\\
  \pi^1_\epsilon,&|\epsilon|\text{ odd}.
 \end{cases}
\tag{5.2}
\]

For every phase and every proper interval length, the higher-cube
derivative gives

\[
 \sum_\epsilon(-1)^{|\epsilon|}
      \bigl(v^1_\epsilon-v^\gamma_\epsilon\bigr)=0.
\tag{5.3}
\]

Thus the two tables have identical complete phase-refined all-depth
loads.

Any fixed-core directed-cycle packet contained in this cube varies at
most two binary coordinates, hence is the four-cycle on a two-face.  On
that face at least one of the \(r-2\) fixed placeholder labels is moved
to a different core gap by \(\gamma\), so the common-core restrictions
required by the cycle move disagree.  No cycle move applies.  Likewise,
every cube of rank at most \(R<r\) fixes at least one placeholder label,
which \(\gamma\) moves to a different gap; no such cube move applies.

Partitioning \(N_H-o(N_H)\) tops into disjoint rank-\(r\) cubes and
choosing their core orders generically excludes cross-gadget moves.  The
factorial number of cyclic core orders dominates the exponentially many
candidate common cores and the polynomial label choices; hence the
standard probabilistic method yields deterministic global tables with
no cross-gadget directed cycle and no rank-at-most-\(R\) cube.  The
detailed union bound is recorded in
`MATH_THEOREM_K_ALL_DEPTH_EXCHANGE_RANK_AND_LAG_H_HOLONOMY_OBSTRUCTION_20260726.md`.

### Theorem 5.1 (fixed-rank isolation)

For every fixed \(R\), and all sufficiently large \(m\), there are two
literal top-margin-one tables which

1. have identical target loads at every phase and every depth;
2. differ on \(N_H-o(N_H)\) roots;
3. are both isolated under all directed-cycle exchanges and all coherent
   cubes of rank at most \(R\); and
4. have an exact MSW owner-star witness for every selected middle
   incidence.

The last item follows solely from \(A\subset D\): the selected frame
need not equal the MSW witness.  This distinction is essential and is
precisely why incidencewise certification does not prove common-frame
connectivity.

For every fixed \(R\), there are

\[
                         \frac{N_H-o(N_H)}{2^{R+1}}
\tag{5.4}
\]

disjoint traps.  Hitting each by deletion or complete-frame replacement
exposes at least the phase-incidence mass in (0.6).  For fixed \(R\)
this is not \(o(W)\).  Formally, the expression in (0.6) falls to
\(O(N_H)\) only near \(R\ge\log_2M-O(1)\); however the isolation proof
is quantified for fixed \(R\) and is not uniform in such growing
\(R\).  This scale observation is therefore not a proved necessity for
a growing-rank library.  The result is also not an additive lower bound
against one recyclable catalyst, a collar lower bound, or a no-go for
growing-rank moves.

## 6. A low-component isolated state with negligible coverage

There is an independent all-rank statewise example.  Fix one cyclic
order \(\Pi\) of \(V\) and select

\[
                         \pi_A=\Pi|_{A^c}
\tag{6.1}
\]

at every promotion root.  This is a literal table with exactly \(N_H\)
rings.  Every common-core tournament induced by these frames is
transitive in the linear order obtained by cutting \(\Pi\) at one core
label, so no directed-cycle exchange applies.  A nontrivial higher-cube
checkerboard would force, on a two-face and for two inverted
placeholders,

\[
 a_{r,0}<a_{s,0}<a_{r,1}<a_{s,1}<a_{r,0},
\tag{6.2}
\]

an impossibility.  Thus no higher cube of any dimension applies.

For \(D\in\binom Vm\), let \(g_1,\ldots,g_m\) be the lengths of its
runs in the open cyclic gaps between consecutive labels of \(D^c\) in
\(\Pi\).  The exact provider multiplicity in (6.1) is

\[
                         r_\Pi(D)=\sum_{j=1}^m\binom{g_j}{H}.
\tag{6.3}
\]

Indeed, for \(A\subset D\), the surviving set \(J=D\setminus A\) is an
\(H\)-window of \(\Pi|_{A^c}\) exactly when all of \(J\) lies in one
such gap.  Therefore a covered \(D\) contains a cyclic run of \(H\)
elements, and the union bound gives

\[
 |\{D:r_\Pi(D)>0\}|
 \le 2m\binom{2m-H}{m-H}
 \le 2m\,2^{-H}W=o(W).
\tag{6.4}
\]

This table already has the desired \(O(N_H)\) separately linearized
frame-block count but has \(W-o(W)\) middle holes, and it is isolated
under the complete exchange library.  Thus the frame-block ledger and
coverage are genuinely independent state variables; neither one controls
the other.  No claim is made about further component mergers supplied by
an external endpoint-splicing theorem.

## 7. The exact positive theorem that survives

Fix an \((M-2)\)-core, a two-placeholder positional word, one deleted
phase, and one nested schedule.  Choosing one of the two placeholder
orders at every pair top is a tournament on the outside labels.  For
every positional interval, intervals containing exactly one placeholder
record the tournament outdegree or indegree of that label.  Hence the
complete phase-refined all-depth load vector depends only on the
tournament score sequence.  If the retained schedule includes one
phase/length cell containing exactly the first placeholder, the refined
load vector also recovers every score, so the sector fibre is exactly a
score fibre.  Without that extra cell, every fixed-score fibre is still
contained in one physical-load fibre, which is all the connectivity
argument below needs.

If two tournaments have the same scores, orient their difference edges
as in the first tournament.  The difference digraph is Eulerian and
decomposes into directed cycles.  Reversing a directed cycle is the exact
all-depth cycle exchange.  Every directed cycle reversal decomposes into
applicable triangle reversals by successively using a chord and shortening
the cycle.  Therefore triangle reversals connect the entire fixed-score
fibre.

Every intermediate state is a literal one-frame-per-top table.  It
preserves the common phase/depth schedule and remains a legal lag-\(H\)
frame table.  It also retains exactly the same number of selected frame
columns, and therefore the same number of separately linearized frame
blocks.  This proves that the exchange bank is a genuine local braid and
a genuine local Markov basis in this sector.  It does not assert an
invariant for physical components after an additional cross-column
endpoint-splicing operation.

The theorem begins only after the common core, one frame per top, and one
common tag history have been selected.  The MSW owner-star lift supplies
none of those simultaneous choices.  This is the exact quantifier at
which the local theorem stops.

## 8. Precise implication boundary

Proved here:

1. every audited complete-frame exchange preserves every root margin;
2. the direct incidencewise MSW literalization and a promotion factor lie
   in different top-margin fibres by a factor \(M\);
3. common-schedule partial-column exchanges preserve the marked run
   count, while cut-only MSW inheritance requires \(\Omega(W/H)\) runs;
4. the exact conjugacy-class form of lag-\(H\) holonomy;
5. the sharp \(2^H\) cube-star and \(O(m^2)\) cycle-sector bounds;
6. dense isolation for every fixed maximum cube rank, even after all
   directed-cycle moves are admitted;
7. an all-rank isolated \(N_H\)-ring state with \(W-o(W)\) middle holes;
   and
8. positive triangle Markov connectivity inside each already-grouped
   fixed-core score fibre.

Not proved:

1. impossibility of an overlapping growing-rank exchange construction;
2. impossibility of a recyclable catalytic frame;
3. impossibility of the nonneutral moving-hole or two-base conveyor
   libraries;
4. impossibility of directly constructing the common-core tight-path
   table; or
5. coefficient one.

The required new primitive is now exact.  It must be a partial-column,
provenance-changing splice (or an equivalent direct global selection)
which simultaneously

\[
 \begin{array}{ll}
 \text{(i)} & \text{reduces the MSW witness multiplicity to one frame per root,}\\
 \text{(ii)}& \text{closes the conjugacy condition }\sigma\sim\rho_H,\\
 \text{(iii)}& \text{couples at least }R_H/2^H\text{ packet incidences per target star,}\\
 \text{(iv)}& \text{changes a bad target-load fibre when necessary, and}\\
 \text{(v)}& \text{leaves only }O(N_H)\text{ final components.}
 \end{array}
\tag{8.1}
\]

The audited triangle/cycle and coherent higher-cube identities do not by
themselves supply (i)--(iv); overlapping or catalytic compositions are
outside that assertion.  Once grouping has already been achieved, the
identities preserve the one-column-per-root ledger relevant to (v), but
they supply no MSW endpoint-splice identity.  This is the rigorous
statewise obstruction beyond component colouring.
