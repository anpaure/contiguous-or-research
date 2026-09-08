# Relative PPR routers, the authenticated Catalan atlas, and the Pascal regeneration gate

Date: 2026-07-30  
Lane: K  
Status: **unconditional topology correction, exact finite atlas audit, exact
Pascal closure theorem, and a quantitative sparse-regeneration obstruction;
the all-odd existence lemma remains open.**

## 0. Result and proof boundary

This note answers two separate questions which must not be conflated.

1. What literal router data are actually present in the authenticated
   `k=11,13,15` optimal certificates?
2. Which part of those data is closed under the odd/even Pascal operations?

The finite answer is sharp.  After splitting at a coordinate, the three
certificates use the same near-perfect open-switch topology:

\[
 (u_1,v_1),(u_2,v_2)
 \longmapsto (u_1,v_2),                              \tag{0.1}
\]

with `k=11` the one-cut degeneration.  The shore types are different:

\[
 \begin{array}{c|c|c}
 k&\text{router}&\text{physical type}\\ \hline
 11&159\!-219\text{ opened}&BB\\
 13&(2395\!-2515),(2167\!-2391)
       \mapsto(2515\!-2391)&BB\\
 15&(19065\!-26745),(18041\!-20081)
       \mapsto(19065\!-18041)&AA.
 \end{array}                                         \tag{0.2}
\]

Each is topologically minimal for its fixed source component count.  Each
also has an exact occurrence-labelled service ledger: every old target has a
retained fragment witness except the targets explicitly listed below, and
each listed target has a literal seam or boundary replacement.

There are, however, two decisive corrections to the proposed induction.

* The `k=13` and `k=15` path endpoints are at Johnson distance two, not one.
  Thus the safe closing edge required by the original definition of
  \({\rm PPR}(r,d)\) does not exist.  A formal dummy edge may be used to
  compute fragment monodromy, but it is not a physical transition.
* The finite routers are relative routers with nonzero service/boundary
  ledgers.  They are not a verified all-depth zero-frame, compiler-pin-
  transparent parametric atlas.  In particular, the `k=15` compiler was
  solved afresh.

The correct finite theorem is therefore a **near-perfect boundary-PPR
theorem**.  It gives the same literal upper bound as PPR without requiring a
nonexistent physical closing edge.

The exact positive recursive statement is also proved here.  An all-depth
zero-frame router with an occurrence-labelled compiler-pin bijection remains
such a router under facet, union, fixed-core extension, relabelling, and the
four-sector Pascal diamond.  Relative service ledgers transform linearly as
well, but their physical boundary capacities must be reverified.

This does not yet prove the all-odd theorem.  Pure Pascal transport has the
tridiagonal depth rule

\[
 D\longmapsto E(D):=\{q:\{q-1,q,q+1\}\subseteq D\}; \tag{0.3}
\]

hence every finite depth band erodes.  Moreover, at critical
\(q=O(\sqrt r)\), \(O({\rm Cat}_r)\) seam collars cannot regenerate one
missing outer lower deck: that deck has \(\Theta(r{\rm Cat}_r)\) targets,
whereas the collars contain only \(O(q{\rm Cat}_r)\) fixed windows.  A
genuinely bulk, core-stable regeneration tile is necessary.

The proposed `codd.py --dup2` shortcut is also settled exactly.  Its quotient
half clauses would indeed give every physical upper target two edge-disjoint
witnesses, but that makes the model statewise impossible already at upper
depth one: for \(k=2r-1\ge7\), the factor has fewer than two edges per
rank-\((r+1)\) target.  The correct safe-opening condition is cut-dependent,
not universal duplicate coverage.

No SAT/CP solve, exhaustive search, web access, or heavy local computation is
used in this note.  The three new finite audits are solver-free replays of
frozen certificates.

## 1. Conventions

For a middle chronology \(T=(T_i)\), put

\[
 L_q(T)_i=\bigcap_{a=0}^{q}T_{i+a},\qquad
 U_q(T)_i=\bigcup_{a=0}^{q}T_{i+a}.                 \tag{1.1}
\]

A lower witness is always an expected-length, expected-rank window.  An
upper witness may be an arbitrary contiguous interval; when fixed width is
intended it will be said explicitly.

For an oriented factor and a set of deleted transitions, a witness is an
**interior witness** if its complete edge span avoids every deleted
transition.  Such a witness survives every reordering and reversal of the
resulting fragments which preserves that fragment internally.

A **service witness** is a literal witness in a new seam collar.  A boundary
pin is a literal occurrence supplied by the source prefix/suffix of the
linear compiler.  A router is **witness-transparent** when each required
target has either an interior witness or a declared service/boundary witness.
This is an occurrence statement, not a nonnegative aggregate load statement.

## 2. The universal coordinate-split skeleton

Let \(F\) be a lower-`q=1`-exact two-factor on

\[
 \binom{[2r+1]}{r+1},
\]

and fix a coordinate \(z\).  Put

\[
 \mathcal A={T:z\in T\}\cong\binom{[2r]}r,
 \qquad
 \mathcal B={T:z\notin T\}\cong\binom{[2r]}{r+1}, \tag{2.1}
\]

and \(C_r={\rm Cat}_r\).  Thus

\[
 |\mathcal A|=(r+1)C_r,\qquad |\mathcal B|=rC_r.    \tag{2.2}
\]

### Theorem 2.1 (exact Pascal shore counts)

The edge-type counts of \(F\) are forced:

\[
 e_{AA}=rC_r,\qquad e_{AB}=2C_r,\qquad
 e_{BB}=(r-1)C_r.                                  \tag{2.3}
\]

If every component of \(F\) meets both shores, then the induced graphs on
\(\mathcal A\) and \(\mathcal B\) are spanning linear forests with exactly
\(C_r\) paths on each shore.  Contracting these paths gives a bipartite
degree-two multigraph whose components are exactly the components of \(F\).

If \(F\) is positively \(d\)-resident, every \(A\)-path has at least
\(d+1\) vertices.  No corresponding lower bound on the \(B\)-path lengths
follows from positive residence alone.

#### Proof

A lower `q=1` colour contains \(z\) exactly when it is the intersection of
an `AA` edge.  Exactness therefore gives

\[
 e_{AA}=\binom{2r}{r-1}=rC_r.                       \tag{2.4}
\]

The degree sum on \(\mathcal A\) gives

\[
 2(r+1)C_r=2e_{AA}+e_{AB},                          \tag{2.5}
\]

so \(e_{AB}=2C_r\).  Subtracting from the total number
\((2r+1)C_r\) of factor edges gives \(e_{BB}=(r-1)C_r\).

