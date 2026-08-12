# All-target protected conveyors: exact Hall bundles and the run-state gate

Date: 2026-07-31  
Lane: A, adversarial pure-mathematics audit  
Status: exact all-target criterion; proved colour-back composition lemma;
proved minimal blocker and short-fragment obstructions.  This note does not
prove the existence of the required PBBS braid in every dimension.

## 0. Verdict

Serving only the targets missing from the disconnected source factor is not
enough.  The cuts forced by those providers can jointly destroy a target that
was formerly present.  The exact casualty set is determined by the
occurrence-span blocker clutters, and it must be recomputed after the **whole**
cut bank is known.

There is nevertheless a clean all-target Hall theorem.  Fix one protected
old occurrence for every previously covered upper target, put every
occurrence killed by the chosen cut into the service bundle of its
destination fragment, and assign every source hole to a destination fibre.
If the
colour-back/key-forward port graph lies in an acyclic order skeleton and
satisfies ordinary Hall, then a perfect matching is one spanning path; every
target is retained or literally re-created, and the lower `q1` deck has
exactly one hole and no repetition.

Residence is not automatic from pairwise port legality.  It becomes
automatic under the following new composition rule.  For a depth `d`
colour-back conveyor, if every fragment has length at least `d`, then a
positive run of length at most `d` can meet at most one seam.  The reason is
that an all-one intermediate fragment forces the first bit of the next
fragment to be one as well.  Consequently internal `d`-cleanliness plus
pairwise seam `d`-cleanliness is globally composition-closed.  In particular,
for the one-cut PBBS components at K17, whose lengths are at least three,
pairwise run guards are exact for depth three.

Without the length hypothesis, even physical colour-back/key-forward
Johnson ports have a three-fragment counterexample.  Thus an unlifted Hall or
Aharoni--Haxell provider theorem is insufficient in the multi-cut setting;
the exact run-summary state must be retained.

## 1. Exact all-target closure

Let `F` be a directed Johnson factor, let \({\cal U}^{\rm req}\) be the
complete required proper-upper universe, let \({\cal U}_F\) be the targets
covered by `F`, and put

\[
                 {\cal H}_F={\cal U}^{\rm req}\setminus{\cal U}_F.
\tag{1.0}
\]

For a component `C` and target `Y` in \({\cal U}_F\), let
\({\cal I}_C(Y)\) be its occurrence-labelled cyclic witness intervals.
For \(I\in{\cal I}_C(Y)\), write `span(I)` for its internal cycle edges.
Let

\[
 {\cal K}_C(Y)=\min_{\subseteq}\{K\subseteq E(C):
       K\cap\operatorname{span}(I)\ne\varnothing
       \text{ for every }I\in{\cal I}_C(Y)\}.
\tag{1.1}
\]

For a global cut bank \(S\), define

\[
 \operatorname{Cas}(S)=
 \left\{Y\in{\cal U}_F:
   \text{for every component }C\text{ supporting }Y,
   \text{ some }K\in{\cal K}_C(Y)\text{ satisfies }K\subseteq S\cap E(C)
 \right\}.
\tag{1.2}
\]

Define the complete debt set

\[
                    \operatorname{Debt}(S)
                       ={\cal H}_F\cup\operatorname{Cas}(S).
\tag{1.2a}
\]

After cutting and ordering the resulting fragments, let
\(\operatorname{New}(S,\pi)\) be the set of targets represented by a new
suffix/full-fragments/prefix interval in that literal order.

### Proposition 1.1 (exact all-target ledger)

The opened chronology has no required upper hole if and only if

\[
                 \operatorname{Debt}(S)
                    \subseteq \operatorname{New}(S,\pi).
\tag{1.3}
\]

#### Proof

A target in \({\cal U}_F\setminus\operatorname{Cas}(S)\) has an old
occurrence whose span avoids every cut, so that occurrence lies in one
retained fragment.  A target in \(\operatorname{Cas}(S)\) has no surviving
old occurrence, and hence is present precisely when it has a new crossing
interval.  A source hole in \({\cal H}_F\) also requires such a new
interval.  Every crossing interval has the unique
suffix/full-fragments/prefix form.  These alternatives are exhaustive.
\(\square\)

The frequently used selected-witness version is stronger but easier to
install.  Choose one occurrence \(I_Y\) for every target in \({\cal U}_F\).
It suffices that
each `span(I_Y)` avoid `S`, or that `Y` be supplied by a displayed new
crossing interval.  This is sufficient, not necessary: another unselected
old occurrence might survive.

