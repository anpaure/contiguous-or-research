# Thread D: regenerative Pascal buffers, exact lift recurrences, and a static-closure no-go

Date: 2026-07-28

Status: proved buffer calculus and obstruction theorem.  A precise
regenerative amplification lemma is isolated but not proved.

## 0. Outcome

Adding a finite scalar “safety margin” to the Pascal flag package does not
make the adjacent-row lifts closed.

There are two independent exact reasons.

1. Passage to the natural first-shadow shore consumes one absolute flag,
   endpoint, and residence level.  Along raw `k -> k+2` lifts the relative
   buffer decreases by at least one at every generation, and by two when
   the deadline rises.  A finite collection of finite-buffer bases therefore
   supports only finitely many raw lifts.
2. A uniform occurrence reserve cannot be regenerated.  In the standard
   `k -> k+2` Catalan `A`-forest, all `b-1` repeat edges are spent making the
   `b=C_r` components.  Every protected both-new immediate-lower target then
   has exactly one occurrence, and cross-sector seams have the wrong
   signature to create another.  Thus an invariant requiring even one spare
   occurrence per protected target fails after one lift.

The correct strengthened object is relational rather than scalar.  It must
carry a **safe-cut complex**: the actual residence-hazard transversal, the
actual all-depth occurrences protected from that transversal, the actual
`U` selector, compatible seam ports, and the common owner absorber.  To
support induction it must also regenerate such an aligned safe-cut atlas for
the child.  This last regeneration statement is a genuinely stronger open
theorem; it is not supplied by all-depth PBBS support, hypersimplex marginal
completion, or the existing one-step compiler theorem.

## 1. A quantitative buffered package

Let `k` be odd, let `d=d(k)`, and let `T` be the middle chronology of a
Pascal flag package.  We separate three absolute radii.

* `R_res` is the largest declared depth through which the chronology is
  lower-fresh.
* `R_end` is the depth through which the completed iterated lower rows and
  their endpoint rank tests are supplied.
* `R_port` is the depth through which every designated future cut has
  inward incidence words and nested lower/upper collar flags.

Put

\[
 R=\min(R_{\rm res},R_{\rm end},R_{\rm port}),
 \qquad \beta=R-d(k).
\tag{1.1}
\]

The nonnegative integer `beta` is the **relative radius buffer**.  Keeping
the three radii separate is useful when constructing examples; taking their
minimum is sufficient for the no-go and recurrence statements below.

The package also carries occurrence data.  For a row/target pair `(q,S)`,
let

\[
 \mathcal O_q(S)
\]

be the family of correctly ranked physical `q`-window occurrences of `S`.
For a contemplated lift, every occurrence is recorded with its **full root
support**: all parent vertices and transition slots needed to materialize
the child window.  Define its support-disjoint occurrence reserve by

\[
 \pi_q(S)=\nu\bigl(\mathcal O_q(S)\bigr),
 \qquad
 \pi_q=\min_S\pi_q(S).
\tag{1.2}
\]

where disjointness includes both vertices and transitions in those root
supports.  This convention is slightly stronger than edge-disjointness, but
it treats native edge cuts and `U`-selector vertex deletions uniformly.  The
symbol `q` may denote a lower row or, after complement duality, the
corresponding descending upper flag row.  Signature-specific rows and their
value maps will be displayed explicitly below.  A parent flag occurrence
and its lifted child window need not have the same support length, so their
reserves are never identified merely because their values agree.

The finite radii control the lower/endpoint band.  Complete package
preservation additionally keeps the occurrence ledger at **every** upper
depth; this all-depth ledger is separate from `R_port`.

Finally, an endpoint/seam buffer is not just a count.  It consists of
designated cut sites, oriented endpoint ports, their full radius-`R`
collars, and a list of permitted joins.  A join is called **transparent
through radius `R`** if it is Johnson, passes the global run test, replaces
every named occurrence lost at its two collars, preserves the nested
endpoint flags, and is admitted by the same common owner core.

## 2. Exact transport of the three radii

### Lemma 2.1 (one-level erosion law)

Fixed-tag transport preserves all three declared radii.  Natural
first-shadow transport on uncompleted interiors

