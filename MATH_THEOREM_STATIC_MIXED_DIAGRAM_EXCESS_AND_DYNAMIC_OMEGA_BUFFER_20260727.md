# Static mixed diagrams and the dynamic excess buffer

Date: 2026-07-27

Scope: repaired promotion-ring slow-greedy hierarchy.

## Correction after the overlapping-cycle audit

The original proof exposed a spanning forest and then asserted that every
cycle-closing incidence paid a fresh endpoint factor.  That assertion was
not justified for overlapping cycles.  The corrected proof below does
not expose cycles separately.  It explores **rows**, applying the already
proved disjoint path-mesh maximum simultaneously to every old column met
by the new row, and applies the internal census to every column introduced
from that row.  Its exponent is identically
\(\sum_j(q_j-1)=\omega\), so theta graphs and arbitrary overlapping
cycles require no extra holonomy lemma.

An independent fixed-endpoint verification of the first core is in
`MATH_THEOREM_THETA_244_PHYSICAL_KERNEL_CLOSURE_20260727.md`.  It proves
the literal subdivided $K_{2,3}$ bound from
$B_X^{(1,1)}(e,e')\le Cd(X)\alpha^2$ and identifies the missing
$\alpha$ directly.  It also records that the uncolored matrix quantity
$\sum_{u,v}(C^2_{uv})^3$ is stronger than the resource-disjoint physical
diagram and is not an equivalent prerequisite.

## 0. Outcome

For a mixed row--column diagram \(\Gamma\), let

\[
 \omega(\Gamma)=
 \#\{\text{owner-witness incidences}\}
 -\#\{\text{nonempty columns}\}.
\tag{0.1}
\]

Rows are formal repaired-catalogue option copies through one fixed owner
\(X\).
Columns are pairwise resource-disjoint protected/selected catalogue edges
or compensation resources.  Repeated row copies are quotiented by their
equality partition for physical counting, but every formal row copy is
retained in the normalizing power of \(d(X)\).

The static mixed-diagram bound is

\[
 \boxed{
 Z_\Gamma(X)
 \le
 d(X)^{a(\Gamma)}(K D)^{c(\Gamma)}
 \left(
 {C(\omega(\Gamma)+1)^4\over m^2}
 \right)^{\omega(\Gamma)}.}
\tag{0.2}

Here \(a(\Gamma)\) is the number of formal row copies before applying the
equality partition,
\(c(\Gamma)\) is the number of nonempty columns, and harmless
fixed-density factors are suppressed.  The physical representation
multiplicity cancels on both sides.

The key point is that the constant in (0.2) is independent of the number
of degree-one columns.  After those private columns are removed, the core
has at most \(\omega\) columns and at most \(2\omega\) incidences.  Each
column is introduced once from a row: its first witness is included in
the $KD$-factor, its remaining witnesses on that row are paid by the
internal census, and every later row incidence is paid jointly by the
disjoint path-mesh maximum.  This proves (0.2) whenever
$2\omega\le L_{\rm pm}$, the certified local path-mesh order.

The stopped generator is exactly upper triangular in \(\omega\): a new
column incident with \(t\) displayed row copies raises \(\omega\) by
\(t-1\).  Thus private \(t=1\) stars are absorbed into the reference
drift and never approach the top of an excess buffer.

However, the static theorem does **not** by itself prove dynamic
regeneration.  A moving excess buffer closes provided one also controls
the flux of a single generator column crossing its outer boundary.  That
crossing-flux condition is an aggregate column-link estimate.  It is not
implied by time-zero (0.2), because residual reference degrees shrink by
\(\exp[-\Theta(m)]\) during one checkpoint while raw diagram counts are
only monotone.

Accordingly:

\[
\boxed{
 \text{all static mixed diagrams have the desired excess scale;
 dynamically the hierarchy is triangular, and the remaining gate is the
 first-moment/quarantine bound for the graded top strip.}
}
\tag{0.3}

## 1. Diagram definition

Fix an owner \(X\).  Let \(R=\{1,\ldots,a\}\) be formal row copies and
\(C=\{1,\ldots,c\}\) be nonempty columns.  For every \((i,j)\), prescribe
a nonnegative multiplicity \(q_{ij}\), and require

\[
                         q_j:=\sum_iq_{ij}\ge1.
\tag{1.1}
\]

Put

\[
                         s=\sum_{i,j}q_{ij},
 \qquad
                         \omega=s-c=\sum_j(q_j-1).
\tag{1.2}
\]

For pairwise resource-disjoint repaired edges
\(e_1,\ldots,e_c\), define

\[
 Z_\Gamma(X;e_1,\ldots,e_c)
 =
 \sum_{f_1,\ldots,f_a\ni X}
 \prod_{i,j}
 \binom{|(f_i\cap e_j)\cap\mathcal X|}{q_{ij}},
\tag{1.3}
\]

where \(\mathcal X\) is the owner shore.  Fix an equality partition
\(\pi\) of the formal rows and impose \(f_i=f_{i'}\) inside every block
of \(\pi\).  Different blocks may be required distinct; dropping that
last requirement only enlarges the count.  The full diagram count is

\[
 Z_\Gamma(X)=
 \sum_{(e_1,\ldots,e_c)}^*
 Z_\Gamma(X;e_1,\ldots,e_c).
\tag{1.4}
\]

Root witnesses and owner witnesses can be mixed.  A prescribed root--owner
incidence has a superpolynomially smaller normalized count than an owner
incidence, so treating it as an owner witness is a valid upper bound.

## 2. Private-column elimination

Let \(C_1=\{j:q_j=1\}\).  A column in \(C_1\) is attached to one row by
one owner witness.  Once that row is fixed, the number of choices of the
column, counted with its witness, is at most

\[
                         KD.
\tag{2.1}
\]

Indeed, sum the degrees of the at most \(K\) resources of the row.
Ignoring disjointness between private columns only increases the count.
Thus all private columns may be summed out at the cost

\[
                         (KD)^{|C_1|}.
\tag{2.2}
\]

They contribute zero to \(\omega\).

Let \(\Gamma_{\ge2}\) be the remaining core.  The compression lemma gives

\[
 |C(\Gamma_{\ge2})|\le\omega,qquad
 |E(\Gamma_{\ge2})|\le2\omega,qquad
 |R(\Gamma_{\ge2})|\le2\omega.
\tag{2.3}
\]

Consequently every orientation, equality, endpoint-component, and witness
ordering choice in the core contributes at most

\[
                         \exp[O(\omega\log(\omega+1))],
\tag{2.4}
\]

which is absorbed by \((C(\omega+1)^4)^\omega\).

## 3. Row-exploration lemma

Put

\[
                 \alpha_\omega={C(\omega+1)^4\over m^2}.
\tag{3.0}
\]

### Lemma 3.1 (arbitrary physical core)

For any prescribed equality partition on $a$ formal rows, the
compressed core satisfies

\[
 Z_{\Gamma,\pi}(X)
 \le
 d(X)^a(KD)^{c(\Gamma)}
 \alpha_\omega^{\omega(\Gamma)}
 \exp[O(\omega\log(\omega+1))].
\tag{3.1}
\]

#### Proof

First drop all prescribed equalities and inequalities between formal
rows.  Every summand is nonnegative, so this only enlarges the count and
leaves $a$ independent formal row sums.  It therefore suffices to
prove (3.1) with no row-equality restrictions.  In particular, no
separate equality credit or witness-equality partition is needed.

Treat one connected component of the physical row--column core.  Choose
one row as root and expose its incident columns.  Thereafter choose a new
row adjacent to at least one already exposed column, and expose every
previously unexposed column incident with that row.  Connectedness makes
such an order possible.

When row \(i\) is exposed, let \(O_i\) be its already exposed incident
columns and \(N_i\) its newly introduced columns.  Put

\[
 s_i^{\rm old}=\sum_{j\in O_i}q_{ij}.
\tag{3.2}
\]

If \(s_i^{\rm old}=0\), choose the row in at most \(d(X)\) ways.  If it
is positive, the columns in \(O_i\) are fixed and pairwise
resource-disjoint.  The original disjoint path-mesh maximum, applied once
to this row and to the full composition \((q_{ij})_{j\in O_i}\), gives

\[
 \sum_{f_i\ni X}
 \prod_{j\in O_i}\binom{|f_i\cap e_j|}{q_{ij}}
 \le d(X)\alpha_\omega^{s_i^{\rm old}}.
\tag{3.3}
\]

The far-pair remainder is absorbed in the same bound throughout the
buffer range, exactly as in the original path-mesh theorem.  Although
that theorem recorded the convenient cutoff $100(\log m)^2$, its
endpoint proof uses only $s=o(m)$, $m-2s\sim m$, and domination of
the far term.  It therefore applies unchanged for
$s=O((\log m)^3)$, the largest order used here.

After fixing \(f_i\), apply the internal path census to its new columns.
Iterating that census over the pairwise disjoint tuple gives

\[
 \sum_{(e_j:j\in N_i)}^*
 \prod_{j\in N_i}
       \binom{|f_i\cap e_j|}{q_{ij}}
 \le
 (KD)^{|N_i|}
 \alpha_\omega^{\sum_{j\in N_i}(q_{ij}-1)}.
\tag{3.4}
\]

Multiply (3.3)--(3.4) over the exploration.  Every row is chosen once,
every column is introduced once, and every formal witness incidence is
paid either in (3.3) or (3.4).  Therefore the total exponent is

\[
 \sum_i\sum_{j\in O_i}q_{ij}
 +\sum_i\sum_{j\in N_i}(q_{ij}-1)
 =\sum_{i,j}q_{ij}-c(\Gamma)
 =\omega(\Gamma).
\tag{3.5}
\]

This proves (3.1), with no cycle exposure and no independence assertion
between cycle closures.  \(\square\)

The exact scope is worth recording.  After private columns are removed,
every core column has total multiplicity at least two.  Hence

\[
                         c\le\omega,qquad s=c+\omega\le2\omega.
\tag{3.6}
\]

If the joint path-mesh maximum and internal census are certified through
total order $L_{\rm pm}$, Lemma 3.1 is unconditional for
$2\omega\le L_{\rm pm}$.  Any use beyond that range requires an
extension of those local estimates; it is not supplied merely by the
diagram exploration.

The proof applies verbatim to theta graphs and all other overlapping
cycle cores: all old incidences of a new row are charged together by
(3.3).

### Dynamic normalization after equality resolution

The loose static form (0.2) retains \(a\) formal row copies and uses the
factor \(d(X)^{a-r_0}\) as credit.  That is not the reference to use in a
dynamic martingale: equal formal rows have only one physical survival
rate.

For dynamics, first resolve both the row equality partition and all
owner-witness equalities.  Let \(b\) be the number of physical rows,
\(\widetilde s\) the number of distinct physical witness incidences, and
put

\[
                    \widetilde\omega=\widetilde s-c.
\tag{3.7}
\]

Apply the row-exploration proof directly to this quotient diagram.  No
equality credit is then needed, and it gives

\[
 Z_{\widetilde\Gamma}(X)
 \le
 d(X)^b(KD)^c
 \alpha_{\widetilde\omega}^{\,\widetilde\omega}
 \exp[O(\widetilde\omega\log(\widetilde\omega+1))].
\tag{3.8}
\]

Thus the dynamic hierarchy is indexed by **physical excess**
\(\widetilde\omega\) and normalized with \(d(X)^b\).  The formal power
expansion is partitioned into these physical types before applying any
drift or moment estimate.  In particular, an equal-row diagonal moves to
a lower physical type instead of being assigned several fictitious row
loss rates.

## 3A. Deprecated cycle-by-cycle proof attempt

The following endpoint-closure argument is retained only to document the
superseded approach.  Its claim of an independent loss for every
nonforest incidence is not used in the theorem.

### Former Lemma 3.2 (one nonforest incidence, with equality credit)

Suppose a compatible mixed core on at most \(2\omega\) incidences has
already been exposed along a spanning forest of its underlying simple
bipartite graph.  Prescribe one further row--column incidence, or one
further parallel witness on an existing row--column pair.  After
partitioning by all owner-witness equalities forced by the exposed data,
the number of completions loses the factor

\[
                         {C(\omega+1)^4\over m^2}.
\tag{3.1}
\]

#### Proof

Use the cyclic phase order of the repaired row or column on which the new
witness is first encountered.  The already exposed witnesses cut that
phase order into endpoint atoms.  There are at most \(2\omega+2\) atoms.

If the new witness lies in the same interval-intersection component as a
previous witness, expose the gap \(g\ge1\) from the existing two-sided
phase hull.  It fixes \(g\) new leaving coordinates and \(g\) new entering
coordinates.  The factorial quotient is at most

\[
                         \binom{m-2\omega}{g}^{-2}.
\tag{3.2}
\]

Summing the side, orientation, atom, and gap choices gives

\[
 \sum_{g\ge1}{C(\omega+1)^2(g+1)\over
                     \binom{m-2\omega}{g}^{2}}
 \le {C(\omega+1)^4\over m^2}.
\tag{3.3}
\]

If it starts a new interval-intersection component, its first interval is
disjoint from the union of the preceding component.  The corresponding
owner pair has Johnson distance at least the smaller exposed arc length;
the exact pair formula gives at most

\[
 {C(\omega+1)^2\over\binom m d^2}
 \le {C(\omega+1)^4\over m^2}
\tag{3.4}
\]

after summing the possible component positions.  For \(d\ge H/4\), the
left side is superpolynomially smaller.  Thus (3.1) holds in both cases.

There are two apparent dependencies.  First, formal row copies may be
equal and may reuse the same witness.  Then a repeated incidence is
indeed forced and (3.1) is not a fresh endpoint loss.  This is why (0.2)
uses the number of formal rows rather than the number of equality blocks.
Merging \(q\) formal rows leaves the unused normalization credit

\[
                         d(X)^{q-1}.
\tag{3.5}
\]

The correlation core has at most \(2\omega\) incidences.  In the buffer
range \(\omega=O((\log m)^3)\), and

\[
 \log d(X)=(1+o(1))m\log m,
 \qquad
 \alpha^{-2\omega}=\exp[O(\omega\log m)],
 \qquad
 \alpha={C(\omega+1)^4\over m^2}.
\tag{3.6}
\]

Thus one saved formal-row factor pays every endpoint factor that can be
lost inside that equality block.  This is numerical domination, not a
claim that an equal-row diagonal creates a new endpoint gap.

Second, with distinct rows the new incidence may reuse an owner already
present in both its row and column.  Put all such hidden equalities into
the witness-equality closure before exposure.  Because distinct columns
are resource-disjoint and every row contains the sole common protected
owner \(X\), such a reuse either merges displayed row blocks (paid by
(3.5)) or creates an additional nonprivate row--row witness.  In the
latter case expose that hidden witness at its first appearance and charge
(3.3) there instead of at the closing row--column incidence.  The number
of closure patterns is bounded by (2.4).  No forced incidence is charged
twice. \(\square\)

The last paragraph is why equality partitions are part of the theorem.
Without closing hidden witness equalities first, a cycle incidence can
look free even though its endpoint cost occurred on another side of the
cycle.

## 4. Historical spanning-tree accounting (not used)

Lemma 3.1 already proves the static theorem.  The accounting below
explains the same exponent when every asserted cycle closure is fresh,
but it is not used for overlapping-cycle cores.

Fix the equality partition.  If it has \(r_0\) physical blocks among
\(a\) formal rows, reserve \(d(X)^{a-r_0}\) as the equality credit from
Lemma 3.1.  It is then enough to treat one connected component of the
physical core; multiply over components afterwards.  Choose a spanning
tree of its underlying simple bipartite graph.

* Choose its first row in at most \(d(X)\) ways.
* Whenever the tree first reaches a column from a row, choose the column
  and its anchor witness in at most \(KD\) ways.
* Whenever the tree first reaches a row from a column, choose the row
  through \(X\) and its anchor witness.  The width-two path estimate costs
  at most

  \[
                         d(X){C(\omega+1)^4\over m^2}.
  \tag{4.1}
  \]

For a core forest with \(r_0\) rows, \(c_0\) columns, and \(k_0\)
components, this gives

\[
 d(X)^{r_0}(KD)^{c_0}
 \left({C(\omega+1)^4\over m^2}\right)^{r_0-k_0}.
\tag{4.2}
\]

The number of remaining simple-graph incidences is its cyclomatic number

\[
 \bigl|E_{\rm simple}\bigr|-(r_0+c_0)+k_0.
\tag{4.3}
\]

Every such incidence was charged by Former Lemma 3.2.  Every parallel
witness beyond the first on a row--column pair was charged by the same
former lemma.
The total number of charged factors is

\[
 (r_0-k_0)
 +\bigl(|E_{\rm simple}|-(r_0+c_0)+k_0\bigr)
 +(s-|E_{\rm simple}|)
 =s-c_0.
\tag{4.4}

This is exactly the physical-core contribution to \(\omega\).  Restore
the equality credit \(d(X)^{a-r_0}\), multiply by the private-column
factor (2.2), and sum over the closure patterns in (2.4).  Under the
former fresh-closure assertion this recovers (0.2); the unconditional
proof is Lemma 3.1.

For \(K_{2,2}\), (4.2) pays one forest factor and Former Lemma 3.2 pays
the closing-cycle factor, recovering the \(m^{-4}\) estimate in the first
\(C_4\) theorem.  For a tree, (4.3) is zero and (4.2) is exactly the
tree-homomorphism estimate.

## 5. Generator triangularity

Let a displayed configuration have diagram \(\Gamma\).  Selection of a
new catalogue edge, or revelation of one compensation resource, adds one
new nonempty column.  If it carries \(t\) witness incidences with the
formal displayed rows (repetitions retained when formal rows are equal),
then

\[
                  \omega(\Gamma')-\omega(\Gamma)=t-1.
\tag{5.1}
\]

Thus:

* \(t=1\) is neutral.  Summing all such private columns gives the exact
  first-order/reference hazard.
* \(t\ge2\) raises excess, and the static scale attaches
  \((C(\omega+t)^4/m^2)^{t-1}\).
* deletion of a protected row or column is a negative jump and is harmless
  for upper envelopes.

After exponential-generating-function summation over private columns and
equality partitions, the centered generator has the formal triangular
shape

\[
 {\cal L}\widehat Z_r
 \le \dot z_r^{\rm ref}
 +\sum_{d\ge1}
       (C(r+d)^4)^d\widehat Z_{r+d},
\tag{5.2}
\]

where the normalization of \(\widehat Z_{r+d}\) contains the factor
\(m^{-2d}\).  No coefficient depends on the number of private columns.

Together with Lemma 3.1, this proves the algebraic triangularity which
fails for a hierarchy indexed by total witness order.

## 6. Finite moving excess buffer

Put

\[
 J=C_0\log m,qquad
 L_0=C_1(\log m)^2,qquad
 L_i=L_0-iJ.
\tag{6.1}
\]

There are \(O(\log m)\) checkpoints.  At fixed survivor density
\(u\ge z=m^{-1/20}\), the accumulated one-excess parameter is

\[
 \Theta_m=
 T{C L_0^4\over m^2z^2}
 =O(m^{-9/10}(\log m)^9)=o(1).
\tag{6.2}

Assume at checkpoint \(i\) that every incidence-weighted diagram of
excess at most \(L_i\) obeys its dynamic version of (0.2).  For a target
of excess at most \(L_i-J\), every time-ordered generator chain which
reaches excess \(L_i\) accumulates total excess at least \(J\).  Equation
(5.2) and the time-simplex bound give the tail

\[
                         (C\Theta_m)^J
 \le\exp[-c(\log m)^2].
\tag{6.3}
\]

The same expansion gives the column quadratic and \(J\)-th jump moments;
the full equality-partition diagrams are precisely the cross terms which
were absent from the scalar buffer.  Therefore, **provided the outer
crossing flux is stopped at its predicted scale**, all diagrams of excess
at most \(L_i-J\) regenerate at checkpoint \(i+1\).  Iterating leaves a
positive \(\Theta((\log m)^2)\) buffer through the full trajectory.

### The remaining boundary condition

The italicized proviso is not automatic.  A single new column can take a
diagram from excess \(r\le L_i-J\) to excess above \(L_i\).  Bounding its
compensator requires

\[
 {1\over K D_t}
 \sum_g
 \left({Z_{\Gamma+g}(t)\over Z_\Gamma(t)}\right)^q
 \le
 \left({C(r+q)^4\over m^2u_t^2}\right)^{q-1}
\tag{6.4}
\]

in incidence-weighted aggregate form.  This is an ACLE/DLE outer-flux
estimate.  If \(\Gamma+g\) remains inside the buffer, it is one of the
stopped variables.  If it jumps past the buffer, time-zero (0.2) gives no
dynamic relative bound: during one checkpoint the reference can shrink by
\(\exp[-\Theta(m)]\).

Consequently the omega buffer removes the private-star/spine obstruction
and makes the generator genuinely triangular, but it does not conjure the
outer crossing estimate.  One must obtain (6.4) by high-column truncation,
an absorber/quarantine argument, or a direct dynamic endpoint theorem.

### Deterministic high-\(t\) truncation by row budget

There is one useful partial removal of the proviso.  If a designated
martingale expansion contains at most \(R\) formal row copies, then every
new column has \(t\le R\), and hence

\[
                         \Delta\omega=t-1<R.
\tag{6.5}
\]

Taking the checkpoint gap to be \(R\), rather than \(J\), makes a
one-step crossing from the protected core impossible.  For the degree and
basic influence martingales, a \(J\)-th jump moment has at most
\(R=O(J)=O(\log m)\) rows.  For the \(J\)-th jump moment of an already
\(J\)-row aggregate energy, the crude bound is
\(R=O(J^2)=O((\log m)^2)\).  Thus a deterministic gap
\(O((\log m)^2)\) and an initial excess buffer
\(O((\log m)^3)\) remain numerically admissible:

\[
 T{C(\log m)^{12}\over m^2z^2}=m^{-9/10}(\log m)^{13}=o(1).
\tag{6.6}
\]

This does not by itself close the induction.  Regenerating those
\(J^2\)-row auxiliary diagrams with another \(J\)-th moment can increase
the row count again.  A complete deterministic truncation therefore
needs either a two-dimensional buffer in \((\omega,\text{row count})\),
or a first-moment/loose-envelope treatment of the high-row boundary.
Treating every auxiliary diagram with the same high-probability moment
recursively simply moves the outer-flux problem into the row coordinate.

### Graded moment improvement

There is a sharper deterministic truncation.  If an excess-\(r\) core is
replicated \(q\) times in a jump moment, first compress its private
columns and partition equal old columns across replicas.  Since a core
has at most \(r\) columns, the replicated old core has excess less than
\(2qr\).  The new selected column meets every nonzero jump replica; keep
canonically one such incidence in each replica and drop all its other
incidences.  Dropping constraints enlarges the count, and the retained
shared column raises excess by \(q-1\).  Hence

\[
          \omega(\text{truncated }q\text{-moment})
          <q(2r+1).
\tag{6.7}
\]

Thus the graded choice

\[
 q(r)=\min\left\{J,
          \left\lfloor{L\over2r+1}\right\rfloor\right\}
\tag{6.8}
\]

never crosses a ceiling \(L\), independently of the actual number of
rows hit by the new column.  Full \(J\)-th moments are available for
\(r\le(L/J-1)/2\), quadratic variation for \(r\le(L-2)/4\), and only a
first-moment loose envelope is needed above that range.  This removes the
recursive row-count objection from the stochastic core.  It does not yet
turn the first-moment top strip into a stopped incidence-weighted
quarantine estimate; that is the remaining boundary problem.

## 7. Final status

Proved unconditionally:

1. private one-incidence columns disappear exactly into \(KD\)-factors;
2. the physical core at excess \(r\) has size \(O(r)\);
3. the excess increment of one new column is exactly \(t-1\);
4. arbitrary static mixed diagrams, including equality partitions, obey
   the excess bound (0.2), by the row-exploration Lemma 3.1, throughout
   the certified range $2\omega\le L_{\rm pm}$.

Conditional consequences:

5. conditional on the first-moment/quarantine estimate for the graded
   top strip, a
   \(\Theta((\log m)^2)\) moving excess buffer survives
   \(O(m\log m)\) slow time.

Not proved:

\[
\boxed{
 \text{the first-moment/quarantine bound for the graded top strip.}
}
\]

This is strictly narrower than the previous all-moment outer-flux gate.
Equation (6.8) prevents crossings throughout the stochastic core; only
the top strip lacks a high moment.  In particular, an arbitrarily long
private-star spine has excess zero and can no longer cause a false
top-boundary failure.