For one cut per PBBS component, every fragment has full union `[k]`.
Therefore a proper upper target cannot cross a complete intermediate
fragment, and every member of `New(S,pi)` crosses exactly one seam.  In this
case all-target service can genuinely be assigned to destination seams.

### Proposition 1.2 (the two-cut blocker obstruction)

Target-wise Hall service for the initially missing targets does not imply
(1.3), even if every chosen cut is individually kernel-safe for every old
target.

#### Proof

Take an old target `Y` with two disjoint occurrence spans, one containing
`e` and the other containing `f`, and no further occurrence.  Then the one-edge
kernel of `Y` is empty, while `{e,f}` contains a minimal blocker.  Suppose
two otherwise disjoint service records force cuts `e` and `f`.  Each record
is individually safe for `Y`, and any Hall or rainbow matching on those two
service records succeeds.  Their union cut bank kills both occurrences of
`Y`.  Unless one of the selected seams also supplies `Y`, the final
chronology has gained the serviced targets and lost `Y`.  This is exactly
the failure of (1.3).  \(\square\)

Thus the 1,838 initially absent K17 targets are not a closed service
universe.  Either the final cut bank must be fixed before the provider
matching, or every provider record must carry sufficient occurrence-span
guards to certify (1.3).

## 2. Destination-bundle colour-back Hall theorem

Fix one cut and orientation on each of `b` components, giving fragments

\[
                    P_i=(s_i,\ldots,t_i),
       \qquad c_i=s_i\cap t_i .
\tag{2.1}
\]

The deleted colours `c_i` are distinct because the source factor is
lower-rainbow.  Fix an initial fragment `a` and a terminal fragment `z`.
For every target in \({\cal U}_F\), choose an old occurrence.  If its
chosen occurrence is killed by the cut of component `j`, put the target in
the destination bundle \({\cal B}_j\).  Independently assign every source
hole in \({\cal H}_F\) to a destination, writing \({\cal H}_j\) for its
assigned fibre.  Require

\[
                         {\cal B}_a={\cal H}_a=\varnothing.
\tag{2.1a}
\]

Let `D` be an acyclic directed graph on the components.  An arc `i -> j`
of `D` is a **fully protected conveyor port** when

1. \(t_i\sim s_j\) in the Johnson graph;
2. it is colour-back:
   \[
                         t_i\cap s_j=c_i;
   \tag{2.2}
   \]
3. it is key-forward: with \(\kappa_j=t_j\setminus s_j\),
   \(\kappa_j\in t_i\);
4. for every \(Y\in{\cal B}_j\cup{\cal H}_j\), an occurrence-labelled suffix of `P_i`
   followed by a prefix of `P_j` has union exactly `Y`;
5. it satisfies every declared endpoint, owner, and run-state guard.

For an outward-ray casualty, clause 3 gives the canonical replacement;
clause 4 records the literal witness and also covers any additional
noncanonical services.  Keeping the clauses separate prevents an empty
destination bundle from silently dropping the key-forward conveyor rule.

Put

\[
 L=[b]\setminus\{z\},\qquad R=[b]\setminus\{a\},
 \qquad N(i)=\{j\in R:i\to j\text{ is a fully protected port}\}.
\tag{2.3}
\]

### Theorem 2.1 (all-target protected conveyor Hall theorem)

Assume

\[
                        |N(X)|\ge |X|
                 \qquad\text{for every }X\subseteq L.
\tag{2.4}
\]

Then there is a spanning `a`-to-`z` fragment path such that

* every chosen old upper witness survives or is exactly replaced, and every
  source hole receives an exact new witness; hence every target in
  \({\cal U}^{\rm req}\) is covered;
* every seam is Johnson;
* the seam lower colours are \(\{c_i:i\ne z\}\), each once; hence the
  lower `q1` ledger is exactly \(H=1,E=0\), with sole hole `c_z`;
* every local guard carried by the selected ports holds.

If the run guards are composition-closed for the selected path, the same
path also has the declared residence/deadline property.

#### Proof

Hall gives a matching from `L` onto `R`.  Direct its edges from sources to
destinations.  Every component except `z` has outdegree one and every
component except `a` has indegree one.  Thus the degree cover is one
`a`-to-`z` path together with directed cycles.  All chosen arcs lie in the
acyclic graph `D`, so no directed cycle exists; the cover is the desired
spanning path.

