# Zero-defect Pascal induction: particle budget, palette Euler law, and the common-cap obstruction

Date: 2026-07-31  
Status: exact scalar and palette theorems; exact conditional induction; the
uniform compatible routing/common-cap existence theorem remains open

## 0. Verdict

The arithmetic part of a zero-defect $k-2\to k$ induction is closed.
If the parent has deadline slack $\sigma$, the child slack is given by the
exact four-sector recurrence in Theorem 1.1 below.  For a fixed child
chronology, the only scalar charge is its deadline-particle loss.  Fragment
count and lower-$q_1$ pinning do not create additional scalar charges.

There are, however, two integral qualifications which prevent this from
being an unconditional proof of $\nu(k)=B(k)$.

1. The same occurrence-labelled braid must preserve all upper witnesses and
   admit a particle schedule whose loss is at most the child slack.
2. After every positional pin is installed, one *common* cap must realize all
   remaining lower targets and all middle owners simultaneously.

These qualifications cannot be separated by compiling the four Pascal
sectors independently.  The empty-tag sector has the positive deficiency in
Theorem 5.2, so cross-sector lower assignments are forced in every step.

There is also a parity correction.  In an odd child, a colour-simple
all-Johnson spanning owner path has exactly one lower-$q_1$ boundary hole.
In an even child, a $q_1$-complete all-Johnson spanning owner path necessarily has a Catalan
repeat reserve.  Thus an all-$k$ induction must not demand lower-$q_1$
rainbowness in even dimensions.

Theorem 6.1 gives the exact zero-defect induction package.  It proves an
optimal child word whenever the package exists.  Bare parent optimality and
the PBBS all-depth factor do not yet prove that the package exists.

## 1. Exact same-parity Pascal budget

Let the parent dimension be

\[
                         n=k-2,
\]

and put

\[
 q=\left\lceil\frac n2\right\rceil,
 \qquad W={n\choose q},
 \qquad \Lambda=\sum_{s=1}^{q-1}{n\choose s}.
\tag{1.1}
\]

Let $d=d(n)$ be the least integer for which

\[
                    dW+{d+1\choose2}\ge\Lambda,
\]

and write

\[
 \sigma=dW+{d+1\choose2}-\Lambda.
\tag{1.2}
\]

Set

\[
 \varepsilon=\mathbf 1_{\{k\text{ even}\}},
 \qquad c=\operatorname{Cat}_q=\frac1{q+1}{2q\choose q}.
\tag{1.3}
\]

The child middle rank is $R=q+1$.  Denote its middle width, lower census,
deadline depth and slack by $W_k,\Lambda_k,D,\sigma_k$.

### Theorem 1.1 (exact $k-2\to k$ scalar recurrence)

For $n\ge3$,

\[
 \boxed{W_k=4W-(1+\varepsilon)c},
 \qquad
 \boxed{\Lambda_k=4\Lambda+\varepsilon c+3}.
\tag{1.4}
\]

Define

\[
 \Gamma=\bigl[d+\varepsilon(d+1)\bigr]c
           +3{d+1\choose2}+3.
\tag{1.5}
\]

Then

\[
                         D\in\{d,d+1\},
\tag{1.6}
\]

with

\[
 D=d\quad\Longleftrightarrow\quad4\sigma\ge\Gamma,
\tag{1.7}
\]

and in both cases

\[
 \boxed{
 \sigma_k=4\sigma-\Gamma+(D-d)(W_k+d+1).}
\tag{1.8}
\]

#### Proof

Expanding the central binomial coefficient twice by Pascal gives the first
identity in (1.4).  Expanding the lower half of the Boolean lattice gives

\[
 \Lambda_k=4\Lambda+\varepsilon c+3,
\]

where the three extra targets are the nonempty subsets of the two new
coordinates and the Catalan correction occurs exactly for an even parent,
equivalently an even child.

Minimality of $d$ gives

\[
                 (d-1)W+{d\choose2}<\Lambda.
\]

