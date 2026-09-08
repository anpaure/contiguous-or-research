# Thread D: the cut-specific safe complex, decorated connector links, and the extreme-shore link-zero obstruction

Date: 2026-07-28

Status: theorem-level structural reduction, with an exact link-zero
obstruction to the internally protected native `k -> k+2` cut-extension
mechanism.  The theorem below gives genuine link/contraction closure.  It
does **not** assert that the required residual link is nonempty, and it
leaves an explicit endpoint/compiler escape.

## 0. Result

The object forced by the static-buffer no-go is not one simplicial complex
on raw cut edges.  The requested conditions have incompatible
monotonicities:

* survival of protected flag occurrences is downward-closed in the cut set;
* cutting every short-run residence hazard is an upward-closed transversal
  condition;
* choosing one `U` representative in every value fibre is a base condition;
* joining all pieces into one oriented path is a port-degree/base condition;
* assigning all owner pins and private hits is a matching/base condition.

The exact reusable object is therefore a **fibre of complex--clutter
systems over complete decorated bases**

\[
 \boxed{
 \mathfrak S
 =\{(\Theta,\mathcal K_\Theta,\mathcal H_D(\Theta)):
                         \Theta\in\mathscr B\}.}
\tag{0.1}
\]

Here \(\mathscr B\) is the set of complete decorated base states: each
\(\Theta\)
already contains its `U` selector, oriented path ports, endpoint chains,
flag witnesses, and one common owner table.  Relative to such a valid
baseline, \(\mathcal K_\Theta\) is the downward complex of optional closed
connector switches which preserve those data, and
\(\mathcal H_D(\Theta)\) is the clutter of
future residence hazards which the optional switches must hit.  After a
partial optional choice, the residual problem is exactly a link of
\(\mathcal K_\Theta\) together with the unhit hazards.  Building
\(\Theta\) from scratch is a separate base problem and is not falsely
declared simplicial.

At first shadow this system can be calculated completely.  If `E_S` is the
set of path edges of lower colour `S`, then

\[
 \mathcal K_1
 =\{C:|C\cap E_S|\le |E_S|-1\text{ for every }S\}
\tag{0.2}
\]

is a partition-matroid complex.  For a completed first-shadow path with
`W-1` edges and `W-b` colours, its rank is exactly `b-1`.  The Catalan
`A`-forest deletes `b-1` safe edges, hence is a base, and

\[
             \operatorname{lk}_{\mathcal K_1}(C_A)=\{\varnothing\}.
\tag{0.3}
\]

This is the sharp form of the **internally protected occurrence** saturation
obstruction.  Ordinary cross-sector seam windows make no same-signature
occurrence contribution: their intersections never contain both new
coordinates, so they cannot replace a protected both-new lower `A`
occurrence.  Dually, a
one-representative `U` selector is
a base of the corresponding deletion-on-value-fibres partition matroid.
Its deletion link is zero; ordered empty-signature upper constraints only
shrink the admissible bases, while ordinary cross-sector seam unions never
have empty new-coordinate signature.

Consequently the standard native `k -> k+2` lift does not preserve a
positive-rank `A` cut-extension atlas which insists that every both-new
first-lower colour remain internally witnessed; the exact `U` deletion base
also has zero extension rank.  This does **not** yet prove that the full
decorated `A` fibre has rank zero, because a newly missing lower colour might
be paid for by a compatible endpoint/compiler cell.  A regenerative theorem
must therefore create same-signature internal switches, rethread the child
chronology, or prove a cut-specific regenerating endpoint/compiler absorber.

The exact `k=11,13,14` certificates calibrate the base side of (0.1):

* `k=11` is a complete base made by one decorated opening;
* `k=13` is a complete base made by a joint two-cut/oriented-port/seam
  choice;
* `k=14` is a complete base made by a four-cut, five-seam braid.  In the
  audited `B-A-B-A-B` five-piece schema, one `A` cut cannot repair the two
  unique colours lost at the fixed `B` ear.

They prove that particular elements of \(\mathscr B\) exist.  They do not
prove that any corresponding \(\mathcal K_\Theta\) has a regenerative link.
In particular,
none of these exact constructions realizes the ordered `U` selector of the
same-parity lift.

## 1. Exact decorated states and the all-depth ledger

Let `F` be a directed Johnson cycle factor or path family.  For sign
`epsilon in {-,+}`, depth `q`, and target `S`, let

\[
 \mathcal O_F^-(q,S)
 =\{\text{old consecutive }(q+1)\text{-vertex windows with intersection }S\},
\]

