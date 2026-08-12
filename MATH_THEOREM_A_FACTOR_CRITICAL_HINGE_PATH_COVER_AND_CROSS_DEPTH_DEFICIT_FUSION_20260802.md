# Factor-critical hinge modules: path-cover fusion and cross-depth deficit cancellation

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Status:** exact conditional one-copy theorem, exact quotient cut bank, and
sharp minimal obstructions.  The local factor-critical atlas and its
literal bridge supply are hypotheses.  Arbitrary-width upper coverage and
common-cap/compiler compatibility are not asserted.

## 0. Outcome

The deficit-one predecessor obstruction does not have to be paid once per
copy.  The correct coupling object is a protected **factor-critical path
module**.  Such a module uses every local owner/target resource except one
root role, leaves one tail capacity unused, and has one connected directed
path from that root to that tail.  A bridge from the tail of one module to
the root of another simultaneously uses the latter's missing role and
cancels both exposed boundary units.

This gives three exact conclusions.

1. A directed path forest on `p` modules with `c` paths coalesces `p`
   disjoint deficit-one copies into exactly `c` exposed root--tail pairs.
   A Hamilton path therefore leaves one controlled deficit, and a
   Hamilton cycle leaves none.
2. When every module has a completed root-by-tail port rectangle, the
   existence of an exact cycle cover is precisely Hall's theorem on one
   quotient coupling digraph.  After a path forest with `c` paths is
   reserved, the complete residual obstruction bank has only `2^c` Hall
   rows.  Requiring the residual matching to be one cycle gives a connected
   Euler carrier.
3. A weighted expansion row closes all quotient Hall cuts, and a
   row/column rejection bound closes topology by protected two-switches.
   Neither follows from one-sided hinge menu size.

The theorem explains how disjoint local deficits may be coupled without an
accumulating sidecar.  It also identifies the exact missing Boolean claim:
construct factor-critical modules and literal cross-depth bridges carrying
the required residence histories.  The screened collar proves stability
of a chosen one-sided menu; it does not itself supply this atlas.

## 1. Protected factor-critical modules

For a directed physical packet use the boundary convention

\[
                         \partial(x\to y)={\bf1}_y-{\bf1}_x.       \tag{1.1}
\]

Let `Q` be a finite set of module labels.  Module `q` has a private set of
owner/lower-target resources `K_q`, a set `R_q` of complete root states and
a set `C_q` of complete tail sockets.  Complete states include the literal
order-`d` history needed to concatenate packets and the clipped signed
residence ages.  Resource sets and physical interiors of different modules
are disjoint, except at declared bridge interfaces.

For `r in R_q` let `kappa_q(r)` be one distinguished resource role whose
fixed head is `r`.  A **factor-critical realization** at `(r,c)` is a
protected physical packet `F_q(r,c)` such that

* its contracted support is a spanning directed path from `r` to `c`, so

  \[
                         \partial F_q(r,c)={\bf1}_c-{\bf1}_r;       \tag{1.2}
  \]

* it uses every resource of `K_q` exactly once except `kappa_q(r)`;
* it leaves exactly the tail capacity at `c` unused; and
* all its internal owner, lower-palette and residence/history checks pass.

A bridge `B_(q,s)(c,r)` is a protected physical packet from `c in C_q` to
`r in R_s` which

\[
 \partial B_{q,s}(c,r)={\bf1}_r-{\bf1}_c             \tag{1.3}
\]

and whose contracted support is one connected directed `c`-to-`r` path, with
no balanced satellite component.  It uses exactly the source module's
unique unused outgoing capacity at `c` and the missing resource
`kappa_s(r)`.  It has no other scarce resource, and both endpoint history
transitions are literally accepted.  Its internal vertices are private
when bridges are combined.  These requirements are occurrence-labelled:
equality of owner masks without equality of the complete boundary histories
is insufficient.

Write

\[
 {\cal P}_q\subseteq R_q\times C_q,
 \qquad {\cal E}_{q,s}\subseteq C_q\times R_s          \tag{1.4}
\]

for the realizable internal paths and bridges.  Call the internal atlas
**port-complete** when

\[
                         {\cal P}_q=R_q\times C_q       \tag{1.5}
\]

for every `q`.  This Cartesian hypothesis is load-bearing only for the
quotient projection in Section 3.  The direct path theorem below needs
only the displayed realizations it uses.