After multiplying by four and using $W_k<4W$, this excludes child depth
$d-1$.  The standard central-binomial estimate in the proof of the
same-parity deadline recurrence shows that depth $d+1$ always suffices;
hence (1.6).  At unchanged depth, direct substitution of (1.4) gives

\[
 dW_k+{d+1\choose2}-\Lambda_k=4\sigma-\Gamma.
\]

Its sign decides whether depth $d$ suffices.  Raising the depth adds
exactly $W_k+d+1$ cells, proving (1.7)--(1.8).  This is the proof of
Theorem 5.1 in
`MATH_LANE_S_MONOTONE_DEADLINE_SCD_COMPILER_AND_DIAMOND_RECURSION_20260728.md`,
rewritten with the child dimension as the index. \(\square\)

Consequently a proposed four-sector chronology with exact particle loss
$\tau$ has enough scalar lower capacity at length $B(k)$ exactly when

\[
 \boxed{\tau\le\sigma_k},
\tag{1.9}
\]

or, equivalently,

\[
 \boxed{
 \Gamma+\tau\le
 4\sigma+(D-d)(W_k+d+1).}
\tag{1.10}
\]

The four literal cases are

\[
\begin{array}{c|c|c}
\text{child parity}&D&\text{maximum admissible }\tau\\ \hline
\text{odd}&d&4\sigma-dc-3{d+1\choose2}-3\\
\text{odd}&d+1&4\sigma-dc-3{d+1\choose2}-3+W_k+d+1\\
\text{even}&d&4\sigma-(2d+1)c-3{d+1\choose2}-3\\
\text{even}&d+1&4\sigma-(2d+1)c-3{d+1\choose2}-3+W_k+d+1.
\end{array}
\tag{1.11}
\]

The four calibration steps are

\[
\begin{array}{c|c|c|c|c}
\text{step}&d&D&\sigma&\sigma_k\\ \hline
15\to17&3&3&2928&7401\\
9\to11&2&3&0&369\\
12\to14&2&2&266&392\\
14\to16&2&3&392&12284.
\end{array}
\tag{1.12}
\]

## 2. The exact deadline-particle obstruction

Fix a proposed child middle chronology

\[
                  T=(T_0,\ldots,T_{W_k-1}).
\]

For nondecreasing start thresholds

\[
             0\le G_0\le\cdots\le G_{D-1}\le W_k,
\]

let $\rho_j^G(T)$ be the exact run frontier from Theorem 3.4 of the
deadline-staircase normal form, and put

\[
                       H^G_{j-1}=\rho_j^G(T)
                       \qquad(1\le j\le D).
\tag{2.1}
\]

The exact loss functional is

\[
 \operatorname{Loss}(G,H)=
   \sum_tH_t+\sum_t(W_k-G_t)
      +\#\{(t,u):G_t<H_u\}.
\tag{2.2}
\]

Define

\[
 \Phi_D(T)=
 \min_{\substack{G\text{ nondecreasing}\\
        (G,H^G)\text{ is legal and chain aligned}}}
      \operatorname{Loss}(G,H^G),
\tag{2.3}
\]

and set $\Phi_D(T)=+\infty$ if the displayed family is empty.

### Theorem 2.1 (sharp row-exact scalar-skeleton test)

The chronology's coordinatewise residence constraints admit a legal,
chain-aligned deadline-threshold skeleton with at least \(\Lambda_k\)
lower-cell identities at length $B(k)$ if and only if

\[
                         \Phi_D(T)\le\sigma_k.
\tag{2.4}
\]

For an actual nonempty word, every maximal envelope letter must additionally
be nonempty.  If the minimal thresholds $H^G$ fail that letter test, one
must optimize over larger legal $H$; their loss can only increase.

#### Proof

