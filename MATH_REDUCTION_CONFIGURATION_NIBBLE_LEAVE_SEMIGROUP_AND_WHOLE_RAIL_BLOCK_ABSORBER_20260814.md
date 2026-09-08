# Configuration-nibble leaves: exact semigroup interface and the whole-rail block absorber

**Date:** 2026-08-14  
**Status:** unconditional exact reduction, one-bite growing-rank estimate,
and a sharp audit of the known `q=2` near-core macro.  This note does not
prove a near-perfect growing-rank nibble or an arbitrary bounded positive
rail absorber.  It identifies the structured leave for which the existing
whole-rail graph absorber is already exact.

## 0. Outcome

There are four distinct layers in the remaining ordering problem.

1. A finite pure-rail completion is membership in a **truncated affine
   semigroup** of complete alternating configurations.  Fractional Hall
   inequalities and signed-lattice membership are necessary, but are not
   sufficient in general.
2. If the nibble is token-partite, its owner/lower leave has an exact
   algebraic shape.  The unmatched shell tokens determine the point roles
   and fixed-pair parity charge; these are not additional random errors.
3. An honest `r`-uniform conflict hypergraph has a rigorous isolated-bite
   estimate with relative collision error controlled by

   \[
                         \theta={r^2\Delta _2\over D}.             \tag{0.1}
   \]

   It covers only `Theta(1/r)` of the current vertices.  The existing
   alternating configuration quotient has the desired external pair ledger,
   but has not yet been realized as such an ordinary hypergraph; this is a
   method condition, not a claimed application.  Iterating to a small leave
   also requires a degree-regeneration theorem which is not proved here.
4. For pairwise resource-disjoint complementary fibres, the semigroup
   becomes a disjoint-block system.  A leave is absorbable if and only if it
   is a union of complete fibre blocks.  This gives an exact finite absorber
   interface and permits one terminal fibre at the scalar level when its
   period may be chosen in a complete residue interval.

The previously proved distance-one `q=2` one-owner macro does not supply
such an alternating absorber.  Both of its lower shores repeat named lower
sets, and its signed lower current has `l1` norm `19`, rather than being one
lower unit.

## 1. The exact finite absorber interface

Let `X` be the complete finite resource set which the terminal argument must
preserve.  At minimum it contains the named owners and named lower sets.  It
may also contain shell-token, upper-ticket, socket, phase, cap, or history
rows.  For every legal parameterized alternating pure-rail configuration
`gamma`, let

\[
                         a_\gamma\in\mathbb Z_{\ge0}^{X}           \tag{1.1}
\]

be its complete resource-incidence column.  Fix a finite catalogue
`Gamma`, usage capacities `m_gamma`, and let `A` be the matrix with columns
`a_gamma`.

### Theorem 1.1 (bounded-semigroup completion criterion)

A residual demand `b in Z_(>=0)^X` has an exact completion from this
catalogue if and only if

\[
 \boxed{
 b\in
 \left\{Ax:x\in\mathbb Z^\Gamma,\quad
                  0\le x_\gamma\le m_\gamma\right\}.}            \tag{1.2}
\]

If every exclusive resource has demand at most one, equation `(1.2)` also
enforces simplicity: two selected columns cannot share such a resource.
Putting one token row of demand one for each residual shell enforces the
choice of exactly one order for that shell.

The continuous relaxation is feasible if and only if, for every real row
weight `y`,

\[
 \sum_\gamma m_\gamma\min(0,y\mathbin\cdot a_\gamma)
 \le y\mathbin\cdot b\le
 \sum_\gamma m_\gamma\max(0,y\mathbin\cdot a_\gamma).            \tag{1.3}
\]

These are the exact support-function, or capacitated Hall, inequalities for
the image of the box.  Integral completion additionally requires the
bounded-semigroup membership `(1.2)`.  Membership in the column lattice,
together with `(1.3)`, is not sufficient without a normality or total-
unimodularity theorem.

#### Proof

Selecting `x_gamma` copies contributes exactly `Ax`; this proves `(1.2)`.
The image under `A` of the real box `prod_gamma[0,m_gamma]` is a zonotope.
Its support function at `y` is the right side of `(1.3)` and its minimum at
`y` is the left side.  The separating-hyperplane theorem proves the stated
fractional equivalence.

