# RSB depth-two and erosion deltas: physical seams, regeneration, and private guards

Date: 2026-07-31  
Status: exact physical-window and fixed-skeleton Hall delta theorem;
conditional private/aligned gluing theorem; literal depth-two collar
obstruction; no all-\(m\) guard-existence theorem

## 0. Verdict

Assume the turn palettes have already been repaired.  The first downstream
RSB row has an exact answer, but its locality parameter is not the length of
the abstract middle-levels switch.

Let \(T,T'\) be the two literal physical middle-owner chronologies after
all decoration, residual-matching phase, and socket choices have been made.
Let

\[
 s=|E(T)\setminus E(T')|
  =|E(T')\setminus E(T)|                              \tag{0.1}
\]

be their actual changed-seam count.  Deleting the old-only seams splits the
common chronology into path fragments \(P\).  For an
\((\ell+1)\)-owner window put

\[
 b_\ell=\sum_P\min\{\ell,|V(P)|\}.                    \tag{0.2}
\]

Then

\[
                         b_\ell\le \ell s,             \tag{0.3}
\]

and exactly \(b_\ell\) old and \(b_\ell\) new based windows fail to lie
inside one common fragment.  Every other intersection or union window
transports bijectively, even when its fragment is reversed.  Consequently:

* depth-two upper shadows change on exactly the two boundary multisets,
  each of size \(b_2\le2s\);
* depth-\(d\) maximal erosion changes on boundary multisets of size
  \(b_d\le ds\); and
* a named compiler cell using \(h\) consecutive erosion letters has owner
  dependency span \(d+h-1\), so its complete signature can change at no
  more than

  \[
                         b_{d+h-1}\le s(d+h-1)         \tag{0.4}
  \]

  starts per cell type on either side.

For a fixed transported controller/core skeleton, these right-vertex
bounds give an exact signed incidence-graph delta.  Restricting an old
lower-target matching to the common graph leaves deficiency at most
\(b_{d+h-1}\) for one width-\(h\) cell type per start, and at most
\(\sum_h a_hb_{d+h-1}\) for \(a_h\) such types.  The new compiler graph is
saturating exactly when the common matching admits the required
vertex-disjoint augmenting linkage.

There are two important negative conclusions.

1. A transparent item-2158 switch fixes selected marks, but need not fix the
   residual matching phase on a long unmarked fragment.  Its physical seam
   support \(s\) can therefore be large.  Transparency alone does not imply
   an \(O(t)\) depth-two or erosion delta for an abstract alternating
   \(2t\)-circuit.
2. A representative-changing switch has at most \(d_0+3t\) augmenting
   paths from an old augmented deficiency \(d_0\), but item2169 bounds their
   number, not their lengths.  Even one augmenting path can change
   arbitrarily many matching representatives.  Item2169 alone supplies no
   bound on the literal chronology seam count \(s\).

Thus a recursive proof has an exact dichotomy:

* **phase-aligned/private step:** certify the actual bounded physical seam
  set and carry local depth-two and compiler guards; or
* **regeneration step:** allow a nonlocal representative/phase change, then
  recompute the complete shadow and compiler state at its output.

This gives a positive gluing-tree theorem after adding private shadow and
compiler guards to the existing private/aligned catalogue.  It does not
prove that such guards exist for every \(m\).

The new repaired \(m=5\) three-\(C_{10}\) packet fits the second branch.
It is a valid palette/decorability/gap-forest regeneration packet.  Its
subsequent physical audit is now sharper: one 42-connector closure supplies
the complete upper/lower flag tower, so depth two passes, but 31 bounded
coordinate runs of length two survive inside 18 forest paths.  For
\(d(10)=2\), residence and therefore the erosion compiler are impossible on
every intact-path closure.  The next move must be an interior physical
rethread whose actual seam support is evaluated by the theorem below.

## 1. Literal physical setup

Let

\[
 T=(T_0,\ldots,T_{N-1}),\qquad
 T'=(T'_0,\ldots,T'_{N-1})                            \tag{1.1}
\]

be cyclic Hamilton chronologies of the same \(N\) labelled rank-\(r\)
owner occurrences.  Every consecutive pair is Johnson-adjacent.  We
identify equal labelled occurrences before comparing the two cycles.
Assume \(E(T)\ne E(T')\), and define

\[
 D^-=E(T)\setminus E(T'),\qquad
 D^+=E(T')\setminus E(T).                             \tag{1.2}
\]

Both cycles are 2-regular on the same vertices, so

\[
                         |D^-|=|D^+|=:s.              \tag{1.3}
\]

The common graph \(E(T)\cap E(T')\) is a disjoint union of paths.  A proper
common cycle is impossible because it would already be a component of the
Hamilton cycle \(T\).  Write these path fragments as

\[
                         {\cal P}=\{P_1,\ldots,P_s\},  \tag{1.4}
\]

allowing isolated vertices, and put \(n_a=|V(P_a)|\).  Then

\[
                         \sum_{a=1}^s n_a=N.          \tag{1.5}
\]

The cycle \(T'\) uses the same fragments, possibly reversed and reordered,
and reconnects them by the seams in \(D^+\).

If \(E(T)=E(T')\), then \(T'\) is only a rerooting or reversal of the same
labelled Hamilton cycle.  Every cyclic intersection/union multiset is
identical, and all cyclic delta statements below are trivial with \(s=0\).
Endpoint-capped linear words may still have different boundary corrections
after a reroot and are handled explicitly in Section 4.

This is the correct comparison point.  An abstract alternating circuit on
an underlying middle-levels cycle does not determine \(D^\pm\) until the
decoration, residual phase, physical path closure, and any
representative-changing linkage have been fixed.

For \(1\le\ell<N\), a based \(\ell\)-window is

\[
 W_i^{(\ell)}(T)
   =(T_i,T_{i+1},\ldots,T_{i+\ell})                  \tag{1.6}
\]

with indices cyclic.  Its edge span is

\[
 \operatorname{span}W_i^{(\ell)}
   =\{T_iT_{i+1},\ldots,T_{i+\ell-1}T_{i+\ell}\}.
                                                               \tag{1.7}
\]

A set statistic \(f\) on such windows is **reversal-invariant** when

\[
 f(X_0,\ldots,X_\ell)=f(X_\ell,\ldots,X_0).           \tag{1.8}
\]

Consecutive intersection and union are reversal-invariant.

## 2. Exact physical-window delta

Define the old and new boundary-window families

\[
 {\cal B}_\ell^-=
 \{W_i^{(\ell)}(T):
       \operatorname{span}W_i^{(\ell)}\cap D^-\ne\varnothing\},
                                                               \tag{2.1}
\]

\[
 {\cal B}_\ell^+=
 \{W_i^{(\ell)}(T'):
       \operatorname{span}W_i^{(\ell)}\cap D^+\ne\varnothing\}.
                                                               \tag{2.2}
\]

### Theorem 2.1 (exact crossing-window identity)

For every reversal-invariant statistic \(f\) and every value \(R\),

\[
\boxed{
 \operatorname{mult}_{T'}(f=R)-\operatorname{mult}_{T}(f=R)
 =
 \#\{W\in{\cal B}_\ell^+:f(W)=R\}
 -
 \#\{W\in{\cal B}_\ell^-:f(W)=R\}.}                  \tag{2.3}
\]

Moreover

\[
\boxed{
 |{\cal B}_\ell^-|
 =|{\cal B}_\ell^+|
 =b_\ell
 :=\sum_{a=1}^s\min\{\ell,n_a\}
 \le \ell s.}                                        \tag{2.4}
\]

#### Proof

A fragment with \(n_a\) vertices contains exactly

\[
                         \max\{n_a-\ell,0\}           \tag{2.5}
\]

based \(\ell\)-edge windows wholly inside it.  Reversal of the fragment
gives a bijection between the old and new internal windows, and
reversal-invariance preserves their values.  Thus all internal windows
cancel target by target.

Both cycles have \(N\) based starts.  Hence the number of noninternal
windows on either side is

\[
\begin{aligned}
 N-\sum_a\max\{n_a-\ell,0\}
 &=\sum_a\bigl(n_a-\max\{n_a-\ell,0\}\bigr)\\
 &=\sum_a\min\{\ell,n_a\}=b_\ell.
\end{aligned}
\]

Since there are \(s\) fragments, \(b_\ell\le\ell s\).  Subtracting the two
boundary multisets after cancellation proves (2.3). \(\square\)

The equality in (2.4), not merely the upper bound, is often useful when
several changed seams have overlapping halos.

For two linear Hamilton paths on the same \(N\) labelled occurrences,
deleting \(s\) old-only edges gives \(s+1\) common fragments.  There are
\(N-\ell\) based windows, so the corresponding exact boundary count is

\[
 b_{\ell,\mathrm{lin}}
 =\sum_P\min\{\ell,|V(P)|\}-\ell
 \le \ell s.                                         \tag{2.4a}
\]

All signed identities remain unchanged.  If a linear reroot also changes
the endpoint-capping convention, its explicit prefix/suffix corrections
must be added separately as in Section 4.

### Corollary 2.2 (exact depth-two upper delta)

Put

\[
 U_i^{(2)}(T)=T_i\cup T_{i+1}\cup T_{i+2}.            \tag{2.6}
\]

For every target \(Z\),

\[
\boxed{
 \mu'_{2}(Z)-\mu_{2}(Z)
 =
 B_2^+(Z)-B_2^-(Z),}                                  \tag{2.7}
\]

where \(B_2^\pm(Z)\) count the boundary triples of value \(Z\).  In
particular,

\[
 \sum_Z B_2^-(Z)=\sum_Z B_2^+(Z)=b_2\le2s,           \tag{2.8}
\]

the number of possibly lost target colours is at most \(2s\), and

\[
 \sum_Z|\mu'_2(Z)-\mu_2(Z)|\le 2b_2\le4s.            \tag{2.9}
\]

The new chronology covers every depth-two upper target exactly when

\[
\boxed{
 \mu_2(Z)-B_2^-(Z)+B_2^+(Z)\ge1
 \quad\text{for every }Z.}                            \tag{2.10}
\]

For one new seam \(X\mid Y\), its two based boundary triples are

\[
 X^-\cup X\cup Y,\qquad X\cup Y\cup Y^+,             \tag{2.11}
\]

where \(X^-\) and \(Y^+\) are the adjacent retained owners.  If a triple
contains two new seams it is listed once in \({\cal B}_2^+\), not once per
seam.

### Corollary 2.3 (all fixed depths)

For

\[
 L_i^{(q)}=\bigcap_{a=0}^{q}T_{i+a},\qquad
 U_i^{(q)}=\bigcup_{a=0}^{q}T_{i+a},                 \tag{2.12}
\]

the same signed identity holds with \(\ell=q\), and each side has exactly
\(b_q\le qs\) boundary occurrences.

These are occurrence bounds, not hole bounds.  One destroyed occurrence
can be the sole witness of a target.

## 3. Exact last-birth characterization through a gluing sequence

Consider a sequence

\[
 T^{(0)},T^{(1)},\ldots,T^{(g)}                       \tag{3.1}
\]

of literal physical rethreadings.  Occurrence labels include the retained
fragment and the ordered edge span.  At step \(j\), every internal old
occurrence has its unique transported copy; the new boundary occurrences
are born at step \(j\).

### Theorem 3.1 (last-birth decomposition)

Every occurrence in \(T^{(g)}\) has a unique last birth:

1. it was present in \(T^{(0)}\) and its transported span avoided every
   later deleted seam; or
2. it was born in the new boundary collar of a unique step \(j\), and its
   transported span avoided every deleted seam at steps \(j+1,\ldots,g\).

Conversely every occurrence satisfying one of these two conditions survives
to \(T^{(g)}\).

Therefore final depth-two upper coverage is equivalent to the following
guard condition:

> for every target \(Z\), choose one base or collar-born \(Z\)-occurrence
> whose transported span avoids every later deleted seam.

#### Proof

Apply the internal-window bijection of Theorem 2.1 at the last step.  An
occurrence is either new there or is the transport of a unique old internal
occurrence.  Iterate backwards until the first time it is new, or until the
base is reached.  This gives existence and uniqueness of the last birth.
The converse follows by forward transport.  The final statement is exactly
the assertion that at least one occurrence of each target survives.
\(\square\)

A target-load histogram without occurrence spans is therefore not a
recursive shadow state.

## 4. Erosion and fixed-skeleton compiler incidence

Fix a depth

\[
                         1\le d<r,\qquad d+1<N.       \tag{4.0}
\]

Assume \(T\) is \(d\)-erosion-safe, while \(T'\) is initially only a
Johnson chronology.  Define the forward cyclic maximal erosion candidates

\[
 P_i=\bigcap_{a=0}^{d}T_{i+a},\qquad
 P'_i=\bigcap_{a=0}^{d}T'_{i+a}.                     \tag{4.1}
\]

### Theorem 4.1 (exact erosion delta and wall locality)

The signed multiset delta \([P']-[P]\) of the erosion letters is (2.3) with
\(\ell=d\).  Thus exactly

\[
                         b_d\le ds                    \tag{4.2}
\]

old and new erosion occurrences lie in the changed collars.

Every wholly internal rank test through depth \(d\) transports.  The new
chronology is \(d\)-erosion-safe exactly when:

1. every new seam-crossing intersection and union window through depth
   \(d\) has its intended rank; and
2. every seam-crossing pair of consecutive deepest intersections satisfies

\[
                         |P'_i\cap P'_{i+1}|=r-d-1.    \tag{4.3}
\]

The complete wall-test dependency uses \(d+2\) owners, hence has boundary
support \(b_{d+1}\le(d+1)s\).

#### Proof

The erosion letters are the depth-\(d\) intersection statistic, so
Theorem 2.1 gives (4.2).  Internal tests are literal copies under reversal.
The ordered all-depth erosion criterion says that (4.3) is exactly the
remaining return wall after the rank tests.  Therefore only windows whose
spans meet a new seam require recomputation. \(\square\)

For a linear endpoint-capped compiler, the same theorem holds when the
linear cut and its \(d\)-letter prefix/suffix halos are fixed.  If the cut
or reroot changes, the endpoint corrections must be listed explicitly.
There are at most \(2d\) endpoint erosion letters per chronology; they are
not silently covered by the cyclic collar formula.

### 4.2 Named cells and dependency width

Fix a physical compiler skeleton.  A named cell \(c\) has:

1. a fixed anchor and base eligibility predicate \(B_c(S)\);
2. a mandatory core/controller mask \(K_c\);
3. a maximal allowed envelope \(P_c\); and
4. every controller footprint and occurrence identifier needed by the
   exact skeleton.

Its target incidence is

\[
 S\sim c
 \quad\Longleftrightarrow\quad
 B_c(S),\qquad K_c\subseteq S\subseteq P_c.           \tag{4.4}
\]

The fixed-skeleton occurrence model is included by taking the complete
signature which determines its literal interval OR value.

Suppose one translation family of cells uses \(h\) consecutive erosion
letters, and assume \(d+h-1<N\).  Its complete owner dependency block has
\(d+h\) owners and \(d+h-1\) owner seams.

### Theorem 4.2 (exact changed-cell support)

If the skeleton, controller footprints and core choices transport on every
common fragment, then the only cells whose complete signatures can change
lie in old and new boundary families \(Z_h^-,Z_h^+\) satisfying

\[
\boxed{
 |Z_h^-|=|Z_h^+|=b_{d+h-1}
 \le s(d+h-1).}                                      \tag{4.5}
\]

For \(a_h\) named cell types anchored at every start, multiply the right
side by \(a_h\).  In particular:

* singleton maximal-envelope ports have \(h=1\) and support \(b_d\);
* adjacent one-core equations have \(h=2\) and support \(b_{d+1}\).

After identifying transported stable cells, every incidence outside
\(Z_h^-\cup Z_h^+\) is identical.  On a changed cell the exact edge delta
is simply the difference of the two predicates (4.4).

#### Proof

The tuple of \(h\) consecutive erosion letters beginning at \(i\) depends
on owners

\[
                         T_i,\ldots,T_{i+d+h-1}.       \tag{4.6}
\]

It transports exactly when this dependency span lies in one common
fragment.  Theorem 2.1 with \(\ell=d+h-1\) gives (4.5).  The fixed-skeleton
hypothesis then makes the complete cell signature, and hence every edge
(4.4), identical on the transported stable cells. \(\square\)

Only the number of changed right vertices is bounded.  The number of
changed incidence edges can be large.  For example, in the pure
rank-\(j\) containment bank with \(K_c=\varnothing\), changing envelope
\(P\) to \(P'\) loses exactly

\[
 { |P| \choose j}-{ |P\cap P'| \choose j}            \tag{4.7}
\]

neighbours and gains

\[
 { |P'| \choose j}-{ |P\cap P'| \choose j}.          \tag{4.8}
\]

If the representative, controller footprint, or residual phase changes on
otherwise internal cells, those cells must be added explicitly to
\(Z_h^\pm\).  There is no collar bound without that hypothesis.

If \(d+h-1\ge N\), the dependency wraps the whole cyclic chronology.  The
safe convention is then to expose all \(N\) starts; no nontrivial local
bound is asserted.

## 5. Exact Hall delta and compiler linkage

Let \(G=(\mathcal L,\mathcal C;E)\) and
\(G'=(\mathcal L,\mathcal C';E')\) be the old and new exact lower-target
incidence graphs for one fixed skeleton.  Identify the transported stable
cells.  Write \(K^-\) and \(K^+\) for all nonstable old and new cells,
including every changed controller/phase cell.

For \(X\subseteq\mathcal L\), define the old Hall slack

\[
                         \sigma_G(X)=|N_G(X)|-|X|.    \tag{5.1}
\]

### Theorem 5.1 (exact Hall-cut delta)

For every \(X\subseteq\mathcal L\),

\[
\boxed{
 |N_{G'}(X)|-|N_G(X)|
 =
 |N_{G'}(X)\cap K^+|-|N_G(X)\cap K^-|.}              \tag{5.2}
\]

Consequently \(G'\) has a matching saturating every lower target if and
only if

\[
\boxed{
 |N_{G'}(X)\cap K^+|-|N_G(X)\cap K^-|
 \ge-\sigma_G(X)
 \quad(X\subseteq\mathcal L).}                        \tag{5.3}
\]

If \(G\) is an equivariant quotient incidence graph with physical orbit
size \(k\), the corresponding weighted quotient slack changes by \(k\)
times the quotient-column delta, with short target orbits retaining their
actual left weights.

#### Proof

The stable neighbour columns are in bijection and have identical
incidences.  They cancel in the difference.  Formula (5.2) remains.
Substitution into Hall's inequality
\(|N_{G'}(X)|\ge|X|\) gives (5.3). \(\square\)

Scalar target positivity is not enough: (5.3) is a simultaneous shore
condition.

### Theorem 5.2 (exact common-core compiler linkage)

Suppose \(G\) has a target-saturating matching \(M\).  Let \(H\) be the
common transported subgraph of \(G\) and \(G'\), let \(M_0\) be a maximum
matching of \(H\), and put

\[
                         r_H=|\mathcal L|-|M_0|.      \tag{5.4}
\]

Then \(G'\) has a target-saturating matching if and only if its
\(M_0\)-alternating digraph contains \(r_H\) pairwise vertex-disjoint
augmenting paths which start at all exposed targets and end at distinct
free cells.

If every changed old right vertex belongs to \(K^-\), then

\[
                         r_H\le |K^-|.                \tag{5.5}
\]

For one width-\(h\) cell type per start, Theorem 4.2 with no extra
phase/controller changes gives

\[
                         r_H\le b_{d+h-1}
                              \le s(d+h-1).           \tag{5.6}
\]

For several width families with \(a_h\) named cell types per start, the
safe bound is instead

\[
                         r_H\le\sum_h a_h b_{d+h-1}.  \tag{5.7}
\]

#### Proof

Restrict \(M\) to the common graph.  At most one matching edge is lost per
removed right vertex, proving (5.5).  Replacing this restriction by a
maximum common matching can only improve it.  The symmetric difference
with any saturating matching of \(G'\) consists of alternating cycles and
exactly \(r_H\) augmenting paths covering all exposed targets.  Conversely,
toggling such paths produces a saturating matching.  Formula (5.6) follows
from (4.5). \(\square\)

This is the compiler analogue of item2169.  Its state is pairing-resolved:
the scalar deficiency \(r_H\) is not enough.

## 6. Why polygon transparency and linkage width do not bound the delta

### 6.1 Residual-phase obstruction

Item2158 transparency preserves selected turn occurrences and their local
palettes.  On an unmarked retained fragment, however, the residual
incidence matching is one of two boundary phases.  Changing the boundary
phase on a path

\[
                         v_1,v_2,\ldots,v_{2n}        \tag{6.1}
\]

replaces

\[
 v_1v_2,\ v_3v_4,\ldots,v_{2n-1}v_{2n}              \tag{6.2}
\]

by the opposite internal pairing together with the two new boundary
connections.  The symmetric difference traverses the whole fragment.
Thus one local transparent reconnection can change \(\Theta(n)\) physical
edges unless the phase-indexed physical state of the exact boundary theorem
is fixed.

Therefore all local shadow/compiler bounds must be stated in the actual
physical seam count \(s\).  An \(O(t)\) corollary is valid only on a
**phase-aligned physical lift** in which:

1. retained fragments keep their residual matching phase;
2. representative choices agree on the retained common core; and
3. socket edits are themselves explicitly bounded.

Item2167 gives at most \(t\) changed records in each of three **augmented
matching graphs**.  Those are not, by themselves, literal adjacency edits
of the final owner chronology.  Suppose an additional audited physical-lift
map proves that every changed augmented record changes at most one literal
chronology seam and that \(c\) socket connectors change.  Only under this
extra Lipschitz certificate does one obtain the conditional bound

\[
                         s\le3t+c.                   \tag{6.3}
\]

If the same certificate also proves that all polygon ports are
selected/private and no residual-incidence record is used there, the
conditional bound improves to

\[
                         s\le2t+c.                   \tag{6.4}
\]

Neither inequality is a consequence of mark transparency, phase alignment,
or item2167 alone.  They are optional consequences of a separately supplied
physical-lift Lipschitz theorem.

### 6.2 One bounded-width linkage can be arbitrarily long

Let the two shores be

\[
 L_0,\ldots,L_n,\qquad R_0,\ldots,R_n.
\]

Take the deficient matching

\[
                         M_0=\{L_iR_{i-1}:1\le i\le n\} \tag{6.5}
\]

and add the diagonal edges

\[
                         A=\{L_iR_i:0\le i\le n\}.    \tag{6.6}
\]

The common deficiency is one, but the unique augmentation is

\[
 L_0,R_0,L_1,R_1,\ldots,L_n,R_n,                    \tag{6.7}
\]

of length \(2n+1\).  It changes all \(n\) old matching edges and all
\(n+1\) new edges.

Hence a bound on the number of augmenting paths gives no bound on their
physical support.  This is an exact matching-algebra obstruction to
deducing an \(O(t)\) shadow collar from item2169.  It is not asserted that
every graph (6.5)--(6.6) is a trace-realizable Catalan fixture.

### 6.3 Core reselection can also propagate

Suppose one coordinate \(z\) lies in a long sequence of stable envelopes.
Writing

\[
 c_i=\mathbf1_{\{z\in C_i\}},
\]

the one-core equations contain

\[
                         c_i\vee c_{i+1}=1.           \tag{6.8}
\]

On an even cyclic block, the minimum-\(\sum c_i\) face has the two
alternating phases.  Opposite boundary pins select opposite phases and
change every position of an arbitrarily long block.  Such a Boolean factor
occurs on any sufficiently long positive run of \(z\).

Thus Theorems 4.2 and 5.1 require a fixed transported core/skeleton or the
full endpoint-typed transfer relation.  They do not give an unconditional
Lipschitz theorem for a reoptimized core.

## 7. Private/aligned shadow--compiler composition

Fix a rooted gluing tree and a bottom-up dynamically valid order of its
selected switches.  Between two **regeneration nodes**, require every
switch to have an audited phase-aligned physical lift and an
occurrence-labelled actual seam set.

A regeneration node may itself be a controlled-debt macro packet of any
finite number of bounded-port circuits.  Its cardinality need not be bounded
independently of \(m\).  Intermediate packet states need not be decorated or
compiler-ready.  What must remain bounded and occurrence-labelled is the
live boundary, the palette/matching debt, the augmenting-linkage terminals,
and the physical footprints needed to reconstruct the accepting endpoint.
At that endpoint the complete depth-two and compiler states are recomputed;
they are not inferred by summing polygon sizes.

Item2184 gives an independent algebraic reason for this boundary form.
Within item2184's ordered-four-transversal determinant model, no positive
monomial can contain complete solutions in both canonical
distinguished-coordinate parent sectors.  More general Pascal braids that
change the outer completion or the cross atoms are not excluded.  Contracting
one directed atom \(T\to H\) in the same directed-forest model requires an
acyclic residual with no \(H\)-to-\(T\) path.  Thus boundary-deficient rails and a
reachability/socket coordinate are necessary upstream companions to the
shadow/compiler guards below.  They are logically separate coordinates:
the no-\(H\)-to-\(T\) test does not imply any depth-two witness or compiler
Hall inequality.

At a node \(x\), let:

* \({\cal B}_{2,x}^\pm\) be its old/new depth-two boundary occurrences;
* \(K_x^\pm\) be its old/new changed compiler cells;
* \(M_x\) be the incoming lower-target matching; and
* \(H_x\) be the common transported incidence graph, with a chosen maximum
  matching \(M_{0,x}\).

### Definition 7.1 (private RSB guard packet)

A node guard consists of:

1. for every depth-two target whose last incoming witness lies in
   \({\cal B}_{2,x}^-\), either a replacement in
   \({\cal B}_{2,x}^+\) or a named common occurrence whose span avoids every
   future deleted seam;
2. a complete \(M_{0,x}\)-augmenting linkage to a saturating matching
   of the new compiler graph;
3. the depth-\(d\) rank and wall acceptance of the whole new collar; and
4. protection of every guard occurrence, controller footprint, matching
   path, and changed cell from hidden reopening by later nodes.

It is **private/aligned** when the noncommon resources of distinct nodes are
disjoint, and every resource meets the retained global state only through
its declared boundary.

### Theorem 7.2 (positive guarded gluing-tree theorem)

Assume:

1. the upstream palette/decoration, component, gap, run, physical socket and
   voltage states are accepted in the exact boundary theorem;
2. every nonregeneration gluing edge has a phase-aligned physical lift;
3. every node has a private RSB guard packet; and
4. the compiler skeleton is occurrence-exact and transported on every
   stable fragment.

Then depth-two upper coverage, depth-\(d\) erosion legality, and a
lower-target saturating compiler matching hold after every gluing step and
at the root.

Inside the frozen-exterior/private-bank subclass, the last-provider
condition of item 1 and the local Hall/augmenting-linkage condition of item
2 are also necessary.

#### Proof

Induct on the bottom-up gluing order.  Theorem 2.1 transports every internal
depth-two occurrence.  Definition 7.1(1) replaces every last witness that
the current collar destroys, and item 4 keeps the chosen replacement alive
later.

Theorem 4.1 transports every internal erosion letter and verifies all new
rank and wall tests in the collar.  Theorem 5.2 replaces exactly the
matching edges lost from the common compiler graph by a vertex-disjoint
augmenting linkage.  Toggling that linkage gives a global matching at the
current step.  Privacy and the no-hidden-reopening condition ensure that a
later node either leaves those records unchanged or exposes and repairs them
again; no undeclared target, cell, controller or path vertex is silently
reused.  The fixed-skeleton hypothesis prevents a nominal local choice from
changing an undeclared cell elsewhere.

The other five coordinates are preserved by antecedent 1 and their own
exact composition laws.  This proves sufficiency.  With a frozen exterior,
no undeclared outside witness or cell can repair the local losses, so
Theorems 2.1 and 5.2 also give necessity of the two local conditions.
\(\square\)

### Corollary 7.3 (static all-cuts guard)

A stronger, simpler sufficient condition is:

1. every depth-two target has one base occurrence whose transported span
   avoids the union of every future deleted seam; and
2. the initial compiler graph has a saturating matching all of whose named
   cell dependency spans avoid that union.

Then both objects transport unchanged through the whole gluing tree.  No
new collar witness or compiler augmentation is needed.

Theorem 7.2 is more flexible: it permits a collar to spend old duplicates
and to repair compiler matches locally.

### Corollary 7.4 (correct extension of the private/aligned catalogue)

The private/aligned catalogue of item2175 becomes an RSB-safe sufficient
catalogue after adjoining:

1. phase-aligned physical fragment records;
2. the depth-two last-birth guard relation;
3. the changed erosion-cell signatures and wall tests; and
4. the pairing-resolved compiler augmenting-linkage relation.

An arbitrary component spanning tree then remains valid only when these
additional rows accept.  Existing component/gap/linkage privacy does not
imply them.

## 8. Literal bounded-switch obstruction in \(J(8,4)\)

Use digit strings for subsets of \(\{0,1,\ldots,7\}\).  Consider the two old
path collars

\[
\begin{split}
 1257-0127-0137-0136,\\
 3457-0347-0247-0246,
\end{split}                                           \tag{8.1}
\]

and switch the two middle seams to obtain

\[
\begin{split}
 1257-0127-0247-0246,\\
 3457-0347-0137-0136.
\end{split}                                           \tag{8.2}
\]

Every displayed edge is a Johnson edge.  This is a two-cut path splice,
so \(s=2\).

The four old depth-two intersections are

\[
                         17,\ 01,\ 47,\ 04,           \tag{8.3}
\]

and the four new ones are

\[
                         27,\ 02,\ 37,\ 03.           \tag{8.4}
\]

All have rank \(r-d=2\).  The consecutive deepest pairs inside the two
paths meet in

\[
 17\cap01=1,\quad47\cap04=4,\quad
 27\cap02=2,\quad37\cap03=3,                          \tag{8.5}
\]

of rank \(r-d-1=1\).  Thus every displayed depth-two rank and wall test
passes on both sides.

The old depth-two upper unions are

\[
 012357,\ 012367,\ 023457,\ 023467,                  \tag{8.6}
\]

whereas the new ones are

\[
 012457,\ 012467,\ 013457,\ 013467.                  \tag{8.7}
\]

All have rank \(r+2=6\).  Hence the switch attains the boundary maximum

\[
                         b_2=4=2s                    \tag{8.8}
\]

on both the lower and upper depth-two rows.

In the pure depth-two envelope incidence instance with the one lower target

\[
                         S=17,                        \tag{8.9}
\]

the old collar has exactly one containing envelope, namely \(17\), while
the new collar has none.  Simultaneously \(012357\) is an old upper
depth-two occurrence with no new collar replacement.

This proves:

> the displayed local depth-two rank and internal wall tests do not force
> preservation of the local depth-two occurrences or lower envelope
> incidences.

The example is parameter-minimal in the following scoped sense:
\(d=2\) is the first deeper row, and two cuts are the minimum for a
nontrivial degree-preserving path splice.  No claim of minimum ambient
dimension among all Catalan gadgets is made.  In particular, (8.1)--(8.2)
is a literal Johnson collar, not an audited item2158-transparent Catalan
decoration.

## 9. Immediate-shadow-neutral depth-two loss

There is also a symbolic obstruction showing why even immediate-shadow
neutrality is insufficient.

Let \(|H|=r-2\), and choose distinct

\[
                         a,b,c,x,p\notin H.
\]

Put

\[
 E_a=H+a+x,\quad E_b=H+b+x,\quad E_c=H+c+x,           \tag{9.1}
\]

\[
 Q_{ab}=H+a+b,\quad Q_{bc}=H+b+c,\quad Q_{ca}=H+c+a.
                                                               \tag{9.2}
\]

Replace the three old seams

\[
 E_aQ_{ab},\quad E_bQ_{bc},\quad E_cQ_{ca}            \tag{9.3}
\]

by

\[
 E_aQ_{ca},\quad E_bQ_{ab},\quad E_cQ_{bc}.           \tag{9.4}
\]

The three old immediate upper colours are

\[
 H+a+b+x,\quad H+b+c+x,\quad H+c+a+x,
\]

and the new multiset is the same three sets in cyclic order.  The lower
seam colours \(H+a,H+b,H+c\) are also fixed.  This is the
common-exterior neutral incidence hexagon.

Nevertheless, if the retained predecessor of \(E_a\) is

\[
                         R_a=H+x+p,                   \tag{9.5}
\]

then one depth-two window changes from

\[
 R_a\cup E_a\cup Q_{ab}=H+p+x+a+b                    \tag{9.6}
\]

to

\[
 R_a\cup E_a\cup Q_{ca}=H+p+x+a+c.                   \tag{9.7}
\]

Thus preservation of both immediate seam palettes does not imply
depth-two preservation.  Since consecutive Boolean levels contain no
4-cycle, the incidence hexagon is the smallest nontrivial alternating
incidence circuit.  This is a local palette-neutral obstruction; it does
not assert that a complete Hamilton factor makes (9.6) globally unique.

## 10. Application to the repaired standard \(m=5\) packet

Items2178,2181 and2183 now give the following exact chain at \(m=5\):

1. both turn palettes are complete;
2. the augmented occurrence graph has a forced-port perfect matching of
   order \(210\);
3. the original/repaired common graph has deficiency \(13\) and an exact
   thirteen-path augmenting linkage;
4. the gap-colour graph is a forest and the ordinary binary trace is on the
   forest side in all four standard-glue states;
5. the forced decoration lifts to a \(252\)-vertex, \(210\)-edge,
   \(42\)-path forest in \(J(10,5)\); and
6. one literal set of \(42\) colour-injective connectors closes that forest
   to a \(252\)-cycle.  Since the clean quotient has \(h=1\), primitive
   voltage is vacuous after this one-cycle check.

The two certified private objects across the glue cube are the lower
**gap-owner** paths

\[
 [82]-g_{83,340}-[84]-g_{85,90}-[88],\qquad
 [50]-g_{51,308}-[52]-g_{53,58}-[56].                \tag{10.1}
\]

They are not named physical endpoint sockets.  The final connector set is
positive, but its occurrence-labelled transport and private ownership
through all intermediate packet/glue states remain open.  The component
evolution is also nonmonotone:

\[
 [36,72,144]\to[36,216]\to[36,48,168]\to[120,132].
                                                               \tag{10.1b}
\]

Thus the static two-label aligned-one-edge component face does not describe
the whole packet.  Also, although the ordinary binary trace is on its forest
side, item2176's stricter zero/one run state fails in all four cube states;
one preglue component has no protected (0^4) breaker.  This mark-trace
failure is distinct from the physical coordinate-residence obstruction
below.

This is a genuine regeneration checkpoint, not an inherited-shadow
certificate.  The three repair switches change representatives.  Their
common-core path count is bounded, but their downstream physical support
cannot be inferred from \(t_{\rm total}=15\).

More precisely, the frozen common-core symmetric difference has thirteen
augmenting paths of vertex lengths

\[
                         \underbrace{4,\ldots,4}_{11\ {\rm paths}},6,16
                                                               \tag{10.1a}
\]

and four alternating cycles of vertex length four.  These data certify the
matching linkage.  They do not specify the phase-resolved physical
chronology or its changed-seam set.

The downstream flag audit is positive.  Before closure, the internal path
windows miss only upper masks

\[
                         \mathtt{0ef},\mathtt{0fd}
 \quad(q=2),\qquad \mathtt{0ff}\quad(q=3),            \tag{10.2}
\]

and lower mask

\[
                         \mathtt{281}\quad(q=2).      \tag{10.3}
\]

The \(42\) connector seams supply all four.  The resulting cycle covers the
complete upper-union and lower-intersection tower through \(q=5\).
Exactly \(46\) linear openings retain that all-depth support, \(39\) of them
at connector edges.

The compiler row nevertheless fails before Hall.  Here \(k=10\) and
\(d(10)=2\).  The \(42\) path interiors contain exactly \(31\) coordinate
one-runs of length two, bounded strictly inside \(18\) paths, with coordinate
multiplicities

\[
                         (5,5,2,3,3,3,3,3,3,1).      \tag{10.4}
\]

Path reversal, permutation and endpoint socket choice preserve every one of
these runs.  Hence no intact-path opening is depth-two resident, so no
valid depth-two maximal-erosion representation, and therefore no lower
erosion compiler, exists on that face.

The exact next move is therefore a controlled-debt interior physical
rethread packet—possibly with a growing number of bounded-port circuits—
which:

1. hits the closed edge span of every one of the \(31\) internal run-two
   occurrences;
2. retains or recreates one complete all-depth witness for every target,
   starting from one of the \(46\) valid openings;
3. passes every new depth-two rank and wall collar test; and
4. only then supplies an exact lower compiler skeleton and the Hall linkage
   of Section 5.

If this interior rethread has actual seam count \(s\), its possible
depth-two losses and erosion changes are exactly the collar multisets and
satisfy

\[
                         b_2\le2s,\qquad b_2^{\rm erosion}\le2s.
                                                               \tag{10.5}
\]

The first inequality controls upper/lower depth-two witnesses; the second
is the \(d=2\) maximal-erosion column budget.  These physical collars, not
the abstract \(C_{10}\) sizes, are the guard budget.

## 11. Exact proved boundary

Proved:

1. the exact signed fixed-depth window delta (2.3) and sharp collar size
   (2.4);
2. the depth-two upper last-provider criterion;
3. the depth-\(d\) erosion and \(h\)-letter compiler dependency bounds;
4. the exact fixed-skeleton Hall-cut and augmenting-linkage criteria;
5. the phase/linkage obstruction to any generic \(O(t)\) theorem;
6. the conditional private/aligned shadow--compiler gluing theorem; and
7. the literal \(J(8,4)\) and symbolic palette-neutral obstructions.

Not proved:

1. a uniform controlled-debt bounded-port repair theorem for every \(m\),
   with possibly growing packet cardinality but bounded live boundary and
   debt;
2. a phase-aligned bounded physical lift for every accepted transparent or
   representative-changing polygon;
3. existence of private depth-two witnesses and compiler guard banks for
   every gluing tree;
4. an interior rethread of the repaired \(m=5\) lift which removes all
   \(31\) immutable run-two occurrences while retaining the all-depth tower;
5. a lower compiler for that repaired \(m=5\) rethread; and
6. recursively private endpoint-pairing/resource transport and the complete
   all-\(m\) common-cap compiler.

The first downstream RSB row is therefore no longer an undefined
“preserve shadows” condition.  It is the exact physical seam-collar and
compiler-linkage state above.  The remaining theorem is existence of an
accepting regeneration/guard schedule.

## 12. Sources

The proof uses and sharpens only the exact statements in:

* MATH_SYNTHESIS_SHORTEST_ALLK_CHAIN_AND_EXACT_MISSING_THEOREM_20260731.md;
* MATH_THEOREM_AD_CATALAN_LEAF_RUN_SOCKET_BOUNDARY_STATE_AND_ROUTING_OBSTRUCTION_20260731.md;
* MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md;
* MATH_THEOREM_CATALAN_JOINT_GRAPHIC_GAMMOID_GLUING_FACE_20260731.md;
* THREAD_AD_EROSION_SAFE_DEBRUIJN_AND_OWNER_OCCURRENCE_FLOW_20260728.md;
* THREAD_K_MMM_COMPILER_READY_DECORATED_PAIR_AND_PASCAL_DIAMOND_RECURSION_20260729.md;
* MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md;
* MATH_AUDIT_CATALAN_M5_THREE_C10_GAIN_SOCKET_COMPATIBILITY_20260731.md;
* THREAD_A_M5_THREE_C10_DOWNSTREAM_COMPATIBILITY_AUDIT_20260731.md;
* MATH_THEOREM_CATALAN_PASCAL_SECTOR_DETERMINANT_AND_TWO_COPY_NOGO_20260731.md.

No web result, SAT solve, or heavy finite search is used.  The
\(J(8,4)\) arithmetic is independently replayed in the companion audit.