\[
 T\longmapsto L^{(1)}(T)
\]

can certify only

\[
 (R_{\rm res},R_{\rm end},R_{\rm port})
 \longmapsto
 (R_{\rm res}-1,R_{\rm end}-1,R_{\rm port}-1)
\tag{2.1}
\]

without fresh surgery or rethreading.  The inserted completion vertex has
the same guarantee only when its endpoint rank tests and completed port
collars are imposed explicitly.  The loss is sharp.

#### Proof

An internal parent one-run of length `ell` becomes a first-shadow one-run of
length `ell-1`.  Thus parent lower-`R_res` freshness guarantees child
lower-`(R_res-1)` freshness.  A parent run of length exactly `R_res+1`
shows sharpness.

For flags and collars,

\[
 L_{L_T^{(1)}}^{(q)}=L_T^{(q+1)}.
\tag{2.2}
\]

Hence a child depth-`q` endpoint or port flag consumes parent depth `q+1`.
Fixed tags commute with every intersection and union, so they consume no
level.  \(\square\)

The natural upper row `U^(1)` does not repair this two-sided radius loss.
Its lower residence may improve, but its upper depth-`q` data require parent
upper depth `q+1`.  More importantly, an arbitrary one-representative
selector `U_*` is not a natural ordered `U^(1)` row and has no inherited
radius at all.

### Theorem 2.2 (sharp transport-only buffer recurrences)

Let an odd parent have deadline `d` and declared radius `R=d+beta`.
Assume every inserted completion vertex passes the endpoint rank and port
tests through the transported radius.

For odd-to-even, write

\[
 e=d(2r)=d-\delta,
 \qquad \delta\in\{0,1\}.
\]

If the same radius-`R` source feeds both shores, the transport-only child
certificate has

\[
 R_e^{\rm tr}=R-1,
 \qquad
 \boxed{\beta_e^{\rm tr}=\beta+\delta-1.}
\tag{2.3}
\]

With separate sources,

\[
 R_e^{\rm tr}=\min(R_A,R_B-1).
\tag{2.4}
\]

Thus a desired child buffer `a` requires

\[
 \beta_A\ge a-\delta,
 \qquad
 \boxed{\beta_B\ge a+1-\delta.}
\tag{2.5}
\]

For `k -> k+2`, write

\[
 d^+=d+\epsilon,
 \qquad \epsilon\in\{0,1\}.
\]

The eroded `A=xy+L^(1)` shore is the bottleneck, so

\[
 R_+^{\rm tr}=R-1,
 \qquad
 \boxed{\beta_+^{\rm tr}=\beta-1-\epsilon.}
\tag{2.6}
\]

For distinct sources and a desired child buffer `a`, the minimum raw
requirements are

\[
 \boxed{\beta_A\ge a+1+\epsilon,}
 \qquad
 \beta_X,\beta_Y\ge a+\epsilon,
\tag{2.7}
\]

plus a directly ordered `U`-shore certificate.

#### Proof

Equations (2.3)--(2.7) are Lemma 2.1 followed by subtraction of the child
deadline.  In the odd-to-even lift only `B` uses `L^(1)`, while `A` is the
unchanged `T` shore.  In the two-coordinate lift `A` uses `L^(1)` and
`X/Y` are fixed-tag copies of `T`.  The displayed equalities concern the
transported declared certificates and assume the explicit completion tests;
they do not claim that the chronology's true maximal radius cannot be
larger.  \(\square\)

The minimum radius amplification required to preserve a fixed relative
buffer is therefore

\[
 g_{\rm OE}=1-\delta\in\{0,1\},
 \qquad
 \boxed{g_{+}=1+\epsilon\in\{1,2\}.}
\tag{2.8}
\]

These are minimum gains beyond literal row transport.  They do not include
occurrence, port, or owner regeneration.

### Corollary 2.3 (finite raw-buffer no-go)

Let `k_i=k_0+2i`, `d_i=d(k_i)`, and let `beta_i` be the relative radius
certified by repeated transport-only `k -> k+2` lifts.  Then

\[
 \boxed{
 \beta_n\le\beta_0-n-(d_n-d_0)\le\beta_0-n.}
\tag{2.9}
\]