For the last assertion, already the scalar columns `6,7` have column
lattice `Z` and nonnegative cone `R_(>=0)`, but demand `1` is not in their
nonnegative semigroup.  These are two consecutive legal periods when
`q=2` (the shortest port-rich periods in the shell convention used by the
protected role construction); thus the warning is present before any
named-resource correlation is added.  \(\square\)

For arbitrary named rail columns, `(1.2)` is the sharp finite interface.
At `q=2`, even optimizing one fixed-shell order against arbitrary owner
weights contains maximum-weight Hamilton cycle.  Thus there is no reason to
expect the inequalities `(1.3)` to collapse to ordinary point Hall rows or
a Birkhoff system.

There is nevertheless one exact preliminary Hall test before the pure-rail
restriction is imposed.  Let `O_0,L_0` be equally large residual named owner
and lower sets, and form the bipartite containment graph

\[
 G_\subseteq=(O_0,L_0;\{AL:L\subset A\}).            \tag{1.4}
\]

### Theorem 1.2 (exact alternating-incidence cut criterion)

The residual vertices have a simple alternating Johnson cycle factor if
and only if, for every `X subseteq O_0` and `Y subseteq L_0`,

\[
 \boxed{
 e_{G_\subseteq}(X,L_0\setminus Y)+2|Y|\ge2|X|.}    \tag{1.5}
\]

Equivalently, `G_subseteq` has a spanning `2`-factor.  This condition is
necessary for completion by pure rails, but not sufficient: it remembers
the alternating owner/lower incidence and forgets the common-core,
consecutive-window, period, and residence constraints.

#### Proof

Give a network arcs of capacity two from the source to every owner, arcs of
capacity one on the containment edges, and arcs of capacity two from every
lower set to the sink.  An integral flow of value `2|O_0|` is exactly a
spanning simple bipartite `2`-factor.  A cut whose source side contains
`X subseteq O_0` and `Y subseteq L_0` has capacity

\[
 2(|O_0|-|X|)+e(X,L_0\setminus Y)+2|Y|.             \tag{1.6}
\]

The max-flow/min-cut theorem and flow integrality give `(1.5)`.
Alternating around a component gives a simple Johnson owner cycle: two
distinct rank-`R` owners containing the same rank-`R-1` lower set are
adjacent and intersect in exactly that lower set. \(\square\)

This separates two possible terminal failures.  Violation of `(1.5)` is
an incidence cut obstruction which no cyclic ordering can repair.  Passing
`(1.5)` only supplies arbitrary Johnson cycles; the remaining pure-rail
obstruction is precisely the bounded-semigroup membership `(1.2)` with the
legal rail catalogue.

## 2. Algebraic shape of a token-partite leave

Put

\[
 |C|=c,\qquad |T|=N,\qquad q=R-c,                   \tag{2.1}
\]

and let one pure rail have owners `C` plus the cyclic `q`-windows of `T`
and lower sets `C` plus the cyclic `(q-1)`-windows.  For a bank of rails,
write `o_x` and `ell_x` for its owner and lower point loads.  Define

\[
 U_x=o_x-\ell_x,
 \qquad
 K_x=q\ell_x-(q-1)o_x.                              \tag{2.2}
\]

### Lemma 2.1 (exact role reconstruction)

For every nonnegative pure-rail bank,

\[
 U_x=\#\{\hbox{rail supports containing }x\},        \tag{2.3}
\]

\[
 K_x=\sum_{Q:x\in C(Q)}N(Q).                        \tag{2.4}
\]

In particular `U_x,K_x` are nonnegative integers and

\[
 \sum_xU_x=\sum_QN(Q),\qquad
 \sum_xK_x=c\sum_QN(Q).                             \tag{2.5}
\]

#### Proof

One period-`N` rail contributes

\[
 o=N\mathbf1_C+q\mathbf1_T,
 \qquad
 \ell=N\mathbf1_C+(q-1)\mathbf1_T.                 \tag{2.6}
\]