Call the bridge atlas **matching-compatible** when every partial
permutation of module pairs supported by the nonempty relations
`E_(q,s)` has a simultaneous choice of witnessing occurrence-labelled
bridges, with private interiors, no shared scarce resource, and no contact
with the corresponding chosen internal paths except at the declared root
and socket states.  This is a joint physical condition.  Pairwise
nonemptiness of the bridge relations does not imply it.

No arbitrary-width upper-witness or common source/compiler condition is
included in this definition.  Such a row may be added to the protected
payload only after every internal path and bridge has been checked against
the same literal occurrence bank.

## 2. The factor-critical conveyor

### Theorem 2.1 (path/cycle deficit fusion)

Let

\[
                         q_1\to q_2\to\cdots\to q_t               \tag{2.1}
\]

be a directed path of distinct modules.  Suppose there are ports
`r_j in R_(q_j)`, `c_j in C_(q_j)` for which

\[
 (r_j,c_j)\in{\cal P}_{q_j},\qquad
 (c_j,r_{j+1})\in{\cal E}_{q_j,q_{j+1}}\quad(1\le j<t).           \tag{2.2}
\]

Assume also that these displayed internal paths and bridges have one
simultaneous occurrence-labelled realization: their physical interiors and
scarce resources are private except at the declared consecutive ports.  If
the closing bridge below is used, it must be compatible with that same
family.

Then

\[
 {\cal F}=\bigcup_{j=1}^t F_{q_j}(r_j,c_j)
       \ \cup\!\bigcup_{j=1}^{t-1}B_{q_j,q_{j+1}}(c_j,r_{j+1})  \tag{2.3}
\]

is one protected spanning path through those modules.  It uses every
module resource exactly once except `kappa_(q_1)(r_1)`, leaves only the tail
capacity `c_t` unused, and has boundary

\[
                         \partial{\cal F}={\bf1}_{c_t}-{\bf1}_{r_1}. \tag{2.4}
\]

If in addition `(c_t,r_1) in E_(q_t,q_1)`, adding that bridge gives a
balanced one-copy Euler component.  More generally, a vertex-disjoint
directed path cover with `c` paths leaves exactly `c` missing root roles,
`c` unused tail capacities, and `c` boundary pairs.

#### Proof

The bridge entering module `q_j`, `j>1`, uses precisely the resource
`kappa_(q_j)(r_j)` omitted by its internal path.  Hence all resources in
those modules are used once; only the first root role remains.  Every
intermediate socket and root cancels in the boundary sum

\[
 \sum_{j=1}^t({\bf1}_{c_j}-{\bf1}_{r_j})
 +\sum_{j=1}^{t-1}({\bf1}_{r_{j+1}}-{\bf1}_{c_j})
 ={\bf1}_{c_t}-{\bf1}_{r_1}.                         \tag{2.5}
\]

The internal paths are connected and each bridge joins consecutive ones,
so the physical support is one path.  Complete endpoint histories make all
joins residence-safe.  The closing bridge cancels (2.4), uses the last
missing resource and makes one Euler component.  Apply the same argument
pathwise for a path cover.  \(\square\)

### Corollary 2.2 (bounded live deficit, not bounded support)

A protected Hamilton path through arbitrarily many factor-critical modules
leaves only one coloured role and one boundary pair.  Thus a single
separately certified closing packet gives `O(1)` exposed endpoint packets,
independent of the number of modules.  Its literal size may still depend on
the depth parameter, so this statement alone is not an additive-`O(1)` word
bound.  A protected Hamilton cycle leaves no exposed endpoint pair.

This uses `t-1` or `t` ordinary bridge roles.  That linear support is
unavoidable: starting from `t` disjoint connected module paths, every
bridge can reduce the number of weak components by at most one.  Therefore
at least `t-c` intermodule bridges are required to obtain at most `c`
components.  The theorem bounds the **residual deficit**, not the total
number of selected one-copy roles.

## 3. Port-complete quotient and exact Hall cuts

Assume now the port-complete condition (1.5) and a matching-compatible
bridge atlas.  Define the quotient coupling digraph `Gamma` on `Q` by

\[
 q\to s\quad\Longleftrightarrow\quad
 {\cal E}_{q,s}\ne\varnothing .                      \tag{3.1}
\]

Loops are allowed; they close a module without coupling it to another.

### Theorem 3.1 (exact quotient cycle-cover theorem)

The protected atlas has a balanced one-copy selection **of the declared
factor-critical form**--one internal path and one incoming/outgoing bridge
per module--if and only if the bipartite copy of `Gamma` has a perfect
matching, equivalently

\[
                         \boxed{|N^+(S)|\ge |S|\quad(S\subseteq Q).} \tag{3.2}
\]