If the selected witness of a target avoided its component cut, it remains
inside one fragment.  Otherwise it belongs to the bundle of its component,
which is not `a` and has exactly one incoming selected port.  Clause 3 of
the port definition carries its key, and clause 4 supplies that target
literally.  Every source hole lies in one fibre \({\cal H}_j\), and clause
4 on the unique incoming port of `j` supplies it as well.  This proves
coverage of the full required universe.

By (2.2), the outgoing seam of source `i` has colour `c_i`.  Sources are
exactly the indices other than `z`, and the `c_i` are distinct deleted
colours.  The cut/seam ledger therefore restores all deleted colours except
`c_z`, without a repeat.  Composition-closed guards are inherited by the
concatenation.  \(\square\)

This is an ordinary Hall theorem only because an entire destination
casualty bundle is tested on one candidate arc.  Applying
Aharoni--Haxell separately to individual targets is neither necessary nor
sufficient: one seam may serve many targets, while independently chosen
target providers need not form a degree-two path.

### Corollary 2.2 (common-key decomposition of the Hall graph)

Put \(\kappa_i=t_i\setminus s_i\).  Every fully protected canonical
colour-back/key-forward arc `i -> j` satisfies

\[
                              \kappa_j=\kappa_i.
\tag{2.5}
\]

Consequently a spanning conveyor from Theorem 2.1 can exist only if all of
its selected component openings have one common departure key.  The port
graph is a disjoint union of its key classes.  In the acyclic skeleton of
Theorem 2.1, if more than one selected key class is nonempty then (2.4) must
fail; otherwise Theorem 2.1 would produce a spanning path, contradicting
key-class separation.

#### Proof

Write \(t_i=c_i\cup\{\kappa_i\}\).  Colour-back gives
\(s_j=c_i\cup\{z\}\) with \(z\ne\kappa_i\).  The destination key
\(\kappa_j\) is absent from `s_j` but, by key-forward, belongs to `t_i`.
It cannot lie in \(c_i\subset s_j\), so the only possibility is
\(\kappa_j=\kappa_i\).  Equality propagates along a spanning path.
\(\square\)

This is a genuine global obstruction, not an extra independent resource
which can be repaired after Hall.  A noncanonical suffix/prefix service may
avoid key-forward and hence avoid this decomposition.

### Corollary 2.3 (linear Johnson-colour normal form)

Along a strict conveyor path \(i_1,\ldots,i_b\), the common key
\(\kappa\) is omitted by every cut colour and

\[
 t_{i_h}=c_{i_h}\cup\{\kappa\},
 \qquad
 s_{i_h}=c_{i_{h-1}}\cup c_{i_h}\quad(2\le h\le b).
\tag{2.6}
\]

Hence consecutive cut colours form a simple path in
\(J([k]\setminus\{\kappa\},r-1)\).  Conversely, protected cut states with
the endpoint form (2.6) satisfy colour-back and key-forward on every
displayed transition.

#### Proof

The endpoint formula for `t` follows from the definition of the common
key.  At the seam into `i_h`, colour-back gives
\(c_{i_{h-1}}\subset s_{i_h}\).  The destination cut gives
\(c_{i_h}\subset s_{i_h}\).  The two colours are distinct rank-`r-1`
sets in the rank-`r` set `s_{i_h}`, so they intersect in rank `r-2` and
their union is exactly `s_{i_h}`.  The converse follows by taking the
intersection and difference in (2.6).  \(\square\)

Thus the fixed-colour Hall graph is not an arbitrary dense bipartite graph:
inside each key class it is the occurrence-labelled lift of a Johnson-colour
path graph, further thinned by all-target and run guards.

### Proposition 2.4 (Hall without topology is insufficient)

The acyclic-skeleton clause in Theorem 2.1 cannot be dropped.  Let

\[
 L=\{a,x,y\},\qquad R=\{x,y,z\},
\]

and take the only arcs to be

\[
                         a\to z,\qquad x\to y,\qquad y\to x.
\tag{2.7}
\]

Every Hall inequality holds, but the unique perfect degree cover is the
one-edge `a`-to-`z` path plus the directed 2-cycle on `x,y`; there is no
spanning chronology.  Aharoni--Haxell applied to richer port resources has
the same topological blind spot.  One needs an acyclic skeleton, rooted
subtour inequalities, or an exact path-state construction.