Substitution in `(2.2)` gives `1_T` and `N 1_C`, respectively.  Sum over
the bank. \(\square\)

Now freeze a labelled shell-token bank before choosing any cyclic orders.
Every order of one token has the same two point vectors `(2.6)`.  Therefore,
after selecting a matching of some token orders, the residual owner/lower
point vectors are exactly the sum of `(2.6)` over the unmatched tokens.
Equations `(2.2)--(2.5)` hold identically for the leave.  This is the
principal advantage of a token-partite nibble: it cannot create an
unexplained point-role defect.

It can still create an arbitrary **named** defect inside those point rows.
The exact-role orbit counterexample shows that point identities alone need
not give even fractional named coverage.  Thus the residual gate is still
the semigroup problem `(1.2)` on the unmatched tokens and named shores.

Relative to a fixed pair structure, give every Johnson edge the signature
`alpha` and charge `eta` from the parity-charge theorem.  Every closed rail
has

\[
                         \sum\alpha=0,
 \qquad                  \sum\eta=N\pmod2.          \tag{2.7}
\]

Consequently a token-partite leave has zero `alpha` boundary and total
charge equal to the sum of its unmatched token periods modulo two.  Its
parity charge is fixed by the token leave; it is not a free error which a
degree-conformal trade can change.

## 3. The exact growing-rank one-bite bound and the quotient gap

Let `H` be an `r`-uniform `D`-regular hypergraph and let `Delta_2` be its
maximum pair codegree.  For an edge `E`, let `Gamma(E)` be the other edges
which meet it.

### Lemma 3.1 (external conflict neighbourhood)

\[
 r(D-1)-{r\choose2}(\Delta _2-1)
 \le |\Gamma(E)|\le r(D-1).                         \tag{3.1}
\]

The lower bound may of course be replaced by zero when its displayed value
is negative.

#### Proof

For each `v in E`, take the `D-1` other edges through `v`.  The upper bound
is the union bound.  In the lower bound, Bonferroni subtracts, for every
pair `u,v in E`, the at most `Delta_2-1` other edges containing both.
\(\square\)

### Theorem 3.2 (exact isolated bite)

Fix `0<gamma<=1`.  Mark every edge independently with probability

\[
                         p={\gamma\over rD}           \tag{3.2}
\]

and retain a marked edge exactly when no other marked edge meets it.  The
retained edges form a matching, and their expected covered fraction lies
between

\[
 {\gamma\over r}(1-p)^{r(D-1)}                       \tag{3.3}
\]

and

\[
 {\gamma\over r}
 (1-p)^{\max\{0,r(D-1)-{r\choose2}(\Delta _2-1)\}}. \tag{3.4}
\]

In particular some matching covers at least `(3.3)` of the vertices.  If

\[
                         \theta={r^2\Delta _2\over D}=o(1),       \tag{3.5}
\]

then the expected covered fraction is

\[
 {\gamma e^{-\gamma}\over r}
 \left(1+O\left({1\over D}+{\theta\over r}\right)\right).       \tag{3.6}
\]

#### Proof

Conditioned on marking `E`, it survives with probability
`(1-p)^|Gamma(E)|`.  Since `|E(H)|=|V(H)|D/r`, multiplying the average
survival probability by `r|E(H)|p/|V(H)|` gives `(3.3)--(3.4)` from Lemma
3.1.  Finally expand `log(1-p)`.  The main exponent is `-gamma`; the
Bonferroni displacement is at most

\[
 p{r\choose2}\Delta _2
 \le {\gamma r\Delta _2\over2D}
 = {\gamma\theta\over2r},                           \tag{3.7}
\]

and the remaining finite-`D` terms are absorbed by `(3.6)`. \(\square\)

The theorem is directly applicable only after the conflict system has been
represented as an honest hypergraph whose vertex intersections are exactly
the forbidden collisions.  The ordinary complete-orbit hypergraph on the
owner and lower shores has rank `2N`, and its incident owner--lower
codegree is `2D/R`.  Hence its unquotiented squared-rank parameter is

\[
                         \Theta(N^2/R)=\Theta(1)      \tag{3.8}
\]