For a perfect matching represented by a permutation `pi`, the number of
weak Euler components is exactly the number of cycles of `pi`.  In
particular, a connected selection exists exactly when `Gamma` contains a
directed Hamilton cycle.

#### Proof

Matching compatibility simultaneously chooses witnessing bridges for all
selected quotient arcs `q -> pi(q)`.  The incoming bridge determines `r_q`
and the outgoing bridge determines `c_q`.  Port completeness supplies the
internal path `F_q(r_q,c_q)` independently for every module.  Theorem 2.1
applied on the cycles of `pi` gives the balanced physical selection and its
component count.

Conversely, in a balanced selection every module supplies one unused tail
to a bridge and receives exactly one bridge using its missing root role.
The bridges therefore project to a permutation supported by `Gamma`.
Hall's theorem gives (3.2).  \(\square\)

Define the exact quotient deficiency

\[
 H_{\min}(\Gamma)=
   \max_{S\subseteq Q}\bigl(|S|-|N^+(S)|\bigr)_+.    \tag{3.3}
\]

By the deficiency form of Hall's theorem, a maximum quotient matching has
size `|Q|-H_min(Gamma)`.  Thus `H_min` is exactly the number of unmatched
module sources and also the number of unmatched module roots in a maximum
partial coupling.  It is a lower bound on the number of exceptional
root--tail sidecar pairs in every completion of the declared
one-bridge-per-module atlas.  It is attained
when the declared sidecar family contains arbitrary compatible packets
between the unmatched sockets and roots; without that physical sidecar
hypothesis it is only the exact quotient defect, not an asserted literal
repair cost.

### Theorem 3.2 (exact residual bank after a path forest)

Let `R` be a partial permutation in `Gamma` whose directed support is a
**spanning** vertex-disjoint path forest, with isolated modules counted as
one-vertex paths.  Here `R` reserves quotient arcs, not frozen physical
bridge witnesses: after choosing a residual matching, matching compatibility
realizes the whole completed permutation afresh.  If literal witnesses of
`R` are to remain fixed, assume the stronger hereditary extension property
that every residual completion has a simultaneous realization extending
those witnesses.  Put

\[
 L_R=Q-\operatorname{dom}R,\qquad
 H_R=Q-\operatorname{im}R.                           \tag{3.4}
\]

Thus `L_R` is the set of path sinks and `H_R` the set of path roots.  The
reserved forest extends to a balanced one-copy selection if and only if

\[
 \boxed{|N^+_R(S)|\ge |S|\quad(S\subseteq L_R),}
 \qquad
 N^+_R(S)=N^+(S)\cap H_R.                            \tag{3.5}
\]

If

\[
                    c=|L_R|=|H_R|=|Q|-|R|,            \tag{3.5a}
\]

then `R` has exactly `c` paths and (3.5) is a bank of only `2^c` rows.  Every residual
perfect matching induces a permutation of the `c` path components.  The
completed carrier is connected if and only if that permutation is one
cycle.

#### Proof

Every source in `dom R` and every destination in `im R` is already used.
The only unfilled outgoing and incoming incidences are respectively
`L_R` and `H_R`.  Extending `R` is exactly a perfect matching between these
two sets in the residual bipartite graph, so (3.5) is Hall's theorem.  On
contracting each reserved path, the residual matching is its successor
permutation, proving the component assertion.  \(\square\)

The exact live endpoint deficit after reserving `R` is

\[
 H_{\min}(R)=
 \max_{S\subseteq L_R}\bigl(|S|-|N_R^+(S)|\bigr)_+.  \tag{3.6}
\]

For a Hamilton path, `c=1`: the sole residual row says exactly that its sink
has a bridge to its root.  If this edge is unavailable, Theorem 2.1 still
leaves only the one boundary pair (2.4), which is the sharp one-pair
endpoint interface.  No dimension-uniform bound on the physical size of a
closing packet is implied.

### Corollary 3.3 (fixed-parameter closure of the endpoint bank)

Once a quotient path forest with `c` paths has been fixed, its complete
endpoint-completion test depends only on those `2c` ports.  Test the `2^c`
inequalities (3.5), then enumerate the at most `c!` perfect residual
matchings and accept exactly when one induces a single cycle on the
contracted paths.  Thus fixed `c` gives a constant-size exact balance and
topology bank.  A literally fixed physical forest additionally needs the
hereditary extension property above.

## 4. Proof-safe expansion and topology rows

Write