## 3. Colour-back makes short runs pair-local

For a coordinate `x`, write its `0/1` trace on a fragment in the usual way.
A fragment is **internally d-clean** when it has no interior positive run
of length at most `d`.  A pair `P_i|P_j` is **seam d-clean** when it has no
interior positive run of length at most `d` whose collar meets the seam.

### Lemma 3.1 (one-extra-bit lemma)

Consider a colour-back fragment path.  If every fragment has length at
least `d`, then every interior positive run of length at most `d` is either
contained in one fragment or meets exactly one seam.

#### Proof

Suppose a positive run meets at least two seams.  It contains every state of
some intermediate fragment `P_i`.  Hence its coordinate `x` belongs to both
endpoints `s_i,t_i`, and therefore to the cut colour

\[
                              c_i=s_i\cap t_i.
\]

The outgoing seam is colour-back, so

\[
                              t_i\cap s_{i+1}=c_i.
\]

Thus `x` also belongs to the first state `s_{i+1}` of the next fragment.
The run consequently contains at least `|P_i|+1 >= d+1` positive states,
contrary to its length being at most `d`.  \(\square\)

### Corollary 3.2 (composition-closed residence)

Under Lemma 3.1, if every fragment is internally `d`-clean and every
selected seam is seam `d`-clean, then the whole fragment path is
`d`-clean.

For one-cut PBBS components at K17, all component lengths are at least
three.  Therefore, at depth three, the all-target Hall theorem needs only
exact internal and two-fragment seam guards; no run can hide across two
selected seams.  This is one unit sharper than the generic
`length >= d+1` criterion because colour-back supplies the extra positive
bit.

The conclusion is scoped to strict source-colour restitution (2.2).  A
remote-colour derangement which assigns an unrelated deleted colour to the
seam need not carry the endpoint intersection `c_i`, and then the extra-bit
argument is unavailable.

## 4. Exact deadline state when zero residence is unavailable

For the flat/canonical depth-`d` test, let \(\Sigma_d(P)\) be the product
over coordinates of the exact truncated run summaries recording

* length;
* all-one status;
* initial and terminal positive-run lengths, capped at `d+1`; and
* the latest local start of an interior run of length at most `q`, for every
  \(q\le d\).

Literal concatenation induces an associative product `star` on these
summaries and decides the canonical frontiers exactly.

An arbitrary-start staircase is position-sensitive: whether a run ending at
`b` is charged depends on `g_(b+1)`.  The translation-invariant truncated
summary alone therefore does not decide every threshold vector.  For a
fixed threshold vector `G`, let \({\cal A}_{d,G}\) be the exact finite online
automaton whose state records the current absolute position, every
coordinate's open-run start and capped length, and all accumulated adjusted
frontiers and scalar loss.  When a run closes, its end position and `G`
determine the exact update.  A fragment `P` induces a deterministic
transition map `T_P`; write `Acc_G` for exact final acceptance.

### Theorem 4.1 (exact run-state path condition)

After the cut/orientation options have been fixed, an all-target,
colour-back, exact-`q1`, deadline-feasible braid exists if and only if the
following finite state graph has an accepting spanning path.

A state for fixed `G` is

\[
                    (S,i,q),
\tag{4.1}
\]

where `S` is the set of components already used, `i in S` is the current
terminal component, and `q` is the state of \({\cal A}_{d,G}\) after their
ordered concatenation.  The initial state is

\[
                    (\{a\},a,T_{P_a}(q_0)).
\tag{4.2}
\]

There is a transition

\[
 (S,i,q)\longrightarrow
 (S\cup\{j\},j,T_{P_j}(q))
\tag{4.3}
\]

precisely when `j` is unused and `i -> j` is a fully protected conveyor
port.  Reading `P_j` immediately after the old word includes the new seam.
A terminal state is accepting precisely when `S=[b]`, `i=z`, and
`Acc_G(q)` holds.  If `G` is not fixed, take the disjoint union over all
admissible threshold vectors.

#### Proof

Every physical braid has a unique sequence of used-component sets,
endpoints, and online deadline states, so it gives a path in
(4.1)--(4.3).
All-target coverage and exact `q1` are enforced by the port definition and
source-colour rule.  Conversely, reading an accepting state path gives a
literal component order using exactly those ports.  Determinism makes its
final state the state obtained by reading that literal word, so `Acc_G` is
exact.  \(\square\)