in the central regime, not `o(1)`.

Contracting each owner's two incident facets as internal configuration data
removes that pair from the **external collision ledger**.  The exact
complete-orbit calculation then gives the formal value

\[
                         \theta_{\rm ext}=O(k^{-1}).  \tag{3.9}
\]

But the alternating triples overlap in their lower resources, and two rails
can conflict through one constituent without containing the same complete
triple.  Thus the bookkeeping quotient is not yet an ordinary hypergraph to
which Theorem 3.2 may simply be applied.  One needs a configuration-matching
or conflict-system theorem which treats those internal correlations without
forgetting constituent collisions.

Even if such an honest quotient is supplied, `(3.6)` covers only
`Theta(1/r)` of the current vertices.  A near-perfect conclusion would need
`Theta(r log(1/epsilon))` regenerated bites, while keeping all token, owner,
lower, reserve-block, and protected loads regular.  Neither Lemma 3.1 nor a
time-zero value of `theta_ext` proves that regeneration.  No growing-rank
near-perfect nibble theorem is inferred here.

## 4. Exact whole-rail block absorber

For each terminal gadget `i`, let `B_i=B_(m_i)(h_i)` be the residual
complementary fibre from the whole-rail graph identity

\[
 \mathcal B_{m_i}(S_i)
 =\mathcal B_{m_i}(G_i)\mathbin{\dot\cup}B_i.        \tag{4.1}
\]

Let `b_i` contain one residual token coordinate together with the complete
owner, lower, and every other compulsory resource occurrence of `B_i`.
Use occurrence-labelled coordinates, so `b_i` is a zero-one column.  Assume
that the two shores have been decorated so that `(4.1)` holds in every row
of `X`, and that the gadget reserves and all columns `b_i` are pairwise
disjoint on every resource row in this terminal interface.  The
complementary-fibre theorem supplies this identity unconditionally for
owners and every proper interval deck; compatibility and disjointness of
any additional compulsory ticket are explicit hypotheses.

### Theorem 4.1 (disjoint-block criterion)

A residual vector `b` is completable by independent switches in these
gadgets if and only if

\[
                         b=\sum_{i\in I}b_i           \tag{4.2}
\]

for some subset `I`.  The subset is unique.  Equivalently, on the support
of each zero-one block `b_i`, every residual exclusive-resource coordinate
has the same value in `{0,1}`, and the residual vector is zero outside the
union of the blocks.

The block incidence matrix has at most one nonzero entry in every resource
row.  Hence its box relaxation is integral: for this structured leave, the
fractional Hall inequalities are sufficient and there are no additional
lattice or semigroup holes.

#### Proof

Switching gadget `i` from the `G_i` shore to the `S_i` shore adds exactly
the complete column `b_i` by `(4.1)`, including its alternating decks.
Disjointness makes the switches independent and makes the coefficient of
`b_i` readable from any one of its exclusive coordinates.  This proves
necessity, sufficiency, and uniqueness.  After permuting rows, the block
matrix is a disjoint union of one-column all-one matrices, which is totally
unimodular. \(\square\)

Thus the exact cover-down target is not merely “few unmatched owners.”  It
is the diagonal event that the unmatched token, all owners of its fibre,
all lower sets of its fibre, and every compulsory ticket of that fibre are
left together.  An ordinary owner matching does not enforce this event.

There is no scalar reason to need `O(q)` terminal fibres if the terminal
period is flexible.  More generally, let the bulk period be any

\[
                         r_0\ge2q                    \tag{4.3}
\]

and let `M` be the total residual mass to be partitioned.  For any minimum
admissible terminal period `m_0>=2q`, the interval
`[m_0,m_0+r_0-1]` contains one representative of every residue modulo
`r_0`.  Therefore there is a unique

\[
 m\in[m_0,m_0+r_0-1],\qquad m\equiv M\pmod {r_0}.    \tag{4.4}
\]