If every factor component meets both shores, a shore-induced cycle would be
a factor component contained in one shore, so neither induced graph contains
a cycle.  Their path counts are therefore

\[
 |\mathcal A|-e_{AA}=C_r,\qquad
 |\mathcal B|-e_{BB}=C_r.                           \tag{2.6}
\]

Each path endpoint has one cross edge, so contraction is degree two and does
not change components.  Finally an \(A\)-path is precisely a positive run of
the trace of \(z\), proving the residence statement. \(\square\)

The qualification that every component meets both shores is necessary: a
shore-pure component is an induced cycle, not a run path.

## 3. The authenticated finite router atlas

The following statements were replayed from the frozen physical artifacts.
The split is \(z=10\) at `k=11`, \(z=12\) at `k=13`, and \(z=14\) at
`k=15`.

### 3.1 Exact shore/channel data

\[
\begin{array}{c|r|r|r|r|r|r}
k&r&C_r&AA&AB&BA&BB\\ \hline
11&5&42&210&42&42&168\\
13&6&132&792&132&132&660\\
15&7&429&3003&429&429&2574.
\end{array}                                         \tag{3.1}
\]

At `k=11` and `k=13`, the lower-with-`z`, lower-without-`z`, upper-with-`z`,
and upper-without-`z` channels are all complete.  Nevertheless the number of
strict rowwise forward/reverse Pascal blocks is respectively

\[
 0/42,\qquad 0/132.                                  \tag{3.2}
\]

The `AA` upper deficits are `40` and `147` and are repaired globally by
cross collars.  Thus neither base is a direct rowwise Pascal lift.

For `k=15`, every one of the fifteen coordinate splits has `429` paths on
each shore.  For \(z=14\), the contracted router has component sizes
`426+3` in run pairs.  Its `A`-path minimum is four, while the `B` histogram
begins

\[
 1^{22},2^{39},3^{73},4^{33},\ldots .               \tag{3.3}
\]

This is the exact reason that positive residence does not imply a dual-gap
buffer.

### 3.2 The `k=11` BB opening

The source is one physical cycle of length `462`.  Delete the `BB` edge

\[
 159-219.                                            \tag{3.4}
\]

The only targets without retained-fragment witnesses are

\[
 \text{lower }q=1:155,\qquad
 \text{lower }q=2:154.                              \tag{3.5}
\]

The verified one-core compiler pins them at source positions `464` and `1`,
respectively.  Every other fixed lower target and every proper arbitrary-
upper target has an interior witness.  The endpoints are Johnson-adjacent,
so the deleted edge itself is a physical formal closure in this case.

### 3.3 The `k=13` BB fusion

The source components have lengths `1547` and `169`.  Delete

\[
 2395-2515,qquad2167-2391,                          \tag{3.6}
\]

and insert

\[
 2515-2391.                                          \tag{3.7}
\]

The only targets without retained-fragment witnesses are

\[
 L_1=\{2135,2387\},\qquad L_2=\{2323\}.             \tag{3.8}
\]

The seam restores `2387`, and

\[
 2455\cap2515\cap2391=2323                          \tag{3.9}
\]

is the literal lower-`q=2` service window.  Source position `1718` supplies
`2135`.  Every other fixed lower target and every proper arbitrary-upper
target has an interior witness.

The independently audited one-core pin map has `1093` deterministic pins.
None of the selected pins uses the promoted interior seam halo

\[
 1546,1547,1548,1549,1550.                          \tag{3.10}
\]

Thus this particular interior compiler halo has \(D=0\); only the global
boundary/suffix data remain.

The final endpoints are `2395,2167`, and

\[
 |2395\triangle2167|=4.                              \tag{3.11}
\]

They are not a Johnson edge.  Moreover, none of the fifty frozen best
one-seam paths has Johnson-adjacent endpoints.

### 3.4 The `k=15` AA fusion

The all-depth resident source has components `6390+45`.  Delete

\[
 19065-26745,qquad18041-20081,                      \tag{3.12}
\]

and insert

\[
 19065-18041.                                        \tag{3.13}
\]

All `858` cross edges and all `BB` edges remain fixed.  The path signature is

\[
 (AA,AB,BB)=(3002,858,2574),                        \tag{3.14}
\]

and its linear block counts are `430` on `A` and `429` on `B`.

The fragment interiors already witness every fixed lower target of depths
`2,...,7` and every arbitrary-upper target except

\[
 20089\quad(|Y|=9),\qquad 28537\quad(|Y|=11).        \tag{3.15}
\]

The one seam supplies both:

\[
 19065\cup18041=20089,                               \tag{3.16}
\]

and the four-state interval at final middle indices `6387,...,6390` has
union `28537`.  The two deleted lower-`q=1` colours are

\[
 18553,qquad18033.                                  \tag{3.17}
\]

The seam colour `17017` recycles neither, and the two global source boundary
cells `0,6437` supply them injectively.

For this fixed cut pair the service ledger is minimal in the following
literal sense.  The two upper targets in (3.15) are distinct and neither has
an interior witness, so two accepting occurrences are necessary.  The two
lower colours in (3.17) are distinct, neither is recycled, and each nested
rank-seven boundary chain has capacity one, so two boundary pins are
necessary.  The displayed ledger attains both bounds.

The final endpoints are `26745,20081`, with

\[
 |26745\triangle20081|=4.                            \tag{3.18}
\]

Again there is no physical formal closing edge.  The exact compiler covers
all `4945` low targets and all `32767` nonempty masks, but it was solved
globally rather than transported from the pre-splice factor.

### 3.5 Minimal topology and noninheritance

A one-cycle factor needs at least one deleted edge to become a path.  A
two-cycle factor needs at least one deletion on each cycle and at least one
new join.  Hence (3.4) and (3.6)--(3.7), (3.12)--(3.13) are topologically
minimal.

They are not one inherited parent-cut template.  The `k=11` `BB` cut is not
a consecutive-union image.  At `k=13`, only the cut `2395-2515` is such an
image; the second cut and the new seam are not.  At `k=15`, the router is an
internal `AA` splice and is not a cross-port permutation at all.  A recursive
library which freezes both sector forests and rematches only the `AB` ports
therefore excludes an authenticated base case.

## 4. Near-perfect boundary PPR

The original PPR definition first completed the fragment router to one
physical cycle and then deleted a Johnson closing edge.  That condition is
stronger than the literal word problem.

### Lemma 4.0 (exact physical circular-opening dichotomy)