For fixed $G$, the arbitrary-start residence theorem says that
$H_{j-1}\ge\rho_j^G(T)$ is necessary and sufficient for every coordinate
run to have a legal residence position.  The vector $H^G$ is
coordinatewise minimal.  Both the first sum and the crossing term in (2.2)
are monotone when a deadline threshold moves right, so $H^G$ minimizes
loss for that $G$.  Minimizing over $G$ proves (2.3).

The complete lower atlas has size

\[
 D W_k+{D+1\choose2}-\operatorname{Loss}(G,H)
 =\Lambda_k+\sigma_k-\operatorname{Loss}(G,H).
\tag{2.5}
\]

It has at least $\Lambda_k$ lower-cell identities exactly when
(2.4) holds.  This is a cardinality statement, not local target
feasibility.  Nonempty envelope letters, Hall, and the integral common cap are
stronger conditions and are not asserted by the scalar calculation.
\(\square\)

For a literal geometry test, let \(\mathcal S_D(T)\) be the set of all
monotone threshold pairs \((G,H)\) which are legal and chain aligned, satisfy
every residence corridor, and whose maximal envelopes are nonempty and
reproduce every \(T_i\).  Define

\[
 \Psi_D(T)=
 \min_{(G,H)\in\mathcal S_D(T)}
       \operatorname{Loss}(G,H),
\tag{2.6}
\]

with value \(+\infty\) for an empty family.  The deadline and envelope
theorems give the exact uncapped geometry criterion

\[
 \boxed{\text{literal middle geometry and scalar capacity at }B(k)
        \iff \Psi_D(T)\le\sigma_k.}
\tag{2.7}
\]

Moreover \(\Phi_D(T)\le\Psi_D(T)\).  Thus
\(\Phi_D(T)>\sigma_k\) is already a solver-free no-go, while a passing
\(\Phi_D\) still requires the envelope test and the common cap.

Equation (2.3) is the first exact obstruction to a proposed Pascal braid.
PBBS all-depth support and the component-neutral colour count do not bound
it.  A seam creates or destroys at most one boundary run per coordinate,
but the absolute starts of those runs enter the frontiers, and the crossing
term in (2.2) is not additive across sectors.

## 3. Euler--palette conservation and the parity correction

Let $Q={k\choose R-1}$ be the size of the child lower-$q_1$ palette.
For a final chronology, let $J$ be its number of Johnson adjacencies and
let $\mu_C$ be the multiplicity of colour $C$.  Put

\[
 H=\#\{C:\mu_C=0\},
 \qquad E=\sum_C(\mu_C-1)^+.
\tag{3.1}
\]

### Lemma 3.1 (universal palette Euler law)

Always

\[
 \boxed{H-E=Q-J.}
\tag{3.2}
\]

If a cyclic all-Johnson chronology on $W_k$ owners is cut at $f$ old
edges and rejoined by seams of which $j$ are Johnson, then

\[
 \boxed{H-E=(Q-W_k)+f-j.}
\tag{3.3}
\]

#### Proof

Summing the colour multiplicities gives

\[
 J=\sum_C\mu_C=Q-H+E,
\]

which is (3.2).  After the cut-and-seam operation the number of Johnson
adjacencies is $W_k-f+j$, proving (3.3). \(\square\)

For an odd child $k=2s-1$, $Q=W_k$, so (3.3) becomes

\[
                         H-E=f-j.
\tag{3.4}
\]

If the output consists of $p$ path components and no cyclic component,
write $a$ for the number of added seams and
$\eta=a-j$ for its non-Johnson seams.  Edge counting gives
$f-a=p$, and hence $f-j=p+\eta$.  In particular, for one path,

\[
                         H=1+\eta+E.
\tag{3.5}
\]

Thus exact one-boundary-hole recycling is equivalent to

\[
                         \eta=0,\qquad E=0.
\tag{3.6}
\]

When the starting cyclic palette is exact, (3.6) says precisely that every
seam is Johnson and its colour set is the set of cut colours with one colour
$h$ omitted.

For an even child $k=2s$,