\[
 \mathcal O_F^+(q,S)
 =\{\text{old consecutive }(q+1)\text{-vertex windows with union }S\}.
\tag{1.1}
\]

A **decorated splice state** is

\[
 \Theta=(C,\zeta,\sigma,J,\mathcal E,\mathcal W,\phi).
\tag{1.2}
\]

Its entries are as follows.

* `C` contains every native transition cut and every native vertex/index
  deletion.
* `zeta` is the ordered `U` selector when that sector is present.
* `sigma` orders and orients the surviving segments.
* `J` is the set of new Johnson seams.
* `E` is the pair of nested endpoint flag chains and their boundary cells.
* `W` names a retained or new witness for each protected signed target.
* `phi` is one common lower-target/owner pin table, including seam and
  boundary pins.

Write `X_C` for the old windows meeting a disruption.  Partition the final
windows into those lying wholly inside one surviving old segment and those
crossing at least one new seam.  Let `N_Theta^epsilon(q,S)` be the latter
windows of value `S`.  Then the exact load is

\[
 \boxed{
 m_\Theta^\epsilon(q,S)
 =|\mathcal O_F^\epsilon(q,S)\setminus\mathcal X_C|
  +|\mathcal N_\Theta^\epsilon(q,S)|.}
\tag{1.3}
\]

This formula counts a multi-seam window once.  It must not be replaced by a
sum of `q` local contributions per seam.  The distinction is already real
in the exact `k=14` braid: its reversed `B_2` piece has three vertices while
the upper audit runs through depth seven.  Any new adjacency created by
skipping deleted `U` indices is classified as a new seam here; it is not
silently credited as an old internal window.

For the common owner table, let `E_p` be the maximal envelope at word
position `p`, and let `I_S` be the interval assigned to lower target `S`.
Put

\[
 M_p=E_p\cap\bigcap_{S:p\in I_S}S.
\tag{1.4}
\]

The exact private-hit conditions are

\[
 M_p\ne\varnothing,
 \qquad
 \bigcup_{p=i}^{i+d}M_p=T_i,
 \qquad
 \bigcup_{p\in I_S}M_p=S,
\tag{1.5}
\]

together with the declared meet-dimension bound.  Separate owner solutions
on different sectors do not imply (1.4)--(1.5).

### Proposition 1.1 (decorated-state criterion)

The state `Theta` gives a strict Pascal flag package at the child deadline
`d` if the following five finite conditions hold.

1. The segments ordered by `sigma`, together with `J`, form one Johnson
   path with the prescribed middle deck.
2. Every internal coordinate run, including every run assembled across one
   or several seams, has length at least `d+1`.
3. For every protected signed target not assigned to an endpoint cell,
   `m_Theta^epsilon(q,S)>=1` at its exact depth.  The audit is made through
   all required upper depths, not only through the residence radius.
4. The endpoint targets assigned in `E` lie in the actual two nested
   endpoint chains with their containment and capacity constraints.
5. The single table `phi` satisfies (1.4)--(1.5), central and target private
   hits, and the required owner meet-dimension bound.

Conversely, every strict package obtained by cutting and reconnecting the
fixed source segmentation determines such a state.

#### Proof

Condition 1 is the literal middle-row requirement.  Condition 2 is the
coordinatewise residence criterion.  Equation (1.3) partitions every final
flag window, so conditions 3--4 are exactly lower/upper support including
the two boundary chains.  Conditions (1.4)--(1.5) are the negative and
positive parts of the common compiler pins.  These are precisely the
finite hypotheses in the fixed-middle realization theorem.  Conversely,
read the cuts, oriented segments, seams, endpoint chains, chosen occurrence
witnesses, and owner table from a finished package.  \(\square\)

The proposition is a certificate test.  It does not assert existence of a
state.

## 2. Why the requested joint family is not a simplicial complex

### Proposition 2.1 (opposite monotonicities)

There is no faithful formulation in which a face is merely a set of raw
cut edges jointly satisfying residence, exact `U` selection, path ports,
and complete owner assignment.

#### Proof

Occurrence survival is preserved when cuts are removed.  In contrast, a
residence hazard `I` imposes `C cap I != empty`, which can fail when a cut is
removed.  A `U` selector requires exactly one retained representative in
each fibre.  A connector path requires exact endpoint degrees and the
absence of an extra cycle.  The owner table is a complete matching/private-
hit base.  None of the latter three conditions is hereditary under taking
subsets.  \(\square\)