\[
 d^-(s)=|\{q:q\to s\}|.                              \tag{4.1}
\]

### Theorem 4.1 (weighted quotient expansion)

If every module satisfies

\[
                         \boxed{\sum_{s\in N^+(q)}{1\over d^-(s)}\ge1,} \tag{4.2}
\]

then all Hall cuts (3.2) hold.  In particular, if every module has at least
`Delta>0` outgoing neighbours and every destination has indegree at most
`Delta`, a balanced one-copy cycle cover exists.  The same statement on the
residual graph, with its indegrees recomputed after restriction, closes every
row (3.5) after a prescribed path forest.

#### Proof

For `S subseteq Q`, sum (4.2) over `q in S` and interchange sums:

\[
 |S|\le\sum_{s\in N^+(S)}
 { |\{q\in S:q\to s\}|\over d^-(s)}
 \le |N^+(S)|.                                      \tag{4.3}
\]

Apply Theorems 3.1 or 3.2.  \(\square\)

Hall does not force one cycle.  The following stronger row is sufficient.
For a quotient cycle cover `pi` and a nonempty proper union `S` of cycles of
`pi`, let

\[
 \begin{split}
 D_\pi(S)=&\ |\{(q,u)\in S\times\bar S:q\not\to\pi(u)\}|\\
           &+|\{(q,u)\in S\times\bar S:u\not\to\pi(q)\}|.          \tag{4.4}
 \end{split}
\]

### Theorem 4.2 (quotient two-switch fusion)

If

\[
                         D_\pi(S)<|S|\,|\bar S|                       \tag{4.5}
\]

for every supported quotient cycle cover and every nonempty proper union
`S` of its cycles, then quotient two-switches turn `pi` into a directed
Hamilton cycle.

Indeed, (4.5) gives `q in S,u outside S` for which both
`q -> pi(u)` and `u -> pi(q)` exist.  Swapping the two successors merges
the two corresponding cycles.  Port completeness and matching compatibility
give a fresh simultaneous physical realization of each resulting
permutation with the same one-copy resource and residence specifications.
They do not, without a stronger hereditary extension property, assert a
literal local switch which freezes every unaffected occurrence.

A graph-level sufficient condition is

\[
 \rho+\kappa<|Q|/2,\qquad
 \rho=\max_q|Q-N^+(q)|,quad
 \kappa=\max_s|Q-N^-(s)|.                            \tag{4.6}
\]

Condition (4.6) itself implies Hall.  Indeed, if
`|N^+(S)|<|S|`, then every `q in S` misses all destinations outside
`N^+(S)`, while any destination outside `N^+(S)` misses every source in
`S`.  Hence

\[
 \rho\ge |Q|-|N^+(S)|,\qquad \kappa\ge |S|,
\]

so `rho+kappa>|Q|`, a contradiction.  Thus at least one cycle cover exists.

Under (4.6), start with any cycle cover and choose a smallest cycle `S`.
Then `|S|<=|Q|/2` and

\[
                         D_\pi(S)\le |S|(\rho+\kappa)
                              <|S|(|Q|-|S|),                         \tag{4.7}
\]

so one fusion is possible.  Iteration proves a connected one-copy carrier.

Theorem 4.2 is sufficient, not necessary: a longer protected circuit may
cross a two-switch-locked shore.

## 5. The deficit-one obstruction is genuinely coupled away

The depth-one four-role obstruction has predecessor arcs, written
`tail -> fixed head`, equal to

\[
                         3\to0,\quad0\to1,\quad0\to2,\quad1\to3.     \tag{5.1}
\]

The three arcs

\[
                         1\to3\to0\to2                              \tag{5.2}
\]

form a spanning factor-critical path.  It omits the head role at `1` and
leaves tail `2` unused.  Thus `r=1,c=2` is an exact quotient port for this
abstract module.

For `p` copies, if one supplies literal protected bridges

\[
                         2_t\longrightarrow1_{t+1}\quad(t\bmod p),  \tag{5.3}
\]

then Theorem 2.1 makes their union one balanced Euler cycle.  The `p`
disjoint Hall deficits have not been paid by `p` sidecars: the `p` bridge
roles are part of the one-copy selection and their boundaries telescope to
zero.

This does not contradict the disjoint-copy sidecar lower bound.  That lower
bound freezes the original menus, in which every copy's deficient shore is
closed.  Equation (5.3) enlarges one omitted role menu in each copy by a
cross-copy predecessor, so each local shore loses one trapped role.  The
new global coupling cycle has no positive boundary.