\[
 W_k-Q=\operatorname{Cat}_s.
\tag{3.7}
\]

An all-Johnson spanning path therefore satisfies

\[
 \boxed{H-E=1-\operatorname{Cat}_s.}
\tag{3.8}
\]

If it is $q_1$-complete, $H=0$, and hence necessarily

\[
 \boxed{E=\operatorname{Cat}_s-1.}
\tag{3.9}
\]

The Catalan number in (3.9) is $\operatorname{Cat}_s$, whereas the
same-parity scalar recurrence from an even parent uses
$c=\operatorname{Cat}_{s-1}$.  They are different quantities.
Repeated even-dimensional adjacency occurrences are not extra lower
targets.  Their cells are not contracted a second time; if locally feasible
for other labels, they remain in the residual compiler.  No reassignment is
automatic.  At \(k=16\), for example, the forced complete-path excess is
\(\operatorname{Cat}_8-1=1429\).

## 4. The component-neutral odd four-sector braid

Now specialize to an odd child

\[
                     k=2r+1,
 \qquad |\Omega|=2r-1.
\]

Put

\[
 M={2r-1\choose r},
 \qquad b=\operatorname{Cat}_r,
 \qquad N=M-b={2r-1\choose r+1}.
\tag{4.1}
\]

The four middle-owner sectors have sizes

\[
                    |A|=|X|=|Y|=M,
                    \qquad |U|=N.
\tag{4.2}
\]

The canonical PBBS source on $\Omega$ has states

\[
 B_i\in{\Omega\choose r-1},
 \qquad T_i=p(B_i)^c=B_i\cup B_{i+1}\in{\Omega\choose r}.
\tag{4.3}
\]

It supplies the exact identities

\[
 T_i\cap T_{i+1}=B_{i+1},
 \qquad V_i=T_i\cup T_{i+1},
\tag{4.4}
\]

where the $V_i$ cover every member of
$\binom{\Omega}{r+1}$ with load between one and three.  Its all-depth
flag theorem also supplies every correct lower and upper window before any
occurrence selection or cutting.

Select one occurrence of every distinct $V_i$, giving the $N$-owner
$U$-deck.  Suppose the tagged $A/X/Y$ residual graph is a coupled
balanced path factor in the following exact sense.

* For every \(Z\in{\Omega\choose r-2}\), choose exactly one compatible
  \(AA\)-edge \(A_iA_j\) of colour \(Z+xy\), with
  \(\deg_{AA}(i)\le2\).
* For every parent index \(i\), choose
  \(\alpha_i,\beta_i\in\{0,1\}\).  The value of \(\alpha_i\) chooses
  \(X_iX_{\operatorname{succ}(i)}\) at zero versus \(X_iA_i\) at one, and
  the value of
  \(\beta_i\) chooses \(Y_iY_{\operatorname{succ}(i)}\) versus
  \(A_iY_{\operatorname{succ}(i)}\), again at zero versus one.
* The cap/socket choices satisfy

\[
                 \deg_{AA}(i)+\alpha_i+\beta_i=2.
\tag{4.5}
\]

* The resulting graph is acyclic and every component has one \(X\)-endpoint
  and one \(Y\)-endpoint.

The first two bullets make the \(xy,x,y\) palettes exact.  The edge count
and endpoint balance then make the graph exactly $b$ path components.

### Theorem 4.1 (arbitrary-component neutral routing)

Let the selected $U$-deck be partitioned into any rainbow $c_U$-path
cover.  Orient and order the $b+c_U$ tagged and untagged paths cyclically.
Assume:

1. every added endpoint seam is a legal $00$-signature Johnson seam;
2. the $N-c_U$ internal $U$-colours and the $b+c_U$ seam colours are
   jointly distinct.

Then the result is a spanning Johnson cycle on the complete child middle
deck, and every child lower-$q_1$ colour occurs exactly once.  Opening any
one seam $e_*$ gives a spanning owner path with exactly one missing
lower-$q_1$ colour