The two-edge minimum example already suffices.  Let a protected colour have
occurrences `e_1,e_2`, and let the residence hazards force deletion of
`e_1`.  The current state may delete `e_1`, but the empty deletion fails
residence.  If the next generation forces deletion of `e_2`, each generation
separately has a safe cut while their union destroys the colour.  Thus even
the smallest two-generation problem is a complex--clutter problem, not a
complex.

There is a physical version inside the exact `k=14` certificate.

### Theorem 2.2 (exact two-repair lower bound in the audited `k=14` five-piece schema)

Fix the two `k=13` resident, all-upper path-carrier shores used by the strict
`k=14` construction.  All indices in this paragraph are zero-based.
Write `x=2^13=8192` for the new coordinate bit.
Deleting the three-vertex `B` block beginning at `966` makes two native `B`
cuts and destroys the two unique first-upper targets

\[
 x\cup7012=15204,
 \qquad
 x\cup2510=10702.
\tag{2.1}
\]

No audited `B-A-B-A-B` five-piece splice which isolates that `B` block and
uses only one `A` cut can restore both targets.  At least two distinct `A`
cuts are required in this schema, one incident to each repair endpoint.  The
certified choices after `418` and `1445`, together with the two `B` cuts,
give a feasible six-piece state.

#### Proof

An `A/B` seam realizing `x union S` has a rank-seven `A` endpoint.  The old
part of its `B` endpoint is a rank-six subset of `S`; hence the `A` endpoint
must equal `S`.  In the `A` path,

\[
 A[419]=2510,
 \qquad
 A[1445]=7012.
\tag{2.2}
\]

Neither is a global endpoint, and they cannot both be exposed by one cut.
The possible incident cut positions are respectively `{418,419}` and
`{1444,1445}`.  Therefore one `A` cut cannot supply both unique repairs.

Cuts after `418` and `1445` expose both required endpoints.  In the certified
six-piece braid the seams

\[
 15200\longrightarrow7012,
 \qquad
 2510\longrightarrow8654
\tag{2.3}
\]

restore exactly the two targets in (2.1), and the full final-path audit
verifies every remaining upper depth, depth-two residence, and the common
owner compiler.  \(\square\)

Thus the successful replacement credits are genuinely compound in the
audited `B-A-B-A-B` family: the feasible four-cut decorated state has no
one-`A`-cut member in that family.  This is not a no-go for every possible
three-cut chronology or nonalternating reconnection.  It does prove that raw
cuts cannot be treated as independently safe choices; the full
cut--orientation--seam--witness--owner packet is the certificate unit.

## 3. The genuine occurrence complex and its exact link

Let `G` be the ground set of disruptable native edges and vertices.  An
occurrence `P` is recorded with its fixed full root support
`supp(P) subseteq G`.  Assume every protected occurrence family below is
nonempty.

For a protected family `A` of signed target/depth pairs, define

\[
 \mathcal K_{\rm occ}(\Omega)
 =\left\{C\subseteq G:
   \forall\alpha\in\mathcal A\ \exists P\in\Omega_\alpha,
   \ C\cap\operatorname{supp}(P)=\varnothing\right\}.
\tag{3.1}
\]

This is the cut-specific safe **complex**.  A fixed named replacement window
may be inserted into the corresponding `Omega_alpha` only when its existence
is independent of the optional face `C`.  Any replacement whose existence
depends on selected cuts, orientations, or seams must instead be carried by
a conditioned decorated action.

Now fix a complete decorated base state \(\Theta\in\mathscr B\); in particular,
its chronology, phase positions, envelopes, `U` selector, ports, endpoints,
and owner table are fixed.  Let `Gamma_Theta` be a bank of optional fully
decorated closed connector actions relative to this baseline.  An action
records both sides of a local switch, a context-independent identification
of its phase positions, its external ports, its selector exchange, all
occurrence replacements, and its owner pins.  It also has a raw disruption
set

\[
 \delta(\gamma)\subseteq G,
 \qquad
 \delta(F)=\bigcup_{\gamma\in F}\delta(\gamma).
\tag{3.1a}
\]

Different orientations, selector choices, witness lists, or owner patches
are different vertices of `Gamma_Theta`; they are not projected to the same
raw cut.  For `F subseteq Gamma_Theta`, use the fixed phase identification
and first define the core already imposed by the complete base:

\[
 B_p^\Theta
 =E_p^\Theta\cap
   \bigcap_{S\in\phi_\Theta:\,p\in I_S}S
 =M_p^\Theta.
\tag{3.1b}
\]

The optional-action core is

\[
 C_p^\Theta(F)=B_p^\Theta\cap
   \bigcap_{\gamma\in F:\,p\in I_\gamma}O_{\gamma,p}.
\tag{3.1c}
\]