Consequently no finite family of finite-buffer base packages supports all
odd dimensions by the raw adjacent-row functor.

#### Proof

Sum (2.6) over the `n` lifts; the deadline increments telescope.  A finite
base family has a finite maximum initial buffer, so the right side is
negative for all sufficiently large `n`.  Odd-to-even steps do not restore
the odd lineage: by (2.3) they either preserve the relative buffer when the
deadline drops or consume one unit when it does not.  \(\square\)

By Stirling's formula,

\[
 d(2r-1)\sim\frac{\sqrt{\pi r}}2,
\]

so deadline rises occur infinitely often.  This is not needed for the
no-go—the compulsory `-n` term already suffices—but it shows that the extra
losses in (2.9) are also unbounded.

## 3. The exact cut cost of radius amplification

The loss in Lemma 2.1 can be repaired only by cutting or rethreading the
short eroded runs.

For an intended child absolute radius `D`, form the interval family

\[
 \mathcal H_D(T)
\tag{3.1}
\]

as follows.  Put `C_i=T_i intersection T_(i+1)`.  For every internal parent
coordinate run `[a,b]`, with `1<=a<=b<=W-2` and length
`2<=ell=b-a+1<=D+1`, take

\[
 I_z(a,b)=
 \{C_{a-1}C_a,C_aC_{a+1},\ldots,C_{b-1}C_b\}.
\tag{3.1a}
\]

This is the native first-shadow edge interval containing the resulting
eroded run.  Let

\[
 \tau_D(T)
\]

be the minimum size of a transversal of this interval family.  Since these
are intervals on a line, `tau_D(T)` is also its maximum edge-disjoint packing
number.

### Theorem 3.1 (minimum internal amplification budget)

A set of native first-shadow cuts produces pieces whose internal runs are
all lower-`D`-fresh if and only if it meets every member of
`H_D(T)`.  Hence the minimum number of cuts is exactly `tau_D(T)`.

#### Proof

A parent run of length `ell` becomes an eroded run of length `ell-1`.
It violates child lower-`D` freshness exactly when `ell-1<D+1`, i.e.
`ell<=D+1`.  If no native edge in its hazard interval is cut, the entire
short run remains inside one piece, possibly reversed.  Conversely, cutting
one edge in every hazard interval prevents every such run from remaining an
internal run.  Interval transversal equals interval packing by the greedy
right-endpoint theorem.  \(\square\)

This theorem addresses only piece interiors.  The exposed terminal and
initial runs must still be paired so every maximal run crossing one or more
seams has total length at least `D+1`.

### Corollary 3.2 (minimum architecture-specific repair conditions)

Suppose a fixed relative buffer is to be preserved.

1. In a same-deadline odd-to-even six-piece lift, the two native `B` cuts
   must hit every parent run of length `R+1`; in particular
   \[
   \boxed{\tau_R(T_B)\le2.}
   \tag{3.2}
   \]
   When the deadline drops, no internal `B` amplification is needed.
2. In a no-rise `k -> k+2` lift, the `A` cuts must hit every run of length
   `R+1`.
3. At a deadline rise, the `A` cuts must hit every run of lengths `R+1` and
   `R+2`, and `X/Y` routing must cut or extend every inherited run of length
   `R+1`.

In the native Catalan `A`-forest architecture, the first of the two-coordinate
conditions gives the necessary bound

\[
 \boxed{\tau_{R+\epsilon}(T)\le C_r-1,}
\tag{3.3}
\]

with the indexing convention of (3.1).

The content of a radius-amplification lemma is not merely (3.3): its chosen
hazard transversal must also be occurrence-safe, port-compatible, and
owner-compatible.

## 4. Occurrence reserves are safe-cut complexes

For a row `R` and protected depth range `q<=H`, define

\[
 \boxed{
 \mathfrak C_H(R)=
 \left\{C\subseteq E(R):
  \forall q\le H\ \forall S\ 
  \exists P\in\mathcal O_q(S)\text{ with }P\cap C=\varnothing
 \right\}.}
\tag{4.1}
\]