\[
                         h=L(e_*).
\tag{4.6}
\]

There is no restriction $c_U\le b$.  That restriction belongs only to the
more specialized topology which inserts at most one $U$-path into each
Catalan macro gap.

#### Proof

The tagged residual factor already saturates the three tagged palettes.
The $U$-path cover contributes $N-c_U$ internal untagged colours.  A
cyclic order of $b+c_U$ paths has exactly $b+c_U$ added seams, so the
untagged count is

\[
                 (N-c_U)+(b+c_U)=N+b=M.
\tag{4.7}
\]

Joint injectivity therefore fills the complete untagged palette.  The
seams join every component into one cycle.  Opening $e_*$ deletes exactly
one edge and its unique colour, proving (4.6). \(\square\)

The three component counts here must not be conflated:

* the source PBBS has at most $\operatorname{Cat}_{r-1}$ cycles, with an
  exact action--angle census;
* $b=\operatorname{Cat}_r$ is the forced number of tagged residual macro
  paths;
* $c_U$ is the component count after selecting and rethreading the
  $U$-deck.

Theorem 4.1 cancels $c_U$ only in the lower-$q_1$ count.  Every pure-old
upper target must still retain a witness internal to one $U$-fragment, or
receive an explicit replacement witness.  PBBS all-depth support is a
source catalogue, not deletion-stable support under the occurrence
transversal and braid.

For the strict macro-gap topology, the more detailed signature ledger is

\[
 H_{00}-E_{00}=p+t+\eta,
 \qquad H_{\rm tag}-E_{\rm tag}=-t,
 \qquad H_{\rm all}-E_{\rm all}=p+\eta,
\tag{4.8}
\]

where $p$ is the number of output paths, $t$ is the number of tagged
Johnson joins, and $\eta$ is the number of non-Johnson joins.  Thus the
$U$-component count cancels even before injectivity is imposed.

## 5. Pins, the common cap, and the sector wall

For a legal particle schedule $(G,H)$, let $\mathcal C(G,H)$ be its
complete lower-cell atlas.  Equation (2.5) gives

\[
 |\mathcal C(G,H)|
  =\Lambda_k+\omega,
 \qquad
 \omega=\sigma_k-\operatorname{Loss}(G,H).
\tag{5.1}
\]

### Lemma 5.1 (pin contraction is scalar-neutral)

Let $\Pi$ be any injective family of $h$ compatible lower-target/cell
pairs.  Install their caps simultaneously, retain their positive OR
equalities, and delete their $h$ target and cell identities from the
residual assignment problem.  Then

\[
 \boxed{
 (|\mathcal C(G,H)|-h)-(\Lambda_k-h)=\omega.}
\tag{5.2}
\]

#### Proof

Both sides of the target/cell injection lose exactly $h$ identities.
\(\square\)

This identity applies to any compatible bank of structurally realized
$q_1$ targets and to an explicit repair pin for an opened colour $h$.
It does not assert that the pins compose.  After capping, all residual
domains must be rebuilt.  A multi-cell pin remains a protected positive
equation, and the residual assignment must pass the maximal-common-cap
criterion.  When $\omega=0$, every residual cell must be used: the final
common-cap injection is a bijection.

For the \(15\to17\) scalar calibration, the tail-start threshold choice
\[
             G=(W_{17},W_{17},W_{17}),\qquad
             H=(0,0,7401)
\]
has loss \(7401=\sigma_{17}\).  If a K17 chronology passes residence with
this choice, its full atlas has exactly \(\Lambda_{17}=65535\) cells.
After any compatible pin contraction the residual common cap is therefore
forced to be bijective.  This is a sharp integral gate, not spare scalar
capacity.

The exact common-cap obstruction is the conflict clutter of the master
compiler theorem.  After fixed-pin propagation, a target transversal is a
compiler if and only if it avoids all five types of bad event:

1. two targets choose the same cell;
2. a physical letter becomes empty;
3. a required middle bit is lost;
4. a selected residual-lower bit is lost;
5. a protected-pin bit is lost.

Ordinary Hall and scalar surplus do not exclude types 2--5.

### Theorem 5.2 (independent-sector compilation is impossible)

For the parent data in Section 1, give the empty-tag Pascal sector its own
isolated depth-$D$ band and even grant it the entire triangular boundary.
Its strict-lower target deficiency is

\[
 \boxed{
 \Delta_0=\Lambda+W-\left[D(W-c)+{D+1\choose2}\right]>0.}
\tag{5.3}
\]

More explicitly,

\[
 \Delta_0=
 \begin{cases}
 W+dc-\sigma\ge d(c-1)+1,&D=d,\\[1mm]
 (d+1)c-d-1-\sigma>0,&D=d+1.
 \end{cases}
\tag{5.4}
\]

Therefore at least $\Delta_0$ empty-status lower assignments must use
cross-status resources.  Four independent sector compilers cannot prove a
zero-defect induction.

#### Proof

The empty-status sector has $W-c$ middle owners and $\Lambda+W$
strict-lower targets.  An isolated depth-$D$ band and the entire triangular
boundary supply at most

\[
                       D(W-c)+{D+1\choose2}
\]

distinct lower cells, proving (5.3).  If $D=d$, substitute (1.2) and use
minimality of $d$, which gives $\sigma\le W+d-1$, to obtain the first
line of (5.4).  If $D=d+1$, the jump inequality $4\sigma<\Gamma$
gives the second line; the detailed integer estimate is Theorem 6.1 of the
same-parity deadline-recursion note. \(\square\)

## 6. Exact zero-defect induction theorem

Call a child construction a **zero-defect Pascal particle braid** if one
and the same occurrence-labelled choice supplies all of the following.

1. **Owner and upper closure.**  The final chronology enumerates every
   rank-$R$ owner once, and every target of rank greater than $R$ has a
   retained consecutive-owner witness.
2. **Parity-correct $q_1$ closure.**  In an odd child, the braid is the
   colour-simple one-hole path of Theorem 4.1.  In an even child, it is
   $q_1$-complete with the forced repeat reserve (3.9), or its explicitly
   listed holes are included in the lower compiler.
3. **Particle staircase.**  There are monotone thresholds $(G,H)$ which
   are chain aligned, satisfy every exact residence corridor, have nonempty
   maximal envelopes reproducing every middle owner, and obey
   
   \[
              \operatorname{Loss}(G,H)\le\sigma_k.
   \tag{6.1}
   \]
4. **Pins and one common cap.**  Every chosen positional pin is jointly
   admissible.  After its target/cell contraction and domain rebuild, one
   residual target injection satisfies the maximal-common-cap equations for
   every lower target, every middle owner, and every protected pin.

Once clause 4 is assumed for *all* lower targets, clause 2 is not needed for
the terminal universality implication.  It is retained because it is the
exact lossless lower-\(q_1\) transport invariant needed to make the Pascal
step regenerative and to keep the pin bank explicit.

### Theorem 6.1 (zero-defect $k-2\to k$ closure)

If a zero-defect Pascal particle braid exists in dimension $k$, then it
compiles to a universal word of length

\[
                         B(k)=W_k+D.
\]

Consequently

\[
                         \boxed{\nu(k)=B(k)}.
\tag{6.2}
\]

If the construction also outputs the occurrence, endpoint, protected-flag,
particle and common-cap data needed to repeat the same operation, it is a
regenerative $k-2\to k$ induction step.

#### Proof

Clause 3 gives a legal length-$B(k)$ staircase and its exact middle
envelopes.  Clause 4 and the maximal-common-cap theorem give nonempty
physical letters realizing every lower target and every middle owner.
Clause 1 supplies each upper target as a consecutive block of middle
owners.  Chain alignment transfers that block to one physical interval with
the same union.  Thus every nonempty subset of $[k]$ occurs.  The
monotone-deadline lower bound gives $\nu(k)\ge B(k)$, proving (6.2).
The regenerative statement is literal iteration of the supplied decorated
package. \(\square\)