Let a collection of physical factor cycles be cut at a set \(C\) of actual
old edges and reassembled with actual new seams into a linear path.  All old
edge spans are interpreted modulo their own source component; no artificial
closure is allowed.

For every arbitrary-upper target \(Y\), the final path contains a witness of
\(Y\) if and only if at least one of the following holds.

1. An old cyclic witness interval of \(Y\) has physical edge span disjoint
   from \(C\).
2. A final witness interval crosses at least one new seam and is an accepting
   path of the literal accumulated-union automaton for \(Y\).

The same dichotomy holds for a fixed lower depth \(q\), with expected-rank
\((q+1)\)-state windows in place of arbitrary intervals.

#### Proof

Every final interval either lies wholly inside one retained fragment or
crosses a new seam.  In the first case it is exactly an old cyclic interval
whose old edge span avoids every cut.  The second case is exactly a path in
the final fragment/seam automaton, and acceptance says that its literal union
is \(Y\).  The lower statement is identical with intersection replacing
union. \(\square\)

Thus a kernel or witness count has meaning only on the actual physical
components and modular edge spans.  A fake cyclic closure of an opened word
can both create nonexistent witnesses and delete genuine kernel edges.

### Definition 4.1 (\(\partial_2{\rm PPR}(r,d)\))

Retain PPR's sector forests, named interior/service witnesses, physical
endpoint graph, and compiler data, but replace its topology/opening clauses
by the following.  The near-perfect endpoint assignment may be supplied
explicitly, as in the three finite certificates, or obtained from the
surplus condition of Theorem 4.2.

1. Choose one terminal tail \(a^*\) and one initial head \(b^*\), disjoint
   from the fixed service bank \(K\).
2. On the residual physical endpoint graph
   \(H^*=H-\{a^*,b^*\}\), extend \(K\) to a perfect matching.
3. Add a dummy arc \(a^*\to b^*\) **only** when computing fragment
   monodromy.  Protected alternating cycles in \(H^*\setminus K\) reduce
   this augmented monodromy to one component.
4. Delete the dummy.  The remaining physical chronology is one spanning
   path.  Every actual transition is Johnson-legal and passes residence.
5. The actual endpoints satisfy the two boundary q1 ledgers, the endpoint
   core/envelope equations, nonempty-envelope conditions, and the terminal
   \(d\)-suffix clauses.  A full occurrence-labelled linear
   \({\rm COMP}_d\) matching is supplied; it may be transported-and-repaired
   or freshly certified.

The dummy is never put into the middle chronology and need not be a Johnson
edge.

### Theorem 4.2 (near-perfect protected completion)

Let the two residual shores of \(H^*\) have size \(n-1\).  Suppose that, for
some integer \(h\ge0\),

\[
 |N_{H^*}(S)|\ge
 \min\{n-1,|S|+h\}                                  \tag{4.1}
\]

for every nonempty residual left set \(S\).  Then every service
matching \(K\subseteq H^*\) of size at most \(h\) extends to a perfect
matching of \(H^*\).

If protected alternating cycles outside \(K\) can fuse the augmented
monodromy to one component, deleting the dummy produces one literal spanning
path while retaining every protected witness and compiler pin.

#### Proof

Delete the endpoints of \(K\).  For a remaining left set \(S\), at most
\(|K|\) neighbours have been deleted, so (4.1) gives Hall in the residual
graph.  The physical bipartite incidence matrix is totally unimodular, hence
the completion is integral.

Fix the dummy throughout the alternating-cycle process.  Every alternating
cycle is contained in \(H^*\setminus K\), so every toggled edge is physical
and every protected socket remains fixed.  When augmented monodromy has one
component, removing its one dummy arc turns that component into a spanning
path from \(b^*\) to \(a^*\).  No legality claim was ever made about the
dummy. \(\square\)

### Theorem 4.3 (boundary-PPR compiler theorem)

If \(\partial_2{\rm PPR}(r,d)\) holds, then

\[
 \nu(2r+1)\le \binom{2r+1}{r+1}+d.                 \tag{4.2}
\]

#### Proof

Clauses 2--4 of Definition 4.1 give the literal middle spanning path;
Theorem 4.2 supplies those clauses in the surplus-completion branch.  The
declared interior and service bank gives every required fixed lower and arbitrary-upper target.
The endpoint ledger gives the targets lost at the two exposed boundaries.
The full occurrence-labelled \({\rm COMP}_d\) matching gives a nonzero source
word of length \(W+d\) whose depth-\(d\) erosion is that path and whose
lower intervals cover every low target.  The upper targets are witnessed by
the middle path itself.  This is exactly the fixed-chronology compiler
theorem. \(\square\)

Original PPR implies boundary-PPR by taking the deleted physical closing edge
as the dummy.  The converse is false inside the authenticated `k=13` and
`k=15` packages by (3.11) and (3.18).

### Corollary 4.4 (the three authenticated bases)

The data in Sections 2--3 and the frozen compiler certificates verify

\[
 \partial_2{\rm PPR}(5,3),\qquad
 \partial_2{\rm PPR}(6,3),\qquad
 \partial_2{\rm PPR}(7,3)                           \tag{4.3}
\]

for the fixed `k=11,13,15` packages, respectively.  Hence Theorem 4.3
contains all three optimal constructions.  This is a fixed-certificate
statement: it does not assert a parametric all-\(r\) family.

#### Proof

Theorem 2.1 supplies the two Catalan shore forests.  Equations
(3.4)--(3.18) and their audits give the near-perfect path topology and the
complete physical witness/service ledgers under Lemma 4.0.  The independently
audited words give the full occurrence-labelled linear compilers.  Every
condition in Definition 4.1 is therefore literal. \(\square\)

## 5. A functorial router class which really is Pascal-closed

Finite occurrence tables become inductive only after a symbolic
core-stability proof.  Raw similarity at three dimensions is not enough.