This is a downward-closed **safe-cut complex**.  Named seam replacements can
be incorporated by allowing the final alternative in (4.1) to be a listed
new seam window, provided the join plan and replacement list are fixed
independently of `C`.  If replacements are chosen adaptively as a function
of `C`, the feasible cut family need not be downward closed and will be
called a safe-cut system rather than a complex.

### Lemma 4.1 (exact reserve degradation)

If the disruption set contains `J_e` transition edges and `J_v` row
vertices, then

\[
 \#\{\text{destroyed depth-}q\text{ occurrences}\}
 \le qJ_e+(q+1)J_v,
\tag{4.2}
\]

\[
 \#\{\text{new depth-}q\text{ holes}\}
 \le qJ_e+(q+1)J_v,
\tag{4.3}
\]

and, for every target,

\[
 \boxed{
 \pi_q^{\rm surviving}(S)\ge\pi_q(S)-J_e-J_v.}
\tag{4.4}
\]

Likewise, `J_s` new seams create at most `qJ_s` new depth-`q` occurrences.

#### Proof

A transition edge belongs to at most `q` windows of `q` edges, and a row
vertex belongs to at most `q+1`, giving (4.2)--(4.3).  Take a maximum
support-disjoint occurrence family for `S`.  Each disrupted edge or vertex
meets at most one member, so (4.4) follows.  The new-seam statement is the
same window count.  Cyclic boundaries, multi-seam windows, and reversal do
not change the argument.  \(\square\)

The scalar

\[
 \rho_H(R)=\min_{q\le H,S}\pi_q(S)-1
\tag{4.5}
\]

guarantees that every cut set of size at most `rho_H` lies in
`C_H(R)`.  It forgets the correlations that make a particular much larger
cut set safe, and is usually zero.

### 4.2 Exact odd-to-even occurrence recursion

Let `c_A,c_B` be the numbers of native cuts in the two shores.  Away from
completion collars, child depth `q` uses the following parent rows:

\[
\begin{array}{c|cc}
 &\text{child lower value}&\text{child upper dual value}\\ \hline
 A&L^{(q)}&F^{(q+1)}\\
 B&L^{(q+1)}&F^{(q)}.
\end{array}
\tag{4.6}
\]

For each entry let

\[
 \widehat\pi_{A,-}(q),\widehat\pi_{A,+}(q),
 \widehat\pi_{B,-}(q),\widehat\pi_{B,+}(q)
\]

denote the support-disjoint reserve of the **full lifted child-window root
supports before cutting**.  These quantities are not automatically equal to
the reserve of the shorter parent flag row: a lifted window may use one
extra parent edge.  Lemma 4.1 gives the valid recurrences

\[
\begin{array}{c|cc}
 A&\widehat\pi_{A,-}(q)-c_A&\widehat\pi_{A,+}(q)-c_A\\
 B&\widehat\pi_{B,-}(q)-c_B&\widehat\pi_{B,+}(q)-c_B.
\end{array}
\tag{4.7}
\]

In the six-piece braid, `c_A=c_B=2`.  Selector-blind preservation of reserve
`a` therefore requires each relevant **lifted-support** reserve to be at
least `a+2`.  A row-value multiplicity alone does not certify this.

There is an exact protected-signature obstruction.  Every mixed seam window
contains both an `A` vertex, without `z`, and a `B` vertex, with `z`.
Consequently its intersection never contains `z` and its union always
contains `z`.  Hence

* `z`-lower `B` flags receive no seam rescue;
* no-`z` upper `A` flags receive no seam rescue.

Their two source cuts must preserve an internal occurrence or the endpoint
compiler must absorb the lower target.

### 4.3 Exact `k -> k+2` occurrence recursion

In the native `U Y A X` block skeleton the row shifts and disruptions are

\[
\begin{array}{c|cc|c}
\text{sector}&\text{child lower value}&\text{child upper dual value}
 &\text{native disruption}\\ \hline
A&L^{(q+1)}&F^{(q)}&b-1\text{ edge cuts}\\
X,Y&L^{(q)}&F^{(q+1)}&b-1\text{ edge cuts each}\\
U&L^{(q-1)}&F^{(q+2)}&b\text{ deleted vertices/indices},
\end{array}
\tag{4.8}
\]