If `M>=m`, `R>=3q`, and `k-R>=m-q+2`, the general-period
complementary-fibre theorem supplies one legal terminal fibre of period
`m`, and `(M-m)/r_0` is a nonnegative integer.  For example, bare bulk
period `r_0=2q+1` and `m_0=2q` use `[2q,4q]`.  If both bulk and terminal
rails must start at the port-rich period `2q+2`, take `r_0=m_0=2q+2` and
the interval `[2q+2,4q+3]`, under the correspondingly stronger ambient
inequality.

This proves only **one-component scalar compatibility**.  It does not
construct a bulk matching whose exact named leave is that chosen fibre.
The reserve behind one graph switch also has polynomially many owners, so
one terminal component is not the same as a constant-size physical reserve.

There is also an exact augmented-matching formulation.  Install the `G_i`
shore of every reserve gadget and let `g_i` be its complete resource vector.
Let `t` be the target vector and let `A_bulk` be the legal bulk columns,
all resource-disjoint from the installed reserves except through the
displayed switch interfaces.

### Theorem 4.2 (augmented exact-cover equivalence)

Within this fixed reserve system, a terminal exact factor exists if and
only if there are a zero-one bulk selection `x` and a subset `I` of block
indices such that

\[
 \boxed{
 A_{\rm bulk}x+\sum_{i\in I}b_i
 =t-\sum_i g_i.}                                    \tag{4.5}
\]

Equivalently, add the complete fibre blocks `b_i` as formal leave edges to
the bulk matching problem and demand an exact cover of the residual target.
Every selected formal leave edge is then discharged by the physical switch
`G_i+B_i -> S_i`.

#### Proof

Given `(4.5)`, retain `G_i` for `i notin I` and replace `G_i+B_i` by `S_i`
for `i in I`.  Since `s_i=g_i+b_i` in every tracked resource row, the final
resource vector is

\[
 A_{\rm bulk}x+\sum_{i\notin I}g_i+\sum_{i\in I}s_i
 =A_{\rm bulk}x+\sum_i g_i+\sum_{i\in I}b_i=t.       \tag{4.6}
\]

All unions are simple by the reserve-disjointness hypotheses.  Conversely,
any terminal factor restricted to these bulk columns and the two states of
each installed gadget yields `(4.5)` by recording which gadgets use their
`S_i` shore. \(\square\)

Theorem 4.2 is the precise structured cover-down target for a future
reserve-aware nibble.  It asks for a perfect matching in an augmented
system, not for a near-perfect matching followed by a theorem that every
small leave is absorbable.

Finally, the block catalogue itself has an exact cut obstruction.  If
`x,y` are two resource rows in one block `b_i`, then the functional
`e_x-e_y` annihilates every block column.  It detects any leave which
contains exactly one of `x,y`.

### Corollary 4.3 (necessary shape of an extra absorber atom)

No union, signed or positive, of the disjoint whole-fibre block columns can
absorb a partial fibre leave.  Any enlarged terminal catalogue which does
absorb such a leave must contain an atom whose restriction to at least one
old block is nonconstant.  In physical terms, it must couple two fibre
blocks or refactor a fibre internally; another disjoint whole-fibre switch
cannot enlarge the block lattice.

## 5. The known `q=2` near-core macro is not alternating

Use the two eight-rail collections `A+`,`A-` from
`MATH_THEOREM_DISTANCE_ONE_NEAR_C_BRIDGE_Q2_POSITIVE_ONE_OWNER_COMMON_RESERVE_20260813.md`.
Suppress their common `(c-1)`-set `C_0`.  The owner current is exactly

\[
                         e_{012}.                    \tag{5.1}
\]

For `q=2`, the lower deck of a rail with reduced core `i` and toggle word
`(v_j)` consists of the reduced pairs `{i,v_j}`.  Direct reconstruction
gives the signed lower current

\[
\begin{aligned}
\lambda={}&02+04+05-07+08+12-14+16-17+18\\
          &-24+25-28+35-38-47-48-56+58.             \tag{5.2}
\end{aligned}
\]

It has

\[
                         \sum_L\lambda_L=1,
 \qquad                  \|\lambda\|_1=19.          \tag{5.3}
\]

More basically, the positive lower shore has `50` occurrences on only `34`
named lower sets, with maximum multiplicity three.  The negative lower
shore has `49` occurrences on only `35` named lower sets, with maximum
multiplicity two.  Hence neither is a lower matching.