Let a router \(R:T\rightsquigarrow T'\) include:

* identical owner multiplicities;
* occurrence vectors \(\Delta L_q,\Delta U_q\) at every fixed depth;
* chosen arbitrary-upper witnesses before and after;
* an occurrence-labelled bijection of compiler pins
  `(core,envelope,target,position)`; and
* identical event queues on every declared socket.

Call \(R\) **all-depth zero-frame** if every fixed-depth signed vector is zero,
every chosen arbitrary-upper witness is carried to a witness of the same
target, and every compiler pin is carried by the displayed bijection.

### Theorem 5.1 (facet/union router functor)

Assume, throughout every transported interval and its endpoint guard, that
the two lower colours incident with each internal parent owner are distinct
for the facet row, and that the two incident upper colours are distinct for
the union row.  Equivalently, the relevant traces have no singleton positive
run, respectively no singleton zero-gap.  For \(q\ge1\),

\[
 \begin{aligned}
 \Delta L_q(\partial R)&=\Delta L_{q+1}(R),\\
 \Delta U_q(\partial R)&=\operatorname{shift}\Delta U_{q-1}(R),\\
 \Delta L_q(\nabla R)&=\operatorname{shift}\Delta L_{q-1}(R),\\
 \Delta U_q(\nabla R)&=\Delta U_{q+1}(R).
 \end{aligned}                                      \tag{5.1}
\]

The corresponding compiler envelopes have the same depth shifts.  Hence an
all-depth zero-frame, compiler-pin-transparent router has all-depth zero-frame
facet and union images.

The same conclusion is preserved under coordinate relabelling and adjoining
a fixed common core to every owner.

#### Proof

The fixed-window identities

\[
 L_q(\partial T)_i=L_{q+1}(T)_i,\qquad
 U_q(\partial T)_i=U_{q-1}(T)_{i+1},                \tag{5.2}
\]

and

\[
 L_q(\nabla T)_i=L_{q-1}(T)_{i+1},\qquad
 U_q(\nabla T)_i=U_{q+1}(T)_i                       \tag{5.3}
\]

hold occurrence by occurrence.  An arbitrary parent upper witness on
\([a,b]\) maps to the facet interval \([a-1,b]\), and, when \(b>a\), to the
union interval \([a,b-1]\); the displayed incident-colour hypotheses are
required on their endpoint guards.  Subtract the source and target occurrence
vectors to obtain (5.1).  The backward envelope identities are the same
intersection identities with reversed indexing, so the pin bijection lifts.
Relabelling commutes with intersection and union, while

\[
 L_q(Q\cup T)=Q\cup L_q(T),\qquad
 U_q(Q\cup T)=Q\cup U_q(T)                          \tag{5.4}
\]

for a fixed disjoint common core \(Q\).  Socket event equality gives the same
seam comparisons before and after the lift. \(\square\)

### Corollary 5.2 (four-sector diamond closure)

Let \(|\Omega|=2r-1\), let \(x,y\notin\Omega\), and put

\[
 A=\{x,y\}+\partial T,\quad X=\{x\}+T,\quad
 Y=\{y\}+T,\quad B=\nabla T.                        \tag{5.5}
\]

If the four lifted routers are assembled through identical certified sockets,
then

\[
 \{x,y\}+\partial R\ \oplus\ \{x\}+R\ \oplus\
 \{y\}+R\ \oplus\ \nabla R                       \tag{5.6}
\]

is an all-depth zero-frame, compiler-pin-transparent child router.

#### Proof

The four owner and target classes are disjoint according to their
intersection with \(\{x,y\}\).  Apply Theorem 5.1 in each class and add the
four zero vectors.  At owner depth zero, the facet and union owner decks are
the parent's lower- and upper-`q=1` decks, which are also preserved by the
zero-frame hypothesis. \(\square\)

This is a genuine recursive atlas theorem.  A finite symbolic router proved
for all common cores and relabellings may be copied recursively.  A finite
list of raw masks at `k=11,13,15` does not establish that symbolic statement.

### Relative ledgers

The theorem has an exact relative version.  If a router has a declared
service/boundary vector \(b\) with

\[
 \Delta+b=0,                                        \tag{5.7}
\]

then facet, union, and fixed-core extension act linearly on both terms, so

\[
 P(\Delta)+P(b)=0.                                  \tag{5.8}
\]

This is only an algebraic closure until every transformed service token has a
literal child seam or boundary cell.  Signature classes are disjoint, so one
unabsorbed parent target can branch to as many as four child debts.  A
bounded parent boundary bank therefore does not remain bounded under naive
iteration.  The transformed ledger must be absorbed back into interior
service, or the recursive generator must be zero-frame.

The authenticated `k=11,13,15` open switches are relative instances of
(5.7).  The `k=15` instance is not yet compiler-pin-transparent.

## 6. What the frozen Markov switches do and do not supply

The authenticated `k=15` all-depth factor was reduced through component
counts

\[
 9\longrightarrow4\longrightarrow3\longrightarrow2             \tag{6.1}
\]

by switches of support `4,6,4`.  A new occurrence-level replay compares all
four stages.

Each switch has zero occurrence drift on lower depths `1,2,3` and upper
depths `1,2`.  The first switch also has zero upper-depth-three drift.  The
first nonzero depths are

\[
\begin{array}{c|c|c|c|c}
\text{switch}&\text{first lower}&\ell_1\text{ drift}
 &\text{first upper}&\ell_1\text{ drift}\\ \hline
4&4&60&4&45\\
6&4&120&3&60\\
4&4&60&3&60.
\end{array}                                         \tag{6.2}
\]

Thus none is an all-depth zero-frame router.  Completeness at every stage is
real, but it is achieved by changing which occurrence witnesses a target.
This distinction is harmless for the finite factor and decisive for a
functorial pin-preserving induction.

The same replay shows that no single fixed literal witness bank survives the
whole chain at the shallow depths; replacement witnesses are essential.  No
claim is made that this excludes a larger compound zero-frame packet.

## 7. Exact interior Pascal depth rule

The four-sector construction (5.5) has the following complete fixed-window
ledger for \(q\ge1\):

\[
\begin{array}{c|c|c}
\text{sector}&L_q&U_q\\ \hline
A&\{x,y\}+L_{q+1}(T)&\{x,y\}+U_{q-1}(T)\\
X&\{x\}+L_q(T)&\{x\}+U_q(T)\\
Y&\{y\}+L_q(T)&\{y\}+U_q(T)\\
B&L_{q-1}(T)&U_{q+1}(T).
\end{array}                                         \tag{7.1}
\]

Reversing the `B` row changes only the based index.  Backward compiler
envelopes have the same depth dependencies \(q+1,q,q,q-1\).

The child lower target counts in the signature classes
`xy`, `x/y`, and empty are

\[
 \binom{2r-1}{r-q-1},\qquad
 2\binom{2r-1}{r-q},\qquad
 \binom{2r-1}{r-q+1},                               \tag{7.2}
\]

while the upper counts are

\[
 \binom{2r-1}{r+q-1},\qquad
 2\binom{2r-1}{r+q},\qquad
 \binom{2r-1}{r+q+1}.                               \tag{7.3}
\]

### Theorem 7.1 (Pascal interior closure)

Suppose the parent has occurrence-labelled lower, upper, and compiler
packages at depths \(q-1,q,q+1\), including the required empty-old-part
ports.  Then all four intact child interiors have complete depth-\(q\)
packages.  The four lifted compiler matchings combine integrally because
their target and position shores have distinct new-label signatures.

Consequently, if these hypotheses hold simultaneously at every required
fixed depth, every arbitrary-upper target also has a transported or service
witness, the promoted halo matching passes, and the near-perfect
fusion/boundary clauses of Section 4 pass, then the child satisfies full
boundary-PPR.  At one specified \(q\), the theorem supplies only that
\(q\)-layer and its compiler package.

#### Proof

Equations (7.1) transport the witnesses and envelopes.  The new-label
signature partitions both targets and positions, so the four occurrence-
labelled matchings are disjoint.  Only windows meeting actual joins are not
covered by this interior transport; those are exactly the declared service
and halo clauses.  Apply Theorem 4.3. \(\square\)

## 8. Depth-band extinction

Let \(D\subseteq\mathbb Z\) be the depths for which one parent chronology
carries all three packages required in Theorem 7.1.  Pure four-sector
transport guarantees

\[
 E(D)=\{q:\{q-1,q,q+1\}\subseteq D\}.               \tag{8.1}
\]

### Theorem 8.1 (iterated erosion of certified depths)

For every \(t\ge0\),

\[
 E^t(D)=\{q:[q-t,q+t]\cap\mathbb Z\subseteq D\}.    \tag{8.2}
\]

In particular,

\[
 E^t([a,b])=[a+t,b-t],                              \tag{8.3}
\]

with the interval empty when \(2t>b-a\).

#### Proof

Equation (8.2) is immediate at \(t=0\).  Applying (8.1) to the induction
hypothesis requires all three intervals centred at \(q-1,q,q+1\); their union
is exactly \([q-(t+1),q+(t+1)]\). \(\square\)

Thus no finite band at `k=11,13,15` is an all-dimension compiler induction.
Even complete finite shadow towers do not supply arbitrarily deep adjacent-
depth compiler packages.  A recursion must regenerate the eroded outer
packages at every generation.

## 9. A quantitative sparse-regeneration obstruction

The previous theorem is formal.  The next one shows that an omitted outer
deck cannot be recreated by merely adding another \(O(C_r)\) seam atlas.

Let \(s_A\) be the number of new `A--A` joins in an intact four-sector
assembly.  Let \(b_A\) be the number of declared boundary fixed-window cells
available outside their ordinary collars.

### Theorem 9.1 (lower outer-deck collar bound)

Let \(h^A_{q+1}\) be the number of parent lower depth-\(q+1\) targets whose
corresponding child `xy` target has no witness wholly inside a retained
`A` fragment.  Suppose all of them are restored using only new `A--A` joins
and the declared boundary cells.  Then

\[
 h^A_{q+1}\le q s_A+b_A.                            \tag{9.1}
\]

At compiler depth \(d\), in the signature-preserving lifted compiler, if
\(H_{\rm comp}\) corresponding `xy` targets have no eligible intact `A`
envelope and all are assigned only to promoted `A` halos or the declared
boundary cells, then

\[
 H_{\rm comp}\le s_A(d+2)+b_A^{\rm comp}.           \tag{9.2}
\]

#### Proof

A lower target containing both \(x,y\) can be the intersection of a middle
window only if every state in that window contains both labels.  Only `A`
states do.  Hence every noninterior witness is a fixed `q`-window crossing an
`A--A` join, or one of the declared boundary cells.  Exactly \(q\) starts of
a \((q+1)\)-state window cross one seam.  This proves (9.1).

The promoted compiler halo of one seam has at most \(d+2\) positions.
Outside intact envelopes, only those positions and the declared boundary
positions have positive incidence degree.  This proves (9.2). \(\square\)

The arbitrary-upper analogue is deliberately not asserted: an arbitrary
upper witness can be longer than its rank difference, so one seam may belong
to more than \(q\) candidate intervals.  Such targets require the exact
accumulated-union automaton.

If the complete outer lower deck is absent, then

\[
 h^A_{q+1}=\binom{2r-1}{r-q-1}.                     \tag{9.3}
\]

The exact ratio to \(C_r\) is

\[
 \frac{\binom{2r-1}{r-q-1}}{C_r}
 =\frac{r+q+1}{2}
   \prod_{j=1}^{q}\frac{r-j}{r+j+1}.                \tag{9.4}
\]

For \(q\le r/4\),

\[
 \prod_{j=1}^{q}\frac{r-j}{r+j+1}
 \ge
 \exp\!\left(-\frac{2(q^2+2q)}r\right).            \tag{9.5}
\]

Indeed,

\[
 \log\frac{r+j+1}{r-j}
 =\log\!\left(1+\frac{2j+1}{r-j}\right)
 \le\frac{2j+1}{r-j},                              \tag{9.6}
\]

and summing, with \(r-j\ge3r/4\), gives a coefficient at most `4/3`, hence
the displayed coefficient `2` is safe.

### Corollary 9.2 (no sparse seam regeneration at Gaussian depth)

If \(s_A\le\kappa C_r\), then an entirely absent outer deck can be restored
only if

\[
 \kappa q+\frac{b_A}{C_r}
 \ge
 \frac r2
 \exp\!\left(-\frac{2(q^2+2q)}r\right).             \tag{9.7}
\]

For fixed \(\kappa\), \(q=O(\sqrt r)\), and
\(b_A/C_r=o(r)\), this fails for all sufficiently large \(r\).  In
particular, the `2C_r-1` interface budget and `O(d)` boundary package of the intact
Pascal assembly cannot manufacture a missing outer deck.

Any successful regeneration by bounded-capacity fixed-window seam/collar
actions at that scale must either carry the outer deck from the parent or use

\[
 \Omega\!\left(\frac r q C_r\right)                 \tag{9.8}
\]

such actions.  At \(q=\Theta(\sqrt r)\), this is
\(\Omega(\sqrt r\,C_r)\), still sublinear in the middle width but
parametrically larger than a Catalan seam atlas.

## 10. Residence buffer consumption

On every intact facet sector, a parent one-run of length \(\ell\) becomes a
run of length \(\ell-1\).  Therefore child depth-\(d\) positive residence
requires

\[
 \min\ell(T)\ge d+2.                                \tag{10.1}
\]

The union sector has the dual zero-gap loss.  A construction carrying both
sectors biresidentially needs one extra unit in both queues.

The authenticated bases have target depth `3` and minimum positive run
`4`; they have no spare facet unit.  In the exact `k=15 -> 16` calibration,
`1425` physical length-four runs become forbidden length-three facet runs.
This is not a compiler or Hall defect.  It is an interior event-buffer
defect.  A valid recursive tile must refresh the run/gap queue as well as the
two eroded depth packages.

## 11. The concrete all-r regeneration lemma

The preceding theorems reduce the missing induction to one parametric
primitive rather than another endpoint-completion theorem.

Let \(d_r=d(2r+1)\), and let \(I_r\) be a finite interval of depths centred
at \(d_r\).  Define `BRG(r)` to be the following statement.

> **Bulk regenerative router `BRG(r)`.**  Starting from the four-sector
> Pascal transport of a boundary-PPR certificate carrying all packages in
> \(I_r\), there is one core-stable, occurrence-labelled physical router
> which:
>
> 1. preserves every package in \(E(I_r)\);
> 2. supplies the missing shell packages in \(I_{r+1}\setminus E(I_r)\)
>    by fresh interior witnesses and a physical compiler matching;
> 3. restores the one unit of facet/union event buffer needed for the next
>    generation;
> 4. absorbs every transformed relative service debt into interior service,
>    leaving only the declared final two-boundary ledger;
> 5. is compatible with near-perfect protected completion and leaves one
>    spanning path satisfying the endpoint/suffix compiler clauses.

The router is allowed the bulk support scale identified by (9.8) in the
wholly-missing-outer-deck, bounded-collar regime; it is not required to be a
bounded collar packet.

### Theorem 11.1 (recursive closure through BRG)

Suppose a verified base boundary-PPR certificate carries every package in
\(I_{r_0}\), and `BRG(r)` holds for every \(r\ge r_0\).  Then boundary-PPR
holds at depth \(d_r\) for every \(r\ge r_0\), and therefore

\[
 \nu(2r+1)\le\binom{2r+1}{r+1}+d_r                \tag{11.1}
\]

for every such \(r\).

#### Proof

Theorem 7.1 transports the interior packages in \(E(I_r)\).  `BRG(r)`
restores the missing shells, event buffer, service ledger, compiler pins, and
near-perfect topology, producing the full state at \(r+1\).  Induction gives
the state for every \(r\), and Theorem 4.3 gives (11.1). \(\square\)

This is not a claim that `BRG(r)` has been proved.  It is the exact remaining
all-r lemma after the universal matching/TU completion and the finite router
mining.  Sections 8--10 prove that an intact-sector tile cannot be `BRG(r)`
when an outer deck is wholly absent and its repair is restricted to
bounded-capacity fixed-window collars/boundary cells.  They do not exclude a
PBBS recursion which already carries additional outer witnesses or performs a
bulk interior rematching.

## 12. Physical two-witness banks and the `codd.py --dup2` audit

Only in this section, reset \(r=(k+1)/2\), so \(k=2r-1\); this is the
notation used by `codd.py` and differs by one from the semilength convention
in Sections 2--11.

The new `--dup2` option must be separated from the approximate
`kernelcount.py` census.  The option itself has a useful exact physical
meaning inside the strict equivariant c-space normal form.

Let

\[
 W=\binom{k}{r}=kN,\qquad
 T_i=\{x:c_{i-xN}=1\},                              \tag{12.1}
\]

with indices modulo \(W\), and let \(\rho\) rotate the coordinates by one.
Then

\[
 T_{i+N}=\rho T_i.                                  \tag{12.2}
\]

Despite the file header's reference to physical halves, the emitted duplicate
clauses split the quotient residues into the two linear
intervals

\[
 H_0=[0,\lfloor N/2\rfloor),\qquad
 H_1=[\lfloor N/2\rfloor,N),                        \tag{12.3}
\]

and require, for every nonfull upper target orbit, one selected union window
lying wholly in each interval.  The selected target images in the two halves
need not be the same image.

### Lemma 12.1 (quotient halves lift to physical disjoint witnesses)

Assume the strict c-space clauses are satisfied.  The `--dup2` upper clauses
imply that every physical nonfull upper target \(Y\) has two literal union
witnesses whose physical edge spans are disjoint.

#### Proof

Suppose the selected half-\(h\) window begins at quotient residue \(j_h\),
has width \(w_h\), and has union \(Y_h\) in the orbit of \(Y\).  Choose
\(t_h\) with \(\rho^{t_h}Y_h=Y\).  Equation (12.2) sends it to the physical
window beginning at

\[
 j_h+t_hN,                                           \tag{12.4}
\]

which still has start and edge residues in \(H_h\).  Because the original
window lies wholly in the half, it does not wrap at either half boundary.
The two residue edge sets are disjoint, so their physical lifts are
disjoint.  This argument also handles short target orbits: only existence of
some aligning rotation is used. \(\square\)

### Lemma 12.2 (the correct physical cut lemma)

Let \(F\) be any physical cycle factor and let \({\cal W}(Y)\) be the edge
spans of literal witnesses of an upper target \(Y\).

1. A cut set \(C\) retains an old interior witness of \(Y\) exactly when some
   \(I\in{\cal W}(Y)\) satisfies \(I\cap C=\varnothing\).
2. If \(Y\) has \(c+1\) pairwise edge-disjoint witnesses, every cut set of
   size at most \(c\) preserves \(Y\).
3. If every target has one witness in each of two disjoint physical banks and
   all cuts lie in one bank, the other bank preserves every target,
   independently of the number of cuts.

#### Proof

Item 1 is the definition of an interior witness.  In item 2, one cut edge can
meet at most one member of a pairwise edge-disjoint family, so \(c\) cuts
cannot hit all \(c+1\) witnesses.  Item 3 is immediate. \(\square\)

Consequently, if a satisfying `--dup2` c-word is one physical Hamilton cycle,
**every single old-edge opening is upper-safe**.  The full-universe target is
witnessed by the whole opened spanning path.  This is a real
kernel-avoidance theorem; no numerical kernel census is needed.

The conditional conclusion is, however, already too strong at upper depth
one.

### Theorem 12.3 (statewise q1 capacity obstruction)

Let \(k=2r-1\) and let a cyclic Johnson chronology contain every rank-\(r\)
owner once.  If every rank-\((r+1)\) target has two edge-disjoint union
witnesses, then

\[
 \binom{2r-1}{r}
 \ge 2\binom{2r-1}{r+1}.                            \tag{12.5}
\]

Equivalently, \(r\le3\).  Hence every `--dup2` instance in the relevant
range \(k\ge7\) is UNSAT, independently of residence, lower rows, or the
compiler.

#### Proof

Let an interval witness a rank-\((r+1)\) target \(Y\).  Every state in the
interval is an \(r\)-subset of \(Y\).  Consecutive states are distinct
Johnson neighbours, so the union of the endpoints of **every edge in the
interval** is exactly \(Y\).  Two edge-disjoint witnesses therefore require
at least two distinct factor edges of upper colour \(Y\).

Upper colours of distinct targets partition the factor edges.  Summing the
required load two over all \(\binom{2r-1}{r+1}\) targets gives (12.5).  But

\[
 \frac{2\binom{2r-1}{r+1}}{\binom{2r-1}{r}}
 =\frac{2(r-1)}{r+1},                               \tag{12.6}
\]

which is at most one exactly when \(r\le3\). \(\square\)

For the authenticated dimensions the impossible demand is respectively

\[
 462<660,\qquad1716<2574,\qquad6435<10010,           \tag{12.7}
\]

at `k=11,13,15`.

Thus the useful safe-opening condition is necessarily cut-dependent.  For a
chosen cut edge, only targets whose witness kernels contain that edge require
an alternative witness.  Demanding two disjoint witnesses for every q1
target spends more occurrences than exist.

More sharply, even if the upper-`q=1` deck is complete, at most

\[
 W-\binom{2r-1}{r+1}=\frac{2W}{r+1}
\]

targets can receive a second edge.  At least

\[
 2\binom{2r-1}{r+1}-W=\frac{r-3}{r+1}W
\]

physical upper-`q=1` targets are forced to have load exactly one.

There is a much cheaper cut-aware fact.  For a fixed old edge \(e\), any
rank-\((r+1)\) witness interval containing \(e\) has target equal to the
upper colour of \(e\).  Hence a single opening can endanger at most one
first-upper target.  The viable invariant is a distinguished-opening witness
bank plus a literal replacement for that one colour, not duplicate coverage
of the whole first-upper deck.

In fact the first-upper kernel is completely classified.  Let

\[
 m(Y)=|\{e:T_i\cup T_{i+1}=Y\}|.
\]

If \(m(Y)=1\), every witness interval uses the unique edge, so its witness
kernel is that singleton.  If \(m(Y)\ge2\), the distinct one-edge witnesses
already have empty common intersection, so the kernel is empty.  When the
first-upper deck is complete,

\[
 \sum_Y(m(Y)-1)
 =W-\binom{2r-1}{r+1}
 =\frac{2W}{r+1}={\rm Cat}_r.                       \tag{12.8}
\]

Thus a q1-safe **cut edge** always exists: choose any edge whose upper colour
has multiplicity at least two.  The real safe-opening gate is whether one of
these Catalan-excess edges also avoids every **deeper** upper kernel and
passes residence/compiler boundary conditions.

If the factor is one physical cycle and is lower-`q=1` exact, opening such an
edge gives a spanning path, deletes exactly one lower colour, and deletes no
upper first-shadow colour.  Hence every lower-exact/upper-complete odd
one-cycle factor has a one-edge opening with the sharp q1 ledger

\[
 (\text{lower debt},\text{upper debt})=(1,0).        \tag{12.9}
\]

Only the deeper shadow kernels and the literal compiler pin for that one
lower colour remain.  This is the correct first-shadow opening lemma to use
in PPR; universal duplicate coverage is unnecessary.

It is not PPR by itself.  Two witnesses need not survive two cuts on two
source components, a component-fusion rethread can hit both, and the clauses
encode only lower `q=1,q=2`, not the all-depth lower tower; they do not
protect residence collars after rethreading or compiler pins.  For a
two-cycle near-perfect fusion one needs three
edge-disjoint witnesses, a common cut-free bank, or literal service
replacements for targets hit twice.

### 12.1 Independent fixed-width and recursion obstructions

The code uses

\[
 \{2,3,4,6,9,13\}                                   \tag{12.10}
\]

as its only witness widths.  Conditional on a satisfying assignment, such a
selected interval would be a genuine arbitrary-upper witness.  The q1
capacity theorem has already ruled out the relevant dimensions; independently,
the width restriction would also block an all-r recursion.

A rank-\((k-1)\) target in a rank-\(r\) Johnson chronology needs at least

\[
 (k-1-r)+1=r-1                                      \tag{12.11}
\]

middle states.  Hence at \(k\ge29\), where \(r-1\ge14\), the emitted list
contains no possible witness for that rank.  The script detects an empty row
and returns before finishing the formula, leaving a partial body rather than
an explicit UNSAT instance.  Thus this fixed-width version is
not an all-odd construction.

Nor is the exact two-half syntax closed under Pascal lifting.  A parent upper
witness on \(T_a,\ldots,T_b\) maps in the facet row to the witness

\[
 \partial T_{a-1},\ldots,\partial T_b,              \tag{12.12}
\]

which expands its edge span by one on the left, while its union-row image
shrinks by one.  Therefore a one-step facet lift preserves disjointness only
when the two parent spans have at least one unused edge between them.  A
`--dup2` half split supplies that one boundary edge, but not an unbounded
guard.  Repeated facet lifts consume the guard, and the widths move by
\(\pm1\), leaving the set (12.10).

Moreover, a generalized Pascal braid may reorder the sector paths, so
quotient halves of the parent are not child physical banks unless that order
is carried as part of the router certificate.

The raw c-space model also enforces the positive-run/lower-turn side only; it
does not enforce the dual zero-gap/upper-turn separation required for a
strict union row.  Thus \(\nabla T\) may already repeat a state before any
bank-separation question is reached.

There is also a new-depth failure independent of guard margins.  Assume here
that the parent chronology is owner-simple and lower-turn-separated, as in
the intended strict c-space factor.  In the facet row

\[
 B_i=\{z\}\cup(T_i\cap T_{i+1}),
\]

the child first-upper target \(\{z\}\cup T_j\) has the inherited interval
\((B_{j-1},B_j)\).  It is the only intact-facet interval with that union:
lower-turn separation makes the two derivative states distinct, and any
extension past them introduces a distinct rank-\(r\) parent owner and hence
an element outside \(T_j\).  Thus parent `--dup2` data do not
even supply two witnesses for this newly created child row.  A fresh
opening-aware service witness is necessary.

There is nevertheless a sparse correct recursion for this row.  The
canonical intervals

\[
 (B_{j-1},B_j)\longmapsto\{z\}\cup T_j
\]

are a bijection with parent owners.  Cutting \(s_B\) old facet edges deletes
exactly \(s_B\) members of this canonical occurrence bank and can therefore
create at most \(s_B\) target casualties.  Retain every other canonical
witness and place only the actual casualties in the PPR service bank.  For
higher targets the interval map (12.12) and its reversed-union analogue
transport the named guarded witnesses literally.  This cut-aware protected
bank, rather than global duplication, is the Pascal-compatible interface.

For higher upper rows, a recursively useful duplicate certificate would have
to be a **guarded physical bank**: store the two actual witness spans for each
selected target, their target-aligning translations, a positive separation
margin, and the child placement of both banks.  Under an intact one-step
diamond, copy and union images preserve the two-bank property, while the
facet image consumes one unit of margin.  A fresh re-spacing/regeneration
step is required before the margin vanishes.  Theorem 12.3 forbids imposing
this on the whole first-upper row.  This guarded higher-row notion is
compatible with the zero-frame functor of Section 5, but it is not implied by
the raw `--dup2` clauses.

### 12.2 Why `kernelcount.py` numbers are not certificates

The current file explicitly performs an approximation and its numerical
output has no theorem status or certified inequality direction here.  In
particular it:

* closes an already opened linear path by a possibly non-Johnson fake edge;
* treats the input as one component even when the source factor has several;
* represents wrapped cyclic edge spans by unreduced integer ranges;
* applies a linear greedy interval schedule, not a circular packing
  algorithm;
* uses `i > lastend`, incorrectly rejecting edge-disjoint intervals which
  meet at one vertex;
* hard-codes the threshold `<=2`; and
* omits unseen upper targets from the blocking histogram rather than
  declaring immediate failure, while also including rank `k`, which the
  `codd.py` upper loop excludes.

The exact replacement is Lemma 12.2 on the actual physical components and
actual modular edge spans.

The audited source hashes are

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/codd.py
947b738205dd228523ddf529b320eaee75061539f1525e770f791ccfa7989c8a

/Users/amir.nuriyev/Downloads/opusproblem/work/kernelcount.py
50386a159ba918cc1e7a0e3f396cbd469b6881adf52dac130446d66651912805
```

No claim is made that a `--dup2` instance is satisfiable in any new
dimension; this section audits the implication of a satisfying assignment.

## 13. K16 and the C9 trap

The sparse-regeneration obstruction does not refute the current finite K16
service problem.  SAAR-93 has only `93` named defects, far below the scale of
an absent Gaussian outer deck.  The separated-port master is precisely the
correct finite collar/service model through depth three.

The saved C9 atoms fail for a different reason.  Each desired rank-eleven
gain creates one lower-rank-five and two upper-rank-ten casualties.  Thus its
full all-depth signed frame is nonzero.  It is not a zero-frame router and it
does not carry a complete relative service ledger.  An `O(C_r)` family of
bounded C9 collars could not be the bulk depth regenerator in any case.

There is a structural explanation for the support scale `9`.  The Pascal
child is radius one in the transition/matching indicator.  If a parent
open-switch changes exactly three such indicator entries, its direct child
image has support at most nine.  Lifting only those physical entries and
omitting the transformed boundary/service tokens is therefore compatible
with the kind of unbalanced C9 packet seen in the finite trap; no claim is
made that an authenticated C9 is the literal image of a specified parent
switch.
The recursive object is the router **plus its full relative ledger**, not the
edge packet alone.

## 14. Frozen artifacts

### `k=11,13` atlas audit

```text
scratch/audit_k11_k13_ppr_router_atlas_20260730.py
db14724c5c6a2c3b335644db0659d8a85d6502b69e70beb82a8858a0630dea9a

scratch/k11_k13_ppr_router_atlas_20260730.audit.json
d54009a03cbebedf7a439723fb1b41e5c45e82c78320d8a6c564a5a7915a8035
```

The replay freezes the split/channel/run tables, all-depth fragment-survivor
rows, deterministic protected-record digests, one-core pin maps, the hollow
`k=13` halo, the parent-image test, and the `0/50` closure census.

### `k=15` relative atlas audit

```text
scratch/audit_k15_relative_ppr_router_atlas_20260730.py
b94f172e0cbe90b41dea2c13376c4051f535694a69d16514cfc1b400141d1a71

scratch/k15_relative_ppr_router_atlas_20260730.audit.json
c4d69d4f3a15f2834776c4abfcb1fdc8b59a0df170d3a6bb16288a7606441746
```

This replay hash-pins the source factor, components, and word; checks all
fifteen coordinate splits and all `429+429` run endpoints per split; and
reconstructs the cut/splice, all fixed lower windows, all arbitrary-upper
witnesses, residence, `DA=DP`, and complete literal coverage.

### `k=15` common-witness/zero-frame audit

```text
scratch/audit_k15_ppr_common_witness_bank_20260730.py
10faf2f1f063fe28ddbe7ea801aab760eae1f6cf2625701d397b0d51fd3983a0

scratch/k15_fixed_matching_pbbs_resident_20260729/
  ppr_common_witness_bank_20260730.audit.json
88260962d026531252710d4217f4bd3261e831813a6e141c6424a7e62b33b13f
```

This last audit is restricted to the four frozen component-reduction stages;
it does not include the final opening or a transported compiler matching.

## 15. Sharp final boundary

The authenticated finite bases prove the following.

1. The universal coordinate split is a Catalan-sized two-shore router.
2. A common near-perfect open-switch macro topology is the smallest verified
   finite pattern; its `BB/BB/AA` shore state matters.  No all-r legal
   parameterization is claimed.
3. Each final surgery has a literal occurrence-level shadow service bank.
4. PPR's physical formal-closing-edge clause is unnecessary and false for
   two authenticated optima; near-perfect boundary-PPR is sufficient.
5. All-depth zero-frame, compiler-pin-transparent routers are exactly closed
   under the Pascal operators.
6. The finite routers do not yet form such a parametric atlas.
7. Pure transport erodes the certified depth band and one event-buffer unit.
8. A Catalan number of seam collars cannot regenerate an absent critical
   outer lower deck.
9. `codd.py --dup2` has a correct conditional physical two-witness meaning,
   but upper-`q=1` edge capacity makes it UNSAT for every relevant
   \(k\ge7\); its approximate kernel census has no certified numerical
   direction.

The remaining theorem is `BRG(r)`: a bulk, core-stable router which refreshes
the adjacent compiler depths, event buffer, and relative ledger while
retaining the exact near-perfect endpoint/compiler structure.  Proving it
would complete this Pascal/PBBS route to the all-odd upper bound.  The finite
`k=11,13,15` atlas supplies the boundary data and the correct topology, but
does not itself prove `BRG(r)`.