Call `F` **decorated-safe** when:

* its action supports are compatible and their simultaneous switches leave
  the prescribed `U` and port bases valid;
* each action pays for every protected occurrence it destroys, without using
  an occurrence credited to a different action;
* every `C_p^Theta(F)` is nonempty; and
* one explicit owner table using the cores `C_p^Theta(F)` re-verifies the
  central private hits and **every** fixed `Theta` target private hit, as well
  as every new action target private hit, with the declared meet-dimension
  bound.

Let \(\mathcal K_\Theta\) be the family of decorated-safe optional action
sets.  This is
a fibre over the already valid state `Theta`; it is not a mechanism for
constructing `Theta` from a cycle factor.

### Lemma 3.1 (closed actions really do form a complex)

Suppose reversion is context-independent: for every decorated-safe `F` and
every `gamma in F`, reverting `gamma` inside the simultaneous state `F`
restores its old transitions, keeps the selector and port bases valid,
removes only its own occurrence credits and owner obligations, and leaves
all other action supports unchanged.  Under the fixed phase identification,
also require every reverted envelope/core to contain its pre-reversion
counterpart and every fixed/action target interval to have the declared
context-independent transport.  Then \(\mathcal K_\Theta\) is
downward-closed.

#### Proof

Let `F` be decorated-safe and remove `gamma`.  The closed switch reverts to
its old valid path and selector state.  By self-payment, no other action used
an occurrence supplied by `gamma`; all remaining occurrence witnesses
therefore survive.  The envelope/core containment hypothesis and removal of
the owner restrictions of `gamma` enlarge each core in (3.1c).  The
transport hypothesis keeps every fixed target interval identified, so the
old private-hit witnesses for all fixed targets remain valid; restricting
the action-target part of the owner table removes only the obligations of
`gamma`.  Iterating proves downward closure.  \(\square\)

Residence is deliberately absent from this lemma: an action may be needed to
hit a short-run hazard, and reverting it can restore that hazard.  This is
why the clutter in (0.1) is essential.

### Theorem 3.2 (exact occurrence-link contraction)

For `C in K_occ`, let

\[
 \Omega_\alpha^C
 =\{P\in\Omega_\alpha:
       C\cap\operatorname{supp}(P)=\varnothing\}.
\tag{3.2}
\]

Then

\[
 \boxed{
 \operatorname{lk}_{\mathcal K_{\rm occ}}(C)
 =\mathcal K_{\rm occ}(\Omega^C)
   \big|_{G\setminus C}.}
\tag{3.3}
\]

#### Proof

A set `D subseteq G setminus C` is in the left side exactly when
`C union D` avoids the full support of at least one occurrence for every
protected target.  Such an occurrence first has to survive `C`, placing it
in `Omega_alpha^C`, and then has to avoid `D`.  This is the condition on the
right.  \(\square\)

Let `H_D(Theta)` be the future short-run hazard intervals on the raw ground
set `G` of the fixed base chronology from the previous buffer note.
The residence-feasible cuts are

\[
 \mathcal A_D
 =\{C\in\mathcal K_{\rm occ}:
       C\cap I\ne\varnothing\text{ for all }I\in\mathcal H_D(\Theta)\}.
\tag{3.4}
\]

This is normally not a complex.

### Theorem 3.3 (decorated link/contraction theorem)

Fix a complete base \(\Theta\in\mathscr B\) and an optional face
\(F\in\mathcal K_\Theta\).  Define

\[
 \mathcal H_D(\Theta)/F
 =\{I\in\mathcal H_D(\Theta):\delta(F)\cap I=\varnothing\}.
\tag{3.5}
\]

Optional extensions of the encoded state `(Theta,F)` which preserve the
fixed base data and hit every future native residence hazard are in
bijection with the sets `D subseteq Gamma_Theta setminus F` satisfying

\[
 D\in\operatorname{lk}_{\mathcal K_\Theta}(F),
 \qquad
 \delta(D)\cap I\ne\varnothing
       \quad(I\in\mathcal H_D(\Theta)/F).
\tag{3.6}
\]

#### Proof

Restriction of an optional completion gives a face of the link, and its raw
disruption image hits every hazard not already hit by `delta(F)`.  Conversely,
join `D` to `F`.  The link condition preserves the already fixed `U`
selector, port path, occurrences, endpoints, and common owner system; the
disruption condition gives every future native residence cut.  New action
collars are part of their decorated-safe certificates.  Proposition 1.1
then applies to the resulting state.  These two operations are inverse on
the fully decorated optional-action encoding.
\(\square\)