where `b=C_r`.  The `b-1` count uses linear source paths partitioned into
`b` nonempty blocks.  A cyclic source needs `b` cuts unless one is identified
with the final global opening.  The `U` line presupposes a selector which
retains native cyclic order and preserves the full lifted supports; without
that hypothesis there is no inherited lower bound at all.

Using shore-specific lifted-support reserves as in (4.7), robust preservation
of reserve `a` requires margin `a+b-1` on linear `A/X/Y` and `a+b` on the
vertex-disjoint `U` supports.  These are support-margin requirements, not
identities between parent row multiplicity and child reserve.

The cross-sector seam signatures are

\[
\begin{array}{c|cccc}
\text{seam}&UY&YA&AX&XU\\ \hline
\text{intersection tags}&\varnothing&\{y\}&\{x\}&\varnothing\\
\text{union tags}&\{y\}&\{x,y\}&\{x,y\}&\{x\}.
\end{array}
\tag{4.9}
\]

Thus cross-sector seams never repair both-new lower `A` flags and never
repair empty-signature upper `U` flags.  Those two families must survive the
native cuts/selector internally.

## 5. A sharp saturation obstruction in the Catalan `A` shore

### Theorem 5.1 (zero spare occurrence after Catalan batching)

Let the completed first-shadow path `Q` have `W` vertices and suppose its
edge intersections cover all rank-`r-2` targets.  Put

\[
 b=C_r,
 \qquad
 \binom{2r-1}{r-2}=W-b.
\tag{5.1}
\]

The native Catalan `A`-forest retains one edge of each rank-`r-2` colour.
It has `b` components, deletes exactly `b-1` edges, and every retained
colour occurs exactly once **inside the retained forest**.  After adjoining `x,y`, every both-new
immediate-lower child target has exactly one internal occurrence and no
cross-sector seam occurrence.

#### Proof

The path `Q` has `W-1` edges and there are `W-b` required colours.  Complete
support therefore has total repeat excess

\[
 (W-1)-(W-b)=b-1.
\]

Retaining one edge per colour keeps `W-b` edges and deletes precisely the
entire `b-1` excess budget.  A forest on `W` vertices with `W-b` edges has
`b` components.  Each retained edge has a different colour by construction.
Finally, (4.9) shows that no cross-sector lower seam has tag `{x,y}`.
\(\square\)

### Corollary 5.2 (no positive uniform reserve invariant)

No strengthened package which requires even one spare occurrence of every
protected first-shadow target is closed under the standard `k -> k+2`
lift.

More strongly, every future `A` cut must be aligned with the complement of
the retained one-edge-per-colour forest.  The residence-amplification problem
is therefore the joint system

\[
 \boxed{
 C_A\text{ hits every member of }\mathcal H_D(T),
 \qquad
 C_A\in\mathfrak C_H^{A,{\rm prot}}(Q;\mathcal N),
 \qquad |C_A|=b-1.}
\tag{5.2}
\]

Here the protected/replacement-aware system requires internal survival only
for the signatures which cross-sector seams cannot repair, while crediting
the fixed named seam replacements `N` for the others.  Requiring the full
`C_H(Q)` would be a stronger sufficient condition.  The joint condition
cannot be certified by the separate inequalities
`tau_D<=b-1` and `pi_q>=1`.

The obstruction is not peculiar to PBBS.  More generally, a cyclic
lower-rainbow odd carrier has `W` first-shadow targets and `W` cyclic edge
occurrences, so every target occurs exactly once.  On the immediate upper
side there are `W` windows and `W-b` targets.  Complete support has excess
`b`, hence at least

\[
 (W-b)-b=W-2b
\]

upper targets are also singletons.  Uniform two-occurrence protection is
therefore unavailable even before a cut is selected.

PBBS adds a quantitative all-depth warning:
its canonical correct depth-`q` load satisfies

\[
 \mu_q(S)\le\binom{2q+1}{q}=\exp(O(q)),
\tag{5.3}
\]

which is `o(b)` for `q<=A sqrt(r)`.  Thus it cannot provide robustness
against arbitrary Catalan-many cuts.