For disjoint coordinate alphabets the literal equalities in (5.3) are
absent.  Consequently (5.3) is an exact algebraic closure and a precise
physical target, not a proof that the raw Boolean obstruction already
contains its own bridges.

## 6. Sharp failures and the finite forbidden bank

### 6.1 Quotient Hall is necessary

With two modules and quotient arcs `1->1, 2->1`, every module has a
nonempty outgoing menu but the shore `{1,2}` has neighbourhood `{1}` and
deficit one.  No coupled completion exists.  This is the smallest quotient
Hall obstruction.

### 6.2 Port projections are insufficient

Two modules with roots and sockets `{0,1}` may have internal relations

\[
                         {\cal P}_1={\cal P}_2=\{(0,0),(1,1)\}.       \tag{6.1}
\]

Let the sole bridge witness from module 1 to 2 be `(c_1,r_2)=(0,1)` and
the sole witness from 2 to 1 be `(c_2,r_1)=(0,1)`.  The projected quotient
has the directed 2-cycle, but a simultaneous lift would force module 1 to
be both state zero and state one, and likewise module 2.  Hence no lift
exists.  This is the smallest intermodule example.  With loops allowed, the
absolute minimum is one module with two ports: `P={(0,0),(1,1)}` and
`E_loop={(0,1)}` have a nonempty projected loop but no joint lift.  With one
port all endpoint relations are Cartesian.

This is why Theorem 3.1 assumes complete internal root-by-socket rectangles
and a matching-compatible bridge atlas.  Without them the exact gate is
the simultaneous occurrence-labelled relation

\[
 (r_q,c_q)\in{\cal P}_q,\qquad
 (c_q,r_{\pi(q)})\in{\cal E}_{q,\pi(q)},              \tag{6.2}
\]

not Hall on its two projections.  Likewise, even when every quotient edge
has a witness separately, a shared physical occurrence or protected
resource can make two matching edges incompatible.  Such a family violates
matching compatibility and must remain in the relational gate (6.2).

### 6.3 Balance and topology are separate

If `Gamma` consists only of its `p` loops, Hall is exact but every selection
has `p` components.  Thus no Hall/expansion statement which ignores the
cycle structure can give an `O(1)`-component carrier.

There are two proof levels.  Without port completeness and universal
matching compatibility, a non-Cartesian internal relation, a missing
projected bridge, or conflicting individual witnesses does **not** by itself
prove impossibility; it invalidates the quotient reduction and forces the
full occurrence-labelled CSP (6.2).  The exact obstruction at that level is
absence of every joint solution of (6.2).

Under the hypotheses of Theorem 3.1, the complete quotient obstruction bank
is:

1. a Hall shore (3.2), or after reserving a spanning path forest, one of the
   `2^c` residual shores (3.5); and
2. for connected completion, absence of any residual successor perfect
   matching which is one cycle.  For fixed `c`, Corollary 3.3 decides this
   by at most `c!` exact checks.

For the particular two-switch descent, a locked cycle union violating
(4.5) obstructs only that proof basis; it is not a global no-go.

## 7. Consequence for the unsaturated hinge program

The screened one-sided hinge theorem supplies a nonempty residence-stable
tail cylinder for one fixed head.  The predecessor-Hall example proves
that independently selecting those cylinders lets deficit-one shores
accumulate.  The present theorem isolates the weakest escape which can
prevent that accumulation:

> partition the selected chain table into protected factor-critical
> modules, find a protected module path forest with `O(1)` paths, and close
> its `O(1)` residual Hall bank.

This is strictly weaker than demanding that every original role menu form
one globally expanding family.  A Hamilton path already contracts an
arbitrary number of local deficits to one endpoint pair.  It is stronger
than fractional clockability: every owner/lower resource is used literally
once and every bridge carries an occurrence-labelled residence state.

What is not proved is that the Boolean/Pascal unsaturated menus contain the
factor-critical root-by-socket rectangles or the cross-depth bridges.  In
particular, the screen coordinate and the absence collars may prevent a
socket from matching the next module's root.  Establishing a bounded-path
cover in that literal compatibility graph is now the exact finite target.
Arbitrary-width upper protection and common-cap/compiler closure remain
independent downstream gates.

## 8. Lightweight audit

`scratch/audit_a_factor_critical_hinge_path_cover_20260802.py` checks the
boundary/resource ledger, the four-role factor-critical path and cyclic
coupling, the two minimal obstructions, the residual path-cover Hall
criterion on all digraphs through three modules, and the row/column
two-switch bound on all cycle covers through five modules.