The theorem is useful because every term in (3.6) has an exact finite
certificate.  It also says precisely what “regeneration” means: the child
must first have a valid complete base \(\Theta_{\rm child}\), and its fibre
\(\mathcal K_{\Theta_{\rm child}}\) must then have a residual link which hits the next hazard
clutter.  A valid base alone is not regeneration.

## 4. The exact first-shadow complex

Let `Q` be a path with edge set `E`.  Assume every edge has a required
first-shadow colour and every required colour occurs.  For every such colour
`S`, let

\[
 E_S=\{e\in E:\operatorname{col}(e)=S\}.
\tag{4.1}
\]

The nonempty sets `E_S` partition `E`.

### Theorem 4.1 (partition-matroid formula)

The cut sets preserving at least one internal occurrence of every colour are

\[
 \boxed{
 \mathcal K_1(Q)
 =\{C\subseteq E:E_S\nsubseteq C\text{ for every }S\}
 =\bigoplus_S U_{|E_S|-1,|E_S|}.}
\tag{4.2}
\]

In particular,

\[
 \operatorname{rk}\mathcal K_1(Q)
 =\sum_S(|E_S|-1)=|E|-|\{S\}|.
\tag{4.3}
\]

#### Proof

Colour `S` survives precisely when not all members of `E_S` are cut.  These
independent capacity constraints are the direct sum of the displayed
uniform matroids.  Summing their ranks gives (4.3).  \(\square\)

For the completed first-shadow path used by the native two-coordinate lift,

\[
 |E|=W-1,
 \qquad
 |\{S\}|=W-b,
 \qquad b=C_r.
\tag{4.4}
\]

Hence the rank is `b-1`.

### Corollary 4.2 (Catalan base and link zero)

Let `C_A` be the native Catalan deletion which retains one edge of every
first-shadow colour.  Then

\[
 |C_A|=b-1,
 \qquad C_A\text{ is a base of }\mathcal K_1(Q),
 \qquad
 \boxed{\operatorname{lk}_{\mathcal K_1(Q)}(C_A)=\{\varnothing\}.}
\tag{4.5}
\]

#### Proof

The retained forest contains exactly `W-b` edges, one of each colour, so
`C_A` has `(W-1)-(W-b)=b-1` edges and is independent.  Its size equals the
rank in (4.3), hence it is a base.  A matroid base has no nonempty independent
extension.  \(\square\)

The qualifier “internal” is essential.  Equation (4.5) is the link in the
complex which insists that every colour retain an internal edge occurrence.
It is not automatically the link of the full compiled package: a cut which
destroys one retained colour might still be feasible if a compatible
endpoint or other lower-compiler cell realizes that target.  Such a repair
belongs to the decorated base fibre and must be audited with the common
owner table.

There is a useful exact representative form.  A base `C_A` is equivalent to
choosing one retained representative

\[
                  r_S\in E_S
\tag{4.6}
\]

for every colour.  A residence hazard interval `I` is hit by the deleted
edges exactly when

\[
                  I\nsubseteq\{r_S:S\}.
\tag{4.7}
\]

If `I` contains two edges of one colour, (4.7) is automatic.  If `I` is
rainbow, it is the explicit clause

\[
       \bigvee_{e\in I}\bigl(r_{\operatorname{col}(e)}\ne e\bigr).
\tag{4.8}
\]

Equations (4.6)--(4.8), plus the ordered `U` interval clauses, port clauses,
and the common owner matching, are the compact cut-specific CSP forced by
the static no-go.  They retain the actual locations and colours; no scalar
reserve appears.

## 5. Closed-action transport and the strongest amplification theorem

A connector action is called **closed and transparent through the protected
depths** when it has two realizations with the same external ports and all
of the following are supplied explicitly:

1. reverting the action in every compatible context restores its old
   transitions and keeps the global path/selector base valid;
2. every occurrence it destroys has a named same-target replacement, and
   its complete prefix/suffix intersection and union traces make windows
   crossing other actions context-independent;
3. its seam-composed coordinate runs pass the declared collar test;
4. its owner pins have a private local patch, or all participating actions
   are certified by one common owner table;
5. no occurrence or private hit supplied by the action is used to pay for a
   different action's disruption.

Compatible closed actions, rather than raw cuts, are legitimate vertices of
`K`.

### Theorem 5.1 (link transport and simplex amplification)