At depth one the singleton obstruction has positive density.  If `a_j`
counts PBBS targets of load `j in {1,2,3}`, then

\[
 a_2+2a_3=\frac{2W}{m+2},
 \qquad
 a_1\ge\frac{m-2}{m+2}W=W-O(W/m).
\tag{5.4}
\]

Only `O(b)=O(W/m)` seam windows are available at depth one, so a Catalan
braid cannot amplify the minimum first-shadow reserve from one to two.

## 6. Endpoint and seam buffer accounting

Scalar window counts have a small positive surplus, but it is not an
occurrence injection.

### Proposition 6.1 (six-piece scalar collar identity)

Cut two length-`W` source paths into six pieces of lengths
`ell_1,...,ell_6`, and put

\[
 I_q=\sum_{i=1}^6(\ell_i-q)^+.
\]

Relative to the two uncut paths, the number of lost internal windows is

\[
 L_q=2(W-q)-I_q.
\]

The concatenated child path has

\[
 N_q=2W-q-I_q=L_q+q
\tag{6.1}
\]

new seam-crossing windows.

#### Proof

The two uncut paths have `2(W-q)` windows; the child length-`2W` path has
`2W-q`.  Subtract `I_q` in both cases.  \(\square\)

### Proposition 6.2 (four-sector scalar collar identity)

For four source paths whose lengths sum to `W^+` and are all longer than
`q`, let `I_q` be the number of windows retained inside their eventual
pieces.  Then

\[
 L_q=(W^+-4q)-I_q,
 \qquad
 N_q=(W^+-q)-I_q=L_q+3q.
\tag{6.2}
\]

The `q` and `3q` surpluses are the exact scalar seam buffers.  They do not
match a lost target to a seam target, respect the protected signatures in
(4.9), or prove endpoint containment.

This proposition is deliberately idealized: it assumes four genuine ordered
source paths, including an ordered `U` path.  A bare one-representative
`U_*` selector does not satisfy its hypotheses.

A flat literal word has only two nested endpoint chains.  At depth `q` they
supply at most `2q` boundary cells, and at the first lower row each end can
realize at most one distinct missing target.  Therefore every lift must
repair all but `O(q)` collar losses internally.  There is no growing unary
endpoint reserve to offset Catalan-many arbitrary losses.

If a bank contains `p` unused reversible ports, a lift consumes `J` of them,
all `p-J` unused ports remain valid after fixed-tag transport and imposition
of the new common owner core, and `a` new seams are themselves proved
transparent and reversible, then