The reduced point currents are

\[
 P_Oe_{012}=e_0+e_1+e_2,                             \tag{5.4}
\]

\[
 P_L\lambda=3e_0+e_1+e_2-3e_4+3e_5-3e_7.           \tag{5.5}
\]

They obey the signed version of the exact role identities:

\[
 P_Oe_{012}-P_L\lambda
 =-2e_0+3e_4-3e_5+3e_7,                              \tag{5.6}
\]

\[
 2P_L\lambda-P_Oe_{012}
 =5e_0+e_1+e_2-6e_4+6e_5-6e_7.                      \tag{5.7}
\]

These are respectively the signed support-degree and weighted-core-degree
currents of the two rail banks.  Every point of the suppressed `C_0`
contributes one additional unit to `(5.7)` and zero to `(5.6)`.

### Corollary 5.1 (coupled-boundary obstruction)

The `q=2` distance-one certificate is a positive simple **owner** absorber,
but it is not a positive alternating owner/lower absorber.  Relabelled
copies can absorb a prescribed alternating leave only after simultaneously
solving their induced lower-current equation.  Owner-unit spanning by
itself gives no such solution.  In fact, in every signed difference of rail
banks, the total owner current equals the total lower current because each
rail has equal owner and lower mass.  Hence an owner current of total mass
one necessarily carries a lower current of total mass one.

The exact computation is frozen by
`verify_q2_near_c_alternating_lower_current.py`.  The companion verifier
`verify_configuration_leave_interface.py` also exhausts the alternating
cut criterion through all bipartite graphs on at most `3+3` vertices,
checks the disjoint-block criterion on a finite model, checks the terminal
residue intervals through `q=64`, and replays this current.

There is a useful exact formulation of what this means for a fixed section
of owner macros.  Suppose one chooses one relabelled certificate `M_H` for
each owner in an index set `J`, with signed current

\[
                         M_H=(e_H,\lambda_H).         \tag{5.8}
\]

Let `Lambda:Z^J -> Z^L` have columns `lambda_H`.

### Theorem 5.2 (fixed one-owner macro graph)

A signed combination of this fixed macro family has owner/lower current
`(u,v)` if and only if

\[
                         v=\Lambda u.                \tag{5.9}
\]

Thus this family spans the graph of `Lambda`, not the full balanced
owner/lower current lattice.  For the displayed `q=2` certificate, trying
to absorb one owner together with one prescribed lower unit leaves lower
discrepancy

\[
                         e_L-\lambda_H               \tag{5.10}
\]

of total mass zero and `l1` norm at least `18`.

#### Proof

If the coefficient of `M_H` is `t_H`, its owner current is
`sum_H t_H e_H`.  Independence of the named-owner unit basis forces
`t_H=u_H`; the lower current is consequently `Lambda u`.  Conversely those
coefficients realize `(u,Lambda u)`.  In `(5.10)`, `lambda_H` has nineteen
coefficients in `{+1,-1}` and `l1` norm nineteen.  Subtracting one positive
unit can lower that norm by only one; all other choices do worse. \(\square\)

This does not rule out a richer catalogue containing several inequivalent
macros above the same owner unit: their owner-zero differences may generate
additional lower currents.  It identifies the exact extra atom needed to
improve the fixed construction—a nontrivial element of the kernel of the
owner projection whose lower current corrects `(5.10)`.  No such positive,
simple alternating near-core atom is presently proved.

## 6. Exact surviving gate

The strongest proved terminal route is therefore:

1. freeze a named-spread shell bank and include a token vertex for every
   shell;
2. prove a reserve-aware growing-rank configuration matching whose leave is
   a union of a bounded number of prescribed complete fibre blocks;
3. use Theorem 4.1 to switch those blocks; and
4. separately preserve non-alternating tickets and chronology.

The algebraic role and parity shape of such a leave is exact by Section 2,
and its final switch is exact by Section 4.  What remains open is the global
structured cover-down theorem.  A small arbitrary named leave, even one in
the full signed rail lattice, is not enough.