Let \(\Theta\) be the complete source base, let
\(F\in\mathcal K_\Theta\) be the optional action face used by the current
lift, and let \(\Theta'\) be an independently
certified complete child base.  Suppose `Phi` is a simplicial embedding

\[
 \Phi:\operatorname{lk}_{\mathcal K_\Theta}(F)
          \hookrightarrow\mathcal K_{\Theta'},
\tag{5.1}
\]

transporting full occurrence supports, port traces, phase identifications,
and owner patches.

Let `N` be an **independent closed bank relative to the image**: its action
supports are mutually disjoint and disjoint from transported supports; every
subfamily reverts independently and keeps the selector/port base valid;
each action self-pays its occurrence losses; and the union of `N` with every
transported face has the displayed common owner certificate.  Then

\[
 \boxed{
 \Phi\bigl(\operatorname{lk}_{\mathcal K_\Theta}(F)\bigr)
       *\Delta(N)
 \ \subseteq\ \mathcal K_{\Theta'}.}
\tag{5.2}
\]

Consequently the available action rank is at least

\[
 \operatorname{rk}\operatorname{lk}_{\mathcal K_\Theta}(F)+|N|.
\tag{5.3}
\]

#### Proof

Take a face in the left side.  Transported actions preserve the same named
occurrences after the appropriate signed row shift.  Every new action
replaces its own destroyed occurrences, and trace transparency prevents
cross terms in windows meeting more than one action.  Reverting any subset
restores old transitions and removes only its own pins, so the selector and
port bases remain valid.  Disjoint private patches, or the common owner certificate,
preserve (1.4)--(1.5).  Thus every subfamily is a face of the child safe
complex.  Rank inequality (5.3) follows from the join.  \(\square\)

The independently certified `Theta'` hypothesis is essential: (5.2)
amplifies a child fibre after the lift base has been built; it does not
construct the child base.

The signed row shifts in this theorem are the following exact tables.  In
odd-to-even,

\[
\begin{array}{c|cc}
\text{shore}&\text{child lower depth }q&\text{child upper depth }q\\ \hline
A&L^{(q)}&F^{(q+1)}\\
B&L^{(q+1)}&F^{(q)}.
\end{array}
\tag{5.4}
\]

Thus `A` needs one extra source level on the upper sign and `B` needs one
extra source level on the lower sign.  In `k -> k+2`,

\[
\begin{array}{c|cc}
\text{sector}&\text{child lower depth }q&\text{child upper depth }q\\ \hline
A&L^{(q+1)}&F^{(q)}\\
X,Y&L^{(q)}&F^{(q+1)}\\
U&L^{(q-1)}&F^{(q+2)}.
\end{array}
\tag{5.5}
\]

The `U` line requires an order-preserving selector with the recorded lifted
supports.  An arbitrary one-representative selector has no inherited link.
In particular, all signed depths through `H` require source upper depth
`H+2` on `U`; describing the lift by one unsigned radius loses this
asymmetry.

For odd-to-even, a safe `c`-cut face of the first-shadow partition matroid
leaves rank exactly

\[
             \operatorname{rk}\mathcal K_1-c.
\tag{5.6}
\]

This is a genuine bounded-loss link theorem.  It does not say that the
chosen cuts hit the residence clutter; that is the second condition in
(3.6).  Nor does it construct the fresh owner/port base \(\Theta'\), which is a
separate hypothesis of Theorem 5.1.

## 6. Sharp failure of internally protected native `k -> k+2` cut extension

In the native `U Y A X` skeleton the cross-sector seam signatures are

\[
\begin{array}{c|cccc}
\text{seam}&UY&YA&AX&XU\\ \hline
\text{intersection tags}&\varnothing&\{y\}&\{x\}&\varnothing\\
\text{union tags}&\{y\}&\{x,y\}&\{x,y\}&\{x\}.
\end{array}
\tag{6.1}
\]

### Theorem 6.1 (extreme-shore link-zero obstruction)

In the standard native `k -> k+2` lift:

1. after the Catalan `A` deletion, the protected both-new first-lower minor
   has link zero;
2. on the ground set of deleted `U` indices, a one-representative value-fibre
   selector is a partition-matroid base and has deletion link zero; imposing
   ordered empty-signature upper constraints can only shrink its admissible
   base family;
3. a final window crossing an ordinary cross-sector seam supplies no
   replacement occurrence of either extreme signature.

Therefore the lift does not transport a positive-rank internally protected
`A` cut-extension atlas, and it has no additional native `U` deletion
capacity after the selector base.  This statement does not rule out
balanced same-signature basis exchanges or lower endpoint/compiler repairs.

#### Proof

Part 1 is Corollary 4.2.

For `U`, let `I_Z` be the native index class of value `Z`, and take deleted
indices as the ground elements.  Exact middle ownership requires retaining
at least one index in each `I_Z`, so the safe deletion complex is

\[
             \bigoplus_Z U_{|I_Z|-1,|I_Z|}.
\tag{6.2}
\]

A one-representative selector deletes `|I_Z|-1` indices in every class and
is a base of (6.2), hence has deletion link zero.  The ordered upper-interval
requirements are extra restrictions on these bases, not extra deletion
capacity.

A both-new lower replacement would need intersection tag `{x,y}`.  Every
window crossing a cross-sector seam contains a state missing at least one
of these tags.  Dually, an empty-signature upper replacement would need
union tag `emptyset`, whereas every such window contains a state with `x`
or `y`.  This is also visible in the two rows of (6.1).  Hence ordinary
cross-sector seam windows contribute no replacement occurrence to either
extreme minor.  A compound action containing a same-signature internal
exchange is not excluded by this assertion.  Deeper occurrence and owner
constraints can only shrink the admissible families.  \(\square\)

This is a structural no-go for **native-base regeneration**, not an
integrality obstruction to all same-parity constructions.  Three escapes
remain logically possible:

* reselect the entire `A` and `U` bases jointly, or perform balanced
  same-signature basis exchanges, before freezing them;
* create off-spine or same-signature internal edges which add new occurrence
  rank;
* spend explicitly compatible lower endpoint/compiler cells on the new `A`
  holes, or build the child chronology afresh and prove a new link there.

The first escape is exactly the representative CSP (4.6)--(4.8) coupled to
ordered `U` intervals, ports, and owners.  It closes one lift if feasible,
but because the internal `A` occurrence system and the `U` deletion system
finish at bases, it does not by itself produce the next-generation atlas.
The third escape is outside `K_1`; its true capacity belongs to the common
endpoint/owner base and is not bounded by Corollary 4.2.

### 6.2 An exact `k=11 -> 13` instance

On the stored exact `k=11` carrier rooted at its compiler cut, the
first-occurrence Catalan selector retains the four consecutive native edges
`253,254,255,256`.  Their five completed-spine vertices have coordinate-one
pattern

\[
                         0,1,1,1,0.
\tag{6.3}
\]

At the `k=13` deadline, an internal one-run must have length at least four,
so this is a residence hazard.  Every retained edge is the chosen
representative of its first-shadow colour.  Cutting one of them after the
base is frozen exits the partition-matroid complex, and a cross-sector seam
cannot replace the both-new lower target.  This is the literal link-zero
collision between the residence clutter and the internally protected `A`
base.  It does not exclude spending an independently certified lower
compiler cell on the resulting hole.

The same rooted first-occurrence `U` selector misses the empty-signature
upper target

\[
                 \{1,2,4,5,6,8,9,11\},
\tag{6.4}
\]

and the last-occurrence selector misses a second explicit target.  Thus even
a complete value-fibre base need not satisfy the ordered all-depth `U`
interval constraints.

The independently found exact `k=13` certificate is not a lift of this
selector, so it does not contradict the obstruction.

## 7. Exact certificate calibration

The connector complex must be read from whole decorated states, not from
cut counts.  Mask labels below are decimal values.  Array positions,
component endpoint indices, cut-after positions, block starts, seam indices,
and owner positions are zero-based, matching the frozen artifacts.

### 7.1 `k=11`: one complete decorated opening base

The exact source is one 462-cycle.  Its chosen opening is the cycle edge

\[
                         159\ --\ 219,
\tag{7.1}
\]

with closing lower colour `155` and completed boundary chain

\[
                         155\supset154\supset152.
\tag{7.2}
\]

The finite verifier finds 242 sites safe for the audited first two upper
rows; the chosen path is depth-three resident and all-depth upper complete.
The separate normalized compiler audit gives owner-dimension histogram

\[
                         0^{397}1^{68}.
\tag{7.3}
\]

This is one feasible complete decorated base state, not a vertex of its
future optional-switch complex.  The empty raw cut set is a cycle, not the
required linear package, illustrating again why complete bases themselves
are not a simplicial family.

### 7.2 `k=13`: a complete decorated oriented-port base

The source has two physical cycles of lengths `1547` and `169`.  The exact
enumeration contains 6,240 cross Johnson pairs and 24,960 oriented port
pairs; 6,032 preserve every upper depth and 1,092 of those are also
depth-three resident.  The chosen state has oriented endpoints

\[
 (3,-1),\qquad(53,+1),
\]

and seam

\[
                         2515\longrightarrow2391.
\tag{7.4}
\]

It leaves exactly the lower-depth-one target `2135` to the flexible compiler,
has no lower holes at depths `2,...,6`, and preserves every upper depth.  Its
separate normalized compiler audit gives owner-dimension histogram

\[
                         0^{1300}1^{419}.
\tag{7.5}
\]

On the cyclic source, the first-upper multiplicity profile is

\[
                         1^{936}2^{273}3^{78}.
\tag{7.5a}
\]

Thus its first-upper occurrence deletion complex, before residence, lower,
port, or owner constraints, has exact partition-matroid rank
`273+2*78=429`, while the 936 singleton classes are forced retained
occurrences.  This is its non-scalar first-upper occurrence capacity before
the bounded splice.

The two cuts, their orientations, the seam, endpoint repair, occurrences,
and owner table form one certified joint decorated base state.

### 7.3 `k=14`: a complete six-piece braid base

The strict state uses `A` cuts after `418,1445` and the two boundary cuts of
the three-vertex `B` block beginning at `966`.  Its order is

\[
 A_1^F,\ B_2^R,\ A_3^F,\ B_1^F,\ A_2^R,\ B_3^F.
\tag{7.6}
\]

The five seams include the two exact repairs (2.3).  The all-depth upper
audit, depth-two residence, and global lower compiler pass.  The normalized
compiler audit gives owner-dimension histogram

\[
                         0^{1910}1^{1519}2^5.
\tag{7.7}
\]

The five width-two positions are

\[
                 1418,1503,3041,3176,3394.
\tag{7.8}
\]

None is a seam; all lie inside `B` segments.  Thus these binary meets are not
seam-collar artifacts.  Compatibility with the seam and lower-pin data was
verified separately by the global normalized owner audit.

Theorem 2.2 proves the narrower, exact conclusion: within the audited
`B-A-B-A-B` family, the fixed `B` ear needs two distinct `A` repair cuts.
It does not exclude every other three-cut or nonalternating chronology.

## 8. What closes and what remains open

Theorems 3.3 and 5.1 give the strongest valid closure statement.

* After a complete base `Theta` is fixed, its optional closed-action fibre
  contracts to an exact residual link.
* Odd-to-even loses only the rank actually consumed by its bounded cut face,
  in the raw first-shadow occurrence minor.  A child base still has to be
  certified with its named seam replacements and one common owner table.
* A jointly independent bank of new same-signature closed actions amplifies
  the child link by a simplex.

The exact `k=11,13,14` states certify nonemptiness at those finite instances.
They do not certify a positive residual rank, and the native `k -> k+2`
internally protected `A` deletion link and exact-middle `U` deletion link
have rank zero after their compulsory bases.  The full `A` fibre with fresh
endpoint/compiler assignments has not been proved rank zero.

The surviving induction gate is therefore the following concrete theorem,
not a scalar reserve statement:

> Construct, in the finished child chronology, new closed transparent
> actions of both extreme signatures--both-new lower in `A` and
> empty-signature upper in `U`--whose residual link contains a transversal
> of the next residence clutter; alternatively, give the `A` cuts a
> regenerating endpoint/compiler assignment.  In either case the fixed child
> base must use the same ordered ports and one common owner table.

Equivalently, one must prove positive new internal occurrence rank after the
current Catalan and `U` bases have been frozen, or prove that the noninternal
compiler capacity used in its place is itself regenerated.  The standard
cross-sector seams contribute zero internal extreme-signature occurrences
by (6.1).  This precisely distinguishes a one-step exact certificate from a
regenerative Pascal induction.

## 9. Source audit

The finite statements used above are recorded in:

* `K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md`;
* `scratch/sigma_sat_k11_allcentral_cap2.certificate.json`;
* `scratch/sigma_sat_k11_allcentral_verify.json`;
* `MATH_PASCAL_FLAG_PACKAGE_AND_CATALAN_LIQUIDITY_20260728.md`;
* `MATH_ATTACK_H_KPLUS2_LABELLED_ROUTING_PHASE_AND_NATURAL_SELECTOR_COUNTEREXAMPLE_20260728.md`;
* `MATH_K13_EXACT_1719_CERTIFICATE_20260728.md`;
* `MATH_K14_EXACT_3434_CERTIFICATE_20260728.md`;
* `MATH_EXACT_CERTIFICATE_FLAG_TOWER_AND_BOUNDED_SURGERY_20260728.md`;
* `MATH_INTERSECTION_TABLEAU_AND_NESTED_OWNER_TARGET_20260728.md`;
* `scratch/raw_optimal_k06_k14_compiler_normal_form_audit.json`;
* `THREAD_D_REGENERATIVE_PASCAL_BUFFER_RECURSION_AND_STATIC_NO_GO_20260728.md`.