\[
 \boxed{p'\ge p-J+a.}
\tag{6.3}
\]

Keeping a fixed port buffer requires at least `a>=J`.  Without the explicit
transport hypothesis on the unused ports, no positive lower bound follows
from counts alone.  The signature and owner conditions in the definition of
transparency are essential; merely creating `J` Johnson seams does not prove
(6.3) with `a=J`.

## 7. Owner reserves are not scalar

Let `E_p` be a maximal source envelope.  Even two separately harmless owner
cuts need not remain harmless together:

\[
 E_p=\{1,2\},\qquad O_1=\{1\},\qquad O_2=\{2\}
\]

have nonempty separate cores and empty common core.  Hence neither a count
of unused owner slots nor separate sector Hall slack is a closed invariant.

The owner component of a regenerative package must be an actual absorber
bank: for every permitted seam/collar choice it names the combined active
owners and verifies

\[
 C_p=E_p\cap\bigcap_{S:p\in I_S}S\ne\varnothing,
\]

all central private hits, all target private hits, and meet dimension at
most two.  A future port is owner-safe only relative to this combined bank.

The hypersimplex theorem removes rankwise marginal balancing from this
discussion: it gives hole-free degree-matched rows separately.  It does not
couple those rows to a deletion chronology or to the common owner cores.

## 8. The minimal regenerative invariant

The preceding theorems identify a non-scalar candidate.  A
**regenerative buffered Pascal frame** at odd dimension `k` consists of:

1. a Pascal flag package with declared radii and relative buffer `beta`;
2. the full protected occurrence families and safe-cut complexes, not only
   their minimum multiplicities;
3. an `A` hazard transversal satisfying (5.2), safe `X/Y` cuts, and an
   occurrence-preserving ordered `U` selector;
4. oriented ports whose multi-piece run sums meet the desired child radius;
5. exact all-depth seam replacement maps and compatible nested endpoints;
6. one common owner absorber for every selected lower/seam/boundary pin;
7. a regenerated safe-cut, port, and owner atlas on the odd child.

Items 1--6 are a sharpened one-step lift frame.  Item 7 is the new
reproductive content: without it, the definition merely repackages the
one-step certificate theorem.

### Theorem 8.1 (minimum amplification quotas)

Any lemma which maps a fixed-buffer regenerative frame to another frame
with the same thresholds must supply at least:

\[
 g_{\rm OE}=1-\delta
\]

new radius units on a recursively used odd-to-even step, and

\[
 \boxed{g_+=1+\epsilon}
\]

new radius units on every `k -> k+2` step.  Selector-blind preservation of a
fixed occurrence reserve would additionally require the relevant lifted
source-support margins to exceed the desired child reserve by `b-1` on each
linear native `A/X/Y` row and by `b` on the native-order, vertex-disjoint
`U` supports.  A fixed port bank must create at least as many transparent
new ports as it consumes.

The scalar occurrence quota is impossible in the standard Catalan `A`
shore by Theorem 5.1.  Therefore any viable amplification theorem must use
the cut-specific safe complexes rather than uniform redundancy.

#### Proof

The radius quotas are (2.8).  The occurrence quotas are Lemma 4.1 applied to
the disruption counts in (4.8).  The port quota is (6.3).  The impossibility
is Corollary 5.2.  \(\square\)

### Theorem 8.2 (finite-base eventual induction, conditional form)

Suppose there are fixed interface thresholds and an integer `k_0` such that:

1. a finite family of regenerative buffered Pascal frames covers the needed
   odd base states at `k_0`; and
2. for every odd `k>=k_0`, an aligned amplification theorem constructs from
   one base state a `k -> k+2` child frame with the same thresholds, while
   the terminal odd-to-even theorem constructs an exact even package.

Then `nu(k)=B(k)` for every `k>=k_0`.

#### Proof

Induct on the odd dimensions using the regenerative `k -> k+2` output.
Package sufficiency gives the exact odd word at every stage.  Apply the
terminal odd-to-even theorem at each stage for the intervening even
dimension.  \(\square\)

This logical induction is valid, but its second hypothesis is not presently
proved.  Theorem 8.1 shows why no lemma controlling only scalar depth,
repeat totals, or targetwise minimum multiplicity can provide it.

## 9. Sharp remaining theorem

The smallest plausible amplification statement within the current
adjacent-row architecture is now the following.

> **Aligned regenerative cut/selector theorem (open).**  For every odd
> buffered package in the induction class, choose the `b-1` deleted native
> `A` edges, the `X/Y` cuts, and the `b` omitted `U` indices so that:
>
> 1. the `A` deletions hit every short-run hazard required by the next
>    radius, while retaining one protected occurrence of every both-new
>    lower flag;
> 2. the `U` selector retains an occurrence interval for every protected
>    empty-signature upper flag;
> 3. all remaining signed flag occurrences survive their sector cuts or
>    receive a signature-compatible seam replacement;
> 4. the oriented ports pass every multi-piece residence inequality and
>    carry compatible nested endpoint flags;
> 5. the combined seam, boundary, spill, and deep pins pass one trace-two
>    owner realization; and
> 6. the child contains another cut/selector/owner atlas satisfying the same
>    conditions at its next deadline.

The first five clauses would close one lift.  Clause 6 is exactly what turns
the result into induction.  Existing PBBS all-depth support proves that the
occurrence families in clauses 1--3 are nonempty; it does not align them
with the residence transversals.  Hypersimplex completion proves separate
rankwise feasibility; it does not produce clauses 4--6.

Accordingly, a finite base family plus the **present** lifts does not yield
unconditional eventual induction.  It would do so after the aligned
regenerative theorem above, but a static numerical buffer cannot substitute
for that theorem.