Under Lemma 3.1, the canonical summary can be replaced by an exact
sequence-dependent frontier ledger.  Let `alpha_{i,q}` be the latest local
start of an internal run of length at most `q`.  Let
`beta_{ij,q}^{ell,r}` be the latest start, relative to the beginning of
`P_i`, of such a run meeting seam `i -> j`, where `ell` records that the
left end of `P_i` is the global left boundary and `r` records that the right
end of `P_j` is the global right boundary.  Runs touching a declared global
boundary are excluded.  These four two-fragment catalogues are literal.
For a path \(\pi\), with

\[
                       L_h=\sum_{u<h}|P_{\pi(u)}|,
\]

one has literally

\[
 \rho_q(\pi)=\max\left(
 0,
 \max_h\{L_h+\alpha_{\pi(h),q}\},
 \max_{h<b}\{L_h+
   \beta_{\pi(h),\pi(h+1),q}^{\mathbf1_{h=1},\mathbf1_{h+1=b}}\}
 \right).
\tag{4.4}
\]

Thus ordinary Hall on the port projection does not decide a nonzero
deadline problem: the absolute starts `L_h` depend on the selected path
order.  Equation (4.1), or a proved reset/halo condition which makes
`Acc_G` automatic, is the exact extra state.

## 5. A physical Johnson counterexample to pairwise run Hall

The state in Section 4 cannot be discarded for short multi-cut fragments.
Here is a literal local configuration in `J(6,3)`.  Use coordinate `1` and
write sets without braces.  Take

\[
 t_1=235,\quad P_2=(123,124),\quad
 P_3\text{ beginning }(146,456).
\tag{5.1}
\]

The two new seams are

\[
                         235-123,\qquad124-146.
\tag{5.2}
\]

They are source-colour-back.  Indeed choose the deleted source edges

\[
                     235-236\quad(c_1=23),
       \qquad        124-145\quad(c_2=14),
\tag{5.3}
\]

and the seams in (5.2) have intersections `23` and `14`, respectively.
They are also key-forward canonical repairs.  For the first destination use
the deleted old flank `135-123`: its departure key is `5`, contained in
`235`, and

\[
                     135\cup123=235\cup123=1235.
\tag{5.4}
\]

For the second use `126-146`: its departure key is `2`, contained in `124`,
and

\[
                     126\cup146=124\cup146=1246.
\tag{5.5}
\]

All displayed old edge colours (`23,13,12,14,16,46`) are distinct, so no
local lower-rainbow violation is hidden in the example.

The coordinate-1 trace across the displayed fragments is

\[
                              0\mid11\mid10.
\tag{5.6}
\]

On the first two fragments the run `11` touches the right boundary; on the
last two the run `111` touches the left boundary.  Hence both two-fragment
ports pass the local test “no interior run of length at most three”.  Their
composition is `01110`, which has an interior run of length three.  The
component/entry Hall graph is a path and both seam colours recycle their
source cuts, yet depth-three residence fails.

The obstruction uses a two-state intermediate fragment, exactly outside
the hypothesis `|P_i| >= d` of Lemma 3.1.  It therefore does not contradict
the K17 one-cut corollary, but it applies immediately once extra cuts create
short fragments.

## 6. Sharp boundary for the PBBS opening lane

The following conjunction is now a proved sufficient all-target opening
theorem:

1. fix a complete cut bank and one old occurrence for every previously
   covered upper target;
2. assign every killed selected occurrence to its destination bundle;
3. assign every source hole to a destination service fibre;
4. verify Hall (2.4) in an acyclic colour-back/key-forward port skeleton;
5. verify either the composition criterion of Corollary 3.2 or the exact
   accepting state of Theorem 4.1.

It yields zero net upper holes and exact lower profile `H=1,E=0`.  A final
common compiler remains a separate literal condition.

What remains unproved is that PBBS supplies such cuts and a Hall-positive
port graph in every dimension.  At K17, the one-cut whole-component factor
has components long enough for the colour-back composition lemma, but the
known cut-collar audit shows that most components retain internal short
runs after every single cut.  Extra cuts can remove those runs, but then
short fragments appear and the exact state gate of Section 4 returns.

Accordingly, neither service of the 1,838 original holes nor marginal
provider Hall is the remaining theorem.  The minimum correct object is the
all-target blocker-closed destination-bundle Hall graph intersected with
the run-summary state path.