### Corollary 6.2 (conditional all-$k$ odd-spine induction)

Assume one regenerative optimum package in an odd base dimension.  If every
odd $2r-1\to2r+1$ four-sector step satisfies Theorem 6.1 and every
intermediate odd-to-even facet step supplies the analogous parity-correct
package, then $\nu(k)=B(k)$ in every subsequent dimension.

The corollary is logically exact but conditional.  Its hypothesis is not
known uniformly.

## 7. The isolated exact obstruction

The proved PBBS theorem supplies, in every odd source dimension:

* the exact immediate lower palette;
* a load-\(1,2,3\) occurrence catalogue for every $U$-owner;
* complete lower and upper flags at every depth;
* an explicit action--angle component census.

It does **not** supply:

* a protected occurrence transversal retaining every deeper pure-old flag;
* the coupled acyclic $AA$/socket residual factor;
* endpoint routing with the joint colour injection in Theorem 4.1;
* a child chronology with particle loss at most $\sigma_k$;
* the post-pin common-cap transversal.

Thus parent equality $\nu(k-2)=B(k-2)$ is not itself a sufficient
induction hypothesis.  Within this Pascal/PBBS braid architecture, the
missing theorem is the nonemptiness of the joint decorated fibre

\[
 \boxed{
 \mathcal J_k=
 \mathcal F_{\rm endpoint/q1}
 \cap\mathcal F_{\rm protected\ upper}
 \cap\mathcal F_{\rm particle}
 \cap\mathcal F_{\rm common\ cap}.}
\tag{7.1}
\]

The first fixed-chronology solver-free scalar obstruction is

\[
                         \Phi_D(T)>\sigma_k.
\tag{7.2}
\]

Passing \(\Phi_D(T)\) does not yet give a physical staircase: the exact
uncapped geometry test is \(\Psi_D(T)\le\sigma_k\) from (2.7).  After that
test passes, the route can still fail protected upper/endpoint compatibility,
and every post-pin lower transversal can still contain one of the five exact
common-cap bad events.  The sector wall (5.3) proves that the compiler gate
must be genuinely cross-sector.

This isolates the current barrier for this architecture without charging PBBS component
count, the $U$-path count, or $q_1$ pin contraction as fictitious
additive defects.

## 8. Auditable dependencies

* `MATH_THEORY_K_ALL_DEADLINE_STAIRCASE_NORMAL_FORM_AND_O1_20260731.md`:
  particle normal form, exact loss, run frontiers and upper transfer.
* `MATH_THEOREM_K_ALL_FRAGMENT_BRAID_LOCALITY_AND_SERVICE_20260731.md`:
  endpoint locality and $H-E=f-j$ in the odd palette.
* `MATH_THEOREM_K_ALL_PBBS_BALANCED_SURJECTIVE_TWO_EXTENSION_20260731.md`:
  PBBS balanced two-extension and Theorem 2.1 all-depth flags.
* `MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`:
  coupled residual factor and component-neutral odd braid.
* `MATH_THEOREM_MASTER_STAIRCASE_PINNED_COMMON_CAP_COMPILER_20260731.md`:
  complete atlas, pin propagation and maximal-common-cap equivalence.
* `MATH_LANE_S_MONOTONE_DEADLINE_SCD_COMPILER_AND_DIAMOND_RECURSION_20260728.md`:
  same-parity recurrence and sector-local capacity wall.

The companion arithmetic verifier is
`scratch/audit_zero_defect_pascal_particle_braid_induction_20260731.py`.
Its frozen normalized output is
`scratch/zero_defect_pascal_particle_braid_induction_20260731.audit.json`,
with payload SHA-256
`6fb489f50fec796714f1f574f5517278ec0bec57851ca0da5f1ea9a7ae541a5f`.
